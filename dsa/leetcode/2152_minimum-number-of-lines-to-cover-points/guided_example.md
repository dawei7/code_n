# Guided Example: Minimum Number of Lines to Cover Points

We analyze and execute the bitmask dynamic programming set-cover algorithm on a representative planar geometry instance, demonstrating how cross-product collinearity grouping eliminates geometric redundancy.

- **Input:** `points = [[0, 1], [2, 3], [4, 5], [4, 3]]`
- **Output:** `2`

This instance illustrates cross-product collinearity verification, line bitmask generation, fixed-point pivot branch reduction, and memoized subset cover.

---

## 1. Problem Overview & Representative Instance

Given an array `points` of $n$ distinct coordinates on the 2D Cartesian plane, we wish to place the minimum number of straight lines such that every point lies on at least one line.
- A single straight line can pass through any number of collinear points.
- Any single point or any pair of points can trivially be covered by one line.
- Lines may intersect freely, and a point may belong to multiple lines.

We must find the absolute minimum number of lines needed to cover all $n$ points.

In our representative instance:
- $n = 4$ points:
  - $P_0 = (0, 1)$
  - $P_1 = (2, 3)$
  - $P_2 = (4, 5)$
  - $P_3 = (4, 3)$

Notice that $P_0, P_1,$ and $P_2$ all lie along the line $y = x + 1$. Point $P_3 = (4, 3)$ is non-collinear with this trio. We must determine the minimal line cover.

---

## 2. Mathematical & Algorithmic Principles

### Exact Collinearity via Integer Cross Products

Three distinct points $A = (x_1, y_1)$, $B = (x_2, y_2)$, and $C = (x_3, y_3)$ are collinear if and only if the cross product of the displacement vectors $\vec{AB}$ and $\vec{AC}$ vanishes:
$$(x_2 - x_1)(y_3 - y_1) - (y_2 - y_1)(x_3 - x_1) = 0$$

Using cross products avoids floating-point division, round-off error, and separate handling of vertical lines with infinite slope ($x_2 = x_1$).

### Maximal Line Bitmask Precomputation

With $n \le 10$, each subset of points can be represented by an integer bitmask in $[0, 2^n - 1]$. For every pair of points $(i, j)$ with $0 \le i < j < n$, we construct a bitmask $L_{i, j}$ representing all points lying on the unique line determined by $P_i$ and $P_j$:
$$\text{bit } k \text{ of } L_{i, j} = 1 \iff P_k \text{ is collinear with } P_i \text{ and } P_j$$

### Bitmask Dynamic Programming with Pivot Reduction

Let $DP[\text{mask}]$ denote the minimum number of lines required to cover all points in `mask`.
- Base case: $DP[0] = 0$.
- For any non-empty `mask`:
  Every point in `mask` must eventually be covered. To prevent symmetric permutations of the same line assignments, we anchor our decision to the lowest set bit $i = \text{ctz}(\text{mask})$ (the first uncovered point).
  Point $i$ must be covered by a line. There are two structural possibilities:
  1. **Singleton Line:** Point $i$ is covered alone (valid when $i$ cannot be paired with any remaining point):
     $$DP[\text{mask}] = 1 + DP[\text{mask} \setminus \{i\}]$$
  2. **Pairwise Line Extension:** Point $i$ is paired with some other point $j \in \text{mask}$ ($j \ne i$). The line through $P_i$ and $P_j$ covers the mask $L_{i, j}$:
     $$DP[\text{mask}] = \min_{j \in \text{mask}, j \ne i} \Big(1 + DP[\text{mask} \ \& \ \sim L_{i, j}]\Big)$$

Taking the minimum across all options yields the optimal subproblem resolution.

| Parameter / State | Formal Definition | Concrete Instance Role ($n = 4$) |
|---|---|---|
| Point Mask | Binary integer in $[0, 15]$ | Subsets of $\{P_0, P_1, P_2, P_3\}$ remaining to be covered |
| Collinearity Test | $(x_2 - x_1)(y_3 - y_1) - (y_2 - y_1)(x_3 - x_1) = 0$ | Verifies $P_0, P_1, P_2$ share the line $y = x + 1$ |
| Line Mask $L_{0, 1}$ | Points $\{0, 1, 2\}$ $\implies 2^0 + 2^1 + 2^2 = 7$ | Encodes simultaneous coverage of three points |
| Anchor Point $i$ | $\text{ctz}(\text{mask})$ | Breaks symmetry by forcing coverage of the first uncovered point |
| Target State | $DP[2^n - 1] = DP[15]$ | Minimum lines covering all four points |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace the algorithm on $P_0 = (0, 1), P_1 = (2, 3), P_2 = (4, 5), P_3 = (4, 3)$.

