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

### Every Authored Instance Through the Same Three Phases

The lengths below follow the method's own convention: the shorter string plays the role of $s$ and the longer plays the role of $t$, so the given pair is swapped whenever the first string is longer.

| Authored instance | $(m, n)$ | Gap | First mismatch $i$ | Branch reached | Test evaluated | Verdict |
|:---|:---:|:---:|:---:|:---|:---|:---:|
| `s = "ab"`, `t = "acb"` | $(2, 3)$ | 1 | 1 | unequal lengths → insertion or deletion | `s[1:] == t[2:]` → `"b" == "b"` | `true` |
| `s = "a"`, `t = "A"` | $(1, 1)$ | 0 | 0 | equal lengths → replacement | `s[1:] == t[1:]` → `"" == ""` | `true` |
| `s = "ab"`, `t = "cd"` | $(2, 2)$ | 0 | 0 | equal lengths → replacement | `s[1:] == t[1:]` → `"b" == "d"` | `false` |
| `s = "algorith"`, `t = "algorithm"` after the swap | $(8, 9)$ | 1 | none, all 8 compared positions match | prefix exhausted | `m + 1 == n` → `9 == 9` | `true` |
| `s = ""`, `t = "7"` | $(0, 1)$ | 1 | none, nothing to compare | prefix exhausted | `m + 1 == n` → `1 == 1` | `true` |
| `s = ""`, `t = ""` | $(0, 0)$ | 0 | none, nothing to compare | prefix exhausted | `m + 1 == n` → `1 == 0` | `false` |
| `s = "a"`, `t = "abc"` | $(1, 3)$ | 2 | never scanned | length gate | not reached | `false` |
| 10,000-character instance, last character `'0'` against `'A'` | $(10000, 10000)$ | 0 | 9999, the final position | equal lengths → replacement | `s[10000:] == t[10000:]` → `"" == ""` | `true` |

---

## 5. Algorithmic Correctness

**Soundness.** If $|m - n| > 1$, no single operation can match the lengths. When the first mismatch occurs at index $i$, any hypothetical edit before index $i$ would break the prefix match. Thus, the edit must occur at index $i$. If lengths are equal, the only valid operation is replacing $s[i]$ with $t[i]$, which requires $s[i+1:] == t[i+1:]$. If lengths differ by 1, the only valid operation is inserting $t[i]$ into $s$, which requires $s[i:] == t[i+1:]$.

**Completeness.** All edit operations (insert, delete, replace) are covered. If no mismatch is found up to index $m - 1$, the only remaining possibility is an extra character at the end of $t$, verified by $m + 1 == n$.

---

## 6. Traps This Instance Exposes

- **Identical Strings ($s == t$):** If $s = \text{"abc"}$ and $t = \text{"abc"}$, edit distance is 0. The problem requires **exactly one** edit distance. Returning `m + 1 == n` correctly yields `False` when $m == n$.
- **Empty String Inputs:** If $s = \text{""}$ and $t = \text{""}$, loop does not run, $m + 1 == n \implies 0 + 1 == 0 \implies \text{False}$. If $s = \text{""}$ and $t = \text{"a"}$, $0 + 1 == 1 \implies \text{True}$.
- **Full Dynamic Programming Overhead:** Running 2D Levenshtein DP takes $O(N^2)$ time and space, which is unnecessary and risks time limit exceeded on large strings ($N = 10^5$).

The word "exactly" is what makes the following outcomes counter-intuitive; each row names the phase that decides it:

| Scenario | Concrete instance | Expected | Phase that decides it |
|:---|:---|:---:|:---|
| Identical strings of any length | `"abc"` against `"abc"`, and `""` against `""` | `false` | the final test `m + 1 == n`, which fails because $m = n$: zero edits is not one edit |
| Equal lengths with a single difference | `"a"` against `"A"` | `true` | replacement branch, and the empty suffixes after index 0 match |
| Equal lengths with two differences | `"ab"` against `"cd"` | `false` | replacement branch: after aligning index 0 the suffixes `"b"` and `"d"` still differ |
| Lengths differing by one, extra character at the end | `"algorith"` against `"algorithm"` | `true` | prefix exhausted, so the trailing-character test answers instead of the loop |
| Lengths differing by one, extra character in the middle | `"ab"` against `"acb"` | `true` | insertion branch: the mismatch at index 1 is resolved by skipping `t[1]` |
| Lengths differing by two | `"a"` against `"abc"` | `false` | length gate, before any character is compared |
| Equal lengths with the only difference at the final index | the 10,000-character instance | `true` | replacement branch; the two suffixes are both empty, so the position of the lone edit does not matter |

---

## 7. Complexity Derivation

Four candidate methods return the same verdict on the sampled instances; the comparison below shows what each one spends, and the ledger after it counts the characters the traced method actually inspects:

| Candidate method | Mechanism | Cost | Failure mode or tradeoff |
|:---|:---|:---|:---|
| Full Levenshtein dynamic programming | fill the $(m+1) \times (n+1)$ table of prefix distances and compare the final distance with $1$ | $O(mn)$ time and space | the 10,000-character instance needs $10^8$ cells, and the stated upper bound of $10^5$ characters would need $10^{10}$ |
| Banded dynamic programming | keep only the diagonal band with $\lvert i - j \rvert \le 1$, three cells per row | $O(N)$ time, $O(1)$ space | correct, but it maintains a recurrence where a prefix scan and two suffix tests are enough |
| Longest common prefix plus longest common suffix | measure the matching head and tail, then require the two unmatched middles to total exactly one | $O(N)$ time | the head and tail must be forced not to overlap; measured independently they double-count, and `"aa"` against `"aa"` yields a negative middle |
| Count positional mismatches | compare the strings index by index and accept at most one difference | $O(N)$ time | wrong in both directions: `"ab"` against `"acb"` has two positional differences yet is one edit away, while `"ab"` against `"ab"` has none yet must be `false` |
| First mismatch plus branch on the length gap | stop at the first difference and validate the remaining suffix | $O(N)$ time, $O(1)$ space | the branch is mandatory: applying the replacement test when the lengths differ misaligns the suffixes and would reject `"ab"` against `"acb"` |

| Authored instance | Full DP cells $(m+1)(n+1)$ | Prefix comparisons | Suffix comparisons | Total character inspections |
|:---|:---:|:---:|:---:|:---:|
| `""` against `""` | 1 | 0 | 0 (the trailing test only compares $m + 1$ with $n$) | 0 |
| `""` against `"7"` | 2 | 0 | 0 | 0 |
| `"a"` against `"A"` | 4 | 1 | 0, both suffixes empty | 1 |
| `"ab"` against `"acb"` | 12 | 2 | 1 | 3 |
| `"ab"` against `"cd"` | 9 | 1 | 1 | 2 |
| `"a"` against `"abc"` | 8 | 0, rejected by the length gate | 0 | 0 |
| `"algorith"` against `"algorithm"` | 90 | 8 | 0, the trailing test decides | 8 |
| 10,000-character instance | 100020001 | 10000 | 0, both suffixes empty | 10000 |

- **Time Complexity:** $O(N)$, where $N = \min(|s|, |t|)$. Finding the first mismatch takes at most $N$ character comparisons. Comparing the remaining suffixes takes at most $N$ character comparisons.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory when comparing suffix indices directly with pointers (or $O(N)$ if string slicing is used).
