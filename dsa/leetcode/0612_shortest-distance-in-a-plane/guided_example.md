# Guided Example: Shortest Distance in a Plane

We trace the step-by-step distinct coordinate pair non-self joining ($(p_1.x \ne p_2.x \lor p_1.y \ne p_2.y)$), 2D Euclidean distance metric evaluation ($\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$), pairwise distance minimization (`MIN` or ascending sort with `LIMIT 1`), and two-decimal numeric rounding on representative planar coordinate tables:

- **Input:**
  - `Point2D` table:
    | `x` | `y` |
    |:---:|:---:|
    | $-1$ | $-1$ |
    | $0$ | $0$ |
    | $-1$ | $-2$ |
- **Required output:**
  | `shortest` |
  |:---:|
  | $1.00$ |
  - Problem objective: Compute the Euclidean distance between all pairs of distinct points in 2D space, find the minimum distance, and round the result to $2$ decimal places.
  - Euclidean distance formula:
    $$
    d(p_1, p_2) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}
    $$
- **Cross-Join & Distinct Pair Filtering Trace:**
  - Joining `Point2D p1` with `Point2D p2`:
    - We must prevent comparing a point with itself ($p_1 = p_2$), which produces a trivial distance of $0$.
    - Non-self predicate:
      $$
      p_1.x \ne p_2.x \quad \lor \quad p_1.y \ne p_2.y
      $$
    - *(Alternatively, strict lexicographical inequality $(p_1.x < p_2.x) \lor (p_1.x = p_2.x \land p_1.y < p_2.y)$ eliminates duplicate symmetric pairs $(p_1, p_2)$ and $(p_2, p_1)$)*.
  - **Step 1: Enumerate Distinct Point Pairs:**
    - Let $A = (-1, -1), \; B = (0, 0), \; C = (-1, -2)$.
    - Distinct unordered pairs:
      1. Pair $(A, B)$: $(-1, -1)$ and $(0, 0)$
      2. Pair $(A, C)$: $(-1, -1)$ and $(-1, -2)$
      3. Pair $(B, C)$: $(0, 0)$ and $(-1, -2)$
  - **Step 2: Calculate Euclidean Distances:**
    - **Pair $(A, B)$:**
      $$
      \Delta x = 0 - (-1) = 1, \quad \Delta y = 0 - (-1) = 1
      $$
      $$
      d(A, B) = \sqrt{1^2 + 1^2} = \sqrt{2} \approx 1.4142
      $$
    - **Pair $(A, C)$:**
      $$
      \Delta x = -1 - (-1) = 0, \quad \Delta y = -2 - (-1) = -1
      $$
      $$
      d(A, C) = \sqrt{0^2 + (-1)^2} = \sqrt{1} = \mathbf{1.0000}
      $$
    - **Pair $(B, C)$:**
      $$
      \Delta x = -1 - 0 = -1, \quad \Delta y = -2 - 0 = -2
      $$
      $$
      d(B, C) = \sqrt{(-1)^2 + (-2)^2} = \sqrt{1 + 4} = \sqrt{5} \approx 2.2361
      $$
  - **Step 3: Extract Global Minimum:**
    $$
    \min(1.4142, \; 1.0000, \; 2.2361) = \mathbf{1.0000}
    $$
  - **Step 4: Numeric Rounding to 2 Decimal Places:**
    $$
    \text{ROUND}(1.0000, \; 2) = \mathbf{1.00}
    $$
    *(Or scalar integer $1$ depending on numeric database engine serialization)*.
- **Horizontal Distance Alignment Instance ($A = (2, 5), B = (8, 5)$):**
  - $\Delta y = 0 \implies \sqrt{(8-2)^2 + 0} = 6.00$.
- **Diagonal Unit Step Instance ($A = (0, 0), B = (1, 1)$):**
  - $d = \sqrt{1 + 1} = \sqrt{2} \approx 1.41 \implies \mathbf{1.41}$.

This instance demonstrates metric spatial distance calculation over relational Cartesian products, mathematically proves why strict point inequality excludes reflexive zero distances, and derives $O(N^2)$ execution time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a `Point2D` table with coordinates $(x, y)$:
Find the **shortest Euclidean distance** between any two distinct points.
Round the answer to 2 decimal places.

