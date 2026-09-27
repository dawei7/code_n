# Guided Example: Longest Uncommon Subsequence II

We trace the step-by-step whole-string candidate theorem (any maximal uncommon subsequence must be one of the input strings), pairwise two-pointer greedy subsequence testing ($check(s, t)$), cross-string disqualification on duplicates, and global maximum length extraction on representative string arrays:

- **Input:** $strs = [\text{"aba"}, \text{"cdc"}, \text{"eae"}]$
- **Required output:** `3`
  - Problem definition: An **uncommon subsequence** of a collection of strings is a string that is a subsequence of **exactly one** string in the collection, and **not** a subsequence of any other string.
  - Number of strings: $N = 3$
- **Candidate Evaluation Principle:**
  - If any uncommon subsequence exists, at least one of the original strings in $strs$ must itself be an uncommon subsequence!
  - Therefore, we only need to test each string $s \in strs$ against every other string $t \in strs$ ($i \ne j$).
  - If string $s$ is NOT a subsequence of any other string $t$, then $s$ is an uncommon subsequence of length $|s|$.
- **Step-by-step candidate execution trace:**
  - **Candidate 1: $s = \text{"aba"}$ (Index 0):**
    - Compare against $t = \text{"cdc"}$ (Index 1):
      - Two-pointer greedy scan:
        - Pointer in $s$: looking for `'a'`, `'b'`, `'a'`.
        - String $t$ has characters `['c', 'd', 'c']`.
        - No characters match $\implies$ `"aba"` is NOT a subsequence of `"cdc"`.
    - Compare against $t = \text{"eae"}$ (Index 2):
      - Two-pointer scan:
        - $t$ has characters `['e', 'a', 'e']`.
        - Matches `'a'` at index 1, but cannot match `'b'` or the second `'a'`.
        - `"aba"` is NOT a subsequence of `"eae"`.
    - **Result for Candidate 0:** Not a subsequence of any other string!
      - Valid uncommon subsequence of length $|s| = \mathbf{3}$.
      - Update answer: $ans = \max(-1, 3) = \mathbf{3}$.
  - **Candidate 2: $s = \text{"cdc"}$ (Index 1):**
    - Not a subsequence of `"aba"` or `"eae"`.
    - Valid uncommon subsequence of length $3$.
    - $ans = \max(3, 3) = 3$.
  - **Candidate 3: $s = \text{"eae"}$ (Index 2):**
    - Not a subsequence of `"aba"` or `"cdc"`.
    - Valid uncommon subsequence of length $3$.
    - $ans = \max(3, 3) = 3$.
  - Final maximum length: **`3`**.
- **Duplicate Disqualification Instance ($strs = [\text{"aaa"}, \text{"aaa"}, \text{"aa"}]$):**
  - Candidate 0 (`"aaa"`): Identical duplicate exists at index 1 $\implies$ `"aaa"` is a subsequence of `"aaa"` at index 1 $\implies$ **Disqualified**!
  - Candidate 1 (`"aaa"`): Identical duplicate exists at index 0 $\implies$ **Disqualified**!
  - Candidate 2 (`"aa"`): Subsequence of both `"aaa"` entries $\implies$ **Disqualified**!
  - No string survives $\implies$ Returns **`-1`**.
- **Containment by Longer String Instance ($strs = [\text{"aabbcc"}, \text{"aabbcc"}, \text{"bc"}]$):**
  - `"aabbcc"` duplicates disqualify each other.
  - Shorter string `"bc"` is contained in `"aabbcc"` $\implies$ Disqualified $\implies \mathbf{-1}$.

This instance demonstrates candidate set reduction in combinatorial language theory, mathematically proves why testing whole strings is necessary and sufficient, and derives $O(N^2 \cdot L)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of strings $strs = [\text{"aba"}, \text{"cdc"}, \text{"eae"}]$:
An **uncommon subsequence** is a string that is a subsequence of one string in $strs$, but **not** a subsequence of any other string in $strs$.
Return the length of the **longest uncommon subsequence**.
If no such subsequence exists, return `-1`.

```text
Candidates: "aba", "cdc", "eae"

Testing "aba":
  Is "aba" a subsequence of "cdc"? -> No.
  Is "aba" a subsequence of "eae"? -> No.
  -> "aba" is an uncommon subsequence! Length = 3.

Testing "cdc":
  Not a subsequence of any other string -> Length = 3.

Testing "eae":
  Not a subsequence of any other string -> Length = 3.

Max Length = 3
```

### The Candidate Reduction Theorem
Suppose there exists an uncommon subsequence $U$ derived from string $s \in strs$.
- If $U$ is not a subsequence of any other string in $strs$, then the full string $s$ itself **cannot** be a subsequence of any other string either!
- Why? If $s$ were a subsequence of some other string $t$, then every subsequence of $s$ (including $U$) would also be a subsequence of $t$, contradicting that $U$ is uncommon.
- Therefore, **we do not need to generate exponential subsequences**.
- We only need to check if each complete string $s \in strs$ is contained as a subsequence in any other string $t \in strs$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Two-Pointer Subsequence Predicate $check(s, t)$:
Determine if string $s$ is a subsequence of string $t$:
- Initialize $i = 0, \; j = 0$.
- While $i < |s|$ and $j < |t|$:
  - If $s[i] == t[j]$: advance $i \leftarrow i + 1$.
  - Advance $j \leftarrow j + 1$.
