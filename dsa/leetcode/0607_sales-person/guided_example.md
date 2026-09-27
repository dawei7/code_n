# Guided Example: Sales Person

We trace the step-by-step target entity identification (company `"RED"`), order-to-company relational joining (`Orders JOIN Company`), forbidden seller identifier set construction (`sales_id IN (RED orders)`), complementary salesperson universe filtering (`NOT IN`), zero-order seller retention, and name projection on representative sales databases:

- **Input:**
  - `SalesPerson` table:
    | `sales_id` | `name` | `salary` | `commission_rate` | `hire_date` |
    |:---:|:---:|:---:|:---:|:---:|
    | $1$ | `Alice` | $50000$ | $10$ | `2020-01-01` |
    | $2$ | `Bob` | $50000$ | $10$ | `2020-01-01` |
    | $3$ | `Charlie` | $50000$ | $10$ | `2020-01-01` |
  - `Company` table:
    | `com_id` | `name` | `city` |
    |:---:|:---:|:---:|
    | $1$ | `RED` | `A` |
    | $2$ | `BLUE` | `B` |
  - `Orders` table:
    | `order_id` | `order_date` | `com_id` | `sales_id` | `amount` |
    |:---:|:---:|:---:|:---:|:---:|
    | $1$ | `2020-01-01` | $1$ | $1$ | $10000$ |
    | $2$ | `2020-01-02` | $2$ | $2$ | $10000$ |
- **Required output:**
  | `name` |
  |:---:|
  | `Bob` |
  | `Charlie` |
  - Business query objective: Report the `name` of all salespersons who did **not have any orders related to the company named "RED"**.
  - Key business requirement: Salespeople who have **no orders at all** (e.g. Charlie) have no orders with RED and **must be included**!
- **Relational Anti-Join & Subquery Exclusion Trace:**
  - **Step 1: Identify Forbidden Salesperson IDs (Tainted by "RED"):**
    - Join `Orders` with `Company` on `com_id` where `Company.name = 'RED'`:
      - Order $1$: `com_id = 1` (Company name: `"RED"`, `sales_id = 1`).
      - Order $2$: `com_id = 2` (Company name: `"BLUE"`).
    - Forbidden ID set $S_{RED}$:
      $$
      S_{RED} = \{1\} \quad (\text{Alice})
      $$
  - **Step 2: Filter the Complete `SalesPerson` Universe:**
    - Scan every salesperson $s \in \text{SalesPerson}$:
      - **Alice (`sales_id = 1`):**
        - $1 \in S_{RED} \implies \mathbf{Forbidden!}$ (Associated with RED order). Excluded.
      - **Bob (`sales_id = 2`):**
        - $2 \notin S_{RED} \implies \mathbf{Clean!}$ (Associated only with BLUE order).
        - Qualifies!
      - **Charlie (`sales_id = 3`):**
        - Has no records in `Orders`.
        - $3 \notin S_{RED} \implies \mathbf{Clean!}$ (Has zero RED orders).
        - Qualifies!
  - **Step 3: Project Resulting Names:**
    - Output list:
      - `"Bob"`
      - `"Charlie"`
- **Salesperson with Both RED and Other Orders:**
  - If a salesperson has 10 orders with BLUE and 1 order with RED, they are still present in $S_{RED}$ and therefore **excluded**.
- **No Company Named RED in Database:**
  - $S_{RED} = \emptyset \implies$ All salespersons qualify $\implies$ full roster returned.
- **Every Salesperson Has an Order with RED:**
  - $S_{RED} = \{1, 2, 3\} \implies$ All excluded $\implies$ empty table.

This instance demonstrates relational set difference and anti-join pattern matching, mathematically proves why subquery complementation correctly preserves zero-transaction entities, and derives $O(O + C + S)$ execution time and $O(S)$ space bounds.

---

## 1. Instance & Teaching Goal

Given tables `SalesPerson`, `Company`, and `Orders`:
Find the names of all salespersons who **never had an order associated with the company "RED"**.

