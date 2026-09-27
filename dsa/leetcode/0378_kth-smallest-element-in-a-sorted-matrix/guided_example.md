# Guided Example: Kth Smallest Element in a Sorted Matrix

We trace the step-by-step value-range binary search ($[\text{MIN}, \text{MAX}] = [matrix[0][0], matrix[n-1][n-1]]$), $O(N)$ staircase predicate counting (`check(mid) >= k`), boundary contraction, and exact $k^{\text{th}}$ rank convergence on representative 2D sorted matrices:

- **Input:** $matrix = \begin{bmatrix} 1 & 5 & 9 \\ 10 & 11 & 13 \\ 12 & 13 & 15 \end{bmatrix}, \quad k = 8$
- **Required output:** $13$
  - Flattened sorted elements: $[1, 5, 9, 10, 11, 12, 13, 13, 15]$
  - The $8^{\text{th}}$ smallest element is $\mathbf{13}$
  - Value range search bounds: $[\text{left}, \text{right}] = [1, 15]$
    - Iteration 1: $mid = 8 \implies \text{count}(\le 8) = 2 < 8 \implies left = 9$
    - Iteration 2: $mid = 12 \implies \text{count}(\le 12) = 6 < 8 \implies left = 13$
    - Iteration 3: $mid = 14 \implies \text{count}(\le 14) = 8 \ge 8 \implies right = 14$
    - Iteration 4: $mid = 13 \implies \text{count}(\le 13) = 8 \ge 8 \implies right = 13$
  - Range converges at $left = right = \mathbf{13}$
- **Single Element Matrix:** $matrix = [[5]], k = 1 \implies 5$
- **All Equal Elements:** $matrix = [[2, 2], [2, 2]], k = 3 \implies 2$

This instance demonstrates binary search on the answer domain rather than array indices, mathematically proves why bottom-left staircase exploration counts matrix elements $\le mid$ in strictly $O(N)$ time, and achieves $O(N \log(\text{MAX} - \text{MIN}))$ time and $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an $n \times n$ matrix ($n = 3$) where each row and each column is sorted in non-decreasing order:
$$
matrix = \begin{bmatrix} 1 & 5 & 9 \\ 10 & 11 & 13 \\ 12 & 13 & 15 \end{bmatrix}, \quad k = 8
$$
Find the $k^{\text{th}}$ smallest element in the matrix with auxiliary memory strictly better than $O(n^2)$:

```text
Matrix:
[  1,   5,   9 ]
[ 10,  11,  13 ]
[ 12,  13,  15 ]

Sorted Values: 1, 5, 9, 10, 11, 12, 13, 13, 15
Rank:          1  2  3   4   5   6   7   8   9
                                     ^
                                 k = 8 -> Value = 13
```

### Why Flattening and Sorting ($O(N^2 \log N)$) Fails Constraints
- Flattening the matrix allocates $O(N^2)$ extra memory, violating the problem constraint.
- Priority queue merging of $N$ rows takes $O(K \log N)$ time and $O(N)$ memory.
- **Value-Range Bisection ($O(N \log(\text{MAX} - \text{MIN}))$):**
  The answer is guaranteed to lie in the range $[matrix[0][0], matrix[n-1][n-1]]$.
  For any candidate value $mid$, we can count how many elements are $\le mid$ in $O(N)$ time using a staircase walk from the bottom-left corner $(n - 1, 0)$!

---

## 2. Conceptual Foundation & Invariants

### 1. The $O(N)$ Staircase Counting Algorithm:
To count elements $\le mid$ in an $n \times n$ row-and-column sorted matrix:
- Start at the bottom-left corner: $i = n - 1, \; j = 0$.
- While $i \ge 0$ and $j < n$:
  - If $matrix[i][j] \le mid$:
    Since column $j$ is sorted ascending, all elements above $(i, j)$ in column $j$ (rows $0 \dots i$) are also $\le mid$.
    Add $i + 1$ to `count`, and advance to the next column: $j \leftarrow j + 1$.
  - Else ($matrix[i][j] > mid$):
    Current element is too large. Move up to a smaller row: $i \leftarrow i - 1$.
