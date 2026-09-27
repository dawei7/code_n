# Guided Example: Longest Palindromic Subsequence

We trace the step-by-step 2D interval dynamic programming grid ($dp[i][j]$), diagonal base initialization ($dp[i][i] = 1$), boundary character matching match expansion ($s[i] == s[j] \implies dp[i+1][j-1] + 2$), asymmetric boundary contraction pruning ($\max(dp[i+1][j], dp[i][j-1])$), and optimal subsequence length extraction on representative character strings:

- **Input:** $s = \text{"bbbab"}$
- **Required output:** `4`
  - String length: $n = 5$
  - Characters: $s[0]=\text{'b'}, \; s[1]=\text{'b'}, \; s[2]=\text{'b'}, \; s[3]=\text{'a'}, \; s[4]=\text{'b'}$
  - Subsequence definition: Can delete any non-palindromic letters without altering the relative order of remaining letters.
  - Optimal candidate: `"bbbb"` (deleting `'a'` at index 3 yields length 4).
- **Interval DP table execution trace ($dp[i][j]$):**
  - Table dimensions: $5 \times 5$, where $dp[i][j]$ denotes the length of the longest palindromic subsequence in $s[i \dots j]$.
  - **Base Case (Interval Length 1):**
    - Every single character is a palindrome of length 1:
      $$
      dp[0][0] = dp[1][1] = dp[2][2] = dp[3][3] = dp[4][4] = \mathbf{1}
      $$
  - **Interval Length 2 ($j - i = 1$):**
    - Substring `"bb"` ($i=0, j=1$): $s[0] == s[1] \implies 0 + 2 = \mathbf{2}$
    - Substring `"bb"` ($i=1, j=2$): $s[1] == s[2] \implies 0 + 2 = \mathbf{2}$
    - Substring `"ba"` ($i=2, j=3$): $s[2] \ne s[3] \implies \max(dp[3][3], dp[2][2]) = \max(1, 1) = \mathbf{1}$
    - Substring `"ab"` ($i=3, j=4$): $s[3] \ne s[4] \implies \max(dp[4][4], dp[3][3]) = \max(1, 1) = \mathbf{1}$
  - **Interval Length 3 ($j - i = 2$):**
    - Substring `"bbb"` ($i=0, j=2$):
      - $s[0] == s[2] \implies dp[1][1] + 2 = 1 + 2 = \mathbf{3}$ (palindrome `"bbb"`)
    - Substring `"bba"` ($i=1, j=3$):
      - $s[1] \ne s[3] \implies \max(dp[2][3], dp[1][2]) = \max(1, 2) = \mathbf{2}$
    - Substring `"bab"` ($i=2, j=4$):
      - $s[2] == s[4] \implies dp[3][3] + 2 = 1 + 2 = \mathbf{3}$ (palindrome `"bab"`)
  - **Interval Length 4 ($j - i = 3$):**
    - Substring `"bbba"` ($i=0, j=3$):
      - $s[0] \ne s[3] \implies \max(dp[1][3], dp[0][2]) = \max(2, 3) = \mathbf{3}$
    - Substring `"bbab"` ($i=1, j=4$):
      - $s[1] == s[4] \implies dp[2][3] + 2 = 1 + 2 = \mathbf{3}$
  - **Interval Length 5 ($j - i = 4$, Full String `"bbbab"`):**
    - Endpoints: $s[0] = \text{'b'}$ and $s[4] = \text{'b'}$.
    - Since $s[0] == s[4]$:
      - Match both outer letters and add $2$ to the inner subproblem $dp[1][3]$ (`"bba"`):
        $$
        dp[0][4] = dp[1][3] + 2 = 2 + 2 = \mathbf{4}
        $$
    - The outer `'b'`s combine with the inner `"bb"` to form palindrome `"bbbb"`!
  - Final maximum length: **`4`**.
