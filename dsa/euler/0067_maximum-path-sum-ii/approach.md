# Maximum Path Sum II - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $\mathbf{T}$ denote a 100-row triangular grid of positive integers, where cell $(r, c)$ contains value $T_{r, c}$ for $0 \le c \le r < R = 100$.

A valid path starts at the top apex $(0, 0)$ and moves to adjacent numbers in the row below, choosing at each step between $(r+1, c)$ and $(r+1, c+1)$.

The objective is to find the maximum total path sum from top to bottom of `triangle.txt`:

$$
S_{\text{max}} = \max_{\mathbf{P}} \sum_{i=0}^{R-1} T_{i, c_i} \quad \text{where } c_0 = 0 \text{ and } c_{i+1} \in \{c_i, c_i + 1\}
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Full Path Enumeration
A naive recursive algorithm traverses every possible path from top to bottom:
```python
def naive_max_path_sum():
    # explores all 2^(R-1) = 2^99 ≈ 6.33 x 10^29 paths!
    # ...
```

### Computational Inefficiencies
1. **Exponential Paths $2^{99}$**: An exhaustive brute force search would take $> 10^{13}$ years of CPU time.
2. **Bottom-Up Dynamic Programming**: By Bellman's Principle of Optimality, collapsing the triangle bottom-up evaluates the global maximum in exactly $\frac{100 \times 101}{2} = 5050$ additions in $\approx 0.002$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Bottom-Up Dynamic Programming Formulation
Let $DP[r][c]$ be the maximum path sum from cell $(r, c)$ down to the base row $R-1$:

$$
DP[r][c] = \begin{cases} T_{r, c} & \text{if } r = R - 1 \\ T_{r, c} + \max(DP[r+1][c], \, DP[r+1][c+1]) & \text{if } 0 \le r < R - 1 \end{cases}
$$

### Triangle In-Place Collapse Progression

| Row $r$ | Operation | New Row Values $DP[r][c] = T[r][c] + \max(DP[r+1][c], DP[r+1][c+1])$ |
| :---: | :--- | :--- |
| **$R-1 = 99$** | Base Row | Initial raw values from `triangle.txt` |
| **$R-2 = 98$** | Step 1 | $T_{98, c} + \max(T_{99, c}, T_{99, c+1})$ |
| **$\dots$** | $\dots$ | $\dots$ |
| **$r = 0$ (Apex)** | Final Step | $DP[0][0] = T_{0, 0} + \max(DP[1][0], DP[1][1]) = \mathbf{7273}$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### In-Place Reduction Algorithm
1. Parse the 100 rows of integers into a 2D list `grid`.
2. For $r = 98, 97, \dots, 0$:
   - For $c = 0 \dots r$:

$$
\text{grid}[r][c] \leftarrow \text{grid}[r][c] + \max(\text{grid}[r+1][c], \, \text{grid}[r+1][c+1])
$$

3. The value remaining at $\text{grid}[0][0]$ is the global maximum path sum.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for 4-Row Sample Triangle

$$
\begin{matrix}
&&& \mathbf{3} &&& \\
&& 7 && 4 && \\
& 2 && 4 && 6 & \\
8 && 5 && 9 && 3
\end{matrix}
$$

- **Row 2 (Collapsing Row 3):**
  - $c=0: 2 + \max(8, 5) = 2 + 8 = \mathbf{10}$
  - $c=1: 4 + \max(5, 9) = 4 + 9 = \mathbf{13}$
  - $c=2: 6 + \max(9, 3) = 6 + 9 = \mathbf{15}$
- **Row 1 (Collapsing Row 2):**
  - $c=0: 7 + \max(10, 13) = 7 + 13 = \mathbf{20}$
  - $c=1: 4 + \max(13, 15) = 4 + 15 = \mathbf{19}$
- **Row 0 (Apex):**
  - $c=0: 3 + \max(20, 19) = 3 + 20 = \mathbf{23}$
- Max Path Sum: $3 \to 7 \to 4 \to 9 \implies \mathbf{23} \checkmark$.

### Example 2: Target 100-Row Triangle
- Collapsing `triangle.txt` from row 98 down to row 0:

$$
S_{\text{max}} = \mathbf{7273}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **File Loading** | Parse lines of `triangle.txt` into 2D array | $\mathcal{O}(R^2)$ |
| **Stage 2** | **Bottom-Up Loop** | For $r \in [R-2, 0]$ step $-1$ | $99$ rows |
| **Stage 3** | **In-Place Collapse** | `grid[r][c] += max(grid[r+1][c], grid[r+1][c+1])` | $5050$ additions |
| **Stage 4** | **Return Apex** | Return `grid[0][0] = 7273` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(R^2)$ where $R = 100$ ($5050$ operations) | $\approx 0.002$ seconds |
| **Space Complexity** | $\mathcal{O}(R^2)$ | 2D matrix $\approx 20$ KB |
| **Dynamic Execution** | $100\%$ Inline | In-place dynamic programming collapse |

### Critical Invariants & Edge Cases Handled:
1. **Dynamic Path Resolution**: Resolves `triangle.txt` relative to package location without relying on external working directories.
2. **Boundary Children Matching**: Cell $(r, c)$ accesses exactly $(r+1, c)$ and $(r+1, c+1)$, which are guaranteed to exist within the triangular bounds.