- Total pointer steps: $i$ decreases at most $n$ times, and $j$ increases at most $n$ times $\implies O(n)$ steps.

### 2. Range Bisection Invariant:
- `left = matrix[0][0], right = matrix[n - 1][n - 1]`.
- While `left < right`:
  - $mid = \lfloor (left + right) / 2 \rfloor$.
  - If $\text{count}(\le mid) \ge k$:
    The $k^{\text{th}}$ smallest element is at most $mid \implies right \leftarrow mid$.
  - Else ($\text{count}(\le mid) < k$):
    The $k^{\text{th}}$ smallest element must be strictly greater than $mid \implies left \leftarrow mid + 1$.

> **Invariant.** The $k^{\text{th}}$ smallest element is always contained in the closed interval $[left, right]$. When $left == right$, this common value is guaranteed to be present in the matrix.

---

## 3. Step-by-Step Worked Execution

We trace $matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]$ with $k = 8$:
Initial range: $left = 1, right = 15$.

---

### Step 1: Probe $mid = 8$
- Midpoint: $mid = \lfloor(1 + 15)/2\rfloor = \mathbf{8}$.
- Staircase walk from $(i = 2, j = 0)$:
  - $(2, 0) = 12 > 8 \implies i \leftarrow 1$.
  - $(1, 0) = 10 > 8 \implies i \leftarrow 0$.
  - $(0, 0) = 1 \le 8 \implies count \mathrel{+}= (0 + 1) = 1, \; j \leftarrow 1$.
  - $(0, 1) = 5 \le 8 \implies count \mathrel{+}= (0 + 1) = 2, \; j \leftarrow 2$.
  - $(0, 2) = 9 > 8 \implies i \leftarrow -1$ (Exits).
- Total count: $2$.
- Compare: $count < k$ ($2 < 8$).
- Eliminate range $\le 8$:
  $$
  left \leftarrow 8 + 1 = \mathbf{9}
  $$
- New range: $[9, 15]$.

---

### Step 2: Probe $mid = 12$
- Midpoint: $mid = \lfloor(9 + 15)/2\rfloor = \mathbf{12}$.
- Staircase walk from $(i = 2, j = 0)$:
  - $(2, 0) = 12 \le 12 \implies count \mathrel{+}= 3 = 3, \; j \leftarrow 1$.
  - $(2, 1) = 13 > 12 \implies i \leftarrow 1$.
  - $(1, 1) = 11 \le 12 \implies count \mathrel{+}= 2 = 5, \; j \leftarrow 2$.
  - $(1, 2) = 13 > 12 \implies i \leftarrow 0$.
  - $(0, 2) = 9 \le 12 \implies count \mathrel{+}= 1 = 6, \; j \leftarrow 3$ (Exits).
- Total count: $6$.
- Compare: $6 < 8$.
- Eliminate range $\le 12$:
  $$
  left \leftarrow 12 + 1 = \mathbf{13}
  $$
- New range: $[13, 15]$.

---

### Step 3: Probe $mid = 14$
- Midpoint: $mid = \lfloor(13 + 15)/2\rfloor = \mathbf{14}$.
- Staircase walk from $(i = 2, j = 0)$:
  - $(2, 0) = 12 \le 14 \implies count \mathrel{+}= 3 = 3, \; j \leftarrow 1$.
  - $(2, 1) = 13 \le 14 \implies count \mathrel{+}= 3 = 6, \; j \leftarrow 2$.
  - $(2, 2) = 15 > 14 \implies i \leftarrow 1$.
  - $(1, 2) = 13 \le 14 \implies count \mathrel{+}= 2 = 8, \; j \leftarrow 3$ (Exits).
- Total count: $8$.
- Compare: $count \ge k$ ($8 \ge 8$).
- Contract upper bound:
  $$
  right \leftarrow \mathbf{14}
  $$
- New range: $[13, 14]$.

---

### Step 4: Probe $mid = 13$
- Midpoint: $mid = \lfloor(13 + 14)/2\rfloor = \mathbf{13}$.
- Staircase walk:
  - $(2, 0) = 12 \le 13 \implies count = 3, \; j = 1$.
  - $(2, 1) = 13 \le 13 \implies count = 6, \; j = 2$.
  - $(2, 2) = 15 > 13 \implies i = 1$.
  - $(1, 2) = 13 \le 13 \implies count = 8, \; j = 3$.