- **Asymmetric Subsequence Instance ($s = \text{"cbbd"}$):**
  - Inner substring `"bb"` gives length $2$.
  - Endpoints `'c'` and `'d'` never match $\implies \mathbf{2}$.
- **Single Character String ($s = \text{"a"}$):**
  - Length 1 base case $\implies \mathbf{1}$.
- **Already Palindromic ($s = \text{"racecar"}$):**
  - Matches every concentric layer $\implies \mathbf{7}$.

This instance demonstrates interval-based 2D dynamic programming, mathematically proves why outer matching guarantees boundary encapsulation without subproblem corruption, and derives $O(N^2)$ runtime and $O(N^2)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"bbbab"}$:
Find the **length of the longest palindromic subsequence** in $s$.
A subsequence can be formed by deleting characters without changing the relative order of the remaining characters.

```text
String:  b  b  b  a  b
Indices: 0  1  2  3  4

Optimal Subsequence:
  Keep indices 0, 1, 2, 4 -> "b b b b"
  Skip index 3 ('a')

Length = 4
```

### Palindromic Boundary Recursion
Consider the boundary characters of any substring $s[i \dots j]$:
- If the endpoints match ($s[i] == s[j]$):
  Both characters can be added to the front and back of any palindromic subsequence found inside the inner substring $s[i+1 \dots j-1]$.
  This adds exactly $2$ to the answer:
  $$
  dp[i][j] = dp[i+1][j-1] + 2
  $$
- If the endpoints do not match ($s[i] \ne s[j]$):
  They cannot both belong to the same palindromic subsequence.
  We must choose whether omitting $s[i]$ or omitting $s[j]$ yields a longer palindrome:
  $$
  dp[i][j] = \max(dp[i+1][j], \; dp[i][j-1])
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. State Definition:
Let $dp[i][j]$ be the length of the longest palindromic subsequence in substring $s[i \dots j]$ ($0 \le i \le j < n$).

### 2. Base Cases:
- All single-character intervals are palindromes of length 1:
  $$
  dp[i][i] = 1 \quad \forall i \in [0, n - 1]
  $$
- Empty intervals ($i > j$) have length 0:
  $$
  dp[i][j] = 0 \quad \text{when } i > j
  $$

### 3. Transition Order:
To compute $dp[i][j]$, we require:
- $dp[i+1][j-1]$ (strictly smaller length)
- $dp[i+1][j]$ (row $i+1$, below)
- $dp[i][j-1]$ (col $j-1$, left)
Hence, we iterate right boundary $j$ ascending from $1$ to $n-1$, and left boundary $i$ descending from $j-1$ down to $0$.

> **Concentric Subproblem Invariant.** Inner subproblems are always solved before their containing outer intervals, guaranteeing that $dp[i+1][j-1]$ is finalized before $dp[i][j]$ evaluates.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"bbbab"}$ ($n = 5$):

---

### Step 1: Base Table Initialization
Diagonal elements ($i == j$):
$$
dp[0][0] = 1, \quad dp[1][1] = 1, \quad dp[2][2] = 1, \quad dp[3][3] = 1, \quad dp[4][4] = 1
$$

---

### Step 2: Fill Table by Increasing Length

- **At $j = 1$ ($s[1] = \text{'b'}$):**
  - $i = 0$ ($s[0] = \text{'b'}$):
    $s[0] == s[1] \implies dp[1][0] + 2 = 0 + 2 = \mathbf{2}$.

- **At $j = 2$ ($s[2] = \text{'b'}$):**
  - $i = 1$ ($s[1] = \text{'b'}$):
    $s[1] == s[2] \implies dp[2][1] + 2 = 0 + 2 = \mathbf{2}$.
  - $i = 0$ ($s[0] = \text{'b'}$):
    $s[0] == s[2] \implies dp[1][1] + 2 = 1 + 2 = \mathbf{3}$.

