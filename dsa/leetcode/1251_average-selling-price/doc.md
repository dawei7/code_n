# Average Selling Price

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1251 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/average-selling-price/) |

## Problem Description

### Goal

The `Prices` table records a product's price over non-overlapping inclusive date intervals. The `UnitsSold` table records how many units of a product were purchased on a particular date. A sale uses the price whose interval contains its purchase date.

For every product appearing in `Prices`, report its average selling price: total revenue divided by total units sold, rounded to two decimal places. A product with no sold units must still appear with an average price of `0`. The result may be returned in any order.

### Function Contract

**Inputs**

- `Prices(product_id, start_date, end_date, price)`: price intervals; intervals for the same product do not overlap, and both endpoints are inclusive.
- `UnitsSold(product_id, purchase_date, units)`: dated sales quantities.
- Let $p$ and $u$ be the row counts of `Prices` and `UnitsSold`, and let $r=p+u$.

**Return value**

- Return `product_id` and `average_price` for every product in `Prices`, rounding the units-weighted average to two decimal places and using `0` when no units were sold.

### Examples

**Example 1**

`Prices`

| product_id | start_date | end_date | price |
|---:|---|---|---:|
| 1 | 2019-02-17 | 2019-02-28 | 5 |
| 1 | 2019-03-01 | 2019-03-22 | 20 |
| 2 | 2019-02-01 | 2019-02-20 | 15 |
| 2 | 2019-02-21 | 2019-03-31 | 30 |

`UnitsSold`

| product_id | purchase_date | units |
|---:|---|---:|
| 1 | 2019-02-25 | 100 |
| 1 | 2019-03-01 | 15 |
| 2 | 2019-02-10 | 200 |
| 2 | 2019-03-22 | 30 |

Output:

| product_id | average_price |
|---:|---:|
| 1 | 6.96 |
| 2 | 16.96 |

**Example 2**

A product with a price interval but no row in `UnitsSold` is returned with `average_price = 0`.

**Example 3**

Sales on `start_date` or `end_date` use that interval's price because interval boundaries are inclusive.

### Required Complexity

- **Time:** $O(r)$
- **Space:** $O(r)$

<details>
<summary>Approach</summary>

#### General

**Match each sale to its effective price.** Left join `Prices` to `UnitsSold` by `product_id` and require `purchase_date` to fall between `start_date` and `end_date`, inclusively. Non-overlapping intervals ensure that a sale matches at most one price row. The left join preserves price-only products.

**Aggregate revenue and quantity together.** For each product, `price * units` is the revenue contributed by a matched sale. Sum those products for total revenue and sum `units` for total quantity. Dividing the two sums produces a units-weighted average; averaging interval prices directly would incorrectly give every interval equal influence.

**Handle empty products after aggregation.** An unmatched product group has null sums. Use `COALESCE` to turn its quotient into zero, then apply `ROUND(..., 2)` to the final weighted average. Group only by `product_id` so all of a product's price intervals contribute to one output row.

#### Complexity detail

With indexes or hash-based join and aggregation, the query processes the $r$ input rows in $O(r)$ logical time and uses $O(r)$ join and grouping state. A database engine may instead choose sort-based or nested-loop physical plans depending on available indexes and statistics.

#### Alternatives and edge cases

- **Correlated aggregate per product:** It is correct but may rescan both tables for every product and grow quadratically.
- **Inner join:** It drops products with no sales instead of returning their required zero average.
- **`AVG(price)`:** It averages price intervals rather than weighting prices by sold units.
- **Average of row-level revenue:** `AVG(price * units)` does not divide total revenue by total units and is semantically different.
- **Inclusive boundaries:** Use `BETWEEN` or equivalent `>=` and `<=` comparisons so endpoint sales are retained.
- **No sold units:** Protect the null quotient with `COALESCE` and emit `0`.

</details>
