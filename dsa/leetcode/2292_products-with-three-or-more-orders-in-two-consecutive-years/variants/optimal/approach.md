## General

**Reduce orders to qualifying product-year groups**

Extract the calendar year from each `purchase_date`, group rows by
`product_id` and year, and keep only groups whose order count is at least
three. `quantity` is deliberately absent from the aggregation because the
contract counts orders, not units purchased.

**Pair each qualifying year with its successor**

Self-join the reduced groups on equal product IDs and a year difference of
exactly one. A joined row proves that the same product met the three-order
threshold in both years of a consecutive pair. Conversely, every qualifying
product has such a pair of retained groups and therefore appears in the join.

Use `DISTINCT` on the final product ID because three or more consecutive
qualifying years can create several adjacent pairs for one product. The output
then contains every and only qualifying product once.

## Complexity detail

Let $r$ be the number of rows in `Orders` and $g$ the number of distinct
product-year groups. In the standard sort-based database model, grouping costs
$O(r \log r)$ time. Joining the reduced groups costs at most $O(g \log g)$
with ordinary indexed, hashed, or sorted execution, so the overall bound is
$O(r \log r)$ time and $O(g)$ working space. Exact plans remain engine
dependent.

## Alternatives and edge cases

- **Correlated count per order:** Counting both years separately from each source row can be correct, but repeats scans and may take $O(r^2)$ time.
- **Count two years together:** Requiring six orders across a two-year window is wrong; each individual year must contain at least three orders.
- **Sum `quantity`:** The threshold concerns order rows, so a single large-quantity order still counts only once.
- **Nonconsecutive years:** Qualifying groups in 2020 and 2022 do not form a valid pair.
- **Long qualifying run:** Three qualifying years create two joined pairs, so `DISTINCT` is required to emit the product once.
- **Year boundary:** Calendar years come from the stored dates; December and January belong to adjacent years even when only days apart.