- **At $j = 3$ ($s[3] = \text{'a'}$):**
  - $i = 2$ ($s[2] = \text{'b'}$):
    $s[2] \ne s[3] \implies \max(dp[3][3], dp[2][2]) = \max(1, 1) = \mathbf{1}$.
  - $i = 1$ ($s[1] = \text{'b'}$):
    $s[1] \ne s[3] \implies \max(dp[2][3], dp[1][2]) = \max(1, 2) = \mathbf{2}$.
  - $i = 0$ ($s[0] = \text{'b'}$):
    $s[0] \ne s[3] \implies \max(dp[1][3], dp[0][2]) = \max(2, 3) = \mathbf{3}$.

- **At $j = 4$ ($s[4] = \text{'b'}$):**
  - $i = 3$ ($s[3] = \text{'a'}$):
    $s[3] \ne s[4] \implies \max(dp[4][4], dp[3][3]) = \max(1, 1) = \mathbf{1}$.
  - $i = 2$ ($s[2] = \text{'b'}$):
    $s[2] == s[4] \implies dp[3][3] + 2 = 1 + 2 = \mathbf{3}$.
  - $i = 1$ ($s[1] = \text{'b'}$):
    $s[1] == s[4] \implies dp[2][3] + 2 = 1 + 2 = \mathbf{3}$.
  - $i = 0$ ($s[0] = \text{'b'}$):
    $s[0] == s[4] \implies dp[1][3] + 2 = 2 + 2 = \mathbf{4}$.

---

### Step 3: Extract Solution
$$
dp[0][4] = \mathbf{4}
$$

---

## 4. Complete DP Table

| $i \backslash j$ | $0$ (`'b'`) | $1$ (`'b'`) | $2$ (`'b'`) | $3$ (`'a'`) | $4$ (`'b'`) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$0$ (`'b'`)** | **$1$** | $2$ | $3$ | $3$ | **$4$** |
| **$1$ (`'b'`)** | $0$ | **$1$** | $2$ | $2$ | $3$ |
| **$2$ (`'b'`)** | $0$ | $0$ | **$1$** | $1$ | $3$ |
| **$3$ (`'a'`)** | $0$ | $0$ | $0$ | **$1$** | $1$ |
| **$4$ (`'b'`)** | $0$ | $0$ | $0$ | $0$ | **$1$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Character String ($s = \text{"z"}$):** Returns base diagonal $dp[0][0] = \mathbf{1}$.
- **All Distinct Characters ($s = \text{"abcdef"}$):** No character pair matches $\implies$ maximum length is $\mathbf{1}$.
- **All Identical Characters ($s = \text{"aaaaa"}$):** Every endpoint matches $\implies$ returns full length $\mathbf{5}$.
- **Two Identical Characters ($s = \text{"aa"}$):** $dp[0][1] = 0 + 2 = \mathbf{2}$.

---

## 6. Traps & Common Anti-Patterns

- **Confusing Subsequence with Substring:** A palindromic *substring* requires contiguous characters. A *subsequence* allows non-contiguous deletions (like skipping `'a'` in `"bbbab"` to obtain `"bbbb"`).
- **Wrong Loop Iteration Order:** Iterating $i$ forward and $j$ forward attempts to read $dp[i+1][j-1]$ before it has been computed, reading uninitialized zeroes. Sweeping $j$ forward and $i$ backwards ensures all dependent states are ready.
- **Off-by-One in Empty Intervals:** For adjacent matching characters ($j = i + 1$), $dp[i+1][j-1] = dp[i+1][i] = 0$. Ensuring out-of-bound cells default to 0 avoids crashes.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The table has size $N \times N$.
  - Only the upper-triangular half is filled: $\frac{N(N - 1)}{2}$ state cells.
  - Each cell computes one equality check and one arithmetic/max operation in $O(1)$ time.
  - Total Time: $\mathcal{O}(N^2)$. For $N = 1000$, $\approx 5 \times 10^5$ operations, completing in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N^2)$ space for the 2D DP matrix.