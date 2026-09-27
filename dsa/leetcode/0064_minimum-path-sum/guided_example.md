# Guided Example: Minimum Path Sum

We trace the step-by-step 2D dynamic programming grid cost minimization on a representative matrix instance:

- **Input:** $\text{grid} = \begin{pmatrix} 1 & 3 & 1 \\ 1 & 5 & 1 \\ 4 & 2 & 1 \end{pmatrix}$
- **Required output:** $7$

This instance demonstrates optimal substructure on a 2D cost grid, prefix accumulation along boundary edges, local bottleneck minimization ($\min(\text{top}, \text{left}) + \text{cost}$), and reconstructing the optimal path.

---

## 1. Instance & Teaching Goal

Given an $M \times N$ grid of non-negative integers ($M = 3, N = 3$), find a path from top-left $(0, 0)$ to bottom-right $(M - 1, N - 1)$ which minimizes the sum of all numbers along its path. You can only move either **down** or **right** at any point.

In the grid:
$$
\begin{pmatrix}
\mathbf{1} & \mathbf{3} & \mathbf{1} \\
1 & 5 & \mathbf{1} \\
4 & 2 & \mathbf{1}
\end{pmatrix}
$$
The optimal route travels right along the top row to $(0, 2)$ and then straight down the rightmost column to $(2, 2)$, accumulating:
$$
1 + 3 + 1 + 1 + 1 = 7
$$
Notice that choosing the locally smaller neighbor at $(1, 0)$ with cost $1$ leads to higher downstream costs ($1 + 1 + 5 + \dots$ or $1 + 1 + 4 + \dots \ge 8$). Dynamic programming evaluates global cumulative costs, avoiding greedy traps.

---

## 2. Conceptual Foundation & Invariants

### Cost Recurrence
Let $DP[r][c]$ be the minimum cumulative path sum required to reach cell $(r, c)$ from $(0, 0)$.

1. **Base Case:**
   Starting point cost is simply its own value:
   $$
   DP[0][0] = \text{grid}[0][0]
   $$
2. **Top Boundary (Row 0):**
   Can only be reached from the left:
   $$
   DP[0][c] = DP[0][c - 1] + \text{grid}[0][c] \quad \forall c \ge 1
   $$
3. **Left Boundary (Column 0):**
   Can only be reached from above:
   $$
   DP[r][0] = DP[r - 1][0] + \text{grid}[r][0] \quad \forall r \ge 1
   $$
4. **General Interior Cells ($r \ge 1, c \ge 1$):**
   Can be reached either from the cell above $(r - 1, c)$ or from the cell to the left $(r, c - 1)$:
   $$
   DP[r][c] = \text{grid}[r][c] + \min(DP[r - 1][c], \, DP[r][c - 1])
   $$

> **Invariant.** For every processed coordinate $(r, c)$, $DP[r][c]$ stores the strictly minimal path sum among all legal paths originating at $(0, 0)$ and terminating at $(r, c)$.

---

## 3. Step-by-Step Worked Execution

We construct the DP cost matrix for the $3 \times 3$ grid:

### Boundary Initialization
- **Start:** $DP[0][0] = \text{grid}[0][0] = 1$.
- **Row 0:**
  - $c = 1: DP[0][1] = 1 + 3 = 4$.
  - $c = 2: DP[0][2] = 4 + 1 = 5$.
  - Row 0 costs: $[1, 4, 5]$.
- **Column 0:**
  - $r = 1: DP[1][0] = 1 + 1 = 2$.
  - $r = 2: DP[2][0] = 2 + 4 = 6$.

---

### Interior Row 1 Evaluation
- $DP[1][0] = 2$.
- **Cell $(1, 1)$ ($\text{cost} = 5$):**
  - Path from top: $DP[0][1] = 4$.
  - Path from left: $DP[1][0] = 2$.
  - Optimal choice: $\min(4, 2) = 2$.
  - $DP[1][1] = 5 + 2 = 7$.
- **Cell $(1, 2)$ ($\text{cost} = 1$):**
  - Path from top: $DP[0][2] = 5$.
  - Path from left: $DP[1][1] = 7$.
  - Optimal choice: $\min(5, 7) = 5$.
  - $DP[1][2] = 1 + 5 = 6$.
- Row 1 costs: $[2, 7, 6]$.

---

### Interior Row 2 Evaluation
- $DP[2][0] = 6$.
- **Cell $(2, 1)$ ($\text{cost} = 2$):**
  - Path from top: $DP[1][1] = 7$.
  - Path from left: $DP[2][0] = 6$.
  - Optimal choice: $\min(7, 6) = 6$.
  - $DP[2][1] = 2 + 6 = 8$.
- **Cell $(2, 2)$ ($\text{cost} = 1$, Goal):**
  - Path from top: $DP[1][2] = 6$.
  - Path from left: $DP[2][1] = 8$.
  - Optimal choice: $\min(6, 8) = 6$.
  - $DP[2][2] = 1 + 6 = \mathbf{7}$.
- Row 2 costs: $[6, 8, 7]$.

Target minimum path sum is $DP[2][2] = 7$.

### Why Each Cell Commits to One Predecessor

