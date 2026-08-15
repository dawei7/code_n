# Maximum Path Sum I - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $T$ be a triangular array of non-negative integers containing $R = 15$ rows, where row $r \in [0, R-1]$ contains $r + 1$ elements denoted by $T[r][c]$ for $c \in [0, r]$.

A valid top-to-bottom path is a sequence of cells $((0, c_0), (1, c_1), \dots, (R-1, c_{R-1}))$ where $c_0 = 0$ and $c_{k+1} \in \{c_k, c_k + 1\}$ for all $k \in [0, R-2]$.

The objective is to compute the maximum total path sum:
$$S_{\text{max}} = \max_{(c_0, \dots, c_{R-1})} \sum_{r=0}^{R-1} T[r][c_r]$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Exhaustive Path Enumeration
A naive algorithm enumerates every valid path from apex to base:
```python
def naive_path_sum(triangle, r=0, c=0):
    if r == len(triangle) - 1:
        return triangle[r][c]
    return triangle[r][c] + max(
        naive_path_sum(triangle, r + 1, c),
        naive_path_sum(triangle, r + 1, c + 1)
    )
```

### Computational Inefficiencies
1. **Exponential Path Count $\mathcal{O}(2^R)$**: An $R$-row triangle has $2^{R-1}$ unique paths ($2^{14} = 16\,384$ for $R=15$, and $2^{99} \approx 6.33 \times 10^{29}$ for $R=100$).
2. **Superiority of Bottom-Up DP**: Collapsing the triangle upwards from bottom to top computes the exact maximum in $\mathcal{O}(R^2)$ operations ($105$ additions).

---

## 3. Core Intuition & Mathematical Structure

By Bellman's Principle of Optimality, the maximum path sum from cell $(r, c)$ to the base is:
$$V(r, c) = T[r][c] + \max(V(r+1, c), V(r+1, c+1))$$
with base condition $V(R-1, c) = T[R-1][c]$.

### Bottom-Up Dynamic Programming Transition

| Stage | Operation | Recurrence / Action | Cell Operations Count |
| :--- | :--- | :--- | :---: |
| **Base Case** | Row $R-1$ (Row 14) | Identity initialization | $15$ cells |
| **Step $r$** | Row $r \in [R-2, 0]$ | $T[r][c] \leftarrow T[r][c] + \max(T[r+1][c], T[r+1][c+1])$ | $r+1$ updates |
| **Apex Solution** | Row $0$, Col $0$ | $T[0][0]$ holds global optimal sum | $1$ cell |
| **Total Operations** | — | $\sum_{r=1}^{R-1} r = \frac{R(R-1)}{2}$ | **$105$ Additions** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### In-Place Reduction
By reducing the triangle from row $R-2$ up to $0$:
1. At row $r$, each cell $(r, c)$ has two downward choices: $(r+1, c)$ and $(r+1, c+1)$.
2. Both sub-paths have already been maximized.
3. Updating $T[r][c] \leftarrow T[r][c] + \max(T[r+1][c], T[r+1][c+1])$ operates completely in-place.
4. When $r = 0$, $T[0][0]$ is the global maximum path sum.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Evaluation on 4-Row Sample Triangle
$$\begin{matrix}
& & & 3 & & & \\
& & 7 & & 4 & & \\
& 2 & & 4 & & 6 & \\
8 & & 5 & & 9 & & 3
\end{matrix}$$

1. **Reduce Row 2** (above base):
   - Cell $(2, 0)$: $2 + \max(8, 5) = 2 + 8 = 10$
   - Cell $(2, 1)$: $4 + \max(5, 9) = 4 + 9 = 13$
   - Cell $(2, 2)$: $6 + \max(9, 3) = 6 + 9 = 15$
   - Row 2 becomes: $[10, 13, 15]$.
2. **Reduce Row 1**:
   - Cell $(1, 0)$: $7 + \max(10, 13) = 7 + 13 = 20$
   - Cell $(1, 1)$: $4 + \max(13, 15) = 4 + 15 = 19$
   - Row 1 becomes: $[20, 19]$.
3. **Reduce Row 0 (Apex)**:
   - Cell $(0, 0)$: $3 + \max(20, 19) = 3 + 20 = \mathbf{23}$.
   - Optimal path: $3 \to 7 \to 4 \to 9 = 23$. Matches sample! $\checkmark$

### Example 2: Target Evaluation on 15-Row Triangle
- Reducing 15 rows bottom-up in-place:
  $$S_{\text{max}} = T[0][0] = \mathbf{1074}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Ragged Grid Parsing** | Parse multiline text into 2D integer array $T$ | $\mathcal{O}(R^2)$ |
| **Stage 2** | **Bottom-Up DP Loop** | For $r \in [R-2, \dots, 0]$ step $-1$ | $R-1$ rows |
| **Stage 3** | **Cell Max Addition** | $T[r][c] += \max(T[r+1][c], T[r+1][c+1])$ | $105$ updates |
| **Stage 4** | **Return Apex** | Return $T[0][0] = 1074$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(R^2)$ | $\approx 0.00004$ seconds for $R = 15$ |
| **Space Complexity** | $\mathcal{O}(R^2)$ | Ragged array storage $\approx 2$ KB |
| **Dynamic Execution** | $100\%$ Inline | Bottom-up Bellman reduction |

### Critical Invariants & Edge Cases Handled:
1. **In-Place Mutation**: Modifying the rows in descending order ensures no cell is overwritten before its parents use it.
2. **Boundary Children**: A cell at column $c$ always has exactly two children $(r+1, c)$ and $(r+1, c+1)$ since row $r+1$ has length $r+2$.
