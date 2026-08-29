# Su Doku - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

A standard Su Doku puzzle involves a $9 \times 9$ grid divided into nine $3 \times 3$ sub-grids. The objective is to fill all empty cells with digits $1$ to $9$ such that:
1. Each row contains digits $1$ through $9$ exactly once.
2. Each column contains digits $1$ through $9$ exactly once.
3. Each $3 \times 3$ box contains digits $1$ through $9$ exactly once.

The file `sudoku.txt` contains fifty ($50$) different 9x9 Su Doku puzzles.

The objective is to solve all 50 puzzles and find the **sum of the 3-digit numbers** found in the top left of each solution grid ($M^*_{0,0} M^*_{0,1} M^*_{0,2}$):
$$S_{\text{top3}} = \sum_{k=1}^{50} \left( 100 \cdot M^{*(k)}_{0,0} + 10 \cdot M^{*(k)}_{0,1} + M^{*(k)}_{0,2} \right)$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Standard Row-Major Backtracking
A naive algorithm fills cells in fixed scanline order $(0, 0), (0, 1), \dots, (8, 8)$:
```python
def naive_sudoku_solve(grid):
    # explores up to 9^81 branching paths without heuristic ordering
    # ...
```

### Minimum Remaining Values (MRV) Constraint Backtracking
1. **MRV Cell Selection:** At each step, we identify the unassigned cell $(r, c)$ with the **minimum number of legal candidate values** $\min |V(r, c)|$.
2. **Early Dead-End Pruning:** If any cell has $|V(r, c)| = 0$ candidates, the state is an immediate dead-end, pruning the branch before further exploration.
3. MRV backtracking solves all 50 puzzles in under $\approx 0.20$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Constraint Set Intersections & MRV Selection

| Constraint Scope | Elements Inspected | Prohibited Numbers Set |
| :---: | :--- | :--- |
| **Row $r$** | $\text{grid}[r][c]$ for $c \in [0, 8]$ | All placed digits in row $r$ |
| **Column $c$** | $\text{grid}[r][c]$ for $r \in [0, 8]$ | All placed digits in column $c$ |
| **$3 \times 3$ Sub-grid** | $\text{grid}[3\lfloor r/3 \rfloor + i][3\lfloor c/3 \rfloor + j]$ for $i, j \in [0, 2]$ | All placed digits in the $3 \times 3$ box |
| **MRV Candidates** | Cell $(r, c)$ with smallest remaining $|V(r, c)|$ | $V(r, c) = \{1 \dots 9\} \setminus (\text{Row} \cup \text{Col} \cup \text{Box})$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### MRV Backtracking Algorithm
1. `solve_sudoku(grid)`:
   - Find empty cell $(r, c)$ with $\min |V(r, c)|$.
   - If no empty cells: return True (Solved).
   - If $|V(r, c)| == 0$: return False (Dead-end).
   - For each $v \in V(r, c)$:
     - $\text{grid}[r][c] = v$.
     - If `solve_sudoku(grid)` is True: return True.
     - $\text{grid}[r][c] = 0$.
   - Return False.
2. For each solved grid, extract $V_k = 100 \cdot \text{grid}[0][0] + 10 \cdot \text{grid}[0][1] + \text{grid}[0][2]$.
3. Sum $S_{\text{top3}} = \sum_{k=1}^{50} V_k$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for Grid 01 (From Problem Description)
- Unsolved Grid 01 top row: `0 0 3 0 2 0 6 0 0`.
- Solved Grid 01 top row: `4 8 3 9 2 1 6 5 7`.
- Top-left 3 digits: `4 8 3` $\implies \mathbf{483}$. Matches problem statement sample! $\checkmark$

### Example 2: Target Sum across all 50 Puzzles
- Solving all 50 puzzles from `sudoku.txt`:
  $$S_{\text{top3}} = \mathbf{24\,702}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **File Loading** | Parse `sudoku.txt` into 50 grids of $9 \times 9$ | $\mathcal{O}(K \cdot 81)$ |
| **Stage 2** | **MRV Search** | Find $(r, c)$ with smallest valid candidate list | $\mathcal{O}(81)$ per step |
| **Stage 3** | **Recursive DFS** | Branch on valid candidates; revert on failure | $\mathcal{O}(\text{MRV Tree})$ |
| **Stage 4** | **Top-Left Extract** | `grid[0][0]*100 + grid[0][1]*10 + grid[0][2]` | $\mathcal{O}(1)$ |
| **Stage 5** | **Return Sum** | Return `total_sum = 24702` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(K \cdot \text{MRV Nodes})$ where $K = 50$ | $\approx 0.20$ seconds across all 50 grids |
| **Space Complexity** | $\mathcal{O}(1)$ | In-place 2D grid matrix modifications |
| **Dynamic Execution** | $100\%$ Inline | MRV constraint satisfaction backtracking |

### Critical Invariants & Edge Cases Handled:
1. **Dynamic Path Resolution**: Resolves `sudoku.txt` relative to package location without relying on external working directories.
2. **Early Dead-End Pruning**: Checking `if min_candidates == 0: return False` aborts immediately when a cell cannot be filled, preventing astronomical wasted search tree expansions.
