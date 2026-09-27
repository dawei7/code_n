# Guided Example: Longest Increasing Path in a Matrix

We trace the step-by-step implicit Directed Acyclic Graph (DAG) formulation, strictly increasing neighbor traversal, memoized depth-first search (DFS with `@cache`), topological longest path propagation, and global maximum length extraction on representative grid instances:

- **Input:**
  $$
  \text{matrix} = \begin{bmatrix}
  9 & 9 & 4 \\
  6 & 6 & 8 \\
  2 & 1 & 1
  \end{bmatrix}
  $$
- **Required output:** $4$
  - Longest increasing path: $[1, 2, 6, 9]$
  - Coordinate sequence: $(2, 1) \to (2, 0) \to (1, 0) \to (0, 0)$
  - Values: $1 < 2 < 6 < 9$ (Length $= 4$)
- **Equal Neighbors Do Not Extend Path:** Paths require strict inequality ($>$); traversing between equal adjacent values (e.g. $9 \to 9$ or $1 \to 1$) is forbidden
- **Single Cell Matrix:** $[[5]] \implies 1$ (A path containing only itself has length 1)
- **Monotonically Decreasing Grid:** In a strictly decreasing grid, all paths have length 1 from each local peak

This instance demonstrates dynamic programming on implicit directed acyclic graphs, mathematically proves why strict value increase prevents directed cycles and eliminates the need for cycle detection visited sets, and analyzes $O(M N)$ time and auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an $M \times N = 3 \times 3$ matrix:
$$
\begin{bmatrix}
9 & 9 & 4 \\
6 & 6 & 8 \\
2 & 1 & 1
\end{bmatrix}
$$
Find the length of the longest path that moves in 4 cardinal directions (up, down, left, right) such that cell values are **strictly increasing**:
$$
\text{matrix}[x][y] > \text{matrix}[i][j]
$$

```text
Matrix values:
(0,0): 9   (0,1): 9   (0,2): 4
(1,0): 6   (1,1): 6   (1,2): 8
(2,0): 2   (2,1): 1   (2,2): 1

Optimal Path:
Start at (2, 1) [val = 1]
  -> Move Left to (2, 0)  [val = 2] (2 > 1)
  -> Move Up   to (1, 0)  [val = 6] (6 > 2)
  -> Move Up   to (0, 0)  [val = 9] (9 > 6)

Path: [1, 2, 6, 9] -> Length = 4
```

### Why the Graph is a DAG (Directed Acyclic Graph)
- From any cell $(i, j)$, a directed edge is drawn to an orthogonal neighbor $(x, y)$ if and only if $\text{matrix}[x][y] > \text{matrix}[i][j]$.
- Since every transition strictly increases the value, it is mathematically impossible to revisit an earlier cell in the same path.
- Therefore, the graph has **zero cycles**.
- The longest path problem on a general graph is NP-hard, but on a **DAG**, it can be solved in strictly linear $O(V + E)$ time using DFS with memoization!

---

## 2. Conceptual Foundation & Invariants

### 1. State Definition
Let $\text{dfs}(i, j)$ denote the length of the longest increasing path starting at cell $(i, j)$:
- Base case: A path consisting of just $(i, j)$ has length $1$.
- Recurrence:
  $$
  \text{dfs}(i, j) = 1 + \max_{(x, y) \in \text{valid neighbors}} \text{dfs}(x, y)
  $$
  where $(x, y)$ are in-bounds orthogonal neighbors satisfying $\text{matrix}[x][y] > \text{matrix}[i][j]$.
  If no such neighbor exists, the maximum is $0$, and $\text{dfs}(i, j) = 1$.

### 2. Four-Directional Offsets
Use pairwise delta coordinate scanning:
$$
\text{directions} = [(-1, 0), \; (0, 1), \; (1, 0), \; (0, -1)] \quad (\text{Up, Right, Down, Left})
$$

### 3. Global Solution
Evaluate the recurrence over every starting cell:
$$
\text{Result} = \max_{0 \le i < M, \; 0 \le j < N} \text{dfs}(i, j)
$$

