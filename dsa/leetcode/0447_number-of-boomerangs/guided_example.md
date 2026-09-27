# Guided Example: Number of Boomerangs

We trace the step-by-step pivot-centered distance grouping, squared Euclidean distance bucketing ($(x_1 - x_2)^2 + (y_1 - y_2)^2$), ordered permutation pair counting ($m(m-1)$), and global symmetry accumulation on representative 2D coordinate sets:

- **Input:** $points = [[0, 0], [1, 0], [2, 0]]$
- **Required output:** `2`
  - A boomerang is an ordered triplet $(i, j, k)$ such that $\text{dist}(i, j) == \text{dist}(i, k)$ (order matters).
  - Pivot evaluations:
    - **Pivot $P_0 = (0, 0)$:**
      - Squared distance to $P_1(1, 0)$: $(0 - 1)^2 + (0 - 0)^2 = 1$
      - Squared distance to $P_2(2, 0)$: $(0 - 2)^2 + (0 - 0)^2 = 4$
      - Distance counts: $\{1: 1, 4: 1\}$
      - Boomerangs with pivot $P_0$: $1(0) + 1(0) = \mathbf{0}$
    - **Pivot $P_1 = (1, 0)$:**
      - Squared distance to $P_0(0, 0)$: $(1 - 0)^2 = 1$
      - Squared distance to $P_2(2, 0)$: $(1 - 2)^2 = 1$
      - Distance counts: $\{1: 2\}$
      - Two points equidistant from $P_1$ ($m = 2$):
        - Permutation choices $P(2, 2) = 2 \times 1 = \mathbf{2}$:
          1. $((1, 0), \; (0, 0), \; (2, 0))$
          2. $((1, 0), \; (2, 0), \; (0, 0))$
    - **Pivot $P_2 = (2, 0)$:**
      - Squared distance to $P_0(0, 0)$: $4$
      - Squared distance to $P_1(1, 0)$: $1$
      - Distance counts: $\{1: 1, 4: 1\} \implies \mathbf{0}$
  - Total boomerangs: $0 + 2 + 0 = \mathbf{2}$
- **Equilateral Triangle Instance:** $points = [[0, 0], [1, 0], [0.5, \frac{\sqrt{3}}{2}]] \implies$ all pairwise distances equal $\implies$ each of the 3 points forms $2$ boomerangs $\implies 3 \times 2 = \mathbf{6}$
- **Two Points Only:** $points = [[1, 1], [2, 2]] \implies$ cannot form a triplet of 3 points $\implies \mathbf{0}$

This instance demonstrates geometric pivot decomposition, mathematically proves why using squared distances avoids floating-point roundoff errors, and derives $O(N^2)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given $n$ distinct points in the plane $points = [[0, 0], [1, 0], [2, 0]]$:
A **boomerang** is a tuple of points $(i, j, k)$ such that the distance between $i$ and $j$ equals the distance between $i$ and $k$ ($i$ serves as the **pivot / apex**).
Because order matters, $(i, j, k)$ and $(i, k, j)$ are counted as distinct.
Return the total number of boomerangs.

```text
Point Coordinates:
  P0: (0, 0)
  P1: (1, 0)
  P2: (2, 0)

Geometry:
  P0 <---- 1 unit ----> P1 <---- 1 unit ----> P2

Equidistant Pairs with Pivot P1:
  dist(P1, P0) = 1
  dist(P1, P2) = 1

Valid Ordered Boomerangs:
  1. (P1, P0, P2)
  2. (P1, P2, P0)

Total Boomerangs: 2
```

### The Pivot Decomposition Principle
Enumerating all triplets $(i, j, k)$ takes $O(N^3)$ brute-force time.
To optimize:
- Fix each point $i$ in turn as the **pivot**.
- Measure the distance from $i$ to all other $N - 1$ points.
- If $m$ points share the exact same distance $d$ from pivot $i$:
  - Any pair of these $m$ points can serve as the two wings $(j, k)$.
  - Since the wings are ordered, the number of valid pairs is the permutation:
    $$
    P(m, 2) = m \times (m - 1)
    $$
- Summing $m(m - 1)$ over all distance buckets for all pivots evaluates all boomerangs in $O(N^2)$ time.

---

## 2. Conceptual Foundation & Invariants

### 1. Squared Euclidean Distance Invariant:
The true Euclidean distance is $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$.
Taking the square root incurs floating-point imprecision that can corrupt hash map equality.
Because distance is non-negative and $f(z) = z^2$ is strictly monotonic on $[0, \infty)$:
$$
\text{dist}(P_1, P_2) == \text{dist}(P_1, P_3) \iff \text{dist}^2(P_1, P_2) == \text{dist}^2(P_1, P_3)
$$
Using the **squared Euclidean distance**:
$$
d^2 = (x_1 - x_2)^2 + (y_1 - y_2)^2
$$
keeps all values strictly integral, guaranteeing zero precision error.

### 2. Combinatorial Counting Formula:
For each pivot point $p_1$:
1. Initialize frequency map $cnt$.
2. For each other point $p_2 \ne p_1$:
   - Compute $d = (p_1.x - p_2.x)^2 + (p_1.y - p_2.y)^2$.
   - Increment: $cnt[d] \leftarrow cnt[d] + 1$.
3. For each frequency $m$ in $cnt$:
   - Add $m(m - 1)$ to total boomerangs.

> **Combinatorial Invariant.** For a fixed pivot $i$, every pair of points in the same distance bucket forms an ordered pair $(j, k)$ with $j \ne k$ satisfying $dist(i, j) = dist(i, k)$. Points in different distance buckets can never form a boomerang with pivot $i$.

