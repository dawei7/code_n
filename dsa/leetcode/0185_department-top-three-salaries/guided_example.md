# Guided Example: Department Top Three Salaries

We trace the step-by-step SQL partitioned dense ranking and correlated greater-salary counting on representative multi-department compensation tables:

- **Input Tables:**
  - `Employee`: `[(1, "Joe", 85000, 1), (2, "Jim", 90000, 1), (3, "Henry", 80000, 2), (4, "Sam", 60000, 2), (5, "Max", 90000, 1), (6, "Janet", 69000, 1), (7, "Randy", 85000, 1)]`
  - `Department`: `[(1, "IT"), (2, "Sales")]`
- **Required output:**
  - `[["IT", "Jim", 90000], ["IT", "Max", 90000], ["IT", "Joe", 85000], ["IT", "Randy", 85000], ["IT", "Janet", 69000], ["Sales", "Henry", 80000], ["Sales", "Sam", 60000]]`
- **Fewer Than Three Salaries Instance:** Department with only 1 or 2 employees $\implies$ All employees in that department qualify.

This instance demonstrates SQL partitioned window ranking (`DENSE_RANK() OVER (PARTITION BY ...)`), explains why ties require dense rather than sparse ranking to avoid skipping tiers, establishes the correlated subquery equivalence ($\text{count of strictly greater distinct salaries} < 3$), and operates in $O(E \log E)$ time.

---

## 1. Instance & Teaching Goal

Given `Employee` and `Department` tables:
$$
\begin{array}{|c|c|c|c|}
\hline
\textbf{id} & \textbf{name} & \textbf{salary} & \textbf{departmentId} \\
\hline
1 & \text{Joe} & 85000 & 1 \\
2 & \text{Jim} & 90000 & 1 \\
3 & \text{Henry} & 80000 & 2 \\
4 & \text{Sam} & 60000 & 2 \\
5 & \text{Max} & 90000 & 1 \\
6 & \text{Janet} & 69000 & 1 \\
7 & \text{Randy} & 85000 & 1 \\
\hline
\end{array}
\qquad
\begin{array}{|c|c|}
\hline
\textbf{id} & \textbf{name} \\
\hline
1 & \text{IT} \\
2 & \text{Sales} \\
\hline
\end{array}
$$
Find all employees who earn in the **top three unique salaries** for their respective department.

Analyzing Department 1 (`"IT"`):
- Salaries present: $90000, 90000, 85000, 85000, 69000$.
- Unique salary values sorted descending:
  1. Rank 1: $90000$ (Earned by Jim and Max)
  2. Rank 2: $85000$ (Earned by Joe and Randy)
  3. Rank 3: $69000$ (Earned by Janet)
Notice that although there are 5 employees in IT, all 5 belong to the top 3 **unique** salary tiers!
If one used standard `RANK()`, the ranks would be $1, 1, 3, 3, 5$, which would wrongly disqualify Janet!
`DENSE_RANK()` assigns ranks $1, 1, 2, 2, 3$, correctly qualifying all five employees.

Analyzing Department 2 (`"Sales"`):
- Unique salaries: $80000$ (Henry, Rank 1) and $60000$ (Sam, Rank 2). Both qualify.

---

## 2. Conceptual Foundation & Invariants

### Method A: Window Function `DENSE_RANK()` (Recommended)
```sql
SELECT 
    Department,
    Employee,
    Salary
FROM (
    SELECT 
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (
            PARTITION BY e.departmentId 
            ORDER BY e.salary DESC
        ) AS rnk
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
) ranked
WHERE rnk <= 3;
```

#### Why `DENSE_RANK()` with `PARTITION BY` Is Optimal:
1. `PARTITION BY e.departmentId`: Restarts the ranking evaluation independently within each department.
2. `ORDER BY e.salary DESC`: Evaluates the highest earners first.
3. Dense Rank Property: Equal salaries receive identical ranks, and the next distinct salary receives rank $+1$ without gaps ($1, 1, 2, 2, 3$).
4. Outer Filter `rnk <= 3`: Keeps all employees whose salary belongs to unique tiers 1, 2, or 3.

### Method B: Correlated Subquery
```sql
SELECT 
    d.name AS Department,
    e1.name AS Employee,
    e1.salary AS Salary
FROM Employee e1
JOIN Department d ON e1.departmentId = d.id
WHERE (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = e1.departmentId 
      AND e2.salary > e1.salary
) < 3;
```
For any employee $e_1$, count the number of distinct salaries in the same department strictly greater than $e_1.\text{salary}$. An employee is in the top 3 unique salaries if and only if fewer than 3 distinct salaries exceed theirs.

> **Invariant.** An employee $e$ qualifies if and only if $|\{ s \in \text{distinct department salaries} \mid s > e.\text{salary} \}| < 3$.

---

## 3. Step-by-Step Worked Execution

