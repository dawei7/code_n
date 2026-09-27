# Guided Example: Unique Paths II

We trace the step-by-step 2D dynamic programming grid evaluation with obstacle zeroing on a representative obstacle grid:

- **Input:** $\text{obstacleGrid} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}$
- **Required output:** $2$

This instance demonstrates handling impassable obstacle cells ($\text{grid}[r][c] == 1 \implies DP[r][c] = 0$), obstacle blockage propagating across boundary rows/columns, path accumulation around obstacles, and terminal cell evaluation.

---

## 1. Instance & Teaching Goal

A robot is located at the top-left corner of an $M \times N$ grid ($M = 3, N = 3$). The robot can only move **right** or **down**. An obstacle is represented as `1`, and an open space as `0`. A path cannot pass through any obstacle cell. We must find the number of unique paths to the bottom-right corner $(2, 2)$.

In the grid:
$$
\begin{pmatrix}
0 & 0 & 0 \\
0 & \mathbf{1} & 0 \\
0 & 0 & 0
\end{pmatrix}
$$
The center cell $(1, 1)$ is blocked.
- Path 1: $(0, 0) \to (0, 1) \to (0, 2) \to (1, 2) \to (2, 2)$ (Moving along the top and right edges).
- Path 2: $(0, 0) \to (1, 0) \to (2, 0) \to (2, 1) \to (2, 2)$ (Moving along the left and bottom edges).
Total unique paths: $2$.

A naive DFS risks visiting exponential paths. Dynamic programming calculates paths in topological order in $O(M \cdot N)$ time and $O(N)$ space.

---

## 2. Conceptual Foundation & Invariants

### DP Recurrence with Obstacle Zeroing
Let $DP[r][c]$ be the number of valid paths reaching cell $(r, c)$.
1. **Obstacle Rule:**
   If $\text{obstacleGrid}[r][c] == 1$:
   $$
   DP[r][c] = 0
   $$
   *(An obstacle can neither be visited nor contribute to downstream paths).*
2. **Start Cell:**
   If $\text{obstacleGrid}[0][0] == 0$:
   $$
   DP[0][0] = 1
   $$
   *(If the start cell is an obstacle, $DP[0][0] = 0$, immediately returning 0).*
3. **General Cell Transition ($r > 0 \lor c > 0$):**
   If $\text{obstacleGrid}[r][c] == 0$:
   $$
   DP[r][c] = (\text{from top: } DP[r-1][c] \text{ if } r > 0 \text{ else } 0) + (\text{from left: } DP[r][c-1] \text{ if } c > 0 \text{ else } 0)
   $$

> **Invariant.** For every cell $(r, c)$, $DP[r][c]$ equals the exact number of obstacle-free paths from $(0, 0)$ to $(r, c)$.

---

## 3. Step-by-Step Worked Execution

We trace the $3 \times 3$ grid:

### Row 0
- **Cell $(0, 0)$:** Free cell $\implies DP[0][0] = 1$.
- **Cell $(0, 1)$:** Free cell $\implies DP[0][1] = DP[0][0] = 1$.
- **Cell $(0, 2)$:** Free cell $\implies DP[0][2] = DP[0][1] = 1$.
- Row 0 state: $[1, 1, 1]$.

---

### Row 1
- **Cell $(1, 0)$:** Free cell $\implies DP[1][0] = DP[0][0] = 1$.
- **Cell $(1, 1)$ (Obstacle!):**
  - $\text{obstacleGrid}[1][1] == 1 \implies DP[1][1] = 0$.
- **Cell $(1, 2)$:**
  - Arrive from top: $DP[0][2] = 1$.
  - Arrive from left: $DP[1][1] = 0$ (blocked).
  - Sum: $DP[1][2] = 1 + 0 = 1$.
- Row 1 state: $[1, 0, 1]$.

---

### Row 2
- **Cell $(2, 0)$:** Free cell $\implies DP[2][0] = DP[1][0] = 1$.
- **Cell $(2, 1)$:**
  - Arrive from top: $DP[1][1] = 0$ (blocked).
  - Arrive from left: $DP[2][0] = 1$.
  - Sum: $DP[2][1] = 0 + 1 = 1$.
- **Cell $(2, 2)$ (Destination):**
  - Arrive from top: $DP[1][2] = 1$.
  - Arrive from left: $DP[2][1] = 1$.
  - Sum: $DP[2][2] = 1 + 1 = \mathbf{2}$.
- Row 2 state: $[1, 1, 2]$.

Terminal answer is $DP[2][2] = 2$.

---

## 4. Complete Execution Trace

### 2D DP State Matrix ($3 \times 3$)

| Row $\downarrow$ / Col $\to$ | Col 0 | Col 1 | Col 2 | Notes |
|:---:|:---:|:---:|:---:|:---|
| **Row 0** | 1 | 1 | 1 | Open corridor along top edge |
| **Row 1** | 1 | **0 (Obstacle)** | 1 | Center blocked; paths route around |
| **Row 2** | 1 | 1 | **2 (Target)** | Two paths converge at bottom-right |

---

## 5. Algorithmic Correctness

**Soundness.** Because paths can only move Right or Down, any valid path reaching $(r, c)$ must immediately precede from either $(r - 1, c)$ or $(r, c - 1)$. Setting $DP[r][c] = 0$ whenever an obstacle is present completely disconnects that cell from contributing to any downstream cell, strictly obeying obstacle semantics.

**Completeness.** Computing cells in topological order (row by row, left to right) ensures all potential incoming paths are aggregated before finalizing each cell. If the destination cell itself is an obstacle, it receives $DP = 0$, correctly identifying that zero paths reach the goal.

---

## 6. Traps This Instance Exposes

- **Obstacle at Start or Goal:** If $\text{obstacleGrid}[0][0] == 1$ or $\text{obstacleGrid}[M-1][N-1] == 1$, no valid path is possible. Returning $0$ immediately handles this correctly.
- **Obstacle Blocking Boundary Rows:** If $\text{obstacleGrid}[0][1] == 1$, all subsequent cells in Row 0 ($(0, 2), (0, 3), \dots$) have zero paths reaching them because the robot cannot jump over obstacles. The loop automatically handles this because $DP[0][c] = DP[0][c-1] = 0$.
- **Space Optimization:** An array of size $N$ updated in-place: `dp[c] = 0 if obstacle else dp[c] + dp[c-1]` solves the problem in $O(N)$ space.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$, where $M$ is the number of rows and $N$ is the number of columns. Each cell performs $O(1)$ operations.
- **Auxiliary Space Complexity:** $O(N)$ using a 1D running row array (or $O(M \cdot N)$ for the full 2D table).