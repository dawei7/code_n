# Sellers With No Sales

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1607 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/sellers-with-no-sales/) |

## Problem Description
### Goal
The database records customers, sellers, and orders. Each order identifies its customer and seller, its cost, and the date on which the sale occurred.

Find every seller who made no sale from January 1, 2020 through December 31, 2020, including both boundary dates. A seller still qualifies when they have orders outside 2020 or have never appeared in `Orders` at all. Return the qualifying seller names in ascending lexicographic order.

### Function Contract
**Inputs**

- `Customer(customer_id, customer_name)`, containing customer identifiers and names.
- `Seller(seller_id, seller_name)`, containing seller identifiers and names.
- `Orders(order_id, sale_date, order_cost, customer_id, seller_id)`, with one row per sale and foreign identifiers for its customer and seller.

**Return value**

Return a relation with the single column `seller_name`. Include sellers for whom no matching order has `sale_date` between `2020-01-01` and `2020-12-31`, and order the rows by `seller_name` ascending.

### Examples
**Example 1**

- Input: Daniel and Elizabeth have sales during 2020, while Frank's only sale is in 2019.
- Output: `Frank`

**Example 2**

- Input: A seller has orders on `2020-01-01` and `2020-12-31`.
- Output: That seller is excluded because both endpoints belong to the target interval.

**Example 3**

- Input: A seller has no rows in `Orders`.
- Output: That seller is included.

### Required Complexity
- **Time:** $O((s+r)\log(s+r))$
- **Space:** $O(s+r)$

<details>
<summary>Approach</summary>

#### General

Let $s$ be the number of rows in `Seller` and $r$ the number of rows in `Orders`.

**Identify sellers active during 2020.** Filter `Orders` with the inclusive condition `sale_date BETWEEN '2020-01-01' AND '2020-12-31'`, then retain distinct `seller_id` values. Multiple qualifying orders by one seller affect exclusion only once.

**Apply an anti-join from the complete seller table.** Left join every `Seller` row to the active-ID relation and keep rows where the joined active ID is `NULL`. Starting from `Seller` is essential: it preserves sellers with no order history as well as sellers whose orders all lie outside the target year. `Customer` and `order_cost` do not affect the requested classification.

Every excluded seller has a witnessed 2020 order in the active relation. Every retained seller lacks such a witness, which is exactly the no-sales condition. Finally, sort `seller_name` ascending as required.

#### Complexity detail

Under a portable comparison-based model, filtering and deduplicating up to $r$ order rows, joining against $s$ sellers, and sorting the result fit within $O((s+r)\log(s+r))$ time. The distinct active IDs, join state, and output ordering may use $O(s+r)$ working space. With suitable indexes or hash joins, a database engine may approach linear expected processing before the required output sort.

#### Alternatives and edge cases

- **Correlated `NOT EXISTS`:** This directly expresses the Accepted anti-join and many optimizers execute it efficiently, but a naive engine can rescan `Orders` for every seller.
- **`NOT IN` over filtered seller IDs:** This is concise when `seller_id` is guaranteed non-null; `NOT EXISTS` or a left anti-join is safer under nullable SQL semantics.
- **Filter all order history:** Excluding any seller found in `Orders` is wrong because orders before or after 2020 do not disqualify the seller.
- The interval is inclusive at both `2020-01-01` and `2020-12-31`.
- A seller with no orders qualifies.
- Several orders by the same seller in 2020 still produce only one exclusion.
- Customer identity and order cost are irrelevant to whether a seller made a sale in the target year.
- The output must be sorted by `seller_name`, not by `seller_id`.

</details>