---

## 3. Step-by-Step Worked Execution

We trace $points = [P_0(0, 0), \; P_1(1, 0), \; P_2(2, 0)]$ ($N = 3$):

---

### Step 1: Evaluate Pivot $P_0 = (0, 0)$
Calculate squared distances from $P_0$ to other points:
- To $P_1(1, 0)$:
  $$
  d^2 = (0 - 1)^2 + (0 - 0)^2 = 1 + 0 = \mathbf{1}
  $$
- To $P_2(2, 0)$:
  $$
  d^2 = (0 - 2)^2 + (0 - 0)^2 = 4 + 0 = \mathbf{4}
  $$
Distance counts: $\{1: 1, \; 4: 1\}$.
Permutations:
- For $d^2 = 1: m = 1 \implies 1(0) = 0$.
- For $d^2 = 4: m = 1 \implies 1(0) = 0$.
Boomerangs with pivot $P_0$: **$0$**.

---

### Step 2: Evaluate Pivot $P_1 = (1, 0)$
Calculate squared distances from $P_1$ to other points:
- To $P_0(0, 0)$:
  $$
  d^2 = (1 - 0)^2 + (0 - 0)^2 = 1 + 0 = \mathbf{1}
  $$
- To $P_2(2, 0)$:
  $$
  d^2 = (1 - 2)^2 + (0 - 0)^2 = (-1)^2 + 0 = \mathbf{1}
  $$
Distance counts: $\{1: 2\}$.
Permutations:
- For $d^2 = 1: m = 2 \implies 2 \times (2 - 1) = \mathbf{2}$.
The 2 boomerangs formed:
1. $(P_1, P_0, P_2)$
2. $(P_1, P_2, P_0)$
Boomerangs with pivot $P_1$: **$2$**.

---

### Step 3: Evaluate Pivot $P_2 = (2, 0)$
Calculate squared distances from $P_2$ to other points:
- To $P_0(0, 0)$:
  $$
  d^2 = (2 - 0)^2 + (0 - 0)^2 = 4
  $$
- To $P_1(1, 0)$:
  $$
  d^2 = (2 - 1)^2 + (0 - 0)^2 = 1
  $$
Distance counts: $\{4: 1, \; 1: 1\}$.
Permutations:
- $1(0) + 1(0) = \mathbf{0}$.
Boomerangs with pivot $P_2$: **$0$**.

---

### Final Accumulation:
$$
\text{Total Boomerangs} = 0 + 2 + 0 = \mathbf{2}
$$

---

## 4. Complete Execution Trace

| Pivot Point $p_1$ | Target Point $p_2$ | Coordinates $(x, y)$ | Squared Dist $d^2$ | Bucket Size $m$ | Permutation Contribution $m(m-1)$ | Cumulative Boomerangs |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $P_0(0, 0)$ | $P_1$ | $(1, 0)$ | $1$ | $1$ | $0$ | $0$ |
| $P_0(0, 0)$ | $P_2$ | $(2, 0)$ | $4$ | $1$ | $0$ | $0$ |
| $P_1(1, 0)$ | $P_0$ | $(0, 0)$ | $1$ | $1$ | — | $0$ |
| $P_1(1, 0)$ | $P_2$ | $(2, 0)$ | $1$ | $2$ | $2 \times 1 = \mathbf{2}$ | **$2$** |
| $P_2(2, 0)$ | $P_0$ | $(0, 0)$ | $4$ | $1$ | $0$ | $2$ |
| $P_2(2, 0)$ | $P_1$ | $(1, 0)$ | $1$ | $1$ | $0$ | **$2$** |

---

## 5. Boundary Cases & Failure Modes

- **Fewer Than Three Points ($N < 3$):** A boomerang requires 3 distinct points. Loops cannot find 2 equidistant partners $\implies \mathbf{0}$.
- **All Points Equidistant (Regular Polygon):** With 4 points forming a square, diagonals and sides create multiple equidistant pairs from each vertex, correctly multiplying counts.
- **Multiple Collinear Points ($P_0, P_1, P_2, P_3$ along a line):** Symmetric spacing pairs symmetric outer points around any central pivot.
- **Negative Coordinates ($[[-1, -1], [0, 0], [1, 1]]$):** Distance squaring handles negative coordinates cleanly.

---

## 6. Traps & Common Anti-Patterns

- **Using Floating-Point Square Roots:** Calling `math.sqrt()` risks floating-point rounding errors (e.g. $\sqrt{5}$ computed slightly differently across operations), placing identical distances into distinct dictionary buckets. Pure integer squared distance avoids this bug completely.
- **Global Map Instead of Per-Pivot Map:** Distance buckets must be cleared for each pivot. Maintaining a single global distance map falsely matches points measured from different origins.
- **Combinations Instead of Permutations:** Computing $\binom{m}{2} = \frac{m(m-1)}{2}$ counts unordered sets. Because the problem definition specifies $(i, j, k) \ne (i, k, j)$, the multiplier is strictly $m(m - 1)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Outer loop selects each of the $N$ points as pivot.
  - Inner loop evaluates distances to the other $N - 1$ points in $O(1)$ time each.
  - Total iterations: $N \times (N - 1)$.
  - Total Time: $\mathcal{O}(N^2)$. For $N = 500$, $500^2 = 2.5 \times 10^5$ operations, completing in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - The frequency map is recreated per pivot, storing at most $N$ distinct squared distances.
  - Total Auxiliary Space: $\mathcal{O}(N)$.
