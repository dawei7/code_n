# Path Sum: Two Ways - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

In the $5 \times 5$ matrix below, the minimal path sum from the top left to the bottom right by moving only right and down has a sum of $2427$:

$$
\begin{pmatrix}
\mathbf{131} & 673 & 234 & 103 & 18 \\
\mathbf{201} & \mathbf{96} & \mathbf{342} & 965 & 150 \\
630 & 803 & \mathbf{746} & \mathbf{422} & 111 \\
537 & 699 & 497 & \mathbf{121} & 956 \\
805 & 732 & 524 & \mathbf{37} & \mathbf{331}
\end{pmatrix}
$$

Let $\mathbf{T}$ denote the $80 \times 80$ integer matrix given in `matrix.txt`.
A valid path $\mathbf{P} = ((r_0, c_0), \dots, (r_k, c_k))$ starts at top-left $(0, 0)$ and reaches bottom-right $(R-1, C-1)$ using only rightward $(r, c+1)$ and downward $(r+1, c)$ moves.

The objective is to find the **minimal path sum** from top-left to bottom-right:

$$
S_{\text{min}} = \min_{\mathbf{P}} \sum_{(r, c) \in \mathbf{P}} T_{r, c}
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Combinatorial Path Enumeration
A naive recursive algorithm explores every path moving right and down:
```python
def naive_min_path_sum(r, c):
    # explores all C(158, 79) ≈ 4.43 x 10^46 paths!
    # ...
```

### 2D Dynamic Programming Formulation
1. Any cell $(r, c)$ can only be entered from the cell above $(r-1, c)$ or the cell to the left $(r, c-1)$.
2. By Bellman's Principle of Optimality:

$$
DP[r][c] = T[r][c] + \min(DP[r-1][c], \, DP[r][c-1])
$$

3. The global minimum is computed in exactly $80 \times 80 = 6400$ state transitions in $\approx 0.001$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### DP Boundary Conditions & Transitions

| Matrix Region | Coordinates | In-Degree Directions | DP Transition Formula |
| :---: | :---: | :---: | :--- |
| **Apex** | $(0, 0)$ | Origin | $DP[0][0] = T[0][0]$ |
| **Top Edge** | $r = 0, \, c > 0$ | Left only | $DP[0][c] = T[0][c] + DP[0][c-1]$ |
| **Left Edge** | $r > 0, \, c = 0$ | Above only | $DP[r][0] = T[r][0] + DP[r-1][0]$ |
| **Interior Cells** | $r > 0, \, c > 0$ | Left and Above | $DP[r][c] = T[r][c] + \min(DP[r-1][c], DP[r][c-1])$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### In-Place Matrix Update Algorithm
1. Parse the 80 lines of comma-separated integers from `matrix.txt` into `grid`.
2. First row prefix sum:

$$
\text{grid}[0][c] \leftarrow \text{grid}[0][c] + \text{grid}[0][c-1] \quad \forall c \in [1, C-1]
$$

3. First column prefix sum:

$$
\text{grid}[r][0] \leftarrow \text{grid}[r][0] + \text{grid}[r-1][0] \quad \forall r \in [1, R-1]
$$

4. Interior cells:

$$
\text{grid}[r][c] \leftarrow \text{grid}[r][c] + \min(\text{grid}[r-1][c], \, \text{grid}[r][c-1]) \quad \forall r \ge 1, c \ge 1
$$

5. The result is stored at $\text{grid}[R-1][C-1]$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for $5 \times 5$ Sample Matrix
- Path: $131 \to 201 \to 96 \to 342 \to 746 \to 422 \to 121 \to 37 \to 331$.
- Total Path Sum:

$$
S = 131 + 201 + 96 + 342 + 746 + 422 + 121 + 37 + 331 = \mathbf{2427}
$$

- Matches problem statement sample! $\checkmark$

### Example 2: Target $80 \times 80$ Matrix
- Updating all 6400 cells of `matrix.txt`:

$$
S_{\text{min}} = \mathbf{427\,337}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **File Loading** | Read `matrix.txt` into 2D integer array | $\mathcal{O}(R \cdot C)$ |
| **Stage 2** | **Top Row Prefix** | `grid[0][c] += grid[0][c-1]` | $C - 1$ steps |
| **Stage 3** | **Left Col Prefix** | `grid[r][0] += grid[r-1][0]` | $R - 1$ steps |
| **Stage 4** | **2D DP Collapse** | `grid[r][c] += min(grid[r-1][c], grid[r][c-1])` | $(R-1)(C-1)$ steps |
| **Stage 5** | **Return Value** | Return `grid[-1][-1] = 427337` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(R \cdot C)$ where $R = C = 80$ | $\approx 0.001$ seconds |
| **Space Complexity** | $\mathcal{O}(R \cdot C)$ | 2D matrix $\approx 25$ KB |
| **Dynamic Execution** | $100\%$ Inline | In-place 2D grid DP transitions |

### Critical Invariants & Edge Cases Handled:
1. **Dynamic Path Resolution**: Resolves `matrix.txt` relative to package location without relying on external working directories.
2. **Boundary Prefix Accumulation**: First row and first column have exactly one incoming direction, preventing index out-of-bounds errors.