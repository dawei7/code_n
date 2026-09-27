# Guided Example: Max Sum of Rectangle No Larger Than K

We trace the step-by-step 2D-to-1D dimension reduction (iterating row bounds $[i, j]$), column sum accumulation (`nums[h] += matrix[j][h]`), prefix sum inequality transformation ($s - S_{\text{prev}} \le k \iff S_{\text{prev}} \ge s - k$), and sorted set binary search (`ts.bisect_left(s - k)`) on representative 2D matrix instances:

- **Input:** $\text{matrix} = [[1, 0, 1], [0, -2, 3]], \quad k = 2$
- **Required output:** $2$
  - Multi-row submatrix evaluation:
    - Span row $i = 0$ to $j = 0$ (Row 0): $[1, 0, 1] \implies$ submatrix $[1, 0, 1]$ has sum $2 \le 2$
    - Span row $i = 0$ to $j = 1$ (Rows 0 and 1):
      - Column sums: $[1 + 0, \; 0 + (-2), \; 1 + 3] = [1, -2, 4]$
      - Prefix sums: $S = [0, 1, -1, 3]$
      - Subarray spanning columns 1 and 2: $(-2) + 4 = 2 \le 2$
      - Corresponding 2D rectangle: $\begin{bmatrix} 0 & 1 \\ -2 & 3 \end{bmatrix}$
      - Sum: $0 + 1 - 2 + 3 = \mathbf{2}$ (Equal to upper bound $k = 2$)
  - Global maximum rectangle sum $\le 2$: $\mathbf{2}$
- **Single Cell Matrix:** $\text{matrix} = [[2, 2, -1]], k = 0 \implies -1$
- **All Negative Matrix:** $\text{matrix} = [[-5, -3], [-2, -4]], k = -2 \implies -2$

This instance demonstrates dimensional compression in geometric grid algorithms, mathematically proves why binary search over historical prefix sums finds the tightest bound $\le k$ in $O(N \log N)$ time, and analyzes $O(M^2 \cdot N \log N)$ computational complexity.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ integer matrix ($m = 2, n = 3$) and an integer $k = 2$:
$$
\text{matrix} = \begin{bmatrix} 1 & 0 & 1 \\ 0 & -2 & 3 \end{bmatrix}
$$
Find the maximum sum of any contiguous 2D submatrix such that the sum is $\le k$:

```text
Matrix:
[ 1,   0,  1 ]
[ 0,  -2,  3 ]

Candidate Submatrices:
[1]                      -> Sum = 1 <= 2
[1, 0]                   -> Sum = 1 <= 2
[1, 0, 1]                -> Sum = 2 <= 2
[[0, 1], [-2, 3]]        -> Sum = 0 + 1 - 2 + 3 = 2 <= 2 (MAXIMAL!)
[[1, 0, 1], [0, -2, 3]]  -> Sum = 1 + 0 + 1 + 0 - 2 + 3 = 3 > 2 (Exceeds k!)

Maximum Valid Sum: 2
```

### The $O(M^2 N^2)$ Brute Force vs $O(M^2 \cdot N \log N)$ Reduction
- Testing all $O(M^2 N^2)$ rectangles takes quadratic time in both dimensions.
- By fixing top row $i$ and bottom row $j$, we compress all rows between $i$ and $j$ into a single 1D array of column sums:
  $$
  nums[h] = \sum_{r=i}^j matrix[r][h]
  $$
- The problem is now reduced to: **Find the maximum sum subarray in `nums` that is $\le k$**.
- This 1D subproblem is solvable in $O(N \log N)$ using a balanced sorted set of prefix sums.

---

## 2. Conceptual Foundation & Invariants

### 1. The Prefix Sum Inequality Transformation
For a 1D array with running prefix sum $s$:
The sum of subarray from index $l$ to $r$ is:
$$
\text{sum}(l \dots r) = s - S_{\text{prev}}
$$
We demand:
$$
s - S_{\text{prev}} \le k \iff S_{\text{prev}} \ge s - k
$$
To **maximize** the subarray sum $s - S_{\text{prev}}$, we must **minimize** $S_{\text{prev}}$.
Therefore, we seek the **smallest prefix sum in our history that is $\ge s - k$**!

