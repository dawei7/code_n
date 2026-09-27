# Guided Example: Department Highest Salary

We trace the step-by-step SQL department partitioned grouping, tuple membership matching, and multi-employee tie preservation on representative company organization tables:

- **Input Tables:**
  - `Employee`: `[(1, "Joe", 85000, 1), (2, "Jim", 90000, 1), (3, "Henry", 80000, 2), (4, "Sam", 60000, 2), (5, "Max", 90000, 1)]`
  - `Department`: `[(1, "IT"), (2, "Sales")]`
- **Required output:**
  - `[["IT", "Jim", 90000], ["IT", "Max", 90000], ["Sales", "Henry", 80000]]` (Both Jim and Max share the top salary of $90,000$ in IT)
- **Single Employee Department Instance:** `Employee = [(1, "Randy", 70000, 1)] \implies [["IT", "Randy", 70000]]`
- **Department With No Employees Instance:** Department exists in `Department` but has no rows in `Employee` $\implies$ Omitted from output.

This instance demonstrates SQL group partition maximums (`MAX(salary)`), proves why naive grouping violates `ONLY_FULL_GROUP_BY` and drops tied employees, uses tuple-membership filtering `(departmentId, salary) IN (...)` to preserve all co-earners, and executes in $O(E + D)$ time.

---

## 1. Instance & Teaching Goal

Given two relational tables:
1. `Employee`:
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
   \hline
   \end{array}
   $$
2. `Department`:
   $$
   \begin{array}{|c|c|}
   \hline
   \textbf{id} & \textbf{name} \\
   \hline
   1 & \text{IT} \\
   2 & \text{Sales} \\
   \hline
   \end{array}
   $$
Find the employee(s) who have the highest salary in each department. If multiple employees in the same department share the top salary, **all of them must be included**.

In this organization:
- In Department 1 (`"IT"`): salaries are $85000, 90000, 90000$. The department maximum is $90000$, earned by both Jim and Max. Both must appear in the result table!
- In Department 2 (`"Sales"`): salaries are $80000, 60000$. The department maximum is $80000$, earned by Henry.
The output table columns must be `["Department", "Employee", "Salary"]`.

---

## 2. Conceptual Foundation & Invariants

### Method A: Tuple Membership Filtering (Recommended)
```sql
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d 
    ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
);
```

#### Why Tuple `IN` Works:
1. **Compute Thresholds First:**
   The inner query aggregates `Employee` by `departmentId` to determine the maximum salary for each department:
   $$
   \mathcal{M} = \{ (\text{dept}_1, \max_1), \, (\text{dept}_2, \max_2), \dots \}
   $$
2. **Filter Matching Employees:**
   The outer query checks if `(e.departmentId, e.salary) \in \mathcal{M}`.
   Every employee whose salary exactly equals their department's maximum passes the filter, cleanly retaining ties without arbitrary selection.
3. **Join Department Name:**
   `JOIN Department d ON e.departmentId = d.id` resolves the textual department name.

