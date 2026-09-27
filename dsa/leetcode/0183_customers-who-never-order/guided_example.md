# Guided Example: Customers Who Never Order

We trace the step-by-step SQL anti-join evaluation and set difference mechanics on representative customer and transaction tables:

- **Input Tables:**
  - `Customers`: `[(1, "Joe"), (2, "Henry"), (3, "Sam"), (4, "Max")]`
  - `Orders`: `[(1, 1), (2, 3)]`
- **Required output:**
  - `{"columns": ["Customers"], "rows": [["Henry"], ["Max"]]}` (Customers 2 and 4 have no registered orders)
- **All Customers Ordered Instance:** `Orders = [(1, 1), (2, 2), (3, 3), (4, 4)] \implies \text{Empty Set}`
- **No Orders Placed Instance:** `Orders = [] \implies \text{All Customers}`

This instance demonstrates relational anti-joins, analyzes the three foundational SQL patterns (`LEFT JOIN ... WHERE IS NULL`, `NOT EXISTS`, and `NOT IN`), exposes the three-valued logic null poisoning hazard of `NOT IN`, and executes in $O(C + O)$ linear time.

---

## 1. Instance & Teaching Goal

Given two relational tables:
1. `Customers`:
   $$
   \begin{array}{|c|c|}
   \hline
   \textbf{id} & \textbf{name} \\
   \hline
   1 & \text{Joe} \\
   2 & \text{Henry} \\
   3 & \text{Sam} \\
   4 & \text{Max} \\
   \hline
   \end{array}
   $$
2. `Orders`:
   $$
   \begin{array}{|c|c|}
   \hline
   \textbf{id} & \textbf{customerId} \\
   \hline
   1 & 1 \\
   2 & 3 \\
   \hline
   \end{array}
   $$
Find all customers who have **never placed an order**.

Cross-referencing customer IDs against orders:
- Customer 1 (`"Joe"`): found in `Orders` (Order 1) $\implies$ Has ordered.
- Customer 2 (`"Henry"`): absent from `Orders` $\implies$ Never ordered.
- Customer 3 (`"Sam"`): found in `Orders` (Order 2) $\implies$ Has ordered.
- Customer 4 (`"Max"`): absent from `Orders` $\implies$ Never ordered.
The result must be a single-column table named `Customers` reporting `Henry` and `Max`.

---

## 2. Conceptual Foundation & Invariants

### The Relational Anti-Join ($\mathbin{\bar{\ltimes}}$)
In relational algebra, finding elements in relation $C$ with no match in relation $O$ is an **anti-join**:
$$
C \mathbin{\bar{\ltimes}} O = C \setminus \pi_{\text{attrs}(C)}(C \bowtie O)
$$

### Pattern 1: Left Anti-Join (Recommended)
```sql
SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o 
    ON c.id = o.customerId
WHERE o.id IS NULL;
```
- A `LEFT JOIN` preserves all rows of `Customers`.
- If customer $c$ has an order, $o.\text{id}$ is populated with the order ID.
- If customer $c$ has no order, $o.\text{id}$ is populated with `NULL`.
- Filtering for `WHERE o.id IS NULL` isolates customers who have never ordered.

### Pattern 2: Correlated `NOT EXISTS`
```sql
SELECT c.name AS Customers
FROM Customers c
WHERE NOT EXISTS (
    SELECT 1 
    FROM Orders o 
    WHERE o.customerId = c.id
);
```
Semi-join optimization stops scanning `Orders` as soon as the first matching order is found.

### Pattern 3: Set Difference `NOT IN`
```sql
SELECT c.name AS Customers
FROM Customers c
WHERE c.id NOT IN (
    SELECT customerId 
    FROM Orders
);
```

> **Invariant.** A customer row $c$ is emitted if and only if the set $\{ o \in \text{Orders} \mid o.\text{customerId} = c.\text{id} \}$ is strictly empty ($\emptyset$).

---

## 3. Step-by-Step Worked Execution

We trace the Left Anti-Join across all customer rows:

