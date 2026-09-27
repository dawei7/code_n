# Guided Example: Managers with at Least 5 Direct Reports

We trace the step-by-step relational foreign-key grouping (`GROUP BY managerId`), group cardinality threshold filtering (`HAVING COUNT(1) >= 5`), self-referencing entity-manager joining (`Employee JOIN ... USING(id)`), nullability manager handling, and manager name projection on representative organizational tables:

- **Input:**
  - `Employee` table:
    | `id` | `name` | `department` | `managerId` |
    |:---:|:---:|:---:|:---:|
    | $101$ | `John` | `A` | `null` |
    | $102$ | `Dan` | `A` | $101$ |
    | $103$ | `James` | `A` | $101$ |
    | $104$ | `Amy` | `A` | $101$ |
    | $105$ | `Anne` | `A` | $101$ |
    | $106$ | `Ron` | `B` | $101$ |
- **Required output:**
  | `name` |
  |:---:|
  | `John` |
  - Business requirement: Identify all managers who have **at least five** ($5$) employees directly reporting to them.
- **Relational Aggregation & Joining Trace:**
  - **Step 1: Group Employees by `managerId` and Count Reports:**
    - Scan all employee records and aggregate their supervising manager:
      - `managerId = null`: John has no manager (top-level executive) $\implies$ Ignored in `managerId` grouping.
      - `managerId = 101`:
        - Employee $102$ (Dan) reports to $101$
        - Employee $103$ (James) reports to $101$
        - Employee $104$ (Amy) reports to $101$
        - Employee $105$ (Anne) reports to $101$
        - Employee $106$ (Ron) reports to $101$
      - Total direct reports for `managerId = 101`:
        $$
        cnt = 1 + 1 + 1 + 1 + 1 = \mathbf{5}
        $$
  - **Step 2: Filter Aggregated Groups (`HAVING cnt >= 5`):**
    - Condition: $cnt \ge 5$.
    - For `managerId = 101`:
      $$
      5 \ge 5 \implies \mathbf{True} \quad (\text{Qualified!})
      $$
    - Intermediate derived relation $t$:
      | `id` | `cnt` |
      |:---:|:---:|
      | $101$ | $5$ |
  - **Step 3: Join Back with `Employee` to Extract Manager Names:**
    - Perform an inner join between $t$ and `Employee` on `Employee.id = t.id`:
      - Match `t.id = 101` with `Employee.id = 101`.
      - Look up employee with `id = 101`:
        - `name = "John"`
    - Project the manager's `name`:
      $$
      \mathbf{\text{"John"}}
      $$
- **Manager with Exactly 4 Reports (Disqualified):**
  - If a manager has 4 direct reports, $cnt = 4 \ngtr 5 \implies$ filtered out by `HAVING` $\implies$ empty table.
- **Multiple Qualifying Managers:**
  - If Manager $101$ has 5 reports and Manager $201$ has 7 reports, both manager IDs survive the `HAVING` clause, projecting both names.
- **Employees Reporting to Non-Existent Managers:**
  - Standard foreign key relationships; joining on `Employee.id` automatically eliminates ghost manager IDs.