### Method B: Window Function `DENSE_RANK()`
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
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
) ranked
WHERE rnk = 1;
```

> **Invariant.** An employee $e$ is emitted if and only if $e.\text{salary} = \max \{ e'.\text{salary} \mid e'.\text{departmentId} = e.\text{departmentId} \}$.

---

## 3. Step-by-Step Worked Execution

We trace the subquery and filter evaluation:

### Step 1: Compute Department Maximums (Subquery)
Group `Employee` by `departmentId` and compute `MAX(salary)`:
- **Department 1:** Salaries $\{85000, 90000, 90000\} \implies \max = \mathbf{90000}$.
  Group pair: `(1, 90000)`.
- **Department 2:** Salaries $\{80000, 60000\} \implies \max = \mathbf{80000}$.
  Group pair: `(2, 80000)`.

Subquery candidate set:
$$
\mathcal{M} = \{ (1, 90000), \, (2, 80000) \}
$$

---

### Step 2: Outer Join and Filter Each Employee
Evaluate each row in `Employee`:
- **Row 1 (Joe):** `(dept: 1, salary: 85000)`.
  Is $(1, 85000) \in \mathcal{M}$? No ($85000 \ne 90000$). Discarded.
- **Row 2 (Jim):** `(dept: 1, salary: 90000)`.
  Is $(1, 90000) \in \mathcal{M}$? **Yes!**
  Join with `Department` 1 $\implies$ Department name `"IT"`.
  Emit row: `["IT", "Jim", 90000]`.
- **Row 3 (Henry):** `(dept: 2, salary: 80000)`.
  Is $(2, 80000) \in \mathcal{M}$? **Yes!**
  Join with `Department` 2 $\implies$ Department name `"Sales"`.
  Emit row: `["Sales", "Henry", 80000]`.
- **Row 4 (Sam):** `(dept: 2, salary: 60000)`.
  Is $(2, 60000) \in \mathcal{M}$? No ($60000 \ne 80000$). Discarded.
- **Row 5 (Max):** `(dept: 1, salary: 90000)`.
  Is $(1, 90000) \in \mathcal{M}$? **Yes!**
  Join with `Department` 1 $\implies$ Department name `"IT"`.
  Emit row: `["IT", "Max", 90000]`.

---

### Step 3: Final Output Assembly
Emitted rows:
- `["IT", "Jim", 90000]`
- `["IT", "Max", 90000]`
- `["Sales", "Henry", 80000]`

---

## 4. Complete Execution Trace

```text
Employee Table:
1: Joe   (Dept 1, 85k)
2: Jim   (Dept 1, 90k) -> MATCH (Dept 1 max)
3: Henry (Dept 2, 80k) -> MATCH (Dept 2 max)
4: Sam   (Dept 2, 60k)
5: Max   (Dept 1, 90k) -> MATCH (Dept 1 max, tie with Jim)

Result Table:
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
```

| Employee ID | Employee Name | Department ID | Salary | In Subquery $\mathcal{M}$? | Department Name | Emitted Output |
|:---:|:---|:---:|:---:|:---:|:---|:---|
| 1 | Joe | 1 | 85000 | No | IT | - |
| **2** | **Jim** | **1** | **90000** | **Yes** | **IT** | **`["IT", "Jim", 90000]`** |
| **3** | **Henry** | **2** | **80000** | **Yes** | **Sales** | **`["Sales", "Henry", 80000]`** |
| 4 | Sam | 2 | 60000 | No | Sales | - |
| **5** | **Max** | **1** | **90000** | **Yes** | **IT** | **`["IT", "Max", 90000]`** |

---

## 5. Algorithmic Correctness

**Soundness.** The grouped subquery extracts the exact numerical maximum salary for each `departmentId`. An employee is selected if and only if their `(departmentId, salary)` pair matches the subquery, guaranteeing that every returned employee is a top earner in their department.

**Completeness.** Unlike a direct `GROUP BY` which selects only one row per department, tuple matching tests every employee independently. When multiple employees tie for the top salary, each tied employee matches the pair and is emitted.

---

## 6. Traps This Instance Exposes

- **Grouping Directly by Department (`GROUP BY d.name`):** Selecting `e.name, MAX(e.salary)` directly with `GROUP BY d.name` fails under standard SQL (`ONLY_FULL_GROUP_BY`) and unpredictably returns only one arbitrary employee when ties exist.
- **Tied Maximums:** Failing to return both Jim and Max fails test cases. Tuple matching or `DENSE_RANK() OVER (PARTITION BY ...)` handles ties cleanly.
- **Empty Departments:** If a department has no employees, it will not appear in the subquery or the inner join, correctly avoiding empty or null employee output.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E + D)$, where $E$ is the number of employees and $D$ is the number of departments. Computing department maximums takes $O(E)$ via hash grouping. Joining and filtering takes $O(E)$ time.
- **Auxiliary Space Complexity:** $O(D)$ hash table memory to store the maximum salary for each department.