```
Points:
P0 = (0, 1)
P1 = (2, 3)
P2 = (4, 5)
P3 = (4, 3)

Lines precomputed:
Line(P0, P1) -> passes through P2!  Mask = {0, 1, 2}  (binary 0111 = 7)
Line(P0, P3) -> {0, 3}              (binary 1001 = 9)
Line(P1, P3) -> {1, 3}              (binary 1010 = 10)
Line(P2, P3) -> {2, 3}              (binary 1100 = 12)
```

### Step 1: Precompute Line Masks
Test collinearity for all $\binom{4}{2} = 6$ pairs:
1. **Pair $(P_0, P_1)$:** $P_0 = (0, 1), P_1 = (2, 3)$.
   - Test $P_2 = (4, 5)$: $(2 - 0)(5 - 1) - (3 - 1)(4 - 0) = 2(4) - 2(4) = 0$. Collinear!
   - Test $P_3 = (4, 3)$: $(2 - 0)(3 - 1) - (3 - 1)(4 - 0) = 2(2) - 2(4) = 4 - 8 = -4 \ne 0$. Not collinear.
   - Resulting line mask: $L_{0, 1} = \{0, 1, 2\} = 2^0 + 2^1 + 2^2 = 7$.
2. **Pair $(P_0, P_3)$:** $P_0 = (0, 1), P_3 = (4, 3)$.
   - Neither $P_1$ nor $P_2$ is collinear.
   - Resulting line mask: $L_{0, 3} = \{0, 3\} = 2^0 + 2^3 = 9$.
3. **Pair $(P_1, P_3)$:** $P_1 = (2, 3), P_3 = (4, 3)$.
   - Horizontal line $y = 3$. $P_0, P_2$ not on this line.
   - Resulting line mask: $L_{1, 3} = \{1, 3\} = 2^1 + 2^3 = 10$.
4. **Pair $(P_2, P_3)$:** $P_2 = (4, 5), P_3 = (4, 3)$.
   - Vertical line $x = 4$. $P_0, P_1$ not on this line.
   - Resulting line mask: $L_{2, 3} = \{2, 3\} = 2^2 + 2^3 = 12$.

### Step 2: Evaluate Subproblems via Dynamic Programming
We seek $DP[15]$ where $15 = \text{`1111`}_2$ (all points $\{0, 1, 2, 3\}$).

- **Evaluate $DP[15]$:**
  - Anchor point: Lowest set bit is $i = 0$ ($P_0$).
  - Option A: Pair $P_0$ with $P_1$:
    - Line mask: $L_{0, 1} = 7$ (`0111`).
    - Remaining mask: $15 \ \& \ \sim 7 = 15 - 7 = 8$ (Point $\{3\}$).
    - Cost: $1 + DP[8]$.
  - Option B: Pair $P_0$ with $P_2$:
    - Same line as $(P_0, P_1)$, mask is $7$. Remaining is $8$.
    - Cost: $1 + DP[8]$.
  - Option C: Pair $P_0$ with $P_3$:
    - Line mask: $L_{0, 3} = 9$ (`1001`).
    - Remaining mask: $15 \ \& \ \sim 9 = 6$ (Points $\{1, 2\}$).
    - Cost: $1 + DP[6]$.

- **Resolve Subproblem $DP[8]$ (Point $\{3\}$):**
  - Only one point remains ($P_3$).
  - Any single point can be covered by $1$ line: $DP[8] = 1$.
  - Option A payoff: $1 + DP[8] = 1 + 1 = 2$.

- **Resolve Subproblem $DP[6]$ (Points $\{1, 2\}$):**
  - Anchor point is $1$. Pair $P_1$ with $P_2$.
  - Line $L_{1, 2}$ covers $\{0, 1, 2\}$. Remaining mask: $6 \ \& \ \sim 7 = 0$.
  - $DP[6] = 1 + DP[0] = 1 + 0 = 1$.
  - Option C payoff: $1 + DP[6] = 1 + 1 = 2$.

Both candidate branches achieve total cost $2$. Minimum lines required is $2$.

---

## 4. Comprehensive State Trace

The table below catalogs every explored mask and optimal subproblem transitions:

