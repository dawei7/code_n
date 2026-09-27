# Guided Example: One Edit Distance

We trace the step-by-step first-mismatch identification and suffix alignment validation on representative string comparison instances:

- **Input:** $s = \text{"ab"}, \quad t = \text{"acb"}$
- **Required output:** `true` (Inserting `'c'` into $s$ yields $t$)
- **Identical Strings Trap:** $s = \text{"ab"}, \quad t = \text{"ab"} \implies \text{false}$ (Zero edits is invalid; exactly one edit required)
- **Character Replacement Instance:** $s = \text{"1203"}, \quad t = \text{"1213"} \implies \text{true}$ (Replacing `'0'` with `'1'`)
- **Length Disparity Failure:** $s = \text{"a"}, \quad t = \text{"abc"} \implies \text{false}$ ($|m - n| = 2 > 1$)

This instance demonstrates early length difference pruning ($|m - n| \le 1$), locating the first differing character, branching on equal lengths (replacement: $s[i+1:] == t[i+1:]$) versus differing lengths (insertion/deletion: $s[i:] == t[i+1:]$), and achieving $O(N)$ linear time.

---

## 1. Instance & Teaching Goal

Given two strings $s$ and $t$, determine if they are **exactly one edit distance apart**.
An edit operation consists of:
1. **Insert** exactly one character into $s$ to get $t$.
2. **Delete** exactly one character from $s$ to get $t$.
3. **Replace** exactly one character of $s$ with a different character to get $t$.

For $s = \text{"ab"}$ and $t = \text{"acb"}$:
- $|s| = 2, \, |t| = 3$. Length difference is $3 - 2 = 1$.
- Inserting character `'c'` at index 1 transforms `"ab"` into `"acb"`.
- The strings are exactly one edit distance apart: return `true`.

A general Levenshtein distance dynamic programming matrix computes the minimum edit distance in $O(|s| \cdot |t|)$ time.
Because we only care whether the distance is **strictly 1**:
- Any length difference $|m - n| > 1$ can be rejected in $O(1)$ time.
- By scanning from left to right, the **first mismatch index** $i$ completely determines the required edit.
- After fixing that mismatch, the remaining suffixes must match **identically**. A single linear pass in $O(N)$ time suffices.

---

## 2. Conceptual Foundation & Invariants

### The First-Mismatch Suffix Invariant
Let $m = |s|$ and $n = |t|$.
Without loss of generality, assume $m \le n$ (if $m > n$, swap $s$ and $t$, since edit distance is symmetric).

#### Phase 1: Global Length Pruning
If $n - m > 1$:
$$
\text{return False}
$$
(No single edit can bridge a length difference of 2 or more).

#### Phase 2: Locate First Discrepancy
Iterate index $i$ from $0$ to $m - 1$:
If $s[i] \ne t[i]$:
- **Case A: Equal Length ($m == n$) $\implies$ Replacement:**
  The character $s[i]$ must be replaced by $t[i]$. All characters after index $i$ must already match:
  $$
  \text{return } s[i+1 :] == t[i+1 :]
  $$
- **Case B: Unequal Length ($m < n$) $\implies$ Deletion from $t$ / Insertion into $s$:**
  Character $t[i]$ must be inserted into $s$ (or removed from $t$). The remainder of $s$ starting at $i$ must match the remainder of $t$ starting at $i + 1$:
  $$
  \text{return } s[i :] == t[i+1 :]
  $$

#### Phase 3: Exhausted Prefix Match
If all $m$ characters match ($s[i] == t[i]$ for all $0 \le i < m$):
The strings are 1 edit apart if and only if $t$ has exactly 1 extra character at the end:
$$
\text{return } m + 1 == n
$$
*(If $m == n$, the strings are identical, which means 0 edits $\implies$ returns False)*.

> **Invariant.** Before index $i$, prefixes $s[0 \dots i-1]$ and $t[0 \dots i-1]$ are identical. A single edit can resolve the discrepancy at $i$ if and only if the specified suffix equality holds.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"ab"}$ and $t = \text{"acb"}$:
$m = |s| = 2, \, n = |t| = 3$. Length gap: $3 - 2 = 1 \le 1$.

