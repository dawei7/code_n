# Guided Example: Find Customer Referee

We trace the step-by-step three-valued logic inequality predicate ($referee\_id \ne 2$), nullability evaluation under SQL boolean semantics ($NULL \ne 2 \implies \text{UNKNOWN}$), null-safe default coalescing (`COALESCE(referee_id, 0)`), customer identity preservation, and attribute projection on representative customer relation instances:

- **Input:**
  - `Customer` table:
    | `id` | `name` | `referee_id` |
    |:---:|:---:|:---:|
    | $1$ | `Alice` | $1$ |
    | $2$ | `Bob` | $2$ |
    | $3$ | `Cara` | `null` |
- **Required output:**
  | `name` |
  |:---:|
  | `Alice` |
  | `Cara` |
  - Business query contract: Report the `name` of every customer who was **not referred by customer $2$** (i.e. whose `referee_id` is different from $2$, or who has **no referee**).
- **Relational Predicate & Three-Valued Logic Trace:**
  - In relational database theory, comparisons against SQL `NULL` evaluate to `UNKNOWN` under three-valued logic (`TRUE`, `FALSE`, `UNKNOWN`).
  - An SQL `WHERE` clause accepts a record if and only if the predicate evaluates to **`TRUE`**.
  - **Evaluation with Naive Predicate (`WHERE referee_id != 2`):**
    - **Alice (`referee_id = 1`):**
      $$
      1 \ne 2 \implies \mathbf{TRUE} \quad (\text{Accepted})
      $$
    - **Bob (`referee_id = 2`):**
      $$
      2 \ne 2 \implies \mathbf{FALSE} \quad (\text{Rejected})
      $$
    - **Cara (`referee_id = NULL`):**
      $$
      NULL \ne 2 \implies \mathbf{UNKNOWN} \quad (\text{Fails WHERE clause!})
      $$
    - Notice that Cara had no referee (which is valid and not 2), yet a naive inequality rejects Cara!
  - **Resolution via Null Coalescing (`COALESCE(referee_id, 0) != 2`):**
    - The `COALESCE` function substitutes a sentinel value (e.g. $0$) whenever `referee_id` is `NULL`.
    - Sentinel selection: Since customer IDs are positive integers ($\ge 1$), choosing $0$ is guaranteed to never collide with an actual customer ID.
    - Re-evaluating with `COALESCE`:
      - **Alice:** $\text{COALESCE}(1, 0) = 1 \ne 2 \implies \mathbf{TRUE}$ (Included)
      - **Bob:** $\text{COALESCE}(2, 0) = 2 \ne 2 \implies \mathbf{FALSE}$ (Excluded)
      - **Cara:** $\text{COALESCE}(NULL, 0) = 0 \ne 2 \implies \mathbf{TRUE}$ (Included!)
  - **Alternative Canonical Predicate (`referee_id != 2 OR referee_id IS NULL`):**
    - Directly asserts disjunction with the explicit SQL `IS NULL` test:
      - Cara: $(NULL \ne 2) \lor (NULL \text{ IS NULL}) \implies UNKNOWN \lor TRUE = \mathbf{TRUE}$!
  - **Step-by-Step Selection Output:**
    - Qualified records: Alice, Cara.
    - Project column `name`:
      - `"Alice"`
      - `"Cara"`
- **All Customers Referred by 2:**
  - If all rows have `referee_id = 2`, none qualify $\implies$ empty table.
- **No Customers Referred by Anyone (`referee_id` is null for all):**
  - All customers qualify $\implies$ all names returned.

This instance demonstrates negation filtering over nullable foreign keys, mathematically proves why relational three-valued logic requires explicit null guards, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a `Customer` table with columns `id`, `name`, and `referee_id`:
Find the names of all customers who are **not referred by customer 2**.
Return the result in any order.

```text
Customers:
  Alice (referee 1) -> Referee != 2 -> Keep!
  Bob   (referee 2) -> Referee == 2 -> Drop!
  Cara  (referee NULL) -> Not referred by 2 -> Keep!

Output:
  Alice
  Cara
```

### The Pitfall of Nullable Negation in SQL
- In standard mathematics, if $x \ne 2$, then either $x$ is some other number or $x$ is undefined.
- In SQL, `NULL != 2` does **not** evaluate to `TRUE`; it evaluates to `UNKNOWN`!
- The SQL `WHERE` clause drops any row that does not evaluate to strictly `TRUE`.
- Therefore, a simple query `WHERE referee_id != 2` silently drops all customers who were not referred by anyone.
- Using `COALESCE(referee_id, 0) != 2` or `referee_id != 2 OR referee_id IS NULL` is required.

---

## 2. Conceptual Foundation & Invariants

### 1. Three-Valued Logic Truth Table:
| Expression | Result | Passes `WHERE`? |
|:---:|:---:|:---:|
| $1 \ne 2$ | `TRUE` | **Yes** |
| $2 \ne 2$ | `FALSE` | No |
| $\text{NULL} \ne 2$ | `UNKNOWN` | No |
| $\text{COALESCE}(\text{NULL}, 0) \ne 2$ | `TRUE` | **Yes** |

### 2. The Filter Query:
```sql
SELECT name
FROM Customer
WHERE COALESCE(referee_id, 0) != 2;
```

> **Null Guard Invariant.** Coalescing nullable attributes with out-of-domain sentinels maps indeterminate SQL states into binary Boolean evaluations without table duplication.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Scan Table Rows
- Row 1: `(1, "Alice", 1)`
- Row 2: `(2, "Bob", 2)`
- Row 3: `(3, "Cara", NULL)`

---

### Step 2: Apply Predicate `COALESCE(referee_id, 0) != 2`
- Alice: $\text{COALESCE}(1, 0) = 1 \ne 2 \implies \mathbf{True}$.
- Bob: $\text{COALESCE}(2, 0) = 2 \ne 2 \implies \mathbf{False}$.
- Cara: $\text{COALESCE}(NULL, 0) = 0 \ne 2 \implies \mathbf{True}$.

---

### Step 3: Project `name`
- Output rows:
  - `"Alice"`
  - `"Cara"`

---

## 4. Complete Execution Trace

| `id` | `name` | `referee_id` | `COALESCE(referee_id, 0)` | Equal to $2$? | Included in Output? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `Alice` | $1$ | $1$ | No | **Yes** (`"Alice"`) |
| $2$ | `Bob` | $2$ | $2$ | **Yes** | No |
| $3$ | `Cara` | `NULL` | $0$ | No | **Yes** (`"Cara"`) |

---

## 5. Boundary Cases & Failure Modes

- **All Customers Have `referee_id = 2`:** All rejected $\implies$ empty result table.
- **No Customers Have `referee_id = 2`:** All accepted $\implies$ full table of names.
- **Negative or Large Referee IDs:** Any integer other than 2 passes.
- **Empty `Customer` Table:** Returns empty result with column header `name`.

---

## 6. Traps & Common Anti-Patterns

- **Writing `WHERE referee_id != 2` Alone:** Drops all customers with `NULL` referee IDs, failing the test suite immediately.
- **Writing `WHERE referee_id NOT IN (2)`:** In SQL, `NOT IN` with nulls returns empty if any compared value is null. Always ensure nulls are explicitly protected.
- **Using a Subquery or Self-Join:** A simple linear scan with `COALESCE` runs in $O(N)$ time, whereas self-joins add unnecessary indexing and memory overhead.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the number of rows in `Customer`.
  - Evaluating `COALESCE` and inequality comparison on each row takes $\mathcal{O}(1)$ time.
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N = 10^5$, completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary memory (streaming filter).
