# Path Sum: Three Ways - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

In the $5 \times 5$ matrix below, the minimal path sum from any cell in the left column to any cell in the right column, by moving only **up**, **down**, and **right**, has a sum of $994$:
$$\begin{pmatrix}
131 & 673 & \mathbf{234} & \mathbf{103} & \mathbf{18} \\
\mathbf{201} & \mathbf{96} & \mathbf{342} & 965 & 150 \\
630 & 803 & 746 & 422 & 111 \\
537 & 699 & 497 & 121 & 956 \\
805 & 732 & 524 & 37 & 331
\end{pmatrix}$$

Let $\mathbf{T}$ denote the $80 \times 80$ integer matrix given in `matrix.txt`.
A valid 3-way path starts at any cell in the first column $(r_{\text{start}}, 0)$ and ends at any cell in the last column $(r_{\text{end}}, C-1)$, using only rightward $(r, c+1)$, upward $(r-1, c)$, and downward $(r+1, c)$ moves.

The objective is to find the **minimal path sum**:
$$S_{\text{min}} = \min_{0 \le r_{\text{start}}, r_{\text{end}} < R, \, \mathbf{P}} \sum_{(r, c) \in \mathbf{P}} T_{r, c}$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Graph Dijkstra Shortest Path
A naive algorithm models the grid as a directed graph and runs Dijkstra's algorithm from all cells in column 0:
```python
def naive_dijkstra_path_sum():
    # priority queue operations over all nodes and edges
    # ...
```

### Column-by-Column Dynamic Programming
1. Since moving to the **left is strictly forbidden**, path progression across columns is strictly unidirectional and acyclic ($c = 0 \to 1 \to \dots \to C-1$).
2. For each column $c$, we compute:
   - **Horizontal step:** $\text{next\_cost}[r] = \text{cost}[r] + T[r][c]$.
   - **Downward relaxation:** $\text{next\_cost}[r] = \min(\text{next\_cost}[r], \, \text{next\_cost}[r-1] + T[r][c])$.
   - **Upward relaxation:** $\text{next\_cost}[r] = \min(\text{next\_cost}[r], \, \text{next\_cost}[r+1] + T[r][c])$.
3. This evaluates the global minimum in $\mathcal{O}(R \cdot C)$ operations in $\approx 0.001$ seconds with $\mathcal{O}(R)$ space.

---

## 3. Core Intuition & Mathematical Structure

### Three-Way Movement DP Relaxation Sweeps

| Sweep Phase | Direction | Target Cells | Relaxation Formula |
| :---: | :---: | :---: | :--- |
| **Phase 1** | Horizontal Step | All $r \in [0, R-1]$ | $\text{next\_cost}[r] = \text{cost}[r] + T[r][c]$ |
| **Phase 2** | Downward Sweep | $r = 1 \dots R-1$ | $\text{next\_cost}[r] = \min(\text{next\_cost}[r], \text{next\_cost}[r-1] + T[r][c])$ |
| **Phase 3** | Upward Sweep | $r = R-2 \dots 0$ | $\text{next\_cost}[r] = \min(\text{next\_cost}[r], \text{next\_cost}[r+1] + T[r][c])$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Column-by-Column Transition Pipeline
1. Initialize $\text{cost} = [T[r][0] \text{ for } r \in [0, R-1]]$.
2. For $c = 1 \dots C-1$:
   - $\text{next\_cost} = [\text{cost}[r] + T[r][c] \text{ for } r \in [0, R-1]]$.
   - For $r = 1 \dots R-1$:
     $$\text{next\_cost}[r] \leftarrow \min(\text{next\_cost}[r], \, \text{next\_cost}[r-1] + T[r][c])$$
   - For $r = R-2 \dots 0$:
     $$\text{next\_cost}[r] \leftarrow \min(\text{next\_cost}[r], \, \text{next\_cost}[r+1] + T[r][c])$$
   - $\text{cost} \leftarrow \text{next\_cost}$.
3. Return $\min(\text{cost})$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for $5 \times 5$ Sample Matrix
- Optimal Path: $(1, 0) \to (1, 1) \to (1, 2) \to (0, 2) \to (0, 3) \to (0, 4)$.
- Cell sequence: $201 \to 96 \to 342 \to 234 \to 103 \to 18$.
- Total Path Sum:
  $$S = 201 + 96 + 342 + 234 + 103 + 18 = \mathbf{994}$$
- Matches problem statement sample! $\checkmark$

### Example 2: Target $80 \times 80$ Matrix
- Column-by-column DP on `matrix.txt`:
  $$S_{\text{min}} = \mathbf{260\,324}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **File Loading** | Read `matrix.txt` into 2D integer array | $\mathcal{O}(R \cdot C)$ |
| **Stage 2** | **Base Column** | `cost = [grid[r][0] for r in range(rows)]` | $\mathcal{O}(R)$ |
| **Stage 3** | **Column Loop** | For $c \in [1, C-1]$ | $C - 1$ columns |
| **Stage 4** | **Dual Relaxation** | Downward loop + Upward loop | $3R$ operations/col |
| **Stage 5** | **Return Value** | Return `min(cost) = 260324` | $\mathcal{O}(R)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(R \cdot C)$ where $R = C = 80$ | $\approx 0.001$ seconds |
| **Space Complexity** | $\mathcal{O}(R)$ | 1D column vector $\approx 640$ bytes |
| **Dynamic Execution** | $100\%$ Inline | Column-by-column dual vertical relaxation DP |

### Critical Invariants & Edge Cases Handled:
1. **Dynamic Path Resolution**: Resolves `matrix.txt` relative to package location without relying on external working directories.
2. **Dual-Pass Optimality**: The top-down and bottom-up passes guarantee that any optimal vertical travel within a single column is captured without redundant loops.