This instance demonstrates self-referencing hierarchical grouping in relational schemas, mathematically proves why `HAVING` filters group cardinalities before projection, and derives $O(N \log N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an `Employee` table with columns `id`, `name`, `department`, and `managerId`:
Find the names of all managers who have **at least 5 direct reports**.

```text
Reporting Relationships:
  Dan   (id 102) -> reports to John (101)
  James (id 103) -> reports to John (101)
  Amy   (id 104) -> reports to John (101)
  Anne  (id 105) -> reports to John (101)
  Ron   (id 106) -> reports to John (101)

John has 5 direct reports -> John qualifies!
```

### Self-Referencing Foreign Key Hierarchy
- In a company schema, both managers and employees are stored in the **same table**.
- An employee's supervisor is represented by `managerId`, which references another employee's `id`.
- To find managers with $\ge 5$ reports:
  1. Group by `managerId` to count how many employees report to each manager.
  2. Filter for groups where count $\ge 5$.
  3. Join the resulting manager IDs back to `Employee.id` to retrieve their human-readable `name`.

---

## 2. Conceptual Foundation & Invariants

### 1. Group Aggregation Subquery:
```sql
SELECT managerId AS id, COUNT(1) AS cnt
FROM Employee
GROUP BY managerId
HAVING COUNT(1) >= 5
```
- Groups rows having the same `managerId`.
- Computes group size `COUNT(1)`.
- `HAVING COUNT(1) >= 5` prunes any manager with fewer than 5 direct reports.

### 2. Primary Key Join:
Join subquery $t$ with `Employee` on `Employee.id = t.id`:
$$
\pi_{name} (\text{Employee} \bowtie_{Employee.id = t.id} t)
$$

> **Hierarchical Role Invariant.** Every row in `Employee` represents an employee when queried by `id`, and represents a supervisor role when queried by `managerId`.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Scan and Group by `managerId`
- Records with `managerId = 101`:
  - Dan (102)
  - James (103)
  - Amy (104)
  - Anne (105)
  - Ron (106)
- Total count for $101$: $5$.

---

### Step 2: Apply `HAVING` Filter
- Condition: $count \ge 5$.
- $5 \ge 5 \implies$ Qualified.
- Result of subquery $t$:
  $$
  t = [(\text{id}: 101, \text{cnt}: 5)]
  $$

---

### Step 3: Join on `Employee.id = 101`
- Look up `id = 101` in `Employee`:
  - `id`: $101$
  - `name`: `"John"`
- Project `name`:
  $$
  \mathbf{\text{"John"}}
  $$

---

## 4. Complete Execution Trace

| `managerId` Group | Reporting Employee IDs | Subquery Count `COUNT(1)` | Passes `HAVING >= 5`? | Manager Name (from `id`) |
|:---:|:---:|:---:|:---:|:---:|
| `null` | None (executive) | $0$ | No | — |
| **$101$** | $102, 103, 104, 105, 106$ | **$5$** | **Yes** | **`"John"`** |
| **Final Output** | — | — | — | **`"John"`** |

---

## 5. Boundary Cases & Failure Modes

- **No Managers with $\ge 5$ Reports:** Filter produces empty result $\implies$ returns empty table with column header `name`.
- **Managers with $> 5$ Reports (e.g. 10 reports):** $10 \ge 5 \implies$ qualifies normally.
- **Top-Level CEO (`managerId` is null):** Grouping ignores or isolates `null` manager IDs; joining on `id = null` produces no match.
- **Multiple Qualifying Managers:** All qualifying manager IDs are joined and projected.

---

## 6. Traps & Common Anti-Patterns

- **Using `WHERE` Instead of `HAVING`:** Aggregate functions like `COUNT(1)` cannot appear in a `WHERE` clause. Aggregate thresholds must be specified in the `HAVING` clause after `GROUP BY`.
- **Correlated Subqueries in `WHERE` ($O(N^2)$):** Writing `WHERE id IN (SELECT managerId FROM Employee WHERE ...)` can trigger quadratic row-by-row re-evaluation in unoptimized query planners. Grouping with an explicit `JOIN` is linear-logarithmic and index-friendly.
- **Selecting `managerId` Instead of `name`:** The problem requires returning the manager's **name**, not their numeric ID. The join back to `Employee.id` is mandatory.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Grouping and aggregating by `managerId`: $\mathcal{O}(N)$ (with hash grouping) or $\mathcal{O}(N \log N)$ (with sort grouping).
  - Joining qualified managers on indexed primary key `id`: $\mathcal{O}(K \log N)$ where $K$ is the number of qualifying managers ($K \le N$).
  - Total Time: $\mathcal{O}(N \log N)$. Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K)$ intermediate memory to hold the grouped supervisor IDs.