| Mask Value | Binary Representation | Points in Mask | Anchor Point $i$ | Optimal Partner $j$ | Line Mask Subtracted | Remaining Mask | Subproblem Cost | Optimal $DP[\text{mask}]$ |
|---|---|---|---|---|---|---|---|---|
| $0$ | `0000` | $\emptyset$ | - | - | - | - | $0$ | $0$ |
| $8$ | `1000` | $\{3\}$ | $3$ | Singleton | `1000` | `0000` | $0$ | $1$ |
| $6$ | `0110` | $\{1, 2\}$ | $1$ | $2$ | `0111` ($L_{1,2}$) | `0000` | $0$ | $1$ |
| $7$ | `0111` | $\{0, 1, 2\}$ | $0$ | $1$ | `0111` ($L_{0,1}$) | `0000` | $0$ | $1$ |
| $15$ | `1111` | $\{0, 1, 2, 3\}$ | $0$ | $1$ | `0111` ($L_{0,1}$) | `1000` ($\{3\}$) | $DP[8] = 1$ | $1 + 1 = 2$ |

### Geometric Cover Verification

- **Line 1:** Passes through $P_0(0, 1), P_1(2, 3), P_2(4, 5)$. Equation: $y = x + 1$.
- **Line 2:** Passes through $P_3(4, 3)$ (e.g., horizontal line $y = 3$, which also passes through $P_1$).
- Points covered: $\{P_0, P_1, P_2\} \cup \{P_3, P_1\} = \{P_0, P_1, P_2, P_3\}$.
- Total lines: $2$.
- Can $1$ line cover all $4$? No, because $P_3$ does not lie on $y = x + 1$. Minimum is strictly $2$.

---

## 5. Algorithmic Correctness & Soundness

### Pivot Invariance
Fixing the anchor $i = \text{ctz}(\text{mask})$ at each recursion step is completely sound:
- Point $i$ must belong to at least one line in any valid covering.
- In that line, point $i$ is either alone or shares the line with at least one other point $j \in \text{mask}$.
- By branching over all possible partners $j \in \text{mask} \setminus \{i\}$ (and the singleton case if $|\text{mask}| \le 2$), all structurally distinct ways of covering point $i$ are explored.
- Because point $i$ is covered in this step and removed from the active mask, the search is strictly acyclic and exhaustively optimal.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Collinear Sets of All Points ($n \le 10$):** If all points lie on one line, $L_{0, 1} = 2^n - 1$. A single line covers the entire set, returning $1$.
2. **Two or Fewer Points ($n \le 2$):** Any $1$ or $2$ points can always be connected by a single straight line, returning $1$.
3. **No Three Points Collinear:** If no three points share a line, each line can cover at most $2$ points. The answer is simply $\lceil n / 2 \rceil$.
4. **Multiple Intersecting Lines with 3+ Points:** The bitmask DP handles shared points across lines automatically because the set subtraction `mask & ~L` removes all points on the chosen line regardless of whether other lines also cover them.

### Common Anti-Patterns
- **Greedy Selection of Largest Collinear Set:** A greedy algorithm that repeatedly selects the line covering the maximum number of remaining points is not optimal for Set Cover. For certain configurations, choosing a line with $3$ points instead of two disjoint pairs of $2$ points forces extra lines later.
- **Slope Division by Zero:** Using $m = (y_2 - y_1) / (x_2 - x_1)$ leads to division-by-zero crashes on vertical lines. Integer cross products handle vertical and horizontal lines uniformly without division.
- **Branching Over All Pairs:** Choosing any arbitrary pair $(j, k)$ in the mask rather than fixing anchor point $i$ causes exponential duplicate work across symmetric permutations of the same lines.

---

## 7. Complexity Analysis

### Time Complexity
- **Line Precomputation:** There are $\binom{n}{2} = O(n^2)$ pairs of points. For each pair, checking all other points takes $O(n)$ time. Total precomputation takes $O(n^3)$ operations.
- **Dynamic Programming Search:**
  - There are $2^n$ subsets.
  - From each state `mask`, fixing the anchor point $i$ allows branching to at most $n - 1$ possible partners $j$.
  - Each transition takes $O(1)$ bitwise operations.
  - Total DP time is $O(n \cdot 2^n)$.
- For $n = 10$, $n^3 = 1000$ and $n \cdot 2^n = 10 \times 1024 \approx 10^4$ operations, which executes in less than $2$ milliseconds.

### Auxiliary Space Complexity
- Memoization table of size $2^n$ integers stores optimal values for each mask.
- Precomputed pairwise line masks require an array of size $O(n^2)$.
- Total auxiliary space complexity is $O(2^n + n^2)$, which takes under $10$ KB for $n = 10$.