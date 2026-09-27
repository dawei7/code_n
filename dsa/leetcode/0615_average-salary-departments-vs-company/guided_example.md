# Guided Example: Average Salary: Departments VS Company

We trace the step-by-step monthly date truncation (`YYYY-MM`), company-wide monthly average salary windowing ($\text{AVG}(amount) \text{ OVER (PARTITION BY } pay\_date)$), departmental monthly average salary windowing ($\text{AVG}(amount) \text{ OVER (PARTITION BY } pay\_date, department\_id)$), relative benchmark comparison (`higher`, `lower`, `same`), deduplicated month-department projection, and comparative payroll reporting on representative corporate compensation datasets:

- **Input:**
  - `Salary` table:
    | `id` | `employee_id` | `amount` | `pay_date` |
    |:---:|:---:|:---:|:---:|
    | $1$ | $1$ | $9000$ | `2017-03-31` |
    | $2$ | $2$ | $6000$ | `2017-03-31` |
    | $3$ | $3$ | $10000$ | `2017-03-31` |
    | $4$ | $1$ | $7000$ | `2017-02-28` |
    | $5$ | $2$ | $6000$ | `2017-02-28` |
  - `Employee` table:
    | `employee_id` | `department_id` |
    |:---:|:---:|
    | $1$ | $1$ |
    | $2$ | $2$ |
    | $3$ | $2$ |
- **Required output:**
  | `pay_month` | `department_id` | `comparison` |
  |:---:|:---:|:---:|
  | `2017-03` | $1$ | `higher` |
  | `2017-03` | $2$ | `lower` |
  | `2017-02` | $1$ | `higher` |
  | `2017-02` | $2$ | `lower` |
  - Business benchmark definitions:
    - **`higher`:** The department's average monthly salary is strictly greater than the entire company's average monthly salary for that month.
    - **`lower`:** The department's average monthly salary is strictly less than the entire company's average monthly salary.
    - **`same`:** The department's average monthly salary equals the company's average monthly salary.
- **Dual Partitioning Window Formulation:**
  - Joining `Salary` and `Employee` provides `(amount, pay_date, department_id)` for every paycheck.
  - To compare a department against the entire company within the same month, we compute two concurrent window functions:
    1. **Company Monthly Average:**
       $$
       \mu_{company} = \text{AVG}(amount) \text{ OVER (PARTITION BY } pay\_date)
       $$
    2. **Department Monthly Average:**
       $$
       \mu_{dept} = \text{AVG}(amount) \text{ OVER (PARTITION BY } pay\_date, department\_id)
       $$
  - Then, `CASE` compares $\mu_{dept}$ against $\mu_{company}$.
- **Step-by-Step Worked Execution Trace:**
  - **Month 1: `2017-03` (`pay_date = '2017-03-31'`):**
    - Paychecks recorded:
      - Emp 1 (Dept 1): $\$9000$
      - Emp 2 (Dept 2): $\$6000$
      - Emp 3 (Dept 2): $\$10000$
    - **Company Average:**
      $$
      \mu_{company} = \frac{9000 + 6000 + 10000}{3} = \frac{25000}{3} \approx 8333.33
      $$
    - **Department 1 Average:**
      - Only Emp 1:
        $$
        \mu_{dept1} = \frac{9000}{1} = 9000.00
        $$
      - Compare: $9000.00 > 8333.33 \implies \mathbf{\text{"higher"}}$
    - **Department 2 Average:**
      - Emp 2 and Emp 3:
        $$
        \mu_{dept2} = \frac{6000 + 10000}{2} = \frac{16000}{2} = 8000.00
        $$
      - Compare: $8000.00 < 8333.33 \implies \mathbf{\text{"lower"}}$
  - **Month 2: `2017-02` (`pay_date = '2017-02-28'`):**
    - Paychecks recorded:
      - Emp 1 (Dept 1): $\$7000$
      - Emp 2 (Dept 2): $\$6000$
    - **Company Average:**
      $$
      \mu_{company} = \frac{7000 + 6000}{2} = \frac{13000}{2} = 6500.00
      $$
    - **Department 1 Average:**
      - Emp 1:
        $$
        \mu_{dept1} = 7000.00
        $$
      - Compare: $7000.00 > 6500.00 \implies \mathbf{\text{"higher"}}$
    - **Department 2 Average:**
      - Emp 2:
        $$
        \mu_{dept2} = 6000.00
        $$
      - Compare: $6000.00 < 6500.00 \implies \mathbf{\text{"lower"}}$
  - **Step 3: Deduplicate with `SELECT DISTINCT`:**
    - Since window functions produce a value per row, multiple employees in the same department share identical $(\mu_{dept}, \mu_{company})$ values.
    - Applying `SELECT DISTINCT pay_month, department_id, comparison` produces exactly one row per `(month, department)` pair.
- **Equal Benchmark Instance (`same`):**
  - If a company has only one department, or if all departments have identical averages, $\mu_{dept} = \mu_{company} \implies \mathbf{\text{"same"}}$.
- **Multiple Employees with Identical Salaries:**
  - Means remain exact and are handled with standard floating/decimal comparison.

