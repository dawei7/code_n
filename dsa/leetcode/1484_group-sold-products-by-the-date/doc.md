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

### Required Complexity
- **Time:** $O(R + P \log P)$
- **Space:** $O(P)$

<details>
<summary>Approach</summary>

#### General

**Removing duplicate sale pairs first**

Project `sell_date` and `product` through `SELECT DISTINCT`. The resulting relation contains exactly one row for each product that should contribute to one date. After this step, an ordinary row count within a date equals the required distinct-product count, and each product name appears exactly once in the eventual list.

This explicit deduplication also keeps the SQLite app-local query portable: SQLite cannot combine `DISTINCT` with a custom separator in every `GROUP_CONCAT` form.

**Establishing product order before concatenation**

Sort the distinct rows by `sell_date` and then `product`. The rows for each date are therefore contiguous and their product names arrive in lexicographic order. Applying `GROUP_CONCAT(product, ',')` to that ordered input produces the required comma-separated list.

The separate LeetCode-native MySQL artifact can state the same requirement directly as `GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',')`.

**Aggregating one row per date**

Group the ordered distinct relation by `sell_date`. Because each input row now represents a unique product for that date, `COUNT(*)` is exactly `num_sold`. Concatenation includes precisely the same set of rows, so the count and list cannot disagree about duplicates.

Finally, apply `ORDER BY sell_date` to the grouped result. Ordering the products inside each group and ordering the result dates are independent requirements; both must be explicit.

**Why every output row is correct**

For a fixed date $d$, the deduplicated relation contains one and only one row for every product sold on $d$. Counting those rows gives the cardinality of the distinct product set. Concatenating their names after sorting lists every member of that set exactly once in lexicographic order. Grouping creates one result for each represented date, and the final ordering places those dates ascending.

#### Complexity detail

Deduplicating $R$ activities requires an $O(R)$ scan under hash-based execution and retains $P$ distinct pairs. Ordering those pairs costs $O(P \log P)$ time, after which grouping and concatenation are linear in $P$. The materialized distinct and ordered data uses $O(P)$ space. Actual database engines may choose equivalent index, hash, or sort plans.

#### Alternatives and edge cases

- **Native MySQL distinct concatenation:** Use `COUNT(DISTINCT product)` with `GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',')`. It is concise and is the platform-native artifact, but the exact syntax is not portable to SQLite.
- **Correlated subqueries per date:** Select distinct dates and run separate count and concatenation scans for each one. This is correct but can repeatedly scan `Activities` and grow quadratically with the number of dates.
- **Deduplicate without ordering:** It gives the right count but leaves concatenation order implementation-dependent and therefore does not satisfy the contract.
- **Duplicate activities:** Repeated copies of the same product on the same date contribute one to `num_sold` and one name to `products`.
- **Same product on different dates:** Deduplication is by the pair, so the product contributes independently to each date.
- **One product on a date:** The list contains that name without an extra comma.
- **Unsorted input rows:** Neither output row order nor product-list order may depend on insertion order.
- **Lexicographic comparison:** Product spelling is preserved; ordering follows the database's configured string collation.
- **Output aliases:** The aggregate columns must be named exactly `num_sold` and `products`.
- **Date ordering:** The outer `ORDER BY` is required even though the inner rows were already sorted.

</details>
