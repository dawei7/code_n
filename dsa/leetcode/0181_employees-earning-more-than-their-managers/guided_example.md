# Guided Example: Employees Earning More Than Their Managers

We trace the step-by-step SQL relational self-join execution and managerial hierarchy salary comparison on representative enterprise organizational tables:

- **Input Table `Employee`:**
  - `[(1, "Joe", 70000, 3), (2, "Henry", 80000, 4), (3, "Sam", 60000, null), (4, "Max", 90000, null)]`
- **Required output:**
  - `{"columns": ["Employee"], "rows": [["Joe"]]}` (Joe earns $70,000$ compared to manager Sam's $60,000$)
- **Top-Level Executive Instance:** `Employee = [(1, "Owner", 100000, null)] \implies \text{Empty Set}` (`managerId = NULL` naturally excluded by inner join)
- **Equal Salary Instance:** `Employee = [(1, "Alice", 50000, 2), (2, "Bob", 50000, null)] \implies \text{Empty Set}` (Strict inequality $e.\text{salary} > m.\text{salary}$ excludes ties)

This instance demonstrates SQL self-joins on hierarchical foreign keys (`e.managerId = m.id`), explains why `NULL` manager IDs are cleanly eliminated by inner joins without explicit `WHERE` guards, evaluates strict salary inequalities, and executes in $O(N)$ time with primary-key indexing.

---

## 1. Instance & Teaching Goal

Given the `Employee` table:
$$
\begin{array}{|c|c|c|c|}
\hline
\textbf{id} & \textbf{name} & \textbf{salary} & \textbf{managerId} \\
\hline
1 & \text{Joe} & 70000 & 3 \\
2 & \text{Henry} & 80000 & 4 \\
3 & \text{Sam} & 60000 & \text{null} \\
4 & \text{Max} & 90000 & \text{null} \\
\hline
\end{array}
$$
Find all employees who earn strictly more than their direct manager.

In this company:
- Joe ($id = 1$, salary $70,000$) reports to Sam ($id = 3$, salary $60,000$).
  Since $70,000 > 60,000$, Joe earns more than his manager.
- Henry ($id = 2$, salary $80,000$) reports to Max ($id = 4$, salary $90,000$).
  Since $80,000 < 90,000$, Henry earns less.
- Sam and Max have no managers (`managerId IS NULL`).
Output must be a table with a single column `Employee` containing `"Joe"`.

---

## 2. Conceptual Foundation & Invariants

### The Relational Self-Join Paradigm
Because both employee and manager records reside within the exact same table, the query joins `Employee` to itself under two distinct roles:
- `e` (Employee perspective): the subordinate whose salary is evaluated.
- `m` (Manager perspective): the supervisor whose salary acts as the benchmark.

```sql
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m 
    ON e.managerId = m.id
WHERE e.salary > m.salary;
```

### Inner Join Filtering Mechanics
1. **Foreign Key Alignment:** `e.managerId = m.id` bridges the subordinate row to the manager's primary key row.
2. **Null Safety:** For employees where `managerId IS NULL` (like the CEO or top executives), evaluating `NULL = m.id` yields `UNKNOWN`. Inner joins only retain tuples where the condition is `TRUE`, naturally filtering out employees without managers.
3. **Strict Salary Inequality:** `WHERE e.salary > m.salary` rejects equal compensation or lower compensation.

> **Invariant.** A row is emitted if and only if $e.\text{managerId} = m.\text{id}$ is valid, and $e.\text{salary} > m.\text{salary}$.

---

## 3. Step-by-Step Worked Execution

We trace the join evaluation across all rows of `Employee`:

### Subordinate Evaluation 1: Joe ($id = 1$)
- Record: `(id: 1, name: "Joe", salary: 70000, managerId: 3)`.
- Join lookup: Find row where $m.\text{id} == 3$.
  - Found: Sam `(id: 3, name: "Sam", salary: 60000)`.
- Compare salaries:
  $$
  e.\text{salary} > m.\text{salary} \iff 70000 > 60000 \implies \mathbf{True}
  $$
- Joe qualifies! Emit `"Joe"`.

---

### Subordinate Evaluation 2: Henry ($id = 2$)
- Record: `(id: 2, name: "Henry", salary: 80000, managerId: 4)`.
- Join lookup: Find row where $m.\text{id} == 4$.
  - Found: Max `(id: 4, name: "Max", salary: 90000)`.
- Compare salaries:
  $$
  e.\text{salary} > m.\text{salary} \iff 80000 > 90000 \implies \mathbf{False}
  $$
- Henry does not qualify. Discarded.

---

### Subordinate Evaluation 3: Sam ($id = 3$)
- Record: `(id: 3, name: "Sam", salary: 60000, managerId: null)`.
- Join lookup: `managerId` is `null`.
- In SQL, `null = m.id` is `UNKNOWN`. No matching row in `m`.
- Discarded by inner join.

---

### Subordinate Evaluation 4: Max ($id = 4$)
- Record: `(id: 4, name: "Max", salary: 90000, managerId: null)`.
- `managerId` is `null`. Discarded by inner join.

---

### Assembly
- Qualifying records: `["Joe"]`.
- Emitted output column: `Employee = "Joe"`.

---

## 4. Complete Execution Trace

```text
Subordinate Table (e)                 Manager Table (m)
1: Joe   (70k, mgr: 3)  <-- join -->  3: Sam (60k)  -> 70k > 60k: KEEP (Joe)
2: Henry (80k, mgr: 4)  <-- join -->  4: Max (90k)  -> 80k > 90k: DROP
3: Sam   (60k, mgr: null)             No manager    -> DROP
4: Max   (90k, mgr: null)             No manager    -> DROP

Result Table:
+----------+
| Employee |
+----------+
| Joe      |
+----------+
```

| Subordinate $e$ | Subordinate Salary | Manager ID | Manager $m$ | Manager Salary | $e.\text{salary} > m.\text{salary}$ | Join Action |
|:---|:---:|:---:|:---|:---:|:---:|:---:|
| **Joe (1)** | **70000** | **3** | **Sam (3)** | **60000** | **$70000 > 60000$ (True)** | **Emit `"Joe"`** |
| Henry (2) | 80000 | 4 | Max (4) | 90000 | $80000 > 90000$ (False) | Rejected |
| Sam (3) | 60000 | `null` | None | - | `null` join | Dropped |
| Max (4) | 90000 | `null` | None | - | `null` join | Dropped |

---

## 5. Algorithmic Correctness

**Soundness.** The predicate `e.managerId = m.id` establishes the direct supervisor relationship. The condition `e.salary > m.salary` selects only employees whose earnings strictly exceed their supervisor's earnings.

**Completeness.** Since an inner join checks every subordinate against their manager, all employee-manager pairs in the company are evaluated.

---

## 6. Traps This Instance Exposes

- **Using Cartesian Product (`FROM Employee e, Employee m`):** Without the join condition `e.managerId = m.id`, an employee would be compared against *every* person in the company rather than their actual manager.
- **Equal Salary ($e.\text{salary} == m.\text{salary}$):** The requirement is strictly *more than*, not *greater than or equal to*. Using `>=` erroneously includes tied salaries.
- **Handling `NULL` Manager IDs:** Using `LEFT JOIN` without filtering would require explicit `WHERE m.salary IS NOT NULL`. An `INNER JOIN` handles `NULL` manager IDs automatically.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of employees. With a primary key index on `Employee.id`, looking up the manager row for each employee takes $O(1)$ time in an index nested-loop join.
- **Auxiliary Space Complexity:** $O(N)$ working memory for join hash tables and result output.
