# Guided Example: Maximum Length of Repeated Subarray

We trace the step-by-step 2D dynamic programming matrix construction ($f[i][j]$), diagonal matching progression ($nums_1[i-1] == nums_2[j-1] \implies f[i-1][j-1] + 1$), contiguous sequence reset on character mismatch ($f[i][j] = 0$), global maximum length extraction ($ans = \max f[i][j]$), and common contiguous subsegment derivation on representative integer sequences:

- **Input:**
  - Sequence 1: $nums_1 = [1, 2, 3, 2, 1]$
  - Sequence 2: $nums_2 = [3, 2, 1, 4, 7]$
- **Required output:** `3`
  - Subarray matching criteria:
    - A subarray is a **contiguous** sequence of elements within an array.
    - Find the length of the longest subarray that appears in both $nums_1$ and $nums_2$.
    - For the input arrays:
      - Subarray $[3, 2, 1]$ appears in $nums_1$ at indices $2 \dots 4$.
      - Subarray $[3, 2, 1]$ appears in $nums_2$ at indices $0 \dots 2$.
      - The maximum common contiguous length is **3**.
- **The Longest Common Contiguous Subarray Invariant:**
  - **State Definition ($f[i][j]$):**
    - Let $f[i][j]$ denote the length of the longest common contiguous subarray that ends precisely at element $nums_1[i - 1]$ and element $nums_2[j - 1]$.
  - **The Strict Contiguity Constraint:**
    - Unlike the Longest Common Subsequence (LCS) problem where non-matching characters can be skipped, a **subarray** requires elements to be strictly consecutive.
    - If the current elements match ($nums_1[i - 1] == nums_2[j - 1]$):
      - Extend the matching chain from the preceding diagonal neighbor:
        $$
        f[i][j] = f[i - 1][j - 1] + 1
        $$
    - If the current elements differ ($nums_1[i - 1] \ne nums_2[j - 1]$):
      - The contiguous match is broken immediately:
        $$
        f[i][j] = 0
        $$
  - **Global Maximum Reduction:**
    - The longest common subarray can end at any pair of positions $(i, j)$ in the matrix:
      $$
      ans = \max_{\substack{1 \le i \le m \\ 1 \le j \le n}} f[i][j]
      $$
- **Step-by-Step Worked Execution Trace on $nums_1 = [1, 2, 3, 2, 1]$ and $nums_2 = [3, 2, 1, 4, 7]$:**
  - Dimensions: $m = 5, n = 5$. Table size $6 \times 6$.
  - Initialize row 0 and col 0 with 0. Global maximum $ans = 0$.
  - **Row $i = 1$ ($nums_1[0] = 1$):**
    - Compare with $nums_2 = [3, 2, 1, 4, 7]$:
    - Matches only at $j = 3$ ($nums_2[2] = 1$):
      $$
      f[1][3] = f[0][2] + 1 = 0 + 1 = \mathbf{1}
      $$
      $$
      ans \leftarrow \max(0, 1) = \mathbf{1}
      $$
  - **Row $i = 2$ ($nums_1[1] = 2$):**
    - Matches only at $j = 2$ ($nums_2[1] = 2$):
      $$
      f[2][2] = f[1][1] + 1 = 0 + 1 = \mathbf{1}
      $$
      All other cells in Row 2 are 0.
  - **Row $i = 3$ ($nums_1[2] = 3$):**
    - Matches at $j = 1$ ($nums_2[0] = 3$):
      $$
      f[3][1] = f[2][0] + 1 = 0 + 1 = \mathbf{1}
      $$
      All other cells in Row 3 are 0.
  - **Row $i = 4$ ($nums_1[3] = 2$):**
    - Matches at $j = 2$ ($nums_2[1] = 2$):
      - Diagonal predecessor is $f[3][1] = 1$!
      - Extend contiguous chain:
        $$
        f[4][2] = f[3][1] + 1 = 1 + 1 = \mathbf{2}
        $$
        *(Represents common subarray $[3, 2]$)*
      - Update global maximum:
        $$
        ans \leftarrow \max(1, 2) = \mathbf{2}
        $$
  - **Row $i = 5$ ($nums_1[4] = 1$):**
    - Match 1 at $j = 3$ ($nums_2[2] = 1$):
      - Diagonal predecessor is $f[4][2] = 2$!
      - Extend contiguous chain:
        $$
        f[5][3] = f[4][2] + 1 = 2 + 1 = \mathbf{3}
        $$
        *(Represents common subarray $[3, 2, 1]$)*
      - Update global maximum:
        $$
        ans \leftarrow \max(2, 3) = \mathbf{3}
        $$
  - **Step 6: Output Result:**
    $$
    ans = \mathbf{3}
    $$
- **Identical Arrays Trace ($nums_1 = [0, 0, 0], nums_2 = [0, 0, 0]$):**
  - Main diagonal continuously increments:
    - $f[1][1] = 1$
    - $f[2][2] = 1 + 1 = 2$
    - $f[3][3] = 2 + 1 = 3$
  - Output: **`3`**.