### Step 1: Index $i = 0$
- $s[0] = \text{'a'}$
- $t[0] = \text{'a'}$
- $s[0] == t[0] \implies$ Characters match. Continue scan.

---

### Step 2: Index $i = 1$ (First Mismatch Detected!)
- $s[1] = \text{'b'}$
- $t[1] = \text{'c'}$
- $s[1] \ne t[1]$ ('b' $\ne$ 'c')!
- Length condition check:
  $$
  m < n \quad (2 < 3)
  $$
- This requires **character insertion** into $s$ (or deletion from $t$):
  - Slice $s[1:] = \text{"b"}$.
  - Slice $t[1 + 1:] = t[2:] = \text{"b"}$.
- Test suffix equality:
  $$
  s[1:] == t[2:] \iff \text{"b"} == \text{"b"} \implies \mathbf{True}
  $$

The suffixes are identical.
Exactly 1 edit operation transforms $s$ into $t$.
Return $\mathbf{True}$.

---

## 4. Complete Execution Trace

```text
Strings:
s = " a   b "  (len = 2)
t = " a   c   b "  (len = 3)
      ^   ^
      |   First mismatch at i=1: s[1]='b' != t[1]='c'
      Matched
Check: len(s) < len(t) -> test s[1:] ("b") == t[2:] ("b") -> MATCH!
Result: True
```

| Iteration $i$ | $s[i]$ | $t[i]$ | Status | Condition Branch Evaluated | Suffix Equality Test | Outcome |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| 0 | `'a'` | `'a'` | Match | Advance $i$ | - | Continue |
| **1** | **`'b'`** | **`'c'`** | **Mismatch** | **$m < n$ (Insert/Delete)** | **$s[1:] == t[2:] \implies \text{"b"} == \text{"b"}$** | **True (Return)** |

### Contrast: Replacement on $s = \text{"1203"}, t = \text{"1213"}$
- $i=0$: `'1' == '1'`
- $i=1$: `'2' == '2'`
- $i=2$: `'0' \ne '1'` (Mismatch, $m == n == 4$).
- Test replacement: $s[3:] == t[3:] \iff \text{"3"} == \text{"3"}$.
- Return **True**.

---

## 5. Algorithmic Correctness

**Soundness.** If $|m - n| > 1$, no single operation can match the lengths. When the first mismatch occurs at index $i$, any hypothetical edit before index $i$ would break the prefix match. Thus, the edit must occur at index $i$. If lengths are equal, the only valid operation is replacing $s[i]$ with $t[i]$, which requires $s[i+1:] == t[i+1:]$. If lengths differ by 1, the only valid operation is inserting $t[i]$ into $s$, which requires $s[i:] == t[i+1:]$.

**Completeness.** All edit operations (insert, delete, replace) are covered. If no mismatch is found up to index $m - 1$, the only remaining possibility is an extra character at the end of $t$, verified by $m + 1 == n$.

---

## 6. Traps This Instance Exposes

- **Identical Strings ($s == t$):** If $s = \text{"abc"}$ and $t = \text{"abc"}$, edit distance is 0. The problem requires **exactly one** edit distance. Returning `m + 1 == n` correctly yields `False` when $m == n$.
- **Empty String Inputs:** If $s = \text{""}$ and $t = \text{""}$, loop does not run, $m + 1 == n \implies 0 + 1 == 0 \implies \text{False}$. If $s = \text{""}$ and $t = \text{"a"}$, $0 + 1 == 1 \implies \text{True}$.
- **Full Dynamic Programming Overhead:** Running 2D Levenshtein DP takes $O(N^2)$ time and space, which is unnecessary and risks time limit exceeded on large strings ($N = 10^5$).

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = \min(|s|, |t|)$. Finding the first mismatch takes at most $N$ character comparisons. Comparing the remaining suffixes takes at most $N$ character comparisons.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory when comparing suffix indices directly with pointers (or $O(N)$ if string slicing is used).
