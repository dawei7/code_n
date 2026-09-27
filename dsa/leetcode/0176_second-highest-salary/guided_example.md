# Guided Example: Second Highest Salary

We trace the step-by-step SQL relational execution of distinct ranking, offset extraction, and scalar subquery null coercion on representative employee salary tables:

- **Input Table `Employee`:**
  - `[(1, 100), (2, 200), (3, 300)]`
- **Required output:**
  - `{"columns": ["SecondHighestSalary"], "rows": [[200]]}`
- **Duplicate Salaries Instance:** `Employee = [(1, 300), (2, 300), (3, 200)] \implies 200` (`DISTINCT` collapses duplicate maximums)
- **Insufficient Distinct Salaries Instance:** `Employee = [(1, 100)] \implies \text{null}` (Scalar subquery evaluates empty set as `NULL`)

This instance demonstrates handling SQL empty-set vs `NULL` semantics, explains why raw `LIMIT 1 OFFSET 1` returns 0 rows (failing the 1-row requirement), wraps the query in a scalar expression or `MAX` filter to guarantee a 1-row `NULL` output, and achieves $O(N)$ execution time.

---

## 1. Instance & Teaching Goal

Given the `Employee` table:
$$
\begin{array}{|c|c|}
\hline
\textbf{id} & \textbf{salary} \\
\hline
1 & 100 \\
2 & 200 \\
3 & 300 \\
\hline
\end{array}
$$
Find the second highest distinct salary. If there is no second highest salary (e.g. fewer than 2 distinct values exist), return `null` as a single-row result table named `SecondHighestSalary`.

### The SQL "0 Rows" vs "1 Row with NULL" Trap
If one naively executes:
```sql
SELECT DISTINCT salary 
FROM Employee 
ORDER BY salary DESC 
LIMIT 1 OFFSET 1;
```
- On the table above, it correctly returns `200`.
- But if the table has only one employee `[(1, 100)]`, the query returns **0 rows (Empty Set)**!
- The problem requirement explicitly demands **1 row containing `null`**:
  $$
  \begin{array}{|c|}
  \hline
  \textbf{SecondHighestSalary} \\
  \hline
  \text{null} \\
  \hline
  \end{array}
  $$
An empty result set evaluates to a wrong answer.
Wrapping the query inside a **scalar subquery** (`SELECT (...) AS SecondHighestSalary`) guarantees that if the inner query returns 0 rows, the scalar expression evaluates to SQL `NULL`, emitting exactly 1 row.

---

## 2. Conceptual Foundation & Invariants

### Method A: Scalar Subquery with Distinct Offset (Optimal)
```sql
SELECT (
    SELECT DISTINCT salary 
    FROM Employee 
    ORDER BY salary DESC 
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
```

#### Why Method A Works:
1. `DISTINCT salary`: Collapses identical salaries so rank 2 is strictly smaller than rank 1 (handling duplicate maximums like `[300, 300, 200]`).
2. `ORDER BY salary DESC`: Sorts unique values in descending order ($300 \to 200 \to 100$).
3. `LIMIT 1 OFFSET 1`: Skips the highest salary (offset 1) and fetches the next single value.
4. `SELECT (...) AS SecondHighestSalary`: In ANSI SQL, a subquery used in place of an expression in a `SELECT` list is a **scalar subquery**. If the subquery produces no rows, the scalar expression evaluates to `NULL`, producing a single output row containing `null`.

### Method B: Aggregate `MAX` Exclusion Filter
```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (
    SELECT MAX(salary) 
    FROM Employee
);
```
Here, the subquery finds the global maximum $300$. The outer query filters for `salary < 300` and takes `MAX(salary)`. If no salary satisfies `< 300`, `MAX()` over an empty group naturally aggregates to `NULL`.

> **Invariant.** The query must emit exactly one row with column title `SecondHighestSalary`, containing the second largest element of the distinct salary set $\mathcal{S}$, or `null` if $|\mathcal{S}| < 2$.