```text
Relationships:
  Alice   (id 1) -> Order with RED   -> Disqualified!
  Bob     (id 2) -> Order with BLUE  -> Qualified!
  Charlie (id 3) -> No orders at all -> Qualified!

Output:
  Bob
  Charlie
```

### The Power of Anti-Join over Aggregation
- A common mistake is an inner join that matches only salespeople who made orders. That silently drops people like Charlie who made zero orders.
- The mathematically clean approach is **Set Subtraction**:
  $$
  \text{Eligible} = \text{All Salespeople} \setminus \text{Salespeople with RED Orders}
  $$
- An SQL `WHERE sales_id NOT IN (...)` subquery directly implements this set complement.

---

## 2. Conceptual Foundation & Invariants

### 1. The Subquery Formulation:
```sql
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders AS o
    JOIN Company AS c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);
```

### 2. Alternative Grouped Left-Join Formulation:
```sql
SELECT s.name
FROM SalesPerson AS s
LEFT JOIN Orders USING (sales_id)
LEFT JOIN Company AS c USING (com_id)
GROUP BY s.sales_id, s.name
HAVING COALESCE(SUM(CASE WHEN c.name = 'RED' THEN 1 ELSE 0 END), 0) = 0;
```

> **Universal Complement Invariant.** A person satisfies "never sold to $X$" if and only if their intersection with the set of transactions with $X$ is the empty set $\emptyset$.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Find RED Company ID
- `Company` row: `com_id = 1, name = 'RED'`.

---

### Step 2: Find Sales IDs with Orders for `com_id = 1`
- `Orders` table check:
  - Order 1: `com_id = 1, sales_id = 1`.
- Tainted set:
  $$
  S_{RED} = \{1\}
  $$

---

### Step 3: Filter `SalesPerson` Table
- Alice (id 1): $1 \in \{1\} \implies$ Disqualified.
- Bob (id 2): $2 \notin \{1\} \implies \mathbf{Kept}$.
- Charlie (id 3): $3 \notin \{1\} \implies \mathbf{Kept}$.

---

### Step 4: Emit Names
- Bob
- Charlie

---

## 4. Complete Execution Trace

| `sales_id` | `name` | Order History | Involves "RED"? | Passes `NOT IN` Filter? |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | `Alice` | Order 1 (`com_id = 1`) | **Yes** | No |
| **$2$** | **`Bob`** | Order 2 (`com_id = 2`) | No | **Yes (`Bob`)** |
| **$3$** | **`Charlie`** | None | No | **Yes (`Charlie`)** |

---

## 5. Boundary Cases & Failure Modes

- **Salesperson with Zero Orders:** Retained because `sales_id` never appears in `Orders`.
- **Multiple RED Orders by Same Person:** Deduplicated in subquery hash set; person correctly excluded once.
- **Empty `Orders` Table:** Subquery is empty $\implies$ all salespeople pass.
- **No Company Named "RED":** Subquery is empty $\implies$ all salespeople pass.

---

## 6. Traps & Common Anti-Patterns

- **Using Inner Join and Filtering `c.name != 'RED'`:** An inner join drops salespeople with zero orders. Furthermore, if Bob sells to RED *and* BLUE, `c.name != 'RED'` would match his BLUE order and erroneously include Bob!
- **Null Safety in `NOT IN`:** If the subquery could return `NULL`, `NOT IN (NULL)` evaluates to `UNKNOWN` and rejects all rows. In this schema, `o.sales_id` is an integer foreign key, but using `JOIN` prevents null IDs.
- **Case Sensitivity:** Ensure `'RED'` matches exact case string literal.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Subquery: join `Orders` and `Company` on indexed `com_id` takes $\mathcal{O}(O + C)$ time.
  - Filtering `SalesPerson` via hash set lookup: $\mathcal{O}(S)$ time where $S$ is salesperson count.
  - Total Time: strictly linear $\mathcal{O}(S + O + C)$. Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K)$ space to store the set of tainted `sales_id`s in memory ($K \le S$).
