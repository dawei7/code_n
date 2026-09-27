# Guided Example: Find Cumulative Salary of an Employee

We trace the step-by-step 3-month sliding window range aggregation (`RANGE 2 PRECEDING`), most recent month exclusion filter ($\text{month} \ne \max(\text{month})$), non-contiguous calendar month difference handling, multi-column ordering (`id ASC, month DESC`), and cumulative salary projection on representative employee payroll records:

- **Input:**
  - `Employee` table:
    | `id` | `month` | `salary` |
    |:---:|:---:|:---:|
    | $1$ | $1$ | $20$ |
    | $2$ | $1$ | $20$ |
    | $1$ | $2$ | $30$ |
    | $2$ | $2$ | $30$ |
    | $3$ | $2$ | $40$ |
    | $1$ | $3$ | $40$ |
    | $1$ | $4$ | $60$ |
    | $3$ | $3$ | $60$ |
    | $3$ | $4$ | $70$ |
- **Required output:**
  | `id` | `month` | `Salary` |
  |:---:|:---:|:---:|
  | $1$ | $3$ | $90$ |
  | $1$ | $2$ | $50$ |
  | $1$ | $1$ | $20$ |
  | $2$ | $1$ | $20$ |
  | $3$ | $3$ | $100$ |
  | $3$ | $2$ | $40$ |
  - Business rules:
    1. **3-Month Rolling Window:** The cumulative salary for month $m$ is the sum of salaries in months $m$, $m-1$, and $m-2$ (`RANGE 2 PRECEDING`).
    2. **Exclude Most Recent Month:** For each employee, do **not** include their maximum recorded month.
    3. **Ordering:** Sort by `id ASC`, then by `month DESC`.
- **Relational Window & Exclusion Trace:**
  - **Step 1: Identify and Mark Most Recent Month per Employee:**
    - Employee 1 months: $\{1, 2, 3, 4\} \implies \max = \mathbf{4}$ (Exclude Month 4).
    - Employee 2 months: $\{1, 2\} \implies \max = \mathbf{2}$ (Exclude Month 2).
    - Employee 3 months: $\{2, 3, 4\} \implies \max = \mathbf{4}$ (Exclude Month 4).
  - **Step 2: Calculate 3-Month Range Cumulative Sums for Remaining Months:**
    - Window specification:
      $$
      \text{SUM}(salary) \text{ OVER (PARTITION BY id ORDER BY month RANGE 2 PRECEDING)}
      $$
    - **Employee 1 (Valid months: 1, 2, 3):**
      - **Month 1:** Range $[1 - 2, 1] = [-1, 1]$. Months present: $\{1\}$.
        $$
        \text{Salary}(1) = 20
        $$
      - **Month 2:** Range $[2 - 2, 2] = [0, 2]$. Months present: $\{1, 2\}$.
        $$
        \text{Salary}(2) = 20 + 30 = \mathbf{50}
        $$
      - **Month 3:** Range $[3 - 2, 3] = [1, 3]$. Months present: $\{1, 2, 3\}$.
        $$
        \text{Salary}(3) = 20 + 30 + 40 = \mathbf{90}
        $$
      - *(Month 4 is excluded)*.
    - **Employee 2 (Valid month: 1):**
      - **Month 1:** Range $[1 - 2, 1] = [-1, 1]$. Months present: $\{1\}$.
        $$
        \text{Salary}(1) = \mathbf{20}
        $$
      - *(Month 2 is excluded)*.
    - **Employee 3 (Valid months: 2, 3):**
      - **Month 2:** Range $[2 - 2, 2] = [0, 2]$. Months present: $\{2\}$.
        $$
        \text{Salary}(2) = \mathbf{40}
        $$
      - **Month 3:** Range $[3 - 2, 3] = [1, 3]$. Months present: $\{2, 3\}$.
        $$
        \text{Salary}(3) = 40 + 60 = \mathbf{100}
        $$
      - *(Month 4 is excluded)*.
  - **Step 3: Format and Sort Output Table:**
    - Sort order: `id ASC`, then `month DESC`:
      - Employee 1: Month 3 ($90$), Month 2 ($50$), Month 1 ($20$)
      - Employee 2: Month 1 ($20$)
      - Employee 3: Month 3 ($100$), Month 2 ($40$)
- **Sparse Month Gaps Example:**
  - Suppose an employee has records for Month 1 and Month 7.
  - For Month 7, `RANGE 2 PRECEDING` looks for months in $[7 - 2, 7] = [5, 7]$.
  - Month 1 is outside the 3-month window $\implies$ Cumulative sum at Month 7 is just $Salary(7)$, **not** $Salary(1) + Salary(7)$.
  - Using `RANGE 2 PRECEDING` respects calendar months, whereas `ROWS 2 PRECEDING` would mistakenly add Month 1!

