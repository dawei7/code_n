# Guided Example: Nth Highest Salary

We trace the step-by-step SQL function execution of parameter offset translation, distinct salary ordering, and scalar subquery null fallback on representative employee salary tables:

- **Input Table `Employee`:**
  - `[(1, 100), (2, 200), (3, 300)]`
  - Parameter: $N = 2$
- **Required output:**
  - `{"columns": ["getNthHighestSalary(2)"], "rows": [[200]]}`
- **Insufficient Records Instance:** `Employee = [(1, 100)], N = 2 \implies \text{null}` (Empty set from offset overflow evaluates to SQL `NULL`)
- **Duplicate Salary Instance:** `Employee = [(1, 300), (2, 300), (3, 200)], N = 2 \implies 200` (`DISTINCT` collapses duplicate salaries)

This instance demonstrates stored routine variable arithmetic (`SET N = N - 1`), maps 1-based rank queries onto 0-based MySQL `LIMIT 1 OFFSET N` operators, guarantees automatic `NULL` return when $N > |\text{distinct salaries}|$ or $N \le 0$, and executes in $O(M \log M)$ time.

---

## 1. Instance & Teaching Goal

Given the `Employee` table and an integer parameter $N = 2$:
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
Write a SQL function `getNthHighestSalary(N INT) RETURNS INT` that returns the $N^{\text{th}}$ highest distinct salary, or `null` if fewer than $N$ distinct salaries exist.

### 1-Based Ranks vs 0-Based SQL Offsets
In user requirements:
- The 1st highest salary has rank 1 ($N = 1$).
- The 2nd highest salary has rank 2 ($N = 2$).
In MySQL pagination:
- `LIMIT 1 OFFSET k` skips the first $k$ rows.
- To obtain rank 1, we skip $0$ rows (`OFFSET 0`).
- To obtain rank 2, we skip $1$ row (`OFFSET 1`).
Therefore, the rank parameter must be decremented:
$$
\text{offset} = N - 1
$$
Executing `SET N = N - 1` before the query aligns user ranks with SQL offset mechanics.

---

## 2. Conceptual Foundation & Invariants

### Stored Function Implementation
```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N
  );
END
```

### Alternative: Window Function `DENSE_RANK`
```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT salary
      FROM (
          SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
          FROM Employee
      ) t
      WHERE rnk = N
      LIMIT 1
  );
END
```

#### Why `DISTINCT` + `OFFSET` Is Preferred
1. **Deduplication:** `DISTINCT salary` ensures identical salaries share the exact same rank.
2. **Deterministic Ordering:** `ORDER BY salary DESC` sorts unique values from largest to smallest.
3. **Scalar Return:** Wrapping the query in `RETURN (...)` naturally coerces an empty set (e.g. when $N$ exceeds available distinct salaries) into SQL `NULL`.

> **Invariant.** For any valid positive rank $N \le |\mathcal{S}|$, the query returns the element at 0-indexed position $N - 1$ in the descending sorted set of distinct salaries. For any $N > |\mathcal{S}|$ or $N \le 0$, it returns `null`.

---

## 3. Step-by-Step Worked Execution

We trace `getNthHighestSalary(2)` on `Employee` with salaries $[100, 200, 300]$:

### Step 1: Adjust Offset
- Parameter received: $N = 2$.
- Execute adjustment:
  $$
  N \leftarrow 2 - 1 = \mathbf{1}
  $$
- The query will skip $1$ row.

---

### Step 2: Extract and Sort Distinct Salaries
- Scan `Employee`: values are $100, 200, 300$.
- Deduplicate and sort descending:
  $$
  \mathcal{S} = [300, \, 200, \, 100]
  $$
  - Index 0: $300$ (Rank 1)
  - Index 1: $200$ (Rank 2)
  - Index 2: $100$ (Rank 3)

---

### Step 3: Apply `LIMIT 1 OFFSET 1`
- `OFFSET 1`: Skip index 0 ($300$).
- `LIMIT 1`: Select index 1 ($200$).
- Value extracted: $200$.

---

### Step 4: Return Scalar Value
- `RETURN (200)` emits scalar integer $\mathbf{200}$.

---

### Contrast Trace: Out-of-Bounds Query $N = 4$
1. $N \leftarrow 4 - 1 = 3$.
2. Distinct sorted salaries: $[300, 200, 100]$ (only 3 elements, indices 0, 1, 2).
3. `LIMIT 1 OFFSET 3`: Attempts to skip 3 rows. No rows remain. Subquery returns $\emptyset$ (0 rows).
4. `RETURN (Empty Set)` coerces to SQL `NULL`.
5. Emits $\mathbf{\text{null}}$.

---

## 4. Complete Execution Trace

```text
Function Call: getNthHighestSalary(N = 2)

Step 1: SET N = 2 - 1 = 1 (offset to skip)
Step 2: SELECT DISTINCT salary -> { 100, 200, 300 }
Step 3: ORDER BY salary DESC   -> [ 300, 200, 100 ]
Step 4: LIMIT 1 OFFSET 1       -> Value 200

Result: 200
```

| Execution Step | Function State | SQL Operation | Result Set Evaluated | Output Return |
|:---:|:---:|:---:|:---:|:---:|
| 1 | $N = 2$ | `SET N = N - 1` | $N = 1$ | Internal variable set |
| 2 | $N = 1$ | `DISTINCT salary` | $\{100, 200, 300\}$ | Unique set formed |
| 3 | $N = 1$ | `ORDER BY salary DESC` | $[300, 200, 100]$ | Ordered descending |
| 4 | $N = 1$ | `LIMIT 1 OFFSET 1` | `200` | 2nd highest isolated |
| **Final** | - | **`RETURN (200)`** | **`200`** | **`200`** |

---

## 5. Algorithmic Correctness

**Soundness.** Sorting distinct salaries in descending order maps the $k$-th distinct value to zero-based array index $k - 1$. Setting offset $N - 1$ ensures that the $N^{\text{th}}$ largest distinct salary is selected.

**Completeness.** When $N > |\mathcal{S}|$, the `OFFSET` skips past all available rows, producing an empty result set. In SQL, evaluating an empty subquery as a scalar expression returns `NULL`. Thus, `null` is returned for all out-of-bounds queries.

---

## 6. Traps This Instance Exposes

- **Failing to Decrement $N$:** Executing `LIMIT 1 OFFSET N` without decrementing causes $N = 2$ to skip 2 rows, incorrectly returning the 3rd highest salary ($100$) instead of the 2nd ($200$).
- **Non-Positive Values of $N$ ($N \le 0$):** If $N = 0$, $N - 1 = -1$, which causes a MySQL syntax error in `LIMIT`. In databases with strict mode, handling $N \le 0$ by validating `IF N < 1 THEN RETURN NULL;` prevents negative offset exceptions.
- **Duplicate Salaries:** Without `DISTINCT`, multiple employees with the same maximum salary occupy ranks 1, 2, etc., causing duplicate values to consume rank slots.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M \log M)$, where $M$ is the number of rows in `Employee`. Extracting unique salaries and sorting takes $O(M \log M)$. If an index exists on `salary`, index traversal achieves $O(N)$ time.
- **Auxiliary Space Complexity:** $O(U) \le O(M)$ temporary working memory to store distinct salary entries.
