# Guided Example: Employee Bonus

We trace the step-by-step outer relational join preservation (`LEFT JOIN Bonus USING (empId)`), missing record nullability emergence, ternary boolean logic evaluation under three-valued SQL semantics ($bonus < 1000 \lor bonus \text{ IS NULL}$), null substitution coalescing (`COALESCE(bonus, 0)`), and qualified employee projection on representative payroll tables:

- **Input:**
  - `Employee` table:
    | `empId` | `name` | `supervisor` | `salary` |
    |:---:|:---:|:---:|:---:|
    | $1$ | `Ada` | `null` | $50000$ |
    | $2$ | `Grace` | $1$ | $50000$ |
    | $3$ | `Linus` | $1$ | $50000$ |
  - `Bonus` table:
    | `empId` | `bonus` |
    |:---:|:---:|
    | $1$ | $500$ |
    | $2$ | $1500$ |
- **Required output:**
  | `name` | `bonus` |
  |:---:|:---:|
  | `Ada` | $500$ |
  | `Linus` | `null` |
  - Business objective: Report the `name` and `bonus` of every employee whose bonus is **strictly less than 1000** ($< 1000$), including employees who received **no bonus record at all**.
- **Relational Outer Join & Three-Valued Logic Trace:**
  - **Step 1: Perform Left Outer Join on `empId`:**
    - An inner join would completely drop employees who have no entry in `Bonus`.
    - A `LEFT JOIN` preserves all employees from `Employee`, filling missing bonus fields with SQL `NULL`:
      - **Ada (`empId = 1`):** Matches `Bonus` record $\implies$ `bonus = 500`.
      - **Grace (`empId = 2`):** Matches `Bonus` record $\implies$ `bonus = 1500`.
      - **Linus (`empId = 3`):** No matching record in `Bonus` $\implies$ `bonus = NULL`.
    - Joined intermediate relation:
      | `empId` | `name` | `bonus` |
      |:---:|:---:|:---:|
      | $1$ | `Ada` | $500$ |
      | $2$ | `Grace` | $1500$ |
      | $3$ | `Linus` | `NULL` |
  - **Step 2: Filter by Threshold with Nullability Handling:**
    - In SQL three-valued logic (`TRUE`, `FALSE`, `UNKNOWN`):
      - Comparison with `NULL` produces `UNKNOWN` (treated as false by `WHERE`).
      - Specifically: `NULL < 1000` evaluates to `UNKNOWN`!
      - Therefore, a naive filter `WHERE bonus < 1000` would mistakenly **drop Linus**!
    - **Resolution Method (Null-Coalescing):**
      - Evaluate `COALESCE(bonus, 0) < 1000` (or `bonus < 1000 OR bonus IS NULL`):
        - **Ada:** $\text{COALESCE}(500, 0) = 500 < 1000 \implies \mathbf{True}$ (Include!)
        - **Grace:** $\text{COALESCE}(1500, 0) = 1500 < 1000 \implies \mathbf{False}$ (Exclude!)
        - **Linus:** $\text{COALESCE}(\text{NULL}, 0) = 0 < 1000 \implies \mathbf{True}$ (Include!)
  - **Step 3: Project Resulting Attributes:**
    - Select `name` and `bonus`:
      - Ada: `('Ada', 500)`
      - Linus: `('Linus', null)`
- **All Employees Exceed 1000:**
  - If all bonuses are $\ge 1000$ and all employees have bonus records, output is empty.
- **No Employees Receive Any Bonus:**
  - All bonuses evaluate to `NULL`; all qualify with `null` bonus projected.

