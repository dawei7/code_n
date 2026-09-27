# Guided Example: Search a 2D Matrix

We trace the step-by-step flattened 1D-to-2D virtual coordinate binary search on a representative sorted matrix:

- **Input:** $\text{matrix} = \begin{pmatrix} 1 & 3 & 5 & 7 \\ 10 & 11 & 16 & 20 \\ 23 & 30 & 34 & 60 \end{pmatrix}$, $\text{target} = 3$
- **Required output:** $\text{True}$
- **Negative Target:** $\text{target} = 13 \implies \text{False}$

This instance demonstrates virtual 1D-to-2D coordinate mapping ($r = \lfloor k / N \rfloor, c = k \pmod N$), exploiting global monotonic row-major ordering, logarithmic candidate space halving ($O(\log(M \cdot N))$ time), and contrasting single-pass search with two-tier bisection.

---

## 1. Instance & Teaching Goal

Given an $M \times N$ matrix ($M = 3, N = 4$) with two structural guarantees:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is strictly greater than the last integer of the previous row.

Given a target value $3$, determine if $target$ exists in the matrix.

Because every row's elements are strictly greater than all elements in earlier rows, the entire matrix forms a single, continuously sorted 1D array of length $M \cdot N = 12$:
$$
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
$$

Rather than scanning all $M \cdot N$ cells in $O(M \cdot N)$ time, or performing two separate binary searches (one on the first column and another on the selected row), virtual coordinate mapping flattens the matrix into a single binary search range $[0, M \cdot N - 1]$, finding the target in $O(\log(M \cdot N))$ time with zero memory overhead.

---

## 2. Conceptual Foundation & Invariants

### Virtual 1D-to-2D Coordinate Bijection
For any 1D index $k \in [0, M \cdot N - 1]$ in a matrix with $N$ columns:
$$
\text{row } r = \lfloor k / N \rfloor
$$
$$
\text{col } c = k \pmod N
$$
The value corresponding to 1D index $k$ is directly $\text{matrix}[r][c]$.

### Binary Search Execution Loop
Initialize $L = 0$ and $R = M \cdot N - 1$.
While $L \le R$:
1. Compute 1D midpoint:
   $$
   M = L + \lfloor (R - L) / 2 \rfloor
   $$
2. Decompose $M$ into 2D coordinates:
   $$
   r = \lfloor M / N \rfloor, \quad c = M \pmod N
   $$
3. Probe matrix value $\text{val} = \text{matrix}[r][c]$:
   - If $\text{val} == \text{target}$: return $\text{True}$.
   - If $\text{val} < \text{target}$: search right half ($L \leftarrow M + 1$).
   - If $\text{val} > \text{target}$: search left half ($R \leftarrow M - 1$).
4. If the loop terminates with $L > R$, return $\text{False}$.

> **Invariant.** If `target` exists anywhere in the matrix, its virtual 1D index lies strictly within the active inclusive interval $[L, R]$.

---

## 3. Step-by-Step Worked Execution

We search for $\text{target} = 3$ in the $3 \times 4$ matrix ($M = 3, N = 4$, $M \cdot N = 12$):

### Initialization
- Search space: $L = 0, R = 12 - 1 = 11$.

---

### Step 1 ($L = 0, R = 11$)
- Midpoint: $M = 0 + \lfloor (11 - 0) / 2 \rfloor = 5$.
- Coordinate transformation ($N = 4$):
  $$
  r = \lfloor 5 / 4 \rfloor = 1, \quad c = 5 \pmod 4 = 1
  $$
- Read cell: $\text{matrix}[1][1] = 11$.
- Comparison: $11 > 3$ (Target is smaller).
- Discard right half: $R \leftarrow M - 1 = 4$.
- Active range: $[0, 4]$.

---

### Step 2 ($L = 0, R = 4$)
- Midpoint: $M = 0 + \lfloor (4 - 0) / 2 \rfloor = 2$.
- Coordinate transformation:
  $$
  r = \lfloor 2 / 4 \rfloor = 0, \quad c = 2 \pmod 4 = 2
  $$