### 2. Sorted Set Bisection
Maintain `ts = SortedSet([0])`.
For each column element $x \in nums$:
1. $s \leftarrow s + x$
2. Query the smallest historical prefix sum $\ge s - k$:
   $$
   p = ts.\text{bisect\_left}(s - k)
   $$
3. If $p < \text{len}(ts)$, then $ts[p]$ is our optimal partner:
   $$
   ans \leftarrow \max(ans, \; s - ts[p])
   $$
4. Insert current prefix sum: $ts.\text{add}(s)$.

> **Invariant.** `ts` contains all prefix sums preceding the current column, allowing $O(\log N)$ retrieval of the tightest lower-bound partner.

---

## 3. Step-by-Step Worked Execution

We trace `matrix = [[1, 0, 1], [0, -2, 3]]` with $k = 2$:

---

### Step 1: Fix $i = 0, j = 0$ (Row 0 only)
- Column sums: `nums = [1, 0, 1]`.
- Initialize: `ts = SortedSet([0]), s = 0, ans = -inf`.
- **Column 0 ($x = 1$):**
  - $s = 0 + 1 = 1$. Target lower bound: $s - k = 1 - 2 = -1$.
  - `bisect_left(-1)` in $\{0\} \implies ts[0] = 0$.
  - Subarray sum: $s - ts[0] = 1 - 0 = \mathbf{1} \le 2$. $ans = 1$.
  - `ts.add(1)` $\implies ts = \{0, 1\}$.
- **Column 1 ($x = 0$):**
  - $s = 1 + 0 = 1$. Target: $1 - 2 = -1 \implies ts[0] = 0$.
  - Subarray sum: $1 - 0 = 1$. $ans = \max(1, 1) = 1$.
- **Column 2 ($x = 1$):**
  - $s = 1 + 1 = 2$. Target: $2 - 2 = \mathbf{0}$.
  - `bisect_left(0)` in $\{0, 1\} \implies ts[0] = 0$.
  - Subarray sum: $s - ts[0] = 2 - 0 = \mathbf{2} \le 2$.
  - Update: $ans \leftarrow \max(1, 2) = \mathbf{2}$.
  - `ts.add(2)` $\implies ts = \{0, 1, 2\}$.

---

### Step 2: Fix $i = 0, j = 1$ (Rows 0 and 1 combined)
- Column sums:
  - Col 0: $1 + 0 = 1$
  - Col 1: $0 + (-2) = -2$
  - Col 2: $1 + 3 = 4$
  - `nums = [1, -2, 4]`.
- Initialize: `ts = SortedSet([0]), s = 0`.
- **Column 0 ($x = 1$):**
  - $s = 1$. Target: $1 - 2 = -1 \implies ts[0] = 0 \implies 1 - 0 = 1$.
  - `ts.add(1)` $\implies ts = \{0, 1\}$.
- **Column 1 ($x = -2$):**
  - $s = 1 + (-2) = -1$. Target: $-1 - 2 = -3$.
  - `bisect_left(-3)` in $\{0, 1\} \implies ts[0] = 0$.
  - Subarray sum: $-1 - 0 = -1$. $ans = \max(2, -1) = 2$.
  - `ts.add(-1)` $\implies ts = \{-1, 0, 1\}$.
- **Column 2 ($x = 4$):**
  - $s = -1 + 4 = 3$. Target: $s - k = 3 - 2 = \mathbf{1}$.
  - `bisect_left(1)` in $\{-1, 0, 1\}$:
    - Smallest element $\ge 1$ is $ts[2] = \mathbf{1}$!
  - Subarray sum:
    $$
    s - ts[2] = 3 - 1 = \mathbf{2} \le 2
    $$
  - This corresponds to the 2D submatrix across rows $0 \dots 1$ and columns $1 \dots 2$:
    $$
    \sum = 0 + 1 + (-2) + 3 = \mathbf{2}
    $$
  - Update: $ans = \max(2, 2) = \mathbf{2}$.

---

### Step 3: Fix $i = 1, j = 1$ (Row 1 only)
- Column sums: `nums = [0, -2, 3]`.
- Best subarray $\le 2$ evaluates to $1$ (from $0 + (-2) + 3 = 1$ or $-2 + 3 = 1$).
- $ans$ remains $\mathbf{2}$.

