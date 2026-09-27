# Guided Example: Count Student Number in Departments

We trace the step-by-step master entity preservation (`Department LEFT JOIN Student`), null-safe attribute counting (`COUNT(student_id)` vs `COUNT(*)`), empty department zero-count normalization, multi-key ordering (`student_number DESC, dept_name ASC`), and aggregated student census reporting on representative academic databases:

- **Input:**
  - `Department` table:
    | `dept_id` | `dept_name` |
    |:---:|:---:|
    | $1$ | `Engineering` |
    | $2$ | `Science` |
    | $3$ | `Law` |
  - `Student` table:
    | `student_id` | `student_name` | `gender` | `dept_id` |
    |:---:|:---:|:---:|:---:|
    | $1$ | `Jack` | `M` | $1$ |
    | $2$ | `Jane` | `F` | $1$ |
    | $3$ | `Mark` | `M` | $2$ |
- **Required output:**
  | `dept_name` | `student_number` |
  |:---:|:---:|
  | `Engineering` | $2$ |
  | `Science` | $1$ |
  | `Law` | $0$ |
  - Business rules:
    1. Output every department in the `Department` table, including departments with **zero currently enrolled students**.
    2. Sort results in descending order of `student_number`.
    3. If two departments have the same number of students, order them alphabetically by `dept_name ASC`.
- **Relational Outer Join & Aggregation Trace:**
  - **Step 1: Left Outer Join from `Department` to `Student`:**
    - An inner join would completely discard `Law` because no student has `dept_id = 3`.
    - A `LEFT JOIN` preserves all department rows, populating absent student attributes with `NULL`:
      - `dept_id = 1` (Engineering): Joins with Jack (`student_id = 1`) and Jane (`student_id = 2`).
      - `dept_id = 2` (Science): Joins with Mark (`student_id = 3`).
      - `dept_id = 3` (Law): No matching students $\implies$ Joined row: `(3, 'Law', NULL, NULL, NULL, 3)`.
  - **Step 2: Group by Department and Count Students:**
    - Group by `dept_id` (or `dept_name`):
      - **Engineering:** Student IDs present: $\{1, 2\}$.
        $$
        \text{COUNT}(student\_id) = \mathbf{2}
        $$
      - **Science:** Student IDs present: $\{3\}$.
        $$
        \text{COUNT}(student\_id) = \mathbf{1}
        $$
      - **Law:** Student IDs present: $\{\text{NULL}\}$.
        - Critical SQL Semantic Rule: `COUNT(column_name)` counts **only non-null values**!
        - Since `student_id` is `NULL`, it contributes $0$:
          $$
          \text{COUNT}(student\_id) = \mathbf{0}
          $$
        - *(Note: If `COUNT(*)` had been used, it would count the row itself and erroneously report 1!)*
  - **Step 3: Sort by Student Count (DESC) and Department Name (ASC):**
    - Tally results:
      1. `Engineering`: $2$ students
      2. `Science`: $1$ student
      3. `Law`: $0$ students
    - Output table correctly orders the counts: $2 \to 1 \to 0$.
- **Alphabetical Tie-Breaking Example:**
  - If `Arts` and `Music` both have 0 students:
    - Secondary sort `dept_name ASC` orders `Arts` before `Music`.
- **All Departments Empty:**
  - All departments report `0`, sorted alphabetically by `dept_name`.

This instance demonstrates outer join entity preservation and null-discriminating SQL aggregation, mathematically proves why `COUNT(attribute)` is necessary to avoid counting null placeholder rows, and derives $O(D + S \log D)$ execution time and $O(D)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a `Department` table and a `Student` table:
Report the department name and number of students enrolled for **all departments** in the database.
If a department has no students, report `0`.
Order by `student_number DESC, dept_name ASC`.