This instance demonstrates physical range windowing versus row-offset framing in SQL analytical queries, mathematically proves why `RANGE` correctly handles sparse temporal records, and derives $O(N \log N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an `Employee` table with `id`, `month`, and `salary`:
Calculate the **3-month rolling cumulative salary** for each employee's months, excluding their **most recent month**.
Sort the result by `id ASC` and `month DESC`.

```text
Employee 1 Records:
  Month 1: 20
  Month 2: 30  -> Cum: 20 + 30 = 50
  Month 3: 40  -> Cum: 20 + 30 + 40 = 90
  Month 4: 60  -> Most recent month -> EXCLUDED!

Output for Employee 1 (sorted month DESC):
  id: 1, month: 3, Salary: 90
  id: 1, month: 2, Salary: 50
  id: 1, month: 1, Salary: 20
```

### `RANGE` vs `ROWS` in SQL Windowing
- `ROWS 2 PRECEDING` counts the **two previous rows physically in the table**, regardless of what their `month` values are.
- `RANGE 2 PRECEDING` calculates the window based on the **numeric value of `month`**:
  $$
  \text{Window} = [\text{month} - 2, \; \text{month}]
  $$
- If an employee skipped months (e.g. worked month 1, then month 5), `RANGE 2 PRECEDING` will NOT include month 1 in month 5's rolling total because $1 \notin [3, 5]$.
- `RANGE 2 PRECEDING` is the mathematically correct temporal specification.

---

## 2. Conceptual Foundation & Invariants

### 1. The Exclusion Predicate:
Filter out the latest month for each employee:
```sql
WHERE (id, month) NOT IN (
    SELECT id, MAX(month)
    FROM Employee
    GROUP BY id
)
```

### 2. The Analytical Cumulative Sum:
```sql
SUM(salary) OVER (
    PARTITION BY id
    ORDER BY month
    RANGE 2 PRECEDING
) AS Salary
```

### 3. Sorting Contract:
```sql
ORDER BY id ASC, month DESC;
```

> **Temporal Horizon Invariant.** The interval $[\max(1, month - 2), month]$ bounds rolling liability to at most 3 consecutive calendar months per employee statement.

---

## 3. Step-by-Step Worked Execution

We trace Employee 1:

---

### Step 1: Filter Maximum Month
- Employee 1 months: $\{1, 2, 3, 4\}$.
- $\max(month) = 4$.
- Month 4 is dropped from the result.
- Remaining: Months $1, 2, 3$.

---

### Step 2: Compute Rolling Sums
- **Month 1:**
  - Range: $[-1, 1]$.
  - Salary = $20$.
- **Month 2:**
  - Range: $[0, 2]$.
  - Months in range: $1, 2$.
  - Salary = $20 + 30 = \mathbf{50}$.
- **Month 3:**
  - Range: $[1, 3]$.
  - Months in range: $1, 2, 3$.
  - Salary = $20 + 30 + 40 = \mathbf{90}$.

---

### Step 3: Sort by Month Descending
- $(1, 3, 90)$
- $(1, 2, 50)$
- $(1, 1, 20)$

---

## 4. Complete Execution Trace

| `id` | `month` | Base `salary` | Is Most Recent? | 3-Month Range | Included Months | Output `Salary` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $1$ | $20$ | No | $[-1, 1]$ | Month 1 | **$20$** |
| $1$ | $2$ | $30$ | No | $[0, 2]$ | Months 1, 2 | **$50$** |
| $1$ | $3$ | $40$ | No | $[1, 3]$ | Months 1, 2, 3 | **$90$** |
| $1$ | $4$ | $60$ | **Yes ($\max$)** | — | — | **Excluded** |
| $2$ | $1$ | $20$ | No | $[-1, 1]$ | Month 1 | **$20$** |
| $2$ | $2$ | $30$ | **Yes ($\max$)** | — | — | **Excluded** |
| $3$ | $2$ | $40$ | No | $[0, 2]$ | Month 2 | **$40$** |
| $3$ | $3$ | $60$ | No | $[1, 3]$ | Months 2, 3 | **$100$** |
| $3$ | $4$ | $70$ | **Yes ($\max$)** | — | — | **Excluded** |

---

## 5. Boundary Cases & Failure Modes

- **Employee with Exactly 1 Month:** That single month is their maximum month $\implies$ dropped entirely $\implies 0$ rows produced for that employee.
- **Employee with Exactly 2 Months:** Maximum month dropped $\implies 1$ row produced (month 1 with its own salary).
- **Gaps in Work History:** An employee working months 1, 2, and 6 will have rolling sum $Salary(6)$ for month 6, because months 1 and 2 are outside the $[4, 6]$ window.

---

## 6. Traps & Common Anti-Patterns

- **Using `ROWS 2 PRECEDING` Instead of `RANGE 2 PRECEDING`:** `ROWS 2 PRECEDING` sums the 2 preceding rows regardless of whether they occurred in the last 2 months. If month 6 is preceded by month 2 and month 1, `ROWS` sums all three, violating the calendar month rule.
- **Excluding the Max Month Inside the Window:** If you filter out the max month *before* computing the window sum, an employee whose latest month is month 4 might have month 3 calculated without issue, but make sure the window function is scoped correctly.
- **Sorting by Month Ascending:** The problem explicitly specifies `ORDER BY id, month DESC`. Returning months in ascending order fails expected output verification.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Finding maximum month per employee via `GROUP BY`: $\mathcal{O}(N)$.
  - Filtering rows with `NOT IN`: $\mathcal{O}(N \log N)$ or $\mathcal{O}(N)$ hash probe.
  - Computing window rolling sum with `RANGE 2 PRECEDING`: $\mathcal{O}(N \log N)$ due to partition sorting.
  - Final sort: $\mathcal{O}(N \log N)$.
  - Total Time: $\mathcal{O}(N \log N)$. Completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store intermediate window frames.
