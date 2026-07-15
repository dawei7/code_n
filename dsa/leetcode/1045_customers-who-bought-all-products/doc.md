# Customers Who Bought All Products

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1045 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/customers-who-bought-all-products/) |

## Problem Description

### Goal

The `Customer` table records purchases using `customer_id` and `product_key`. It may contain duplicate rows, `customer_id` is not null, and each `product_key` references the `Product` table. The `Product` table lists each catalog key exactly once because `product_key` is its primary key.

Report the identifiers of customers whose purchase records cover every product listed in `Product`. Repeated purchases of one product do not compensate for a missing different product. Return one `customer_id` column; the platform accepts the result rows in any order.

### Function Contract

**Inputs**

- `Customer(customer_id, product_key)`: $R$ purchase rows, possibly including duplicate customer-product pairs.
- `Product(product_key)`: $Q$ distinct product rows defining the complete catalog.

**Return value**

- One row containing `customer_id` for each customer who has bought all $Q$ distinct products.
- Result order is unrestricted by the problem; the local reference orders identifiers ascending for deterministic validation.

### Examples

**Example 1**

`Customer`

| customer_id | product_key |
|---:|---:|
| 1 | 5 |
| 2 | 6 |
| 3 | 5 |
| 3 | 6 |
| 1 | 6 |

`Product`

| product_key |
|---:|
| 5 |
| 6 |

Output:

| customer_id |
|---:|
| 1 |
| 3 |

Customers `1` and `3` each bought products `5` and `6`; customer `2` did not buy product `5`.

### Required Complexity

- **Time:** $O(R log R + Q)$
- **Space:** $O(R+Q)$

<details>
<summary>Approach</summary>

#### General

**Group purchases by customer:** Use `GROUP BY customer_id` so each output candidate is evaluated from all of that customer's purchase rows.

**Count covered products distinctly:** Compute `COUNT(DISTINCT product_key)` within each group. Distinct counting is essential because the source table may repeat the same customer-product pair; duplicates must not inflate catalog coverage.

**Compare with the catalog size:** A scalar subquery obtains `COUNT(*)` from `Product`. Because product keys in `Customer` reference that table, a customer's distinct purchase count equals the catalog count exactly when that customer has every catalog product. Keep only those groups with a matching count, then order by `customer_id` solely to make local output deterministic.

Every returned customer has $Q$ distinct referenced product keys and therefore covers the $Q$-row catalog. Conversely, a customer who bought every catalog product contributes at least one row for each key, so distinct counting produces $Q$ and the group passes the `HAVING` condition.

#### Complexity detail

Let $R$ be the number of `Customer` rows and $Q$ the number of `Product` rows. A sort-based grouping and distinct aggregation costs $O(R log R)$ time, while counting the catalog costs $O(Q)$. Grouping, distinct state, input relations, and output sorting require at most $O(R+Q)$ execution space. Database indexes or hash aggregation may improve the physical plan.

#### Alternatives and edge cases

- **Double `NOT EXISTS`:** Express relational division by rejecting a customer when any catalog product lacks a matching purchase. It is logically exact but correlated execution can repeatedly scan the purchase table.
- **Cross join and left join:** Form every customer-product requirement, join purchases, and retain customers with no missing pair. This can materialize $O(CQ)$ rows for $C$ customers.
- **Plain `COUNT(product_key)`:** This is incorrect when duplicate purchase rows exist because repeated copies can mimic full coverage.
- **Duplicate purchases:** `COUNT(DISTINCT product_key)` counts a product once for a customer regardless of repetition.
- **One-product catalog:** Every customer appearing with that referenced product qualifies.
- **Incomplete customers:** Missing even one catalog key excludes the customer.
- **Empty purchase table:** No customer identifier is available to report, so the result is empty.
- **Output order:** LeetCode permits any order; ascending order is an implementation-level deterministic choice.

</details>
