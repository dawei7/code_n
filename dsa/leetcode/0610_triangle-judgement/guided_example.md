# Guided Example: Triangle Judgement

We trace the step-by-step Euclidean metric triangle inequality validation ($x + y > z \land x + z > y \land y + z > x$), degeneracy edge condition checks ($a + b = c$), conditional column projection (`CASE WHEN ... THEN 'Yes' ELSE 'No' END`), and geometric classification on representative line segment dimension tables:

- **Input:**
  - `Triangle` table:
    | `x` | `y` | `z` |
    |:---:|:---:|:---:|
    | $13$ | $15$ | $30$ |
    | $10$ | $20$ | $15$ |
- **Required output:**
  | `x` | `y` | `z` | `triangle` |
  |:---:|:---:|:---:|:---:|
  | $13$ | $15$ | $30$ | `No` |
  | $10$ | $20$ | $15$ | `Yes` |
  - Problem specification: For each row of segment lengths $(x, y, z)$, determine whether they can form a valid non-degenerate triangle. Add a fourth column `triangle` containing `'Yes'` or `'No'`.
- **Triangle Inequality Theorem:**
  - In Euclidean geometry, three positive segment lengths $x, y, z$ construct a non-degenerate triangle if and only if the sum of lengths of any two segments is **strictly greater** than the length of the remaining segment:
    1. $x + y > z$
    2. $x + z > y$
    3. $y + z > x$
  - If even one of these inequalities fails, the segments either cannot connect or collapse into a flat collinear line segment (degenerate triangle with zero area).
- **Step-by-Step Row Evaluation Trace:**
  - **Row 1 ($x = 13, \; y = 15, \; z = 30$):**
    - Inequality 1 ($x + y > z$):
      $$
      13 + 15 = 28
      $$
      $$
      28 > 30 \implies \mathbf{False!}
      $$
    - The two shorter segments cannot bridge the distance of $30$.
    - The triangle cannot close!
    - Classification:
      $$
      \mathbf{\text{"No"}}
      $$
  - **Row 2 ($x = 10, \; y = 20, \; z = 15$):**
    - Inequality 1 ($x + y > z$):
      $$
      10 + 20 = 30 > 15 \implies \mathbf{True}
      $$
    - Inequality 2 ($x + z > y$):
      $$
      10 + 15 = 25 > 20 \implies \mathbf{True}
      $$
    - Inequality 3 ($y + z > x$):
      $$
      20 + 15 = 35 > 10 \implies \mathbf{True}
      $$
    - All three inequalities hold simultaneously!
    - Classification:
      $$
      \mathbf{\text{"Yes"}}
      $$
- **Collinear Degeneracy Instance ($x = 3, y = 4, z = 7$):**
  - $3 + 4 = 7 \ngtr 7$ (sum equals third side $\implies$ flat line segment).
  - Strict inequality fails $\implies \mathbf{\text{"No"}}$.
- **Equilateral Triangle Instance ($x = 5, y = 5, z = 5$):**
  - $5 + 5 = 10 > 5$ in all directions $\implies \mathbf{\text{"Yes"}}$.
- **Isosceles Triangle Instance ($x = 5, y = 5, z = 9$):**
  - $5 + 5 = 10 > 9 \implies \mathbf{\text{"Yes"}}$.

This instance demonstrates geometric predicate validation via relational conditional projection, mathematically proves why strict triangle inequality conjunction is necessary and sufficient for planar closure, and derives $O(N)$ execution time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a `Triangle` table with three segment lengths $x, y, z$:
Determine for every row whether the segments form a triangle:
Append a column `triangle` containing `'Yes'` or `'No'`.

```text
Row 1: (13, 15, 30)
  13 + 15 = 28 <= 30 (Too short to close!) -> "No"

Row 2: (10, 20, 15)
  10 + 15 = 25 > 20 (Valid)
  10 + 20 = 30 > 15 (Valid)
  15 + 20 = 35 > 10 (Valid)
  All 3 pass! -> "Yes"
```

### The Triangle Inequality Theorem
- Three positive numbers form a triangle if and only if each side is strictly smaller than the sum of the other two.
- Equivalently, the **longest side** must be strictly smaller than the sum of the two shorter sides:
  $$
  \max(x, y, z) < \text{sum}(x, y, z) - \max(x, y, z)
  $$
- In SQL, writing all three pairwise inequalities explicitly avoids computing the maximum:
  $$
  x + y > z \quad \text{AND} \quad x + z > y \quad \text{AND} \quad y + z > x
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. The SQL Query:
```sql
SELECT
    x,
    y,
    z,
    CASE
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;
```

### 2. Strict Inequality:
- The inequality must be **strictly greater than** (`>`).
- If $a + b = c$, the three segments lie flat along a straight line, forming a degenerate segment of zero area, which does not constitute a valid triangle.

> **Metric Convexity Invariant.** In any metric space, the shortest distance between two points is a straight line; a triangle has non-zero area if and only if no side realizes this geodesic bound.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Evaluate Row 1 $(13, 15, 30)$
- $13 + 15 = 28 \le 30 \implies$ Condition fails.
- Emit:
  $$
  (13, 15, 30, \mathbf{\text{"No"}})
  $$

---

### Step 2: Evaluate Row 2 $(10, 20, 15)$
- $10 + 20 = 30 > 15 \implies \text{True}$.
- $10 + 15 = 25 > 20 \implies \text{True}$.
- $20 + 15 = 35 > 10 \implies \text{True}$.
- All 3 pass $\implies$ Emit:
  $$
  (10, 20, 15, \mathbf{\text{"Yes"}})
  $$

---

## 4. Complete Execution Trace

| Segment $x$ | Segment $y$ | Segment $z$ | $x + y > z$ | $x + z > y$ | $y + z > x$ | Triangle Formed? | Output Column `triangle` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $13$ | $15$ | $30$ | $28 > 30$ (**False**) | $43 > 15$ (True) | $45 > 13$ (True) | No | **`No`** |
| $10$ | $20$ | $15$ | $30 > 15$ (True) | $25 > 20$ (True) | $35 > 10$ (True) | **Yes** | **`Yes`** |

---

## 5. Boundary Cases & Failure Modes

- **Degenerate Line Segment ($1, 2, 3$):** $1 + 2 = 3 \ngtr 3 \implies$ `'No'`.
- **Equilateral ($1, 1, 1$):** $1 + 1 = 2 > 1 \implies$ `'Yes'`.
- **Very Large Sides ($10^9$):** Evaluated with 64-bit integer arithmetic without overflow.
- **Empty Table:** Returns empty result table with columns `x, y, z, triangle`.

---

## 6. Traps & Common Anti-Patterns

- **Using $\ge$ Instead of $>$:** Allowing $a + b \ge c$ permits flat collinear segments (zero area), which are not triangles.
- **Checking Only One Pair:** If side lengths are unordered, you cannot just check $x + y > z$; you must check all three pairs or first sort the sides.
- **Incorrect Output String Case:** Returning `'YES'` or `'true'` instead of the exact case `'Yes'` and `'No'` fails automated grading.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - A single sequential scan through the $N$ rows of `Triangle`.
  - Exactly 3 additions and 3 comparisons per row: $\mathcal{O}(1)$ operations.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space (streaming output pipeline).
