# Sales Analysis II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1083 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/sales-analysis-ii/) |

## Problem Description

### Goal

The `Product` table maps each `product_id` to its product name and unit price. The `Sales` table records purchases, including the product and buyer involved in each sale along with seller, date, quantity, and price details.

Report the `buyer_id` of every buyer who purchased the product named `S8` and never purchased the product named `iPhone`. Purchases of other products neither qualify nor disqualify a buyer. Return each qualifying buyer once; result rows may appear in any order.

### Function Contract

**Inputs**

- `Product(product_id, product_name, unit_price)`: $P$ product rows keyed by `product_id`.
- `Sales(seller_id, product_id, buyer_id, sale_date, quantity, price)`: $R$ sale rows whose `product_id` values refer to `Product`.

**Return value**

- One column named `buyer_id`.
- One row for each buyer with at least one `S8` purchase and zero `iPhone` purchases.
- Result order is unrestricted; the local reference orders by `buyer_id` for deterministic validation.

### Examples

**Example 1**

`Product`

| product_id | product_name | unit_price |
|---:|---|---:|
| 1 | S8 | 1000 |
| 2 | G4 | 800 |
| 3 | iPhone | 1400 |

`Sales`

| seller_id | product_id | buyer_id | sale_date | quantity | price |
|---:|---:|---:|---|---:|---:|
| 1 | 1 | 1 | 2019-01-21 | 2 | 2000 |
| 1 | 2 | 2 | 2019-02-17 | 1 | 800 |
| 2 | 1 | 3 | 2019-06-02 | 1 | 800 |
| 3 | 3 | 3 | 2019-05-13 | 2 | 2800 |

Output:

| buyer_id |
|---:|
| 1 |

Buyer 1 purchased `S8` and no `iPhone`. Buyer 3 purchased both named products, while buyer 2 never purchased `S8`.

### Required Complexity

- **Time:** $O(P+R\log R)$
- **Space:** $O(P+R)$

<details>
<summary>Approach</summary>

#### General

**Attach product names to purchases:** Join `Sales` with `Product` on `product_id`. Filtering by numeric identifiers alone would assume which rows represent `S8` and `iPhone`; the contract identifies them by `product_name`.

**Summarize both conditions per buyer:** Group the joined rows by `buyer_id`. A conditional sum counts rows named `S8`, and another counts rows named `iPhone`. Keep a group only when the first count is positive and the second equals zero.

Every retained buyer has witnessed at least one `S8` row and no `iPhone` row by the two `HAVING` predicates. Conversely, any buyer satisfying the requested purchase history has a positive first count and zero second count, so that buyer's group is retained exactly once. Other product names contribute zero to both counts and cannot change eligibility.

#### Complexity detail

A hash join can build a $P$-row product lookup and process $R$ sales in expected $O(P+R)$ time. Sort-based grouping and deterministic output ordering can add $O(R\log R)$ time. Join, grouping, and sort state use up to $O(P+R)$ execution space; indexes and the optimizer may choose another plan.

#### Alternatives and edge cases

- **Set difference:** Select distinct `S8` buyers and subtract distinct `iPhone` buyers. It directly models the condition but may require two scans or engine-specific set syntax.
- **Correlated anti-subquery:** Start with `S8` purchases and test separately for an `iPhone` purchase per buyer. It is correct but can repeatedly rescan sales without a suitable index.
- **Filter out iPhone rows before grouping:** It is incorrect because deleting the disqualifying evidence can make an iPhone buyer appear eligible.
- **Several S8 purchases:** Return the buyer once, not once per sale.
- **S8 plus other products:** The buyer remains eligible unless one of those products is `iPhone`.
- **iPhone without S8:** The buyer does not qualify.
- **Product identifiers:** Resolve names through `Product`; do not assume fixed IDs for the named products.

</details>
