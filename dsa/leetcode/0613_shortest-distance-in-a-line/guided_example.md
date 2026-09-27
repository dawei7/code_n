# Guided Example: Shortest Distance in a Line

We trace the step-by-step 1D coordinate pair asymmetric joining ($p_1.x < p_2.x$), linear distance delta evaluation ($p_2.x - p_1.x$), global scalar minimization (`MIN`), self-comparison elimination, and shortest distance extraction on representative 1D point tables:

- **Input:**
  - `Point` table:
    | `x` |
    |:---:|
    | $-1$ |
    | $0$ |
    | $2$ |
- **Required output:**
  | `shortest` |
  |:---:|
  | $1$ |
  - Problem objective: Determine the smallest absolute distance between any two distinct points on a 1-dimensional number line.
  - 1D distance definition:
    $$
    d(x_1, x_2) = |x_1 - x_2|
    $$
- **Asymmetric Joining & Scalar Minimization Trace:**
  - On a 1D real line, if we enforce the strict inequality $p_1.x < p_2.x$:
    - Points cannot be compared to themselves ($p_1.x \ne p_2.x$).
    - The difference $p_2.x - p_1.x$ is **guaranteed to be strictly positive**, eliminating the need for `ABS()`.
    - Every pair of distinct points is examined exactly once (asymmetric selection).
  - Join formulation:
    ```sql
    SELECT MIN(p2.x - p1.x) AS shortest
    FROM Point AS p1
    JOIN Point AS p2 ON p1.x < p2.x;
    ```
  - **Step-by-Step Row Pair Evaluation:**
    - Given points: $A = -1, \; B = 0, \; C = 2$.
    - **Candidate Pair 1 ($p_1 = A, \; p_2 = B$):**
      - Check condition: $-1 < 0 \implies \mathbf{True}$.
      - Calculate distance:
        $$
        \Delta = 0 - (-1) = \mathbf{1}
        $$
    - **Candidate Pair 2 ($p_1 = A, \; p_2 = C$):**
      - Check condition: $-1 < 2 \implies \mathbf{True}$.
      - Calculate distance:
        $$
        \Delta = 2 - (-1) = \mathbf{3}
        $$
    - **Candidate Pair 3 ($p_1 = B, \; p_2 = C$):**
      - Check condition: $0 < 2 \implies \mathbf{True}$.
      - Calculate distance:
        $$
        \Delta = 2 - 0 = \mathbf{2}
        $$
  - **Step 2: Aggregate Scalar Minimum (`MIN`):**
    - The candidate distances are $\{1, 3, 2\}$.
    - Evaluate aggregate:
      $$
      \min(1, 3, 2) = \mathbf{1}
      $$
    - Output scalar column:
      $$
      shortest: \mathbf{1}
      $$
- **Negative Coordinate Pairs ($x = -10, -8, -5$):**
  - $-8 - (-10) = 2$.
  - $-5 - (-8) = 3$.
  - Minimum distance is $2$.
- **Adjacent Consecutive Integers:**
  - If any two points differ by 1, the minimum possible distance for integers ($1$) is immediately realized.

This instance demonstrates metric difference minimization on 1-dimensional coordinate projections, mathematically proves why strict inequality ordering avoids symmetric redundancy and absolute value branching, and derives $O(N^2)$ join execution time (or $O(N \log N)$ with windowing) and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a `Point` table with 1D coordinates $x$:
Find the **shortest distance** between any two distinct points:
$|x_1 - x_2|$.

```text
Points on number line:
  ... -1 ... 0 ... 2 ...

Distances:
  Between -1 and  0: |0 - (-1)| = 1  <-- Shortest!
  Between  0 and  2: |2 - 0|    = 2
  Between -1 and  2: |2 - (-1)| = 3

Result: 1
```

### The Strict Inequality Technique
- In 1D, points are totally ordered.
- By joining on `p1.x < p2.x`:
  1. We prevent self-joins ($x = x$).
  2. The subtraction `p2.x - p1.x` is always positive without calling `ABS()`.
  3. We only evaluate $\binom{N}{2}$ pairs instead of $N^2$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Cross-Join Query:
```sql
SELECT MIN(p2.x - p1.x) AS shortest
FROM Point AS p1
JOIN Point AS p2 ON p1.x < p2.x;
```

### 2. Window Function Optimization ($O(N \log N)$):
On a 1D line, the shortest distance between any two points must occur between **two adjacent points in sorted order**:
```sql
WITH S AS (
    SELECT x - LAG(x) OVER (ORDER BY x) AS diff
    FROM Point
)
SELECT MIN(diff) AS shortest FROM S;
```

> **Metric Adjacency Invariant.** For any finite subset $S \subset \mathbb{R}$, $\min_{u, v \in S, u \ne v} |u - v| = \min_{i} (x_{i+1} - x_i)$ where $x_i$ is the sorted permutation of $S$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Form Valid Pairs ($p_1.x < p_2.x$)
- $(-1, 0) \implies \Delta = 0 - (-1) = 1$.
- $(-1, 2) \implies \Delta = 2 - (-1) = 3$.
- $(0, 2) \implies \Delta = 2 - 0 = 2$.

---

### Step 2: Compute `MIN(diff)`
$$
\min(1, 3, 2) = \mathbf{1}
$$

---

## 4. Complete Execution Trace

| Point $p_1.x$ | Point $p_2.x$ | Condition $p_1.x < p_2.x$ | Distance $\Delta = p_2.x - p_1.x$ |
|:---:|:---:|:---:|:---:|
| **$-1$** | **$0$** | **Yes** | **$1$ (Minimum)** |
| $-1$ | $2$ | **Yes** | $3$ |
| $0$ | $2$ | **Yes** | $2$ |
| **Output** | — | — | **`shortest: 1`** |

---

## 5. Boundary Cases & Failure Modes

- **Two Points in Table:** Returns the single distance between them.
- **Large Gap Between Points ($0, 1000$):** Returns $1000$.
- **Negative and Positive Zero:** In IEEE 754 / standard SQL, $-0 = +0$, but coordinates are distinct integers.
- **Points Far Apart ($[-10^9, 10^9]$):** Handled with 64-bit integer arithmetic.

---

## 6. Traps & Common Anti-Patterns

- **Joining with `p1.x != p2.x` Without `ABS()`:** When $p_2.x < p_1.x$, $p_2.x - p_1.x$ is negative. Taking `MIN()` on negative numbers returns a negative value instead of the distance. Enforcing `p1.x < p2.x` guarantees strictly positive values.
- **Self-Distance Zero:** Joining with `<=` allows identical points to yield $0$.
- **Naming the Column Incorrectly:** Must be aliased `AS shortest`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Self-join: $\mathcal{O}(N^2)$ candidate comparisons.
  - Streaming scalar `MIN`: $\mathcal{O}(N^2)$ time.
  - Or using window functions: $\mathcal{O}(N \log N)$ sort time.
  - Total Time: $\mathcal{O}(N^2)$ (or $\mathcal{O}(N \log N)$). Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space.