---

## 3. Step-by-Step Worked Execution

We trace the query on `Employee` with salaries $[100, 200, 300]$:

### Step 1: Extract Distinct Salaries
- Source rows: `100, 200, 300`.
- Distinct projection:
  $$
  \mathcal{S} = \{100, 200, 300\}
  $$

---

### Step 2: Sort Descending
- Sort $\mathcal{S}$ descending:
  $$
  [300, \, 200, \, 100]
  $$
  - Row 0 (Rank 1): $300$
  - Row 1 (Rank 2): $200$
  - Row 2 (Rank 3): $100$

---

### Step 3: Apply `LIMIT 1 OFFSET 1`
- `OFFSET 1`: Skip row 0 ($300$).
- `LIMIT 1`: Select row 1 ($200$).
- Inner query result: a single tuple with value `200`.

---

### Step 4: Scalar Subquery Coercion
- The outer `SELECT (200) AS SecondHighestSalary` wraps the scalar value.
- Emits 1 row: `[[200]]`.

---

### Contrast Trace: Single Employee Table `[(1, 100)]`
1. Distinct salary: $\{100\}$.
2. Order descending: $[100]$.
3. `LIMIT 1 OFFSET 1`: Skips $100$. No rows remain. Inner query produces $\emptyset$ (0 rows).
4. Outer scalar wrapper evaluates $\emptyset$ as `NULL`.
5. Emits 1 row: `[[null]]`.

---

## 4. Complete Execution Trace

```text
Table: Employee (salaries: 100, 200, 300)

Step 1: SELECT DISTINCT salary -> { 100, 200, 300 }
Step 2: ORDER BY salary DESC   -> [ 300, 200, 100 ]
Step 3: LIMIT 1 OFFSET 1       -> [ 200 ]
Step 4: Scalar Subquery Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```

| Execution Stage | Input Rows Evaluated | Operation Applied | Intermediate State | Output Contribution |
|:---:|:---|:---:|:---:|:---:|
| 1 | `[100, 200, 300]` | `DISTINCT` | $\{100, 200, 300\}$ | Deduplicated |
| 2 | $\{100, 200, 300\}$ | `ORDER BY DESC` | $[300, 200, 100]$ | Sorted descending |
| 3 | $[300, 200, 100]$ | `OFFSET 1 LIMIT 1` | `200` | Second distinct picked |
| **4** | **`200`** | **Scalar `SELECT`** | **Single row `[[200]]`** | **`SecondHighestSalary = 200`** |

---

## 5. Algorithmic Correctness

**Soundness.** `DISTINCT` partitions the salary domain into unique equivalence classes. Ordering descending places the true distinct maxima at index 0 and the second distinct maximum at index 1.

**Completeness.** When fewer than 2 distinct salaries exist, `LIMIT 1 OFFSET 1` returns 0 rows. By the ANSI SQL standard for scalar subqueries, an empty subquery used as an expression evaluates to `NULL`. Wrapping it in an outer `SELECT` without a `FROM` clause guarantees exactly 1 row with `NULL` is returned.

---

## 6. Traps This Instance Exposes

- **Returning Empty Set Instead of NULL:** Without the outer `SELECT (...)` scalar wrapper, `LIMIT 1 OFFSET 1` produces an empty result set on 1-row tables, which fails tests.
- **Ignoring `DISTINCT`:** If an employer has multiple employees earning 300 (e.g. `[300, 300, 200]`), omitting `DISTINCT` causes `LIMIT 1 OFFSET 1` to return 300 as the "second" salary instead of 200.
- **Incorrect Column Alias:** LeetCode validates column header names verbatim. The alias must match `SecondHighestSalary` exactly.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$ or $O(N)$ with an index on `salary`. Scanning $N$ rows and selecting the top 2 distinct values takes $O(N)$ using quickselect or max-heap tracking.
- **Auxiliary Space Complexity:** $O(U) \le O(N)$ memory to buffer unique salary values during sorting.