### Step 1: Perform `LEFT JOIN Orders ON c.id = o.customerId`
Join each customer with `Orders`:
- **Customer 1 (Joe):** Matches Order 1 ($o.\text{id} = 1$).
  Joined tuple: `(c.id: 1, c.name: "Joe", o.id: 1, o.customerId: 1)`.
- **Customer 2 (Henry):** No matching order. Padded with `NULL`.
  Joined tuple: `(c.id: 2, c.name: "Henry", o.id: NULL, o.customerId: NULL)`.
- **Customer 3 (Sam):** Matches Order 2 ($o.\text{id} = 2$).
  Joined tuple: `(c.id: 3, c.name: "Sam", o.id: 2, o.customerId: 3)`.
- **Customer 4 (Max):** No matching order. Padded with `NULL`.
  Joined tuple: `(c.id: 4, c.name: "Max", o.id: NULL, o.customerId: NULL)`.

---

### Step 2: Filter `WHERE o.id IS NULL`
Examine the right-side attribute `o.id`:
- Joe: $o.\text{id} = 1 \implies$ `1 IS NULL` is `False`. Discarded.
- Henry: $o.\text{id} = \text{NULL} \implies$ `NULL IS NULL` is `True`. **Retained!**
- Sam: $o.\text{id} = 2 \implies$ `2 IS NULL` is `False`. Discarded.
- Max: $o.\text{id} = \text{NULL} \implies$ `NULL IS NULL` is `True`. **Retained!**

---

### Step 3: Project `c.name AS Customers`
- Emitted rows: `[["Henry"], ["Max"]]`.

---

## 4. Complete Execution Trace

```text
Customers Table:            Orders Table:
1: Joe                      1: (custId: 1)
2: Henry                    2: (custId: 3)
3: Sam
4: Max

Left Outer Join:
  1: Joe   <-> Order 1      (o.id = 1)    -> Excluded
  2: Henry <-> [NO MATCH]   (o.id = NULL) -> INCLUDED (Henry)
  3: Sam   <-> Order 2      (o.id = 2)    -> Excluded
  4: Max   <-> [NO MATCH]   (o.id = NULL) -> INCLUDED (Max)

Output Table:
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
```

| Customer ID | Customer Name | Order ID Matched | Filter `o.id IS NULL` | Decision | Emitted Output |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | Joe | 1 | `False` | Has ordered | - |
| **2** | **Henry** | **`NULL`** | **`True`** | **Never ordered** | **`"Henry"`** |
| 3 | Sam | 2 | `False` | Has ordered | - |
| **4** | **Max** | **`NULL`** | **`True`** | **Never ordered** | **`"Max"`** |

---

## 5. Algorithmic Correctness

**Soundness.** In a relational left join, any row from the left table that finds no match in the right table has all right-table attributes set to SQL `NULL`. Because `Orders.id` is a primary key, it is guaranteed non-null in any genuine order record. Thus, $o.\text{id} \text{ IS NULL}$ is true if and only if no matching order exists for that customer.

**Completeness.** The left join retains every customer in `Customers`. All customers without orders are preserved and emitted.

---

## 6. Traps This Instance Exposes

- **The `NOT IN` NULL Poisoning Hazard:** In SQL three-valued logic, if the subquery returns even a single `NULL` value (e.g. `customerId = NULL` in `Orders`), the expression `id NOT IN (1, 3, NULL)` evaluates to `UNKNOWN` for all rows, returning an **empty result set**! Using `LEFT JOIN ... WHERE IS NULL` or `NOT EXISTS` avoids this trap entirely.
- **Wrong Column Name in Alias:** The source table column is `name`, but the output table schema requires header `Customers`. Forgetting `AS Customers` fails verification.
- **Multiple Orders Per Customer:** If customer 1 had placed 5 orders, an inner join would duplicate customer 1 five times. However, for customers who never ordered, exactly one row with `NULL` is generated, ensuring no spurious duplicate names for non-ordering customers.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C + O)$, where $C$ is the number of rows in `Customers` and $O$ is the number of rows in `Orders`. The query planner performs a hash anti-join or index look-up in $O(1)$ amortized time per customer.
- **Auxiliary Space Complexity:** $O(O)$ hash table memory to store active customer IDs from `Orders`.
