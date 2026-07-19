# Group Sold Products By The Date

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1484 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/group-sold-products-by-the-date/) |

## Problem Description
### Goal

The `Activities` table records a sale date and product name for each market activity. It has no primary key, so identical rows may appear more than once.

Produce one row for every represented `sell_date`. Report the number of different products sold on that date as `num_sold`, and report those distinct names as one comma-separated `products` string in lexicographic order. Sort the result rows by `sell_date` in ascending order.

### Function Contract
**Inputs**

Let $R$ be the number of rows in `Activities`, and let $P$ be the number of distinct `(sell_date, product)` pairs.

**`Activities`**

| Column | Type | Meaning |
|---|---|---|
| `sell_date` | date | Date on which the market sold the product. |
| `product` | varchar | Product name recorded for that activity. |

- The table has no primary key.
- Duplicate `(sell_date, product)` rows are allowed and must not increase either output field.

**Return value**

Return a relation with these columns:

- `sell_date`: a date present in `Activities`;
- `num_sold`: the number of distinct product names sold on that date;
- `products`: those distinct names joined with commas in lexicographic order.

Order rows by `sell_date` ascending.

### Examples
**Example 1**

Input `Activities`:

| sell_date | product |
|---|---|
| 2020-05-30 | Headphone |
| 2020-06-01 | Pencil |
| 2020-06-02 | Mask |
| 2020-05-30 | Basketball |
| 2020-06-01 | Bible |
| 2020-06-02 | Mask |
| 2020-05-30 | T-Shirt |

Output:

| sell_date | num_sold | products |
|---|---:|---|
| 2020-05-30 | 3 | Basketball,Headphone,T-Shirt |
| 2020-06-01 | 2 | Bible,Pencil |
| 2020-06-02 | 1 | Mask |

The repeated `Mask` activity contributes only one distinct product on `2020-06-02`.
