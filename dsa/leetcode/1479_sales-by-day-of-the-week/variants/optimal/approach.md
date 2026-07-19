## General
**Preserving categories before sales**

Start from `Items` and left join `Orders`. This retains every item and therefore every category even when no matching order exists. Starting from orders or using an inner join would silently remove unsold categories.

**Pivoting weekdays with conditional aggregation**

For each weekday, sum a `CASE` expression that contributes `quantity` when `order_date` belongs to that day and zero otherwise. SQLite `strftime('%w', order_date)` numbers Sunday as `'0'` through Saturday as `'6'`; the native MySQL query uses `WEEKDAY`, which numbers Monday as `0` through Sunday as `6`.

**Why null joined rows become zeros**

An unsold item receives a left-joined row with null order fields. No weekday predicate matches, so all seven expressions contribute zero. Sold and unsold items sharing a category are grouped together, and the zero contributions do not alter real totals.

**Grouping at category level**

Group only by `item_category`; grouping by item would split a required category row. Each order joins to its item, contributes its quantity to exactly one weekday expression, and belongs to exactly one category group. Explicit ordering then produces the required deterministic row sequence.

## Complexity detail
With ordinary indexed or hash join and grouping execution, scanning item and order rows costs $O(I+O)$. Sorting the $C$ grouped rows costs $O(C\log C)$. Seven totals per category require $O(C)$ aggregate state.

## Alternatives and edge cases
- **Seven correlated subqueries:** Correct, but repeatedly scans sales for every category and can grow quadratically.
- **Inner join:** Omits categories that have items but no orders.
- **Group by item first:** Can be aggregated again, but creates an unnecessary intermediate level.
- **Dynamic pivot:** Unnecessary because the seven output weekdays are fixed.
- **No orders:** Preserve the category and return seven zeros.
- **Multiple items or orders:** Sum every quantity into the shared category and weekday.
- **Sunday mapping:** SQLite and MySQL use different weekday indices; the two artifacts account for that.
- **Output order:** Grouped SQL results have no implicit order, so `ORDER BY Category` is required.