---

### Step 4: Final Maximum
All row pairs $[i, j]$ evaluated. Global maximum sum $\le 2$:
$$
\mathbf{2}
$$

---

## 4. Complete Execution Trace

```text
matrix = [[1, 0, 1], [0, -2, 3]], k = 2

Row Pair (0, 0): nums = [1, 0, 1]
  x=1: s=1, bisect_left(1-2=-1)->0 -> sum=1-0=1, ans=1
  x=0: s=1, bisect_left(1-2=-1)->0 -> sum=1-0=1, ans=1
  x=1: s=2, bisect_left(2-2=0) ->0 -> sum=2-0=2, ans=2

Row Pair (0, 1): nums = [1, -2, 4]
  x=1 : s=1,  bisect_left(-1)->0 -> sum=1-0=1,  ans=2
  x=-2: s=-1, bisect_left(-3)->0 -> sum=-1-0=-1,ans=2
  x=4 : s=3,  bisect_left(1) ->1 -> sum=3-1=2,  ans=2

Row Pair (1, 1): nums = [0, -2, 3] -> max sum <= 2 is 1

Global Maximum <= k: 2
```

| Row Range $[i, j]$ | Column Sums `nums` | Prefix Sum $s$ | Search Target $s - k$ | Best Historical $S_{\text{prev}}$ | Valid Subarray Sum | Global Max `ans` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $[0, 0]$ | `[1, 0, 1]` | 1 | $-1$ | 0 | 1 | 1 |
| $[0, 0]$ | `[1, 0, 1]` | 1 | $-1$ | 0 | 1 | 1 |
| **$[0, 0]$** | **`[1, 0, 1]`** | **2** | **0** | **0** | **2** | **2** |
| $[0, 1]$ | `[1, -2, 4]` | 1 | $-1$ | 0 | 1 | 2 |
| $[0, 1]$ | `[1, -2, 4]` | $-1$ | $-3$ | 0 | $-1$ | 2 |
| **$[0, 1]$** | **`[1, -2, 4]`** | **3** | **1** | **1** | **2** | **2** |
| $[1, 1]$ | `[0, -2, 3]` | 1 | $-1$ | 0 | 1 | **2 (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** For any pair of row boundaries $i$ and $j$, the 1D projection `nums` represents the exact vertical sum of the slab across columns. In the 1D prefix sum array, any subarray sum is given by $s - S_{\text{prev}}$. Since $S_{\text{prev}} \ge s - k$, the difference satisfies $s - S_{\text{prev}} \le k$. Choosing the minimal $S_{\text{prev}}$ via `bisect_left` maximizes $s - S_{\text{prev}}$, ensuring that no valid subarray sum smaller than or equal to $k$ within this row slab is overlooked.

**Completeness.** The outer loops iterate over all $\frac{m(m+1)}{2}$ row pairs $[i, j]$. Because all possible vertical extents are examined and the optimal horizontal boundaries are found via exact prefix sum search, the maximum sum across all rectangular submatrices is found.

---

## 6. Traps This Instance Exposes

- **Negative Numbers in Matrix:** Kadane's algorithm alone cannot find the maximum subarray $\le k$ when negative numbers are present because the subarray sum is non-monotonic. Sorted set bisection is mandatory.
- **Orientation Optimization:** If $m \gg n$, looping over columns ($n^2$) and running bisection over rows ($m \log m$) reduces operations from $O(m^2 n \log n)$ to $O(n^2 m \log m)$.
- **Missing Base Prefix $0$:** Initializing `SortedSet([0])` is critical. Without $0$ in the set, a subarray starting at index 0 (whose sum is simply $s - 0$) would not have an initial anchor.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M^2 \cdot N \log N)$, where $M$ is the number of rows and $N$ is the number of columns.
  - There are $O(M^2)$ pairs of rows $[i, j]$.
  - For each pair, iterating over $N$ columns and performing balanced set bisection takes $O(N \log N)$ time.
  - With $M, N \le 100$, total operations are $\approx 5000 \times 100 \times 7 \approx 3.5 \times 10^6$, running well under the time limit.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store `nums` and the sorted set `ts`.
