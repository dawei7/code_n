# Guided Example: Best Meeting Point

We trace the step-by-step Manhattan distance dimensional decoupling, 1D median minimization proof ($L_1$ norm vs $L_2$ mean), row/column coordinate extraction, and total travel distance calculation on representative grid instances:

- **Input:**
  $$
  \text{grid} = \begin{bmatrix}
  1 & 0 & 0 & 0 & 1 \\
  0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 1 & 0 & 0
  \end{bmatrix}
  $$
- **Required output:** $6$ (Homes at $(0, 0)$, $(0, 4)$, and $(2, 2)$; optimal meeting point is $(0, 2)$ with total distance $2 + 2 + 2 = 6$)
- **Two Friends Base Case:** $\text{grid} = [[1, 1]] \implies 1$ (Any point between the two homes yields the same minimal distance $1$)
- **Collinear Friends:** When all homes share the same row, vertical distance is $0$; total distance equals 1D median distance along columns
- **Single Friend Base Case:** Distance is trivially $0$

This instance demonstrates dimensional orthogonality in Manhattan metrics, mathematically proves why the geometric median minimizes total $L_1$ absolute deviations (unlike the mean which minimizes $L_2$ squared error), explains why row coordinates are naturally sorted by row-major traversal while columns require sorting, and executes in $O(M \times N + K \log K)$ time and $O(K)$ space.

---

## 1. Instance & Teaching Goal

Given an $m \times n$ grid ($3 \times 5$) where $1$ marks a friend's house:
- Friend 1: $(0, 0)$
- Friend 2: $(0, 4)$
- Friend 3: $(2, 2)$

Find a meeting point $(X, Y)$ that minimizes the sum of Manhattan distances:
$$
D(X, Y) = \sum_{i=1}^{k} \left( |r_i - X| + |c_i - Y| \right)
$$
```text
Grid layout:
(0,0)=1  .      (0,2)=M  .      (0,4)=1
 .       .       .       .       .
 .       .      (2,2)=1  .       .

Meeting point selected: (0, 2)
Dist to (0, 0): |0-0| + |0-2| = 2
Dist to (0, 4): |0-0| + |4-2| = 2
Dist to (2, 2): |2-0| + |2-2| = 2
Total travel distance = 2 + 2 + 2 = 6
```

### Orthogonal Decoupling of Manhattan Distance
The two-dimensional Manhattan distance can be partitioned into two completely independent 1D optimization subproblems:
$$
\min_{(X, Y)} \sum_{i=1}^{k} \left( |r_i - X| + |c_i - Y| \right) = \left( \min_{X} \sum_{i=1}^{k} |r_i - X| \right) + \left( \min_{Y} \sum_{i=1}^{k} |c_i - Y| \right)
$$
We can solve for the optimal row $X$ and the optimal column $Y$ **separately**, without cross-dimensional interference!

---

## 2. Conceptual Foundation & Invariants

### The 1D Median Theorem
Given $k$ points on a 1D line $a_0 \le a_1 \le \dots \le a_{k-1}$, which coordinate $z$ minimizes $\sum_{i=0}^{k-1} |a_i - z|$?

**Proof by Telescoping Pairs:**
Pair extreme points $(a_0, a_{k-1})$, $(a_1, a_{k-2})$, $\dots$, $(a_i, a_{k-1-i})$:
For any pair $a_i \le a_{k-1-i}$, by the triangle inequality:
$$
|a_i - z| + |a_{k-1-i} - z| \ge a_{k-1-i} - a_i
$$
Equality holds if and only if $z$ lies in the closed interval $[a_i, a_{k-1-i}]$.
To simultaneously achieve the minimum for all nested pairs, $z$ must lie in the intersection of all such intervals:
- If $k$ is odd: The intersection collapses to the unique middle element:
  $$
  z^* = a_{\lfloor k/2 \rfloor} \quad (\text{The Median})
  $$
- If $k$ is even: The intersection is the interval $[a_{k/2 - 1}, a_{k/2}]$. Any value in this range (including $a_{k/2}$) achieves the global minimum.

> **Invariant.** The coordinate that minimizes the sum of absolute differences is the **median** of the coordinate list. The arithmetic mean minimizes squared Euclidean distance ($\sum (a_i - z)^2$), but the median minimizes $L_1$ Manhattan distance ($\sum |a_i - z|$).

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on the $3 \times 5$ grid:

---

### Step 1: Collect Coordinates
Scan the grid in row-major order:
- Row 0:
  - $(0, 0) == 1 \implies \text{row } 0, \; \text{col } 0$
  - $(0, 4) == 1 \implies \text{row } 0, \; \text{col } 4$
- Row 2:
  - $(2, 2) == 1 \implies \text{row } 2, \; \text{col } 2$