- Read cell: $\text{matrix}[0][2] = 5$.
- Comparison: $5 > 3$ (Target is smaller).
- Discard right half: $R \leftarrow M - 1 = 1$.
- Active range: $[0, 1]$.

---

### Step 3 ($L = 0, R = 1$)
- Midpoint: $M = 0 + \lfloor (1 - 0) / 2 \rfloor = 0$.
- Coordinate transformation:
  $$
  r = \lfloor 0 / 4 \rfloor = 0, \quad c = 0 \pmod 4 = 0
  $$
- Read cell: $\text{matrix}[0][0] = 1$.
- Comparison: $1 < 3$ (Target is larger).
- Discard left half: $L \leftarrow M + 1 = 1$.
- Active range: $[1, 1]$.

---

### Step 4 ($L = 1, R = 1$)
- Midpoint: $M = 1$.
- Coordinate transformation:
  $$
  r = \lfloor 1 / 4 \rfloor = 0, \quad c = 1 \pmod 4 = 1
  $$
- Read cell: $\text{matrix}[0][1] = 3$.
- Comparison: $3 == 3$.
- **Match Found!** Return $\text{True}$.

---

## 4. Complete Execution Trace

| Step | Left $L$ | Right $R$ | Virtual Mid $M$ | Decoded 2D $(r, c)$ | Probed Value | Comparison vs Target ($3$) | New Search Interval |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0 | 11 | 5 | $(1, 1)$ | 11 | $11 > 3$ | $[0, 4]$ |
| 2 | 0 | 4 | 2 | $(0, 2)$ | 5 | $5 > 3$ | $[0, 1]$ |
| 3 | 0 | 1 | 0 | $(0, 0)$ | 1 | $1 < 3$ | $[1, 1]$ |
| 4 | 1 | 1 | 1 | $(0, 1)$ | **3** | **$3 == 3$ (Match)** | **Return True** |

### Absent Target Trace ($\text{target} = 13$)
- Step 1: $M = 5 \implies \text{matrix}[1][1] = 11 < 13 \implies L \leftarrow 6$.
- Step 2: $L = 6, R = 11 \implies M = 8 \implies \text{matrix}[2][0] = 23 > 13 \implies R \leftarrow 7$.
- Step 3: $L = 6, R = 7 \implies M = 6 \implies \text{matrix}[1][2] = 16 > 13 \implies R \leftarrow 5$.
- Step 4: $L = 6 > R = 5 \implies$ Halts! Return $\text{False}$.

---

## 5. Algorithmic Correctness

**Soundness.** The transformation $(r, c) \mapsto r \cdot N + c$ is a strict bijection from $[0, M-1] \times [0, N-1]$ to $[0, M \cdot N - 1]$. The matrix conditions ensure that $k_1 < k_2 \implies \text{matrix}[r_1][c_1] \le \text{matrix}[r_2][c_2]$. Because monotonicity is strictly preserved, eliminating half of the virtual indices upon inequality never discards the target.

**Completeness.** Each iteration strictly reduces $(R - L + 1)$ by at least half. When $L > R$, every possible cell has been ruled out, guaranteeing that an absent target returns $\text{False}$.

---

## 6. Traps This Instance Exposes

- **Matrix Dimension Division:** Dividing by $M$ instead of $N$ is a common coordinate mapping error. Columns define the stride of a row, so row index is always $\lfloor M / N \rfloor$ and column index is $M \pmod N$.
- **Empty Matrix Validation:** If $\text{matrix} = []$ or $\text{matrix}[0] = []$, calculating $N = \text{len}(\text{matrix}[0])$ raises an `IndexError`. Checking `if not matrix or not matrix[0]: return False` upfront prevents this.
- **Search a 2D Matrix I vs II:** This problem (LeetCode 74) has the second condition ($\text{matrix}[r][0] > \text{matrix}[r-1][N-1]$), allowing a single 1D binary search. In LeetCode 240 (Search a 2D Matrix II), rows and columns are independently sorted without inter-row dominance, which requires starting from the top-right corner in $O(M + N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log(M \cdot N)) = O(\log M + \log N)$. The search range of size $M \cdot N$ is halved each iteration.
- **Auxiliary Space Complexity:** $O(1)$. Index arithmetic uses constant extra memory.