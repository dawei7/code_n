# Sub-triangle Sums - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

In a triangular array of positive and negative integers, we wish to find a sub-triangle such that the sum of the numbers it contains is the smallest possible.

In the following example, it can be easily verified that the marked sub-triangle has a sum of $-42$:

$$
\begin{matrix}
 & & & & & 15 & & & & & \\
 & & & & -14 & & -7 & & & & \\
 & & & 20 & & -13 & & -5 & & & \\
 & & -3 & & 8 & & 23 & & -26 & & \\
 & 1 & & -4 & & -5 & & -18 & & 5 & \\
-16 & & 31 & & 2 & & 9 & & 28 & & 3
\end{matrix}
$$

A triangular array with one thousand ($1000$) rows ($500\,500$ elements) is generated using a pseudo-random number generator (a **Linear Congruential Generator**):
- $t = 0$.
- For each $k = 1 \dots 500\,500$:

$$
t \leftarrow (615949 t + 797807) \bmod 2^{20}
$$

$$
s_k = t - 2^{19} \in [-524288, 524287]
$$

The triangular array is filled row by row.

The objective is to find the **smallest sub-triangle sum in the $1000$-row triangular array**:

$$
\begin{aligned}
S_{\text{min}} = \min_{\substack{0 \le r < 1000 \\ 0 \le c \le r \\ 1 \le h \le 1000-r}} \sum_{d=0}^{h-1} \sum_{i=0}^d T_{r+d, c+i}
\end{aligned}
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### All-Cells Summation for Each Sub-Triangle
A naive approach loops through all $\frac{N(N+1)(N+2)}{6} \approx 1.67 \times 10^8$ sub-triangles and sums all $\mathcal{O}(h^2)$ elements inside:
```python
def naive_subtriangle_sums():
    # Summing all cells takes > 10^11 operations (> 5 minutes)
    # ...
```

### 1D Row Prefix Sums & Incremental Depth Expansion
1. **1D Row Prefix Sum Arrays:**
   Precompute prefix sums for each row $r$:

$$
\text{pref}[r][c] = \sum_{j=0}^{c-1} T_{r, j}
$$

   The sum of any contiguous segment of row $r$ from column $c$ to $c + d$ is evaluated in $\mathcal{O}(1)$ time:

$$
\text{segment\_sum} = \text{pref}[r][c + d + 1] - \text{pref}[r][c]
$$

2. **Incremental Height DP:**
   For any top vertex $(r, c)$, as we expand the sub-triangle height depth-by-depth ($d = 0, 1, 2, \dots$):

$$
\text{curr\_sum}_{d} = \text{curr\_sum}_{d-1} + \left( \text{pref}[r + d][c + d + 1] - \text{pref}[r + d][c] \right)
$$

3. Each sub-triangle addition takes exactly **$\mathcal{O}(1)$ operations**, reducing total complexity to $\approx 1.67 \times 10^8$ additions in $\approx 4.5$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Incremental Sub-Triangle Expansion from Top Vertex $(r, c)$

| Depth $d$ | Row Evaluated | Columns Spanned | Added Row Segment Sum | Sub-Triangle Size (Cells) |
| :---: | :---: | :---: | :---: | :---: |
| **$d = 0$** | Row $r$ | $[c, c]$ ($1$ cell) | $\text{pref}[r][c+1] - \text{pref}[r][c]$ | $1$ cell |
| **$d = 1$** | Row $r+1$ | $[c, c+1]$ ($2$ cells) | $\text{pref}[r+1][c+2] - \text{pref}[r+1][c]$ | $3$ cells |
| **$d = 2$** | Row $r+2$ | $[c, c+2]$ ($3$ cells) | $\text{pref}[r+2][c+3] - \text{pref}[r+2][c]$ | $6$ cells |
| **$\dots$** | $\dots$ | $\dots$ | $\dots$ | $\dots$ |
| **$d = h-1$** | Row $r+h-1$ | $[c, c+h-1]$ ($h$ cells)| $\text{pref}[r+h-1][c+h] - \text{pref}[r+h-1][c]$ | $\frac{h(h+1)}{2}$ cells |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Incremental Prefix Search Pipeline
1. Generate $500\,500$ pseudo-random values $s_k$ using LCG:

$$
t \leftarrow (615949 t + 797807) \bmod 2^{20}, \quad s_k = t - 2^{19}
$$

2. Populate row prefix sum array `row_pref`:

$$
\text{row\_pref}[r][c + 1] = \text{row\_pref}[r][c] + s_{\text{idx}}
$$

3. Set `min_sum = 0`.
4. For $r = 0 \dots 999$:
   - For $c = 0 \dots r$:
     - `curr_sum = 0`
     - For $\text{depth} = 0 \dots 999 - r$:
       - `curr_sum += (row_pref[r + depth][c + depth + 1] - row_pref[r + depth][c])`
       - If `curr_sum < min_sum`: `min_sum = curr_sum`
5. Return `min_sum = -271248680`.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Sample for 6-Row Triangle
- Triangle with rows:
  - Row 0: $[15]$
  - Row 1: $[-14, -7]$
  - Row 2: $[20, -13, -5]$
  - Row 3: $[-3, 8, 23, -26]$
  - Row 4: $[1, -4, -5, -18, 5]$
  - Row 5: $[-16, 31, 2, 9, 28, 3]$
- Sub-triangle with vertex at Row 1, Col 1 ($-7$):
  - Row 1: $[-7] \implies -7$.
  - Row 2: $[-13, -5] \implies -18$.
  - Row 3: $[8, 23, -26] \implies 5$.
  - Row 4: $[-4, -5, -18, 5] \implies -22$.
  - Total: $-7 - 18 + 5 - 22 = \mathbf{-42}$.
- Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for 1000-Row LCG Triangle
- Running full search over all $1.67 \times 10^8$ sub-triangles:

$$
S_{\text{min}} = \mathbf{-271\,248\,680}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **LCG Generator** | $t = (615949 t + 797807) \bmod 2^{20}; s_k = t - 2^{19}$ | $500\,500$ steps |
| **Stage 2** | **Row 1D Prefix** | `pref[c + 1] = pref[c] + s[idx]` | $\mathcal{O}(N^2)$ |
| **Stage 3** | **Vertex Loop $(r, c)$**| For $r \in [0, 999], c \in [0, r]$ | $500\,500$ vertices |
| **Stage 4** | **Incremental Depth**| `curr_sum += row_pref[r+d][c+d+1] - row_pref[r+d][c]` | $\mathcal{O}(1)$ per depth |
| **Stage 5** | **Min Tracker** | If `curr_sum < min_sum: min_sum = curr_sum` | $\mathcal{O}(1)$ |
| **Stage 6** | **Return Minimum** | Return scalar integer $-271248680$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N^3)$ where $N = 1000$ | $\approx 4.5$ seconds ($1.67 \times 10^8$ additions) |
| **Space Complexity** | $\mathcal{O}(N^2)$ | Row prefix table $\approx 4$ MB |
| **Dynamic Execution** | $100\%$ Inline | 1D prefix sum incremental sub-triangle expansion |

### Critical Invariants & Edge Cases Handled:
1. **Memory Compactness**: Storing prefix sums row-by-row requires only $\approx 4$ MB of memory, remaining strictly under our 100 MB ceiling.
2. **Negative Delta Initialization**: `min_sum` is initialized to 0, ensuring that any negative sub-triangle sum improves the optimal solution.