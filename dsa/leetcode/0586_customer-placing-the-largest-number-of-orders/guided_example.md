# Guided Example: Customer Placing the Largest Number of Orders

We trace the step-by-step order grouping by customer ID (`GROUP BY customer_number`), order cardinality counting (`COUNT(1)`), descending frequency ranking (`ORDER BY COUNT(1) DESC`), top-1 singular winner slicing (`LIMIT 1`), and customer number projection on representative transaction tables:

- **Input:**
  - `orders` table:
    | `order_number` | `customer_number` |
    |:---:|:---:|
    | $1$ | $1$ |
    | $2$ | $2$ |
    | $3$ | $2$ |
    | $4$ | $1$ |
    | $5$ | $2$ |
- **Required output:**
  | `customer_number` |
  |:---:|
  | $2$ |
  - Business query contract: Identify the `customer_number` of the customer who has placed the **largest total number of orders**.
  - Problem guarantee: Exactly one customer has strictly more orders than all other customers in all test cases.
- **Relational Aggregation & Top-1 Ranking Trace:**
  - **Step 1: Group Orders by `customer_number`:**
    - Scan the `orders` relation and partition rows into buckets:
      - **Bucket `customer_number = 1`:**
        - Contains order $1$ and order $4$.
        - Order count:
          $$
          \text{COUNT}(1) = 1 + 1 = \mathbf{2}
          $$
      - **Bucket `customer_number = 2`:**
        - Contains order $2$, order $3$, and order $5$.
        - Order count:
          $$
          \text{COUNT}(1) = 1 + 1 + 1 = \mathbf{3}
          $$
  - **Step 2: Order Aggregated Groups by Frequency (DESC):**
    - Sort group totals in descending order:
      1. `customer_number = 2`: $3$ orders (**Highest!**)
      2. `customer_number = 1`: $2$ orders
  - **Step 3: Extract Leading Customer with `LIMIT 1`:**
    - Taking the first row of the sorted stream yields:
      $$
      customer\_number = \mathbf{2}
      $$
- **High-Volume Customer Instance:**
  - If Customer 5 places 100 orders and Customer 1 places 1 order $\implies$ Customer 5 is extracted.
- **Single Order Table ($N = 1$):**
  - Group size is 1 $\implies$ that single customer is returned immediately.

This instance demonstrates hash-based categorical group aggregation and descending plurality extraction in relational databases, mathematically proves why top-1 truncation isolates the unique mode of a discrete distribution, and derives $O(N \log K)$ execution time and $O(K)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an `orders` table with `order_number` and `customer_number`:
Find the `customer_number` of the customer who placed the **most orders**.

```text
Orders Breakdown:
  Customer 1: Orders [1, 4]       -> Total = 2 orders
  Customer 2: Orders [2, 3, 5]    -> Total = 3 orders  <-- Most!

Winner: Customer 2
```

### The Group-Count-Limit Pattern
- The relational pipeline follows standard SQL group-by analytics:
  1. `GROUP BY customer_number` aggregates all transactions belonging to each customer.
  2. `COUNT(1)` tallies the number of rows in each group.
  3. `ORDER BY COUNT(1) DESC` ranks customers from highest order volume to lowest.
  4. `LIMIT 1` extracts the singular highest-volume customer.

---

## 2. Conceptual Foundation & Invariants

### 1. The Relational Query:
```sql
SELECT customer_number
FROM orders
GROUP BY customer_number
ORDER BY COUNT(1) DESC
LIMIT 1;
```

### 2. Guarantees:
- By problem contract, the maximum order count is strictly unique; no tie-breaking logic is necessary.

> **Mode Isolation Invariant.** Grouping by discrete entity identifiers and ordering by group size descending isolates the unique mathematical mode of the transaction stream.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Bucket Orders
- Customer 1: orders 1, 4 $\to$ count = 2.
- Customer 2: orders 2, 3, 5 $\to$ count = 3.

---

### Step 2: Sort by Count Descending
1. Customer 2 (count: 3)
2. Customer 1 (count: 2)

---

### Step 3: Apply `LIMIT 1`
- Customer 2 is selected.
- Project `customer_number`:
  $$
  \mathbf{2}
  $$

---

## 4. Complete Execution Trace

| `customer_number` | Order Numbers | Aggregated `COUNT(1)` | Sorted Rank | Selected by `LIMIT 1`? |
|:---:|:---:|:---:|:---:|:---:|
| **$2$** | $2, 3, 5$ | **$3$** | **$1$** | **Yes (`2`)** |
| $1$ | $1, 4$ | $2$ | $2$ | No |

---

## 5. Boundary Cases & Failure Modes

- **Single Order in Table:** Count is 1; customer is returned.
- **Many Customers with 1 Order Each Except One with 2:** The single customer with 2 orders is placed at rank 1 and returned.
- **Large Dataset ($10^5$ rows):** Hash-grouping aggregates all orders in a single linear pass over the table.

---

## 6. Traps & Common Anti-Patterns

- **Subquery with `MAX(COUNT(*))` ($O(N^2)$):** Writing nested subqueries to compute the maximum count before filtering requires multiple passes. Direct `ORDER BY COUNT(1) DESC LIMIT 1` is handled in a single pass using a size-1 heap.
- **Projecting `COUNT(1)` Instead of `customer_number`:** The query must return the customer's ID, not the number of orders they placed.
- **Sorting Ascending:** Forgetting `DESC` returns the customer with the *fewest* orders.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the number of rows in `orders` and $K$ be the number of distinct customers.
  - Grouping and counting: $\mathcal{O}(N)$ using hash aggregation.
  - Slicing top 1 with `ORDER BY ... DESC LIMIT 1`: $\mathcal{O}(K \log K)$ (or $\mathcal{O}(K)$ with top-1 min-heap).
  - Total Time: $\mathcal{O}(N + K \log K)$. For $N = 10^5, K = 1000$, completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(K)$ space to maintain the hash map of customer order counts.