- Return $i == |s|$.
Takes $O(|s| + |t|)$ linear time.

### 2. The Verification Loop:
Initialize $ans = -1$.
For each string $s$ at index $i$:
- Check whether there exists any index $j \ne i$ such that $check(s, strs[j])$ is `True`.
- If NO such index $j$ exists ($s$ is completely uncommon):
  $$
  ans \leftarrow \max(ans, \; |s|)
  $$
Return $ans$.

> **Candidate Sufficiency Invariant.** If a valid uncommon subsequence exists, the longest one is guaranteed to be one of the original strings in $strs$.

---

## 3. Step-by-Step Worked Execution

We trace $strs = [\text{"aba"}, \text{"cdc"}, \text{"eae"}]$ ($N = 3$):

---

### Step 1: Candidate 0 ($s = \text{"aba"}$, length 3)
- Compare with $j = 1$ ($t = \text{"cdc"}$):
  - $check(\text{"aba"}, \text{"cdc"})$:
    - Target `'a'` not found in `"cdc"`.
    - Returns `False`.
- Compare with $j = 2$ ($t = \text{"eae"}$):
  - $check(\text{"aba"}, \text{"eae"})$:
    - Finds `'a'` at $t[1]$. Next needs `'b'`. But $t[2]$ is $\text{'e'} \ne \text{'b'}$.
    - Returns `False`.
- String `"aba"` is not contained in any other string!
- Candidate valid:
  $$
  ans = \max(-1, 3) = \mathbf{3}
  $$

---

### Step 2: Candidate 1 ($s = \text{"cdc"}$, length 3)
- Compare with $j = 0$ ($t = \text{"aba"}$): Returns `False`.
- Compare with $j = 2$ ($t = \text{"eae"}$): Returns `False`.
- Candidate valid:
  $$
  ans = \max(3, 3) = \mathbf{3}
  $$

---

### Step 3: Candidate 2 ($s = \text{"eae"}$, length 3)
- Compare with $j = 0$ ($t = \text{"aba"}$): Returns `False`.
- Compare with $j = 1$ ($t = \text{"cdc"}$): Returns `False`.
- Candidate valid:
  $$
  ans = \max(3, 3) = \mathbf{3}
  $$

---

### Final Output:
$$
ans = \mathbf{3}
$$

---

## 4. Complete Execution Trace

| Candidate $s$ (Index $i$) | Tested Against Other Strings $t$ | $check(s, t)$ Result | Is $s$ Uncommon? | Length $\lvert s \rvert$ | Running $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **`"aba"` ($0$)** | `"cdc"`, `"eae"` | All `False` | **Yes** | $3$ | **$3$** |
| **`"cdc"` ($1$)** | `"aba"`, `"eae"` | All `False` | **Yes** | $3$ | **$3$** |
| **`"eae"` ($2$)** | `"aba"`, `"cdc"` | All `False` | **Yes** | $3$ | **$3$** |
| **Result** | — | — | — | — | **$3$** |

### Contrast with Duplicate Input `["aaa", "aaa", "aa"]`:
| Candidate $s$ (Index $i$) | Compared Against $t$ | $check(s, t)$ Result | Disqualified By |
|:---:|:---:|:---:|:---:|
| `"aaa"` ($0$) | `"aaa"` ($1$) | **True** | Duplicate copy at index 1 |
| `"aaa"` ($1$) | `"aaa"` ($0$) | **True** | Duplicate copy at index 0 |
| `"aa"` ($2$) | `"aaa"` ($0$) | **True** | Proper subsequence of index 0 |
| **All Disqualified** | — | — | **Result: $-1$** |

---

## 5. Boundary Cases & Failure Modes

- **All Duplicate Strings ($[\text{"a"}, \text{"a"}]$):** Both strings match each other $\implies \mathbf{-1}$.
- **Different Lengths ($[\text{"a"}, \text{"b"}, \text{"c"}]$):** None contain each other $\implies \mathbf{1}$.
- **One Long Unique String ($[\text{"abc"}, \text{"def"}, \text{"abcdef"}]$):** `"abcdef"` cannot be contained in the shorter strings $\implies \mathbf{6}$.
- **Single Character Strings with One Duplicate ($[\text{"a"}, \text{"a"}, \text{"b"}]$):** `"b"` is unique $\implies \mathbf{1}$.

---

## 6. Traps & Common Anti-Patterns

- **Generating All Subsequences of All Strings:** Generating all subsequences takes $O(N \cdot 2^L)$ time, which crashes for $L = 50$. Testing whole strings with two pointers takes $O(N^2 \cdot L)$ time.
- **Skipping Identical Strings by Value:** Comparing $s \ne t$ instead of index $i \ne j$ ignores identical duplicate strings, falsely claiming a duplicated string is "uncommon". Comparing by index `i != j` correctly identifies that duplicate strings eliminate each other.
- **Sorting Strings without Proper Subsequence Verification:** Sorting by descending length is an optimization, but each candidate must still be strictly verified against all other strings using the two-pointer check.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N = |strs|$ and $L$ be the maximum string length.
  - There are $N$ candidate strings.
  - Each candidate is compared against $N - 1$ other strings.
  - The two-pointer subsequence check $check(s, t)$ takes $O(L)$ time.
  - Total Time: $\mathcal{O}(N^2 \cdot L)$. For $N \le 50, L \le 10$, $50^2 \times 10 = 2.5 \times 10^4$ operations, completing in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ extra space using two pointer indices.