```text
Points:
  p1: (-1, -1)
  p2: ( 0,  0)
  p3: (-1, -2)

Distances:
  d(p1, p2) = √((0 - -1)^2 + (0 - -1)^2)   = √2 ≈ 1.41
  d(p1, p3) = √((-1 - -1)^2 + (-2 - -1)^2) = √1 = 1.00  <-- Shortest!
  d(p2, p3) = √((-1 - 0)^2 + (-2 - 0)^2)   = √5 ≈ 2.24

Shortest distance = 1.00
```

### Preventing Self-Distance Contamination
- Every point has distance 0 to itself ($d(p, p) = 0$).
- If self-comparison is not prevented, the minimum distance returned will always be 0.
- The join condition `p1.x != p2.x OR p1.y != p2.y` strictly restricts the candidates to **distinct physical points**.

---

## 2. Conceptual Foundation & Invariants

### 1. The SQL Query:
```sql
SELECT ROUND(SQRT(POW(p1.x - p2.x, 2) + POW(p1.y - p2.y, 2))::numeric, 2) AS shortest
FROM Point2D AS p1
JOIN Point2D AS p2
    ON p1.x != p2.x OR p1.y != p2.y
ORDER BY shortest ASC
LIMIT 1;
```

### 2. Lexicographical Asymmetric Optimization:
Using `(p1.x < p2.x) OR (p1.x = p2.x AND p1.y < p2.y)` halves the candidate join rows from $N(N - 1)$ to $\binom{N}{2}$, eliminating redundant reverse checks.

> **Metric Non-Negativity Invariant.** For all distinct points $p_1 \ne p_2$, $d(p_1, p_2) > 0$. Filtering out identical coordinates guarantees that the minimum distance is strictly positive.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Compute Distances
- Pair $((-1, -1), (0, 0)) \implies \sqrt{1 + 1} \approx 1.414$.
- Pair $((-1, -1), (-1, -2)) \implies \sqrt{0 + 1} = 1.000$.
- Pair $((0, 0), (-1, -2)) \implies \sqrt{1 + 4} \approx 2.236$.

---

### Step 2: Sort and Select Minimum
- Ranked list:
  1. $1.000$
  2. $1.414$
  3. $2.236$
- Minimum is $1.000$.

---

### Step 3: Round to 2 Decimals
$$
\text{ROUND}(1.000, 2) = \mathbf{1.00}
$$

---

## 4. Complete Execution Trace

| Point $p_1$ | Point $p_2$ | $\Delta x^2$ | $\Delta y^2$ | $\sqrt{\Delta x^2 + \Delta y^2}$ | Distance | Rank |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $(-1, -1)$ | $(-1, -2)$ | $0$ | $1$ | $\sqrt{1}$ | **$1.00$** | **$1$ (Shortest)** |
| $(-1, -1)$ | $(0, 0)$ | $1$ | $1$ | $\sqrt{2}$ | $1.41$ | $2$ |
| $(0, 0)$ | $(-1, -2)$ | $1$ | $4$ | $\sqrt{5}$ | $2.24$ | $3$ |

---

## 5. Boundary Cases & Failure Modes

- **Exactly Two Points in Table:** The single distance between them is returned.
- **Points with Large Coordinates ($10^4$):** Standard 64-bit float math handles $(2 \times 10^4)^2$ without precision loss.
- **Vertical Alignment ($\Delta x = 0$):** Handled with $\sqrt{\Delta y^2} = |\Delta y|$.
- **Horizontal Alignment ($\Delta y = 0$):** Handled with $\sqrt{\Delta x^2} = |\Delta x|$.

---

## 6. Traps & Common Anti-Patterns

- **Joining with `p1.x != p2.x AND p1.y != p2.y`:** Using `AND` instead of `OR` erroneously ignores all points that share the same $x$-coordinate or same $y$-coordinate! In our sample, $(-1, -1)$ and $(-1, -2)$ share $x = -1$; using `AND` would miss the actual shortest distance.
- **Forgetting to Cast to Numeric in PostgreSQL:** PostgreSQL's `ROUND(double precision, integer)` requires casting `ROUND(...::numeric, 2)`.
- **Forgetting `LIMIT 1`:** Returning all distances instead of the scalar minimum fails the result format.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Cross-joining $N$ points produces $\mathcal{O}(N^2)$ candidate pairs.
  - Sifting for the minimum distance: $\mathcal{O}(N^2)$ time.
  - Total Time: $\mathcal{O}(N^2)$. For typical test sets ($N \le 1000$), completes in $< 20$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space when evaluated with a streaming `MIN` aggregate.
