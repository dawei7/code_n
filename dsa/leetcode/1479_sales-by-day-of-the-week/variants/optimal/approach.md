## General

**Begin from items so categories with no sales survive.** The query uses `Orders RIGHT JOIN Items` on `item_id`. This is logically the same preservation direction as `Items LEFT JOIN Orders`: every item row remains even when no matching order exists.

Preserving items is crucial because a category such as T-Shirt must appear with seven zeros even if it has never been ordered. An inner join would remove it entirely.

**Group at category level.** Multiple items may share one `item_category`, and each item may have many orders. After the join, grouping by `category` combines every order quantity from all items in that category into one report row.

The selected alias `item_category AS category` supplies the required first column and is reused for grouping and ordering.

**Pivot weekdays with conditional sums.** MySQL `DAYOFWEEK(order_date)` returns one for Sunday, two for Monday, through seven for Saturday. Each output expression keeps `quantity` only when the order belongs to its designated weekday and otherwise contributes zero.

For example, the Monday column is `SUM(IF(DAYOFWEEK(order_date) = '2', quantity, 0))`. Tuesday checks three, and the sequence continues through Saturday seven and Sunday one.

Although the literals are written as strings, MySQL coerces them for comparison with the numeric weekday result. Numeric literals would communicate the type more directly but produce the same behavior here.

**Why missing orders become zero rather than null.** A preserved item without an order has null order fields. `DAYOFWEEK(NULL)` does not equal any weekday code, so every `IF` chooses its explicit zero branch. Summing those zeros produces zero for the category.

This explicit else value avoids relying on `SUM` of nulls, which could return null when a category has no matching quantity.

**Understand the joined row multiplicity.** An item with three orders produces three joined rows, one per order, so all three quantities can contribute. An item with no orders produces one null-extended row solely to preserve its category. Grouping by category then collapses all of these rows into one report record. The right join does not create spurious quantities because null-extended rows contribute zero in every conditional sum.

Categories are derived from `Items` rather than `Orders`. This matters when an order table is empty: every category still forms a group through its preserved items and receives seven zero totals.

**Trace one category.** If two Book items have Monday orders of ten each, both joined rows satisfy the Monday condition and contribute twenty together. A Tuesday order of five contributes only to Tuesday. Every other weekday expression receives zero from those rows.

The seven aggregations run over the same joined group but route each order quantity into exactly one weekday column because one date has one weekday.

**Ordering.** `ORDER BY category` sorts category names ascending as required. No weekday-row ordering is needed because weekdays are fixed output columns.
The outer-preserving join creates a row for every item and attaches all of its orders. Grouping combines precisely the items sharing a category. For each weekday, the conditional expression contributes every and only quantity ordered on that day, with zero for other or missing dates. Therefore each sum is the required category-weekday total, including all-zero categories.

## Complexity detail

Let `I` be item rows, `O` order rows, and `C` categories. With a hash or indexed join, reading and joining inputs takes expected `O(I + O)` time. Conditional aggregation performs constant work per joined row.

Maintaining one seven-value accumulator per category uses `O(C)` space. Sorting the `C` result rows costs `O(C log C)` time and `O(C)` working or result space. Total expected time is `O(I + O + C log C)`, matching the manifest.

Actual database plans may use indexes, sort aggregation, temporary storage, or disk spilling. The bound describes the standard in-memory logical strategy.

The output always has one row per distinct item category, not one per item or order.

## Alternatives and edge cases

- **Items LEFT JOIN Orders:** This is usually easier to read and is logically equivalent to the stored right join.
- **CASE WHEN instead of IF:** Conditional sums with `CASE` are more portable across SQL systems.
- **Inner join:** It is incorrect because categories without orders disappear.
- **No orders for a category:** Its preserved item rows contribute zero to all seven columns.
- **Several items in one category:** Their quantities aggregate together.
- **Several orders on one weekday:** All quantities are summed, not merely counted.
- **Sunday numbering:** MySQL uses one for Sunday; assuming Monday is one would shift every column.
- **Null order date:** It follows every zero branch, which is correct for an item with no order.
- **Zero quantity outside typical data:** It contributes zero naturally.
- **Duplicate category names:** Grouping intentionally merges items with the same category.
- **Category ordering:** Alphabetic ascending order comes from `ORDER BY category`.
- **String weekday literals:** MySQL coercion makes them work, though numeric literals are clearer.
- **Fixed columns:** This static pivot is appropriate because the seven weekday categories are known in advance.
- **Exact totals:** The query sums `quantity` units, not order-row counts.
- **Item with many orders:** Each joined order row contributes independently to its matching weekday.
- **Completely empty Orders table:** Preserved item rows still create every category with zeros.
- **Order referencing an item:** The join obtains its category from the unique `Items.item_id` row.