This instance demonstrates multi-level hierarchical aggregation using partitioned SQL window functions, mathematically proves why dual-granularity partitions evaluate departmental benchmarks against global baselines in a single pass, and derives $O(N \log N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given `Salary` and `Employee` tables:
For every month and every department, compare the **department's average salary** against the **company's average salary**:
- Output `'higher'` if dept avg > company avg.
- Output `'lower'` if dept avg < company avg.
- Output `'same'` if dept avg = company avg.

```text
March 2017:
  Company Avg = (9000 + 6000 + 10000) / 3 = 8333.33
  Dept 1 Avg  = 9000 (Higher than company)
  Dept 2 Avg  = (6000 + 10000) / 2 = 8000 (Lower than company)

February 2017:
  Company Avg = (7000 + 6000) / 2 = 6500
  Dept 1 Avg  = 7000 (Higher than company)
  Dept 2 Avg  = 6000 (Lower than company)
```

### The Invariant of Dual-Grain Windowing
- Instead of grouping by month in a subquery, grouping by `(month, department)` in another subquery, and joining them:
- SQL window functions allow computing both averages **simultaneously in one single scan**:
  - `AVG(amount) OVER (PARTITION BY pay_date)` (company level).
  - `AVG(amount) OVER (PARTITION BY pay_date, department_id)` (department level).

---

## 2. Conceptual Foundation & Invariants

### 1. The Window Query:
```sql
WITH t AS (
    SELECT
        TO_CHAR(pay_date, 'YYYY-MM') AS pay_month,
        department_id,
        AVG(amount) OVER (PARTITION BY pay_date) AS company_avg,
        AVG(amount) OVER (PARTITION BY pay_date, department_id) AS dept_avg
    FROM Salary AS s
    JOIN Employee AS e ON s.employee_id = e.employee_id
)
SELECT DISTINCT
    pay_month,
    department_id,
    CASE
        WHEN dept_avg > company_avg THEN 'higher'
        WHEN dept_avg < company_avg THEN 'lower'
        ELSE 'same'
    END AS comparison
FROM t;
```

### 2. Output Deduplication:
- Because the CTE contains one row per salary payment, a department with 10 employees will produce 10 identical comparison rows.
- `SELECT DISTINCT` flattens these into a single tuple per `(pay_month, department_id)`.

> **Convex Combination Invariant.** The global company average is a convex combination of departmental averages weighted by department headcount $\mu_{comp} = \sum \frac{n_i}{N} \mu_i$; therefore, at least one department must be $\ge \mu_{comp}$ and at least one must be $\le \mu_{comp}$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Compute Window Means
- Row 1 (March, Dept 1, $9000$): $company\_avg = 8333.33, \; dept\_avg = 9000$.
- Row 2 (March, Dept 2, $6000$): $company\_avg = 8333.33, \; dept\_avg = 8000$.
- Row 3 (March, Dept 2, $10000$): $company\_avg = 8333.33, \; dept\_avg = 8000$.
- Row 4 (Feb, Dept 1, $7000$): $company\_avg = 6500, \; dept\_avg = 7000$.
- Row 5 (Feb, Dept 2, $6000$): $company\_avg = 6500, \; dept\_avg = 6000$.

---

### Step 2: Evaluate `CASE` Comparison
- March, Dept 1: $9000 > 8333.33 \implies$ `'higher'`.
- March, Dept 2: $8000 < 8333.33 \implies$ `'lower'`.
- Feb, Dept 1: $7000 > 6500 \implies$ `'higher'`.
- Feb, Dept 2: $6000 < 6500 \implies$ `'lower'`.

---

### Step 3: Emit Distinct Records
Four unique tuples returned as requested.

---

## 4. Complete Execution Trace

| `pay_month` | `department_id` | Dept Avg $\mu_{dept}$ | Company Avg $\mu_{comp}$ | Relation | Output `comparison` |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `2017-03` | $1$ | $9000.00$ | $8333.33$ | $\mu_{dept} > \mu_{comp}$ | **`higher`** |
| `2017-03` | $2$ | $8000.00$ | $8333.33$ | $\mu_{dept} < \mu_{comp}$ | **`lower`** |
| `2017-02` | $1$ | $7000.00$ | $6500.00$ | $\mu_{dept} > \mu_{comp}$ | **`higher`** |
| `2017-02` | $2$ | $6000.00$ | $6500.00$ | $\mu_{dept} < \mu_{comp}$ | **`lower`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Department in Company:** Dept avg equals company avg $\implies$ `'same'`.
- **Month with Single Employee:** Dept avg equals company avg $\implies$ `'same'`.
- **Identical Averages Across All Departments:** Evaluates to `'same'`.
- **Date Formatting:** Truncated to `'YYYY-MM'` format (e.g. `'2017-03'`).

---

## 6. Traps & Common Anti-Patterns

- **Comparing `pay_date` Directly Instead of Month:** If payments occur on different days in the same month (e.g. 2017-03-15 and 2017-03-31), partitioning by `pay_date` fragments the month. Always partition by the truncated month (`YYYY-MM`).
- **Forgetting `DISTINCT`:** Without `DISTINCT`, departments with multiple employees output duplicate rows.
- **Subquery Sprawl:** Writing three separate `GROUP BY` subqueries and joining them is error-prone and slow; window functions accomplish this cleanly in one step.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Joining `Salary` and `Employee`: $\mathcal{O}(N)$ where $N$ is payment count.
  - Sorting and evaluating window partitions: $\mathcal{O}(N \log N)$.
  - Sifting distinct month-department pairs: $\mathcal{O}(N)$.
  - Total Time: $\mathcal{O}(N \log N)$. Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for window buffer frames.