This instance demonstrates outer join relational semantics and null-safe predicate filtering, mathematically proves why three-valued SQL logic requires explicit null coalescing, and derives $O(N \log N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given tables `Employee` and `Bonus`:
Find the name and bonus amount of each employee with a bonus **strictly less than 1000**, including those who received no bonus at all.

```text
Employees:
  Ada   (empId 1) -> Bonus: 500   (< 1000, Qualifies!)
  Grace (empId 2) -> Bonus: 1500  (>= 1000, Disqualified)
  Linus (empId 3) -> Bonus: NULL  (No bonus, Qualifies!)

Output:
  Ada   | 500
  Linus | null
```

### The Pitfall of SQL Three-Valued Logic
- In standard SQL, comparisons with `NULL` (such as `NULL < 1000` or `NULL = 1000`) evaluate to `UNKNOWN`, not `TRUE`.
- A `WHERE` clause keeps only rows where the predicate evaluates to `TRUE`.
- Therefore, simply writing `WHERE bonus < 1000` drops all employees with no bonus record!
- Using `COALESCE(bonus, 0) < 1000` or `WHERE bonus < 1000 OR bonus IS NULL` ensures that employees without bonus entries are correctly preserved.

---

## 2. Conceptual Foundation & Invariants

### 1. The Left Outer Join:
```sql
FROM Employee
LEFT JOIN Bonus USING (empId)
```
- Guarantees every row in `Employee` appears in the joined stream.
- Employees without bonuses receive a synthetic `NULL` in the `bonus` column.

### 2. Null-Safe Predicate:
$$
\text{WHERE COALESCE}(bonus, 0) < 1000
$$
- If `bonus` is numeric: returns `bonus` directly.
- If `bonus` is `NULL`: substitutes `0`, which satisfies $0 < 1000$.

> **Completeness Invariant.** A left join paired with null coalescing guarantees that employee records with absent bonus receipts are treated identically to zero-bonus recipients without dropping rows.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Left Join `Employee` with `Bonus`
- Ada (id 1): matched with bonus $500$.
- Grace (id 2): matched with bonus $1500$.
- Linus (id 3): no match $\implies bonus = \text{NULL}$.

---

### Step 2: Evaluate Filter Predicate
- Ada: $\text{COALESCE}(500, 0) = 500 < 1000 \implies \mathbf{True}$.
- Grace: $\text{COALESCE}(1500, 0) = 1500 < 1000 \implies \mathbf{False}$.
- Linus: $\text{COALESCE}(\text{NULL}, 0) = 0 < 1000 \implies \mathbf{True}$.

---

### Step 3: Project `name` and `bonus`
- Ada: `("Ada", 500)`
- Linus: `("Linus", null)`

---

## 4. Complete Execution Trace

| `name` | Joined `bonus` | `COALESCE(bonus, 0)` | $< 1000$? | Included in Result? | Output Row |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **Ada** | $500$ | $500$ | **Yes** | **Yes** | `Ada, 500` |
| Grace | $1500$ | $1500$ | No | No | — |
| **Linus** | `NULL` | $0$ | **Yes** | **Yes** | `Linus, null` |
| **Final** | — | — | — | — | **`[Ada, 500], [Linus, null]`** |

---

## 5. Boundary Cases & Failure Modes

- **Bonus Exactly 1000:** The condition is strictly $< 1000$, so an employee with bonus 1000 is excluded.
- **Empty `Bonus` Table:** All employees join with `NULL`, so all employees qualify and are returned with `null` bonus.
- **Multiple Employees with Same Name:** Joined by primary key `empId`, preserving distinct employee rows regardless of name collisions.

---

## 6. Traps & Common Anti-Patterns

- **Using `INNER JOIN`:** An inner join discards all employees who have no entry in `Bonus`, omitting users with null bonuses entirely.
- **Using `WHERE bonus < 1000` Without Null Check:** Fails to include employees with `bonus = NULL` due to SQL three-valued logic.
- **Filtering on Bonus in the `ON` Clause vs `WHERE` Clause:** Filtering `ON Employee.empId = Bonus.empId AND Bonus.bonus < 1000` in a `LEFT JOIN` causes employees with $\ge 1000$ to still appear in the output with a synthetic `NULL` bonus, erroneously including them. The threshold filter must be in the `WHERE` clause.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $E$ be the number of employees and $B$ be the number of bonus records.
  - Left outer hash join on `empId`: $\mathcal{O}(E + B)$.
  - Row-by-row predicate filter and projection: $\mathcal{O}(E)$.
  - Total Time: strictly linear $\mathcal{O}(E + B)$. Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(B)$ memory to build the hash table for the `Bonus` relation.