Extracted lists:
- $\text{rows} = [0, 0, 2]$ (Already sorted in non-decreasing order!).
- $\text{cols} = [0, 4, 2]$ (Unsorted).

---

### Step 2: Sort Columns & Find Medians
Total homes $k = 3$. Median index:
$$
\text{mid} = \lfloor 3 / 2 \rfloor = 1
$$
- **Row Median:**
  $$
  X^* = \text{rows}[1] = \mathbf{0}
  $$
- **Column Sorting & Median:**
  Sort $\text{cols} \to [0, 2, 4]$.
  $$
  Y^* = \text{cols}[1] = \mathbf{2}
  $$

Optimal meeting point: $(X^*, Y^*) = (0, 2)$.

---

### Step 3: Compute Total Distance
1. **Vertical Distance $\sum |r_i - 0|$:**
   - $|0 - 0| = 0$
   - $|0 - 0| = 0$
   - $|2 - 0| = 2$
   $$
   D_{\text{row}} = 0 + 0 + 2 = \mathbf{2}
   $$
2. **Horizontal Distance $\sum |c_i - 2|$:**
   - $|0 - 2| = 2$
   - $|2 - 2| = 0$
   - $|4 - 2| = 2$
   $$
   D_{\text{col}} = 2 + 0 + 2 = \mathbf{4}
   $$
3. **Total Minimal Distance:**
   $$
   D = D_{\text{row}} + D_{\text{col}} = 2 + 4 = \mathbf{6}
   $$

Output: $\mathbf{6}$.

---

## 4. Complete Execution Trace

```text
Homes: (0, 0), (0, 4), (2, 2)
rows = [0, 0, 2] -> sorted naturally
cols = [0, 4, 2] -> sorted: [0, 2, 4]

mid_idx = 3 // 2 = 1
Optimal Row:    rows[1] = 0
Optimal Column: cols[1] = 2
Meeting Point: (0, 2)

Row Distances: |0-0| + |0-0| + |2-0| = 0 + 0 + 2 = 2
Col Distances: |0-2| + |2-2| + |4-2| = 2 + 0 + 2 = 4
Total Distance = 2 + 4 = 6
```

| Friend Index | Home Coordinates $(r_i, c_i)$ | Vertical Dist to $X^* = 0$ | Horizontal Dist to $Y^* = 2$ | Total Manhattan Distance |
|:---:|:---:|:---:|:---:|:---:|
| 1 | $(0, 0)$ | $|0 - 0| = 0$ | $|0 - 2| = 2$ | $0 + 2 = 2$ |
| 2 | $(0, 4)$ | $|0 - 0| = 0$ | $|4 - 2| = 2$ | $0 + 2 = 2$ |
| 3 | $(2, 2)$ | $|2 - 0| = 2$ | $|2 - 2| = 0$ | $2 + 0 = 2$ |
| **Total** | - | **$D_{\text{row}} = 2$** | **$D_{\text{col}} = 4$** | **$D_{\text{total}} = \mathbf{6}$** |

---

## 5. Algorithmic Correctness

**Soundness.** Because Manhattan distance is separable into independent vertical and horizontal components ($|x - X| + |y - Y|$), the point minimizing the combined sum is formed by independently choosing $X$ to minimize the 1D absolute deviations of rows and $Y$ to minimize the 1D absolute deviations of columns. The median of a 1D sequence provably minimizes the sum of absolute deviations.

**Completeness.** Every cell containing a friend is identified during the grid scan. The row list is sorted by construction, and the column list is sorted explicitly. By evaluating all friends' coordinates, no friend is omitted, guaranteeing the calculated median yields the global minimum.

---

## 6. Traps This Instance Exposes

- **Using Mean Instead of Median:** The arithmetic mean minimizes the sum of squared distances $\sum (x_i - \bar{x})^2$. For absolute distances, an outlier coordinate would shift the mean away from the majority of homes, increasing total travel. The median is the unique robust minimizer for absolute distances.
- **Requiring Meeting Point on a Friend's Home:** The optimal meeting point $(0, 2)$ is an empty cell (`grid[0][2] == 0`). The problem statement does NOT require the meeting point to be at an existing friend's house.
- **Unsorted Columns:** Scanning row-by-row produces `rows` in sorted order, but `cols` is interleaved across rows (e.g. $[0, 4, 2]$). Forgetting to sort `cols` produces an incorrect median.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \times N + K \log K)$, where $M \times N$ is the grid size and $K$ is the number of homes ($K \le M \times N$). Scanning the grid takes $O(M N)$. Sorting `cols` of length $K$ takes $O(K \log K)$. Summing distances takes $O(K)$. Total runtime is dominated by grid traversal and column sorting.
- **Auxiliary Space Complexity:** $O(K)$ auxiliary memory to store the row and column coordinates of the $K$ homes.