The recurrence is a comparison, so every cell can be annotated with the two candidate totals it weighed and the winner it kept. Recording the direction also reconstructs the optimal route without storing parent pointers.

| Cell $(r, c)$ | $\text{grid}[r][c]$ | Arriving from above $DP[r-1][c]$ | Arriving from the left $DP[r][c-1]$ | $\min$ chosen | $DP[r][c]$ | Optimal arrival direction |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $(0, 0)$ | 1 | none (boundary) | none (boundary) | — | **1** | Start cell |
| $(0, 1)$ | 3 | none (row 0) | 1 | 1 | 4 | From the left |
| $(0, 2)$ | 1 | none (row 0) | 4 | 4 | 5 | From the left |
| $(1, 0)$ | 1 | 1 | none (column 0) | 1 | 2 | From above |
| $(1, 1)$ | 5 | 4 | 2 | 2 | 7 | From the left |
| $(1, 2)$ | 1 | 5 | 7 | 5 | 6 | From above |
| $(2, 0)$ | 4 | 2 | none (column 0) | 2 | 6 | From above |
| $(2, 1)$ | 2 | 7 | 6 | 6 | 8 | From the left |
| $(2, 2)$ | 1 | 6 | 8 | 6 | **7** | From above |

Reading the last column backwards from $(2, 2)$ yields $(2, 2) \leftarrow (1, 2) \leftarrow (0, 2) \leftarrow (0, 1) \leftarrow (0, 0)$, the five-cell route of total $7$. The tie-free winner at every cell is what makes that reconstruction unambiguous.

---

## 4. Complete Execution Trace

### 2D DP State Matrix ($3 \times 3$)

| Row $\downarrow$ / Col $\to$ | Col 0 | Col 1 | Col 2 | Notes |
|:---:|:---:|:---:|:---:|:---|
| **Row 0** | **1** | **4** | **5** | Optimal path traverses $(0, 0) \to (0, 1) \to (0, 2)$ |
| **Row 1** | 2 | 7 | **6** | Optimal path turns down to $(1, 2)$ |
| **Row 2** | 6 | 8 | **7 (Target)** | Optimal path finishes at $(2, 2)$ |

---

## 5. Algorithmic Correctness

**Soundness.** Any valid path into $(r, c)$ must have its penultimate step at $(r - 1, c)$ or $(r, c - 1)$. By the Principle of Optimality, the minimum sum to reach $(r, c)$ is the cell's own cost plus the minimum of the optimal sums to those two preceding positions.

**Completeness.** Evaluating cells in row-major order ensures that both prerequisite dependencies are finalized before each cell transition is computed. The bottom-right cell is guaranteed to reflect the global minimum over all possible paths.

---

## 6. Traps This Instance Exposes

- **Greedy Choice Fallacy:** Choosing the smaller immediate adjacent number (moving down to $(1, 0)$ with value $1$ rather than right to $(0, 1)$ with value $3$) traps the path into higher cumulative costs downstream. Dynamic programming avoids myopic local decisions.
- **In-Place Modification:** The input `grid` can be overwritten directly (`grid[r][c] += min(...)`), saving space and requiring $O(1)$ auxiliary memory.
- **Single Row / Single Column Grid:** A $1 \times N$ or $M \times 1$ grid has only one viable path (prefix sum). The boundary formulas handle this naturally without conditional exceptions.

The boundary rules are exactly the prefix sums, so each instance below can be checked from its two edges inward:

| Instance | Grid (rows top to bottom) | Row-0 prefix sums $DP[0][c]$ | Column-0 prefix sums $DP[r][0]$ | Goal computation | Expected output |
|:---|:---|:---|:---|:---|:---:|
| Single cell | `[5]` | `[5]` | `[5]` | The goal is the start cell | 5 |
| Rectangular grid | `[1,2,3]`, `[4,5,6]` | `[1, 3, 6]` | `[1, 5]` | `min(6, 8) + 6 = 12` | 12 |
| Main square | `[1,3,1]`, `[1,5,1]`, `[4,2,1]` | `[1, 4, 5]` | `[1, 2, 6]` | `min(6, 8) + 1 = 7` | 7 |
| Zero-valued route | `[0,9,9]`, `[0,0,9]`, `[9,0,0]` | `[0, 9, 18]` | `[0, 0, 9]` | `min(9, 0) + 0 = 0` | 0 |
| Greedy-trap grid | `[1,1,50,1]`, `[2,1,50,1]`, `[2,1,1,1]` | `[1, 2, 52, 53]` | `[1, 3, 5]` | `min(54, 5) + 1 = 6` | 6 |

The single-cell grid shows why $DP[0][0] = \text{grid}[0][0]$ rather than $1$: the start cell's own cost is part of every path, so a one-cell grid answers with its own value. The greedy-trap grid shows the same recurrence defeating a myopic choice: marching straight along row 0 costs $1 + 1 + 50 + 1 = 53$, while the detour through the $1$s costs only $6$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$, where $M$ is the number of rows and $N$ is the number of columns. Each cell performs $O(1)$ arithmetic operations.
- **Auxiliary Space Complexity:** $O(1)$ if mutating `grid` in place, or $O(N)$ if maintaining a single running row buffer.