> **Invariant.** For every cell $(i, j)$, $\text{dfs}(i, j)$ computes and caches the exact maximum length of any strictly increasing path originating at $(i, j)$.

---

## 3. Step-by-Step Worked Execution

We trace the recursive memoization on the $3 \times 3$ matrix:

---

### Step 1: Evaluate Local Peaks (Values of 9)
1. **Cell $(0, 0)$ [Value 9]:**
   - Neighbors: $(0, 1)$ [9], $(1, 0)$ [6].
   - Neither neighbor has value $> 9$.
   - $\text{dfs}(0, 0) = 1 + 0 = \mathbf{1}$.
2. **Cell $(0, 1)$ [Value 9]:**
   - Neighbors: $(0, 0)$ [9], $(0, 2)$ [4], $(1, 1)$ [6].
   - No neighbor $> 9$.
   - $\text{dfs}(0, 1) = 1 + 0 = \mathbf{1}$.

---

### Step 2: Evaluate Upper-Level Nodes (Values of 6 and 8)
1. **Cell $(1, 2)$ [Value 8]:**
   - Neighbors: $(0, 2)$ [4], $(1, 1)$ [6], $(2, 2)$ [1].
   - No neighbor $> 8$.
   - $\text{dfs}(1, 2) = 1 + 0 = \mathbf{1}$.
2. **Cell $(1, 0)$ [Value 6]:**
   - Neighbors: $(0, 0)$ [9], $(2, 0)$ [2], $(1, 1)$ [6].
   - Only neighbor $(0, 0)$ [9] is $> 6$.
   - $\text{dfs}(1, 0) = 1 + \text{dfs}(0, 0) = 1 + 1 = \mathbf{2}$.
3. **Cell $(1, 1)$ [Value 6]:**
   - Neighbors: $(0, 1)$ [9], $(2, 1)$ [1], $(1, 0)$ [6], $(1, 2)$ [8].
   - Neighbors with greater values: $(0, 1)$ [9] and $(1, 2)$ [8].
   - $\text{dfs}(1, 1) = 1 + \max(\text{dfs}(0, 1), \text{dfs}(1, 2)) = 1 + \max(1, 1) = \mathbf{2}$.

---

### Step 3: Evaluate Cell $(2, 0)$ [Value 2]
- Neighbors: $(1, 0)$ [6], $(2, 1)$ [1].
- Neighbor $(1, 0)$ [6] is $> 2$.
- Path extends through $(1, 0)$:
  $$
  \text{dfs}(2, 0) = 1 + \text{dfs}(1, 0) = 1 + 2 = \mathbf{3}
  $$
  (Path: $(2, 0) [2] \to (1, 0) [6] \to (0, 0) [9]$).

---

### Step 4: Evaluate Cell $(2, 1)$ [Value 1] (Global Origin!)
- Neighbors of $(2, 1)$ [1]:
  - Up: $(1, 1)$ [6] ($6 > 1$). Cached $\text{dfs}(1, 1) = 2$.
  - Left: $(2, 0)$ [2] ($2 > 1$). Cached $\text{dfs}(2, 0) = 3$.
  - Right: $(2, 2)$ [1] (Not greater; $1 \ngtr 1$).
- Calculate optimal continuation:
  $$
  \text{dfs}(2, 1) = 1 + \max(\text{dfs}(1, 1), \; \text{dfs}(2, 0)) = 1 + \max(2, 3) = 1 + 3 = \mathbf{4}
  $$
- Longest path discovered:
  $$
  (2, 1) [1] \longrightarrow (2, 0) [2] \longrightarrow (1, 0) [6] \longrightarrow (0, 0) [9] \quad (\text{Length } 4)
  $$

---

### Step 5: Global Maximum Extraction
Scanning all cells $(i, j)$ in the matrix:
The maximum cached value is $\text{dfs}(2, 1) = \mathbf{4}$.

---

## 4. Complete Execution Trace

