# Sales Analysis III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1084 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/sales-analysis-iii/) |

## Problem Description

### Goal

The `Product` table identifies each product and stores its name and unit price. The `Sales` table contains sale information and may contain duplicate rows; every sale's `product_id` refers to a product.

Report the products that were sold only during the first quarter of 2019: every sale for the product must have a `sale_date` from `2019-01-01` through `2019-03-31`, inclusive. A reported product must actually have at least one sale, so an unsold product does not qualify vacuously. Return `product_id` and `product_name` in any order.

### Function Contract

**Inputs**

- `Product(product_id, product_name, unit_price)`: $P$ product rows keyed by `product_id`.
- `Sales(seller_id, product_id, buyer_id, sale_date, quantity, price)`: $R$ sale rows; duplicate rows are allowed and `product_id` refers to `Product`.

**Return value**

- Columns `product_id` and `product_name`.
- One row for each sold product whose earliest and latest sale dates both lie within the inclusive first-quarter window.
- Result order is unrestricted; the local reference orders by `product_id` for deterministic validation.

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
| 2 | 2 | 3 | 2019-06-02 | 1 | 800 |
| 3 | 3 | 4 | 2019-05-13 | 2 | 2800 |

Output:

| product_id | product_name |
|---:|---|
| 1 | S8 |

Product 1 has sales only inside the quarter. Product 2 also has a June sale, and product 3 has no sale inside the quarter.

### Required Complexity

- **Time:** $O(P+R\log R)$
- **Space:** $O(P+R)$

<details>
<summary>Approach</summary>

#### General

**Require a real sale through the join:** Inner-join `Product` with `Sales`. This both supplies each output name and excludes products with no sales, which must not qualify merely because they have no outside-window row.

**Reduce all dates to two boundaries:** Group by the product's identifier and name. All of a product's sale dates lie inside an inclusive interval exactly when its minimum date is at least `2019-01-01` and its maximum date is at most `2019-03-31`.

**Apply inclusive comparisons:** Keep only groups meeting both `HAVING` predicates. Duplicate sales do not change either date boundary, although they remain valid input rows.

Every retained group contains at least one sale because of the inner join, and its minimum and maximum bound every other date within the required quarter. Conversely, if every sale of a product is within the quarter, its minimum and maximum satisfy both predicates, so the product is returned.

#### Complexity detail

A hash join can build a $P$-row product lookup and process $R$ sales in expected $O(P+R)$ time. Sort-based grouping and deterministic output ordering can add $O(R\log R)$ time. Join, grouping, and sort state use up to $O(P+R)$ execution space.

#### Alternatives and edge cases

- **Conditional outside-date count:** Group sales and require the count of dates outside the quarter to be zero. It is equally valid but expresses a contiguous range less directly than minimum and maximum.
- **Correlated minimum and maximum:** Compute both boundaries separately for each product. It is correct but can repeatedly rescan `Sales` and approach quadratic time.
- **Filter dates before grouping:** It is incorrect because it erases outside-quarter evidence and can admit a product sold both inside and outside the quarter.
- **Boundary dates:** Sales on `2019-01-01` and `2019-03-31` are included.
- **Unsold product:** Exclude it because the product was not sold during the quarter.
- **Duplicate rows:** They do not change qualification.
- **Any outside sale:** A sale before January or after March disqualifies the product even if it also sold inside the quarter.

</details>