- **Completely Disjoint Arrays ($nums_1 = [1, 2], nums_2 = [3, 4]$):**
  - Zero matches across the entire grid.
  - $ans = \mathbf{0}$.

This instance demonstrates longest common substring dynamic programming and diagonal contiguous chain tracking, mathematically proves why zeroing mismatch cells preserves strict contiguity, and derives $O(M \cdot N)$ runtime and $O(M \cdot N)$ (or $O(N)$ space-optimized) space bounds.

---

## 1. Instance & Teaching Goal

Given two integer arrays $nums_1$ and $nums_2$:
Find the **maximum length of a contiguous subarray** present in both arrays.

```text
nums1 = [ 1, 2, 3, 2, 1 ]
nums2 = [ 3, 2, 1, 4, 7 ]

Matching subsegment:
  nums1[2..4] is [ 3, 2, 1 ]
  nums2[0..2] is [ 3, 2, 1 ]

Length = 3
Result: 3
```

### The Invariant of Diagonal Contiguity
- A common contiguous subarray ending at $nums_1[i-1]$ and $nums_2[j-1]$ can only extend a common subarray ending at $nums_1[i-2]$ and $nums_2[j-2]$.
- When characters match, add 1 to the diagonal predecessor $f[i-1][j-1]$.
- When characters differ, the contiguous chain is broken $\implies f[i][j] = 0$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Dynamic Programming Recurrence:
For $1 \le i \le m, 1 \le j \le n$:
$$
f[i][j] = \begin{cases} f[i - 1][j - 1] + 1 & \text{if } nums_1[i - 1] == nums_2[j - 1] \\ 0 & \text{otherwise} \end{cases}
$$

### 2. Maximum Value Reduction:
$$
ans = \max_{i, j} f[i][j]
$$

> **Diagonal Trace Contiguity Invariant.** The family of common factors between strings $u$ and $v$ corresponds bijectively to contiguous diagonal paths of 1s in the boolean product matrix $(u_i = v_j)$, whose path lengths satisfy the diagonal recurrence $f[i, j] = (f[i-1, j-1] + 1) \cdot \mathbf{1}_{u_i = v_j}$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Base State
- All edges $f[0][j] = 0, f[i][0] = 0$.

---

### Step 2: Diagonal Chain Extension
- At $(3, 1)$ ($3 == 3$): $f[3][1] = 0 + 1 = 1$.
- At $(4, 2)$ ($2 == 2$): $f[4][2] = f[3][1] + 1 = 1 + 1 = 2$.
- At $(5, 3)$ ($1 == 1$): $f[5][3] = f[4][2] + 1 = 2 + 1 = \mathbf{3}$.

---

### Step 3: Output
- Global maximum = **`3`**.

---

## 4. Complete Execution Trace

| Row $i$ ($nums_1$) | Col 1 (`3`) | Col 2 (`2`) | Col 3 (`1`) | Col 4 (`4`) | Col 5 (`7`) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **`1`** | $0$ | $0$ | $1$ | $0$ | $0$ |
| **`2`** | $0$ | $1$ | $0$ | $0$ | $0$ |
| **`3`** | **$1$** | $0$ | $0$ | $0$ | $0$ |
| **`2`** | $0$ | **$2$** | $0$ | $0$ | $0$ |
| **`1`** | $0$ | $0$ | **`3`** | $0$ | $0$ |

---

## 5. Boundary Cases & Failure Modes

- **No Shared Elements:** Table is entirely 0 $\implies$ returns 0.
- **Identical Arrays ($N = 1000$):** Main diagonal equals $N \implies$ returns $N$.
- **Single Element Arrays ($[1]$ and $[1]$):** Returns 1.
- **Duplicate Characters:** Handled correctly by checking all $(i, j)$ pairings.

---

## 6. Traps & Common Anti-Patterns

- **Confusing Subarray with Subsequence:** For LCS (subsequence), we do `max(f[i-1][j], f[i][j-1])`. For subarrays (substrings), non-matching cells must be strictly reset to $0$.
- **Brute Force Subarray Comparison ($O(N^3)$):** Checking all subarray pairs takes cubic time (TLE). 2D dynamic programming runs in strictly quadratic $\mathcal{O}(M \cdot N)$ time.
- **Off-By-One Indexing:** Remember that $nums_1[i-1]$ corresponds to table row $i$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Standard 2D table of dimensions $(M + 1) \times (N + 1)$.
  - Each cell performs constant number of operations: $\mathcal{O}(1)$.
  - Total Time: strictly $\mathcal{O}(M \cdot N)$. For $M = N = 1000$, completes in $< 25$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(M \cdot N)$ space for the full 2D array, or $\mathcal{O}(N)$ using a single 1D rolling array.