```text
Departments:
  Engineering (id 1): Jack, Jane -> 2 students
  Science     (id 2): Mark       -> 1 student
  Law         (id 3): (No one)   -> 0 students

Output:
  Engineering | 2
  Science     | 1
  Law         | 0
```

### The Pitfall of `COUNT(*)` vs `COUNT(student_id)`
- When a `LEFT JOIN` finds no matching right row, it produces a single row filled with `NULL`s for all columns of the right table.
- `COUNT(*)` counts the **number of rows in the group**; for `Law`, there is 1 joined row, so `COUNT(*)` would evaluate to `1`!
- `COUNT(student_id)` counts the **number of non-null values** in that specific column; since `student_id` is `NULL` for `Law`, it correctly evaluates to `0`!

---

## 2. Conceptual Foundation & Invariants

### 1. Left Outer Join:
```sql
FROM Department
LEFT JOIN Student USING (dept_id)
```
- Guarantees every department appears in the result stream.

### 2. Null-Aware Aggregation:
```sql
SELECT dept_name, COUNT(student_id) AS student_number
GROUP BY dept_id, dept_name
```
- Counts only valid, non-null student IDs.

### 3. Multi-Key Ordering:
```sql
ORDER BY student_number DESC, dept_name ASC;
```

> **Entity Preservation Invariant.** Performing a left join anchored on the master entity table `Department` prevents orphaned or unpopulated categories from being pruned from enterprise census reporting.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Left Join
- Engineering (1) $\bowtie$ Student 1 (Jack)
- Engineering (1) $\bowtie$ Student 2 (Jane)
- Science (2) $\bowtie$ Student 3 (Mark)
- Law (3) $\bowtie$ (NULL, NULL, NULL)

---

### Step 2: Group by `dept_id`
- **Group 1 (Engineering):**
  - Non-null `student_id` values: $[1, 2] \implies \text{COUNT} = \mathbf{2}$.
- **Group 2 (Science):**
  - Non-null `student_id` values: $[3] \implies \text{COUNT} = \mathbf{1}$.
- **Group 3 (Law):**
  - Non-null `student_id` values: $[] \implies \text{COUNT} = \mathbf{0}$.

---

### Step 3: Sort
- Rank 1: Engineering ($2$)
- Rank 2: Science ($1$)
- Rank 3: Law ($0$)

---

## 4. Complete Execution Trace

| `dept_name` | `dept_id` | Matching `student_id`s | `COUNT(student_id)` | Rank (Count DESC, Name ASC) |
|:---:|:---:|:---:|:---:|:---:|
| **`Engineering`** | $1$ | $1, 2$ | **$2$** | **$1$** |
| **`Science`** | $2$ | $3$ | **$1$** | **$2$** |
| **`Law`** | $3$ | `NULL` | **$0$** | **$3$** |

---

## 5. Boundary Cases & Failure Modes

- **Tied Student Counts:** Secondary ordering `dept_name ASC` sorts alphabetically.
- **Empty `Student` Table:** All departments produce count `0`, listed in alphabetical order.
- **Single Department:** Projects that single department with its count.

---

## 6. Traps & Common Anti-Patterns

- **Using `INNER JOIN`:** Discards departments with no students (e.g. `Law`), failing the requirement to report on *all* departments.
- **Using `COUNT(*)` in Outer Joins:** Counts the synthetic null row as 1, erroneously reporting 1 student in empty departments.
- **Grouping Only by `dept_name` Without ID:** If two distinct departments share the same name but have different `dept_id`s, grouping only by `dept_name` merges their student bodies. Grouping by `dept_id` preserves department identity.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $D$ be the number of departments and $S$ be the number of students.
  - Left outer hash join on `dept_id`: $\mathcal{O}(D + S)$.
  - Grouping and aggregation: $\mathcal{O}(D)$.
  - Sorting $D$ departments: $\mathcal{O}(D \log D)$.
  - Total Time: $\mathcal{O}(D \log D + S)$. Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(D)$ space to store aggregated department counts.