- Total count: $8$.
- Compare: $8 \ge 8 \implies right \leftarrow \mathbf{13}$.
- New range: $[13, 13]$.

---

### Step 5: Termination
$left == right == 13$. Loop terminates.
Return:
$$
\mathbf{13}
$$

---

## 4. Complete Execution Trace

```text
matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]], k = 8

Iter 1: range [1, 15]  -> mid = 8  -> count(<=8)  = 2 < 8  -> left = 9
Iter 2: range [9, 15]  -> mid = 12 -> count(<=12) = 6 < 8  -> left = 13
Iter 3: range [13, 15] -> mid = 14 -> count(<=14) = 8 >= 8 -> right = 14
Iter 4: range [13, 14] -> mid = 13 -> count(<=13) = 8 >= 8 -> right = 13

Left == Right == 13 -> Return 13
```

| Iteration | Active Range $[L, R]$ | Midpoint $mid$ | Staircase Walk $\le mid$ Count | Condition $\text{count} \ge k$ | Action Taken | Next Range |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $[1, 15]$ | 8 | 2 | $2 < 8$ (False) | $left \leftarrow 8 + 1 = 9$ | $[9, 15]$ |
| 2 | $[9, 15]$ | 12 | 6 | $6 < 8$ (False) | $left \leftarrow 12 + 1 = 13$ | $[13, 15]$ |
| 3 | $[13, 15]$ | 14 | 8 | $8 \ge 8$ (True) | $right \leftarrow 14$ | $[13, 14]$ |
| **4** | **$[13, 14]$** | **13** | **8** | **$8 \ge 8$ (True)** | **$right \leftarrow 13$** | **$[13, 13]$** |
| **Exit** | $[13, 13]$ | - | - | $L == R$ | **Converged** | **`13` (Output)** |

---

## 5. Algorithmic Correctness

**Soundness.** Let $C(x)$ be the number of matrix elements $\le x$. As $x$ increases, $C(x)$ is monotonically non-decreasing. The $k^{\text{th}}$ smallest element is the unique smallest integer $x$ such that $C(x) \ge k$. By maintaining the invariant that the target is $\le right$ whenever $C(mid) \ge k$, and strictly $> mid$ whenever $C(mid) < k$, the binary search converges to the minimum integer satisfying $C(x) \ge k$.

**Completeness.** Could the algorithm converge to an integer not present in the matrix?
Suppose it converged to a phantom integer $v$ not in the matrix. Then the count of elements $\le v$ would be identical to the count of elements $\le v - 1$ (since no element equals $v$). But the binary search logic would have contracted $right$ further to $v - 1$. Therefore, the converged value $left$ is guaranteed to be an actual element of the matrix.

---

## 6. Traps This Instance Exposes

- **Duplicate Elements:** If elements are duplicated (e.g. two 13s in this matrix), $\text{count}(\le 13) = 8$. The algorithm correctly handles multiplicity because $k^{\text{th}}$ denotes rank in sorted order with duplicates counted individually.
- **Negative Elements:** Elements in `matrix` can be negative (e.g. $-10^9$). Python bit-shift `(left + right) >> 1` correctly floors negative midpoints.
- **Index vs Value Binary Search:** Bisection is performed over the continuous value interval $[matrix[0][0], matrix[n-1][n-1]]$, NOT over array coordinates or indices.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log(\text{MAX} - \text{MIN}))$, where $N$ is the matrix dimension and $\text{MAX} - \text{MIN}$ is the difference between the largest and smallest element.
  - Binary search over the value range takes $O(\log(\text{MAX} - \text{MIN}))$ iterations ($\le 32$ iterations for 32-bit integers).
  - Each iteration performs a staircase walk visiting at most $2N$ cells in $O(N)$ time.
  - Overall time is strictly $O(N \log(\text{MAX} - \text{MIN}))$, requiring zero sorting.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory, using only scalar coordinates and count registers.