We trace the partitioned dense rank calculation for each department:

### Department 1 (`"IT"`, $departmentId = 1$):
Sorted distinct salaries: $90000 > 85000 > 69000$.
- **Jim ($90000$):** Highest salary $\implies \mathbf{\text{rnk} = 1} \le 3$. **Included.**
- **Max ($90000$):** Tied with Jim $\implies \mathbf{\text{rnk} = 1} \le 3$. **Included.**
- **Joe ($85000$):** 2nd highest distinct $\implies \mathbf{\text{rnk} = 2} \le 3$. **Included.**
- **Randy ($85000$):** Tied with Joe $\implies \mathbf{\text{rnk} = 2} \le 3$. **Included.**
- **Janet ($69000$):** 3rd highest distinct $\implies \mathbf{\text{rnk} = 3} \le 3$. **Included.**

All 5 employees in IT qualify!

---

### Department 2 (`"Sales"`, $departmentId = 2$):
Sorted distinct salaries: $80000 > 60000$.
- **Henry ($80000$):** Highest salary $\implies \mathbf{\text{rnk} = 1} \le 3$. **Included.**
- **Sam ($60000$):** 2nd highest distinct $\implies \mathbf{\text{rnk} = 2} \le 3$. **Included.**

Both employees in Sales qualify!

---

### Final Output Assembly
All 7 employee rows qualify:
- `["IT", "Jim", 90000]`
- `["IT", "Max", 90000]`
- `["IT", "Joe", 85000]`
- `["IT", "Randy", 85000]`
- `["IT", "Janet", 69000]`
- `["Sales", "Henry", 80000]`
- `["Sales", "Sam", 60000]`

---

## 4. Complete Execution Trace

```text
IT Department (Dept 1):
  Jim   (90k) -> DENSE_RANK = 1 <= 3 -> KEEP
  Max   (90k) -> DENSE_RANK = 1 <= 3 -> KEEP
  Joe   (85k) -> DENSE_RANK = 2 <= 3 -> KEEP
  Randy (85k) -> DENSE_RANK = 2 <= 3 -> KEEP
  Janet (69k) -> DENSE_RANK = 3 <= 3 -> KEEP

Sales Department (Dept 2):
  Henry (80k) -> DENSE_RANK = 1 <= 3 -> KEEP
  Sam   (60k) -> DENSE_RANK = 2 <= 3 -> KEEP

Result: All 7 employees qualify
```

| Employee | Department | Salary | `DENSE_RANK()` | `RANK()` Contrast (Sparse) | `rnk <= 3` Condition | Final Status |
|:---|:---|:---:|:---:|:---:|:---:|:---|
| **Jim** | IT | 90000 | **1** | 1 | $1 \le 3$ | **Emitted** |
| **Max** | IT | 90000 | **1** | 1 | $1 \le 3$ | **Emitted** |
| **Joe** | IT | 85000 | **2** | 3 | $2 \le 3$ | **Emitted** |
| **Randy** | IT | 85000 | **2** | 3 | $2 \le 3$ | **Emitted** |
| **Janet** | IT | 69000 | **3** | 5 *(dropped)* | $3 \le 3$ | **Emitted** |
| **Henry** | Sales | 80000 | **1** | 1 | $1 \le 3$ | **Emitted** |
| **Sam** | Sales | 60000 | **2** | 2 | $2 \le 3$ | **Emitted** |

---

## 5. Algorithmic Correctness

**Soundness.** `DENSE_RANK()` partitions employees by department and ranks unique salary values. Since ties share the same rank and the rank only increases by 1 between distinct salary values, filtering `rnk <= 3` captures every employee whose salary is in the top 3 unique values.

**Completeness.** Every employee is evaluated within their department. If a department has fewer than 3 unique salaries, all employees in that department will have `rnk <= 2` or `rnk = 1`, guaranteeing that no employee is falsely dropped.

---

## 6. Traps This Instance Exposes

- **Using `RANK()` Instead of `DENSE_RANK()`:** In IT, using `RANK()` produces $[1, 1, 3, 3, 5]$, dropping Janet even though her salary $69000$ is the 3rd unique salary in IT!
- **Correlated Subquery `< 3` vs `<= 3`:** When counting strictly greater distinct salaries (`e2.salary > e1.salary`), the condition is `< 3` (meaning $0, 1,$ or $2$ strictly greater salaries exist). Using `<= 3` would include the top 4 tiers.
- **Forgetting `DISTINCT` in Subquery:** If counting greater salaries without `DISTINCT`, multiple higher-paid employees would overcount and prematurely push lower tiers out of the top 3.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E \log E)$, where $E$ is the number of rows in `Employee`. The database sorts rows by `(departmentId, salary DESC)` in $O(E \log E)$ and computes the window dense rank in a single $O(E)$ pass.
- **Auxiliary Space Complexity:** $O(E)$ working memory to maintain the window partitions.