```text
matrix:
[ [9, 9, 4],
  [6, 6, 8],
  [2, 1, 1] ]

dfs evaluations:
dfs(0, 0) [9] -> no greater neighbor -> 1
dfs(0, 1) [9] -> no greater neighbor -> 1
dfs(1, 2) [8] -> no greater neighbor -> 1
dfs(0, 2) [4] -> neighbors (0,1)[9], (1,2)[8] -> 1 + max(1, 1) = 2
dfs(1, 0) [6] -> neighbor (0,0)[9] -> 1 + dfs(0,0) = 1 + 1 = 2
dfs(1, 1) [6] -> neighbors (0,1)[9], (1,2)[8] -> 1 + max(1, 1) = 2
dfs(2, 0) [2] -> neighbor (1,0)[6] -> 1 + dfs(1,0) = 1 + 2 = 3
dfs(2, 1) [1] -> neighbors (2,0)[2], (1,1)[6] -> 1 + max(3, 2) = 4 (MAX!)
dfs(2, 2) [1] -> neighbor (1,2)[8] -> 1 + dfs(1,2) = 1 + 1 = 2

Global Maximum = 4
```

| Cell $(i, j)$ | Matrix Value | Valid Greater Neighbors | Transitions Evaluated | Child Sub-lengths | Computed $\text{dfs}(i, j)$ |
|:---:|:---:|:---|:---|:---:|:---:|
| $(0, 0)$ | 9 | None | - | - | 1 |
| $(0, 1)$ | 9 | None | - | - | 1 |
| $(1, 2)$ | 8 | None | - | - | 1 |
| $(0, 2)$ | 4 | $(0, 1)$ [9], $(1, 2)$ [8] | $1 + \max(\text{dfs}(0, 1), \text{dfs}(1, 2))$ | $\max(1, 1)$ | 2 |
| $(1, 0)$ | 6 | $(0, 0)$ [9] | $1 + \text{dfs}(0, 0)$ | $1$ | 2 |
| $(1, 1)$ | 6 | $(0, 1)$ [9], $(1, 2)$ [8] | $1 + \max(\text{dfs}(0, 1), \text{dfs}(1, 2))$ | $\max(1, 1)$ | 2 |
| $(2, 0)$ | 2 | $(1, 0)$ [6] | $1 + \text{dfs}(1, 0)$ | $2$ | 3 |
| **$(2, 1)$** | **1** | **$(2, 0)$ [2], $(1, 1)$ [6]** | **$1 + \max(\text{dfs}(2, 0), \text{dfs}(1, 1))$** | **$\max(3, 2) = 3$** | **$\mathbf{4}$ (Max)** |
| $(2, 2)$ | 1 | $(1, 2)$ [8] | $1 + \text{dfs}(1, 2)$ | $1$ | 2 |

---

## 5. Algorithmic Correctness

**Soundness.** Because transitions are restricted to strictly greater neighbors ($\text{matrix}[x][y] > \text{matrix}[i][j]$), the underlying graph is acyclic. A topological DAG traversal guarantees that the longest path from any node is well-defined. Memoizing $\text{dfs}(i, j)$ returns the optimal suffix path length without redundant re-evaluation.

**Completeness.** Every cell $(i, j)$ in the $M \times N$ matrix is considered as a potential starting position. Since $\text{dfs}(i, j)$ exhaustively checks all 4 cardinal neighbors and records the maximum, no longer increasing path can exist.

---

## 6. Traps This Instance Exposes

- **Exponential Time Without Memoization:** Naive DFS without caching explores every path independently, leading to $O(4^{MN})$ worst-case time complexity. Memoization reduces runtime to $O(MN)$.
- **Strict vs Non-Decreasing Inequality:** The problem specifies strictly increasing paths. Neighbors with equal values ($\text{matrix}[x][y] == \text{matrix}[i][j]$) must NOT be traversed.
- **Unnecessary Visited Set:** In general graphs, cycles require maintaining a `visited` set to avoid infinite loops. Because values strictly increase here, cycles are impossible, making a `visited` set redundant.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \cdot N)$, where $M, N$ are grid dimensions. There are $M \cdot N$ states in the memoization table. Each state explores at most 4 orthogonal neighbors, costing $O(1)$ operations per state.
- **Auxiliary Space Complexity:** $O(M \cdot N)$ auxiliary memory for the memoization cache and the recursion stack.
