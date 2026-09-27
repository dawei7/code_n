# Guided Example: Classes With at Least 5 Students

We trace the step-by-step course grouping by subject (`GROUP BY class`), enrollment headcount counting (`COUNT(student)`), aggregated threshold filtering (`HAVING COUNT(1) >= 5`), primary key uniqueness deduplication guarantees, and class attribute projection on representative course enrollment registries:

- **Input:**
  - `Courses` table:
    | `student` | `class` |
    |:---:|:---:|
    | `A` | `Math` |
    | `B` | `English` |
    | `C` | `Math` |
    | `D` | `Biology` |
    | `E` | `Math` |
    | `F` | `Computer` |
    | `G` | `Math` |
    | `H` | `Math` |
    | `I` | `Math` |
- **Required output:**
  | `class` |
  |:---:|
  | `Math` |
  - Business qualification rule: Report all classes that have **at least five** ($5$) students enrolled.
  - Table constraint: `(student, class)` is the primary key, meaning no student is listed multiple times in the same class.
- **Relational Aggregation & Threshold Filter Trace:**
  - **Step 1: Partition Enrollments by `class`:**
    - Scan the `Courses` table and group students by their registered class:
      - **Group `class = 'Math'`:**
        - Enrolled students: `['A', 'C', 'E', 'G', 'H', 'I']`
        - Total enrollment headcount:
          $$
          \text{Headcount}(\text{Math}) = 1 + 1 + 1 + 1 + 1 + 1 = \mathbf{6}
          $$
      - **Group `class = 'English'`:**
        - Enrolled students: `['B']`
        - Headcount: $\mathbf{1}$
      - **Group `class = 'Biology'`:**
        - Enrolled students: `['D']`
        - Headcount: $\mathbf{1}$
      - **Group `class = 'Computer'`:**
        - Enrolled students: `['F']`
        - Headcount: $\mathbf{1}$
  - **Step 2: Apply `HAVING` Filter Predicate (`HAVING COUNT(1) >= 5`):**
    - The `WHERE` clause cannot filter aggregated group sizes; group size thresholds must be evaluated in the `HAVING` clause:
      - **`Math`:** $6 \ge 5 \implies \mathbf{True} \quad (\text{Qualified!})$
      - **`English`:** $1 \ge 5 \implies \mathbf{False} \quad (\text{Disqualified})$
      - **`Biology`:** $1 \ge 5 \implies \mathbf{False} \quad (\text{Disqualified})$
      - **`Computer`:** $1 \ge 5 \implies \mathbf{False} \quad (\text{Disqualified})$
  - **Step 3: Project Qualified Classes:**
    - The sole qualifying class is:
      $$
      \mathbf{\text{"Math"}}
      $$
- **Exact Boundary Enrollment ($N = 5$ students):**
  - If a class has exactly 5 students, $5 \ge 5 \implies \mathbf{True}$, which is included.
  - A class with 4 students has $4 \ge 5 \implies \mathbf{False}$, which is excluded.
- **Multiple Qualifying Classes:**
  - If both `Math` (5 students) and `History` (7 students) meet the threshold, both class names are returned.

This instance demonstrates grouped cardinality filtering in relational query languages, mathematically proves why `HAVING` applies post-aggregation boundary thresholds, and derives $O(N)$ execution time and $O(K)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a `Courses` table with `student` and `class`:
Find all classes that have **at least 5 students**.
Return the result table in any order.

```text
Enrollments:
  Math:     A, C, E, G, H, I  -> 6 students (>= 5, Qualifies!)
  English:  B                 -> 1 student
  Biology:  D                 -> 1 student
  Computer: F                 -> 1 student

Output:
  Math
```

### Relational Group Filtering
- Standard row-level filtering with `WHERE` examines individual rows.
- Group-level filtering with `HAVING` evaluates summary properties across an entire group of rows:
  $$
  \sigma_{\text{COUNT}(student) \ge 5} (\gamma_{class, \text{COUNT}(student)}(\text{Courses}))
  $$
- The combination of `GROUP BY class` and `HAVING COUNT(1) >= 5` isolates qualifying classes.

---

## 2. Conceptual Foundation & Invariants

### 1. The SQL Query:
```sql
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(1) >= 5;
```

### 2. Primary Key Uniqueness:
- Because `(student, class)` is declared as the primary key in modern problem statements, each row represents a unique student enrollment in that course.
- Therefore, `COUNT(1)` or `COUNT(student)` accurately measures distinct students without needing `COUNT(DISTINCT student)`.

> **Cardinality Threshold Invariant.** The predicate `COUNT(1) >= 5` in the `HAVING` clause guarantees that only groups with at least 5 distinct tuples survive into the projection.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Group Students by Class
- `Math`: $[A, C, E, G, H, I] \to$ count = 6.
- `English`: $[B] \to$ count = 1.
- `Biology`: $[D] \to$ count = 1.
- `Computer`: $[F] \to$ count = 1.

---

### Step 2: Evaluate `HAVING COUNT(1) >= 5`
- `Math`: $6 \ge 5 \implies \mathbf{True}$.
- Others: $1 < 5 \implies \mathbf{False}$.

---

### Step 3: Project `class`
- Result:
  $$
  \mathbf{\text{"Math"}}
  $$

---

## 4. Complete Execution Trace

| `class` | Students Enrolled | `COUNT(student)` | $\ge 5$? | Included in Output? |
|:---:|:---:|:---:|:---:|:---:|
| **`Math`** | $A, C, E, G, H, I$ | **$6$** | **Yes** | **Yes (`Math`)** |
| `English` | $B$ | $1$ | No | No |
| `Biology` | $D$ | $1$ | No | No |
| `Computer` | $F$ | $1$ | No | No |

---

## 5. Boundary Cases & Failure Modes

- **Class with Exactly 5 Students:** $5 \ge 5 \implies$ Qualifies!
- **Class with 4 Students:** $4 < 5 \implies$ Disqualified.
- **No Classes with $\ge 5$ Students:** Query outputs empty result table with header `class`.
- **Large University Dataset ($10^5$ enrollments):** Hash aggregation groups courses in a single linear pass.

---

## 6. Traps & Common Anti-Patterns

- **Attempting `WHERE COUNT(*) >= 5`:** In SQL, aggregate functions cannot appear in the `WHERE` clause because aggregation happens *after* `WHERE` filtering. Aggregate filters must go in `HAVING`.
- **Using Strict Greater-Than (`> 5`):** The problem specifies *at least* 5, meaning 5 is valid. Writing `> 5` drops classes with exactly 5 students.
- **Using Subqueries Instead of `HAVING`:** Writing `SELECT class FROM (SELECT class, count(*) ... ) WHERE count >= 5` works but is unnecessarily verbose compared to the standard `HAVING` clause.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the number of rows in `Courses` and $K$ be the number of distinct classes.
  - Grouping and counting with hash aggregation: $\mathcal{O}(N)$.
  - Filtering $K$ groups via `HAVING`: $\mathcal{O}(K)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K)$ space for group aggregation accumulators.
