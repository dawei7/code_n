## General

**First reduce raw orders to one row per product and year**

The condition concerns how many orders a product received in each calendar year. Individual purchase dates within a year no longer matter after their year is extracted.

The common table expression `P` groups `Orders` by `product_id` and `YEAR(purchase_date)`. Each resulting row represents one product-year combination.

`COUNT(1) >= 3 AS mark` counts order rows in that group and produces a MySQL Boolean value: one when the product has at least three orders that year, zero otherwise.

The query counts orders, not units. `quantity` is intentionally unused because a single order for quantity ten is still one order, while three order rows are three orders.

**Why calendar-year extraction is required**

`YEAR(purchase_date)` maps every date to its calendar year. Consecutive years mean numerical year values differing by one, regardless of the months or days of the purchases.

Grouping by the full date would split orders too finely. Grouping only by product would lose the information needed to find two distinct adjacent years.

**Keep both qualifying and nonqualifying groups in the CTE**

The exact CTE creates a row for every observed product-year and stores qualification in `mark`. It does not discard low-count groups with `HAVING`.

The outer `WHERE p1.mark AND p2.mark` later requires both joined years to qualify. In MySQL, nonzero Boolean values are true and zero values are false.

This two-phase layout separates “calculate yearly status” from “find adjacent qualifying statuses.”

**Join a product to itself one year later**

The CTE is referenced as `p1` and `p2`. The join requires the same product:

`p1.product_id = p2.product_id`.

It also requires

`p1.y = p2.y - 1`,

which is algebraically equivalent to `p2.y = p1.y + 1`. Thus, `p2` is exactly the next calendar year after `p1`.

Missing years cannot accidentally qualify. If a product has groups in 2020 and 2022 but none in 2021, their difference is two and no join row is produced.

**Require both sides to have at least three orders**

The outer filter `p1.mark AND p2.mark` accepts a joined adjacent-year pair only when both yearly counts are at least three.

A product with three orders in 2020 but only two in 2021 has a join row, yet its second mark is false and it is excluded. A product with qualifying 2020 and 2022 groups but a nonqualifying 2021 group also has no adjacent pair with two true marks.

**Remove duplicate product results**

A product can qualify for more than one consecutive pair. For example, qualifying in 2019, 2020, and 2021 creates pairs 2019–2020 and 2020–2021.

The requested output contains product IDs, not one row per qualifying year pair. `SELECT DISTINCT p1.product_id` collapses all successful pairs for the same product into one result row.

The problem permits any output order, so no `ORDER BY` is needed.

**Trace the example**

Product one creates a 2020 group with count three and mark true, plus a 2021 group with count three and mark true. The self-join matches those rows because 2021 is one more than 2020. Both marks pass, so product one is selected.

Product two has only one order in 2022. Its CTE row has a false mark and has no adjacent product-two year row, so it cannot reach the result.

**Why the query is correct**

If a product is returned, it came from two CTE rows with the same product ID, years differing by exactly one, and true marks. Each mark proves at least three order rows in its year, so the product satisfies the contract.

Conversely, if a product has at least three orders in each of two consecutive years, grouping creates two marked rows for exactly those product-year combinations. The self-join matches them, the filter accepts them, and `DISTINCT` retains the product. Therefore, every and only qualifying product appears.

## Complexity detail

Let `r` be the number of order rows and `g` the number of distinct product-year groups. The physical cost depends on MySQL's execution plan and indexes.

Conceptually, grouping processes all `r` rows and may use sorting or hashing. Under a sort-based bound this is `O(r\log r)`. The self-join processes the `g` aggregate rows using a hash join, merge join, or indexes; it is typically linear or `O(g\log g)` after grouping. The manifest summarizes total time as `O(r\log r)` and intermediate group storage as `O(g)`.

`DISTINCT` may require an additional hash or sort over successful product IDs, bounded by the aggregate result size.

## Alternatives and edge cases

- **Filter with** `HAVING COUNT(*) >= 3`: The CTE could retain only qualifying product-years, eliminating `mark` and the outer Boolean filter; the exact query keeps a mark column instead.
- **Window function over yearly groups:** `LAG` can compare the preceding qualifying year, but gaps and count filtering must be handled carefully.
- **Correlated subquery:** It can test for an adjacent qualifying year but may repeat aggregate work without suitable optimization.
- **Use** `SUM(quantity)`: That answers how many units were ordered, not how many orders occurred, and is incorrect here.
- **Exactly three orders:** `COUNT(1) >= 3` includes the boundary.
- **More than three orders:** The Boolean mark remains true; exact count is not needed later.
- **Three qualifying consecutive years:** Two join pairs are produced and `DISTINCT` returns one product row.
- **Gap between qualifying years:** Years differing by two or more do not join.
- **Only one qualifying year:** No two-year pair exists.
- **Low-count intervening year:** It prevents either adjacent pair from passing both marks.
- **Several products:** Product equality in the join prevents years from different products being paired.
- **Unique order IDs:** Each table row is one distinct order, supporting `COUNT(1)`.
- **Any output order:** Omitting `ORDER BY` is intentional.
