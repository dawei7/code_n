# Sales Analysis I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1082 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/sales-analysis-i/) |

## Problem Description

### Goal

The `Product` table identifies each product and records its name and unit price. The `Sales` table records individual sales, including the seller, product, buyer, date, quantity, and the total `price` of that sale.

Add the `price` values for each seller and report the `seller_id` of the seller or sellers with the greatest total sales price. If several sellers tie for the greatest total, return all of them. Result rows may be returned in any order.

### Function Contract

**Inputs**

- `Product(product_id, product_name, unit_price)`: product details keyed by `product_id`.
- `Sales(seller_id, product_id, buyer_id, sale_date, quantity, price)`: $R$ sale rows; `price` is the total price recorded for the sale.

**Return value**

- One column named `seller_id`.
- One row for every seller whose sum of `Sales.price` equals the greatest seller total.
- Result order is unrestricted; the local reference orders by `seller_id` for deterministic validation.

### Examples

**Example 1**

`Sales`

| seller_id | product_id | buyer_id | sale_date | quantity | price |
|---:|---:|---:|---|---:|---:|
| 1 | 1 | 1 | 2019-01-21 | 2 | 2000 |
| 1 | 2 | 2 | 2019-02-17 | 1 | 800 |
| 2 | 2 | 3 | 2019-06-02 | 1 | 800 |
| 3 | 3 | 4 | 2019-05-13 | 2 | 2800 |

Output:

| seller_id |
|---:|
| 1 |
| 3 |

Sellers 1 and 3 each have a total recorded sales price of 2800, greater than seller 2's total of 800.

### Required Complexity

- **Time:** $O(R\log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Aggregate at seller grain:** Group `Sales` by `seller_id` and compute `SUM(price)`. The `price` column already stores the sale's total price, so multiplying it by `quantity` would change the stated value and produce an incorrect seller total.

**Compare with one global maximum:** Materialize the grouped totals as `seller_totals`. A scalar subquery computes the maximum of those totals, and the outer query keeps every seller whose total equals it. Equality preserves all ties rather than choosing an arbitrary row.

Every returned seller has the maximum grouped sum by the filter. Every seller attaining that sum satisfies the same equality and is returned, so the result contains exactly all top sellers. The `Product` table is unnecessary because neither product names nor unit prices affect the requested aggregation.

#### Complexity detail

Let $R$ be the number of `Sales` rows. Sort-based grouping and deterministic output ordering take $O(R\log R)$ time and up to $O(R)$ execution space. Hash aggregation can make the grouping phase expected $O(R)$; indexes and the optimizer may choose a different physical plan.

#### Alternatives and edge cases

- **Dense rank over seller totals:** Rank grouped sums in descending order and keep rank one. It preserves ties but adds a window step when a maximum comparison is sufficient.
- **Correlated seller sum:** Recompute one seller's total for every sale row and deduplicate afterward. It is correct but can rescan `Sales` repeatedly and approach quadratic time.
- **Order and limit one:** `ORDER BY SUM(price) DESC LIMIT 1` discards other sellers tied for first.
- **Multiply by quantity:** It is incorrect because `Sales.price` is already the total price for that sale.
- **Several sales by one seller:** Sum every recorded `price` in that seller's group.
- **Tied maximum:** Return each tied `seller_id` once.
- **Product attributes:** They do not affect total recorded sales price and require no join.

</details>
