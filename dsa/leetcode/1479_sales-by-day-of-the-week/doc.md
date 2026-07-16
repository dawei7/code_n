# Sales by Day of the Week

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1479 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/sales-by-day-of-the-week/) |

## Problem Description
### Goal

The `Items` table assigns every item to a category, while `Orders` records dated quantities sold for those items. Produce one row for every distinct item category and summarize its total ordered quantity separately for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday.

A category must still appear when none of its items has a matching order; every day total for such a category is zero. Combine all items within the same category, count every order quantity on the weekday of `order_date`, and return rows ordered lexicographically by category.

### Function Contract
**Input tables**

Let $I$ be the number of `Items` rows, $O$ the number of `Orders` rows, and $C$ the number of distinct categories.

- `Items(item_id, item_name, item_category)` stores item identifiers, names, and categories.
- `Orders(order_id, customer_id, order_date, item_id, quantity)` stores dated quantities and references `Items.item_id`.
- Several items may share a category, and an item or entire category may have no orders.

**Return value**

Return `Category`, then `Monday` through `Sunday`. Each weekday column is the sum of `quantity` for that category on that weekday, or zero when no matching order exists. Sort rows by `Category` ascending.

### Examples
**Example 1**

The official fixture produces `Book` totals `[20,5,0,0,10,0,0]`, `Glasses` totals `[0,0,0,0,5,0,0]`, `Phone` totals `[0,0,5,1,0,0,10]`, and seven zeros for the unsold `T-shirt` category.

**Example 2**

If two `Food` items sell quantities `3` and `7` on Monday, the single `Food` row reports Monday as `10`.

**Example 3**

A category with only Saturday orders reports zero in the other six weekday columns.

### Required Complexity
- **Time:** $O(I+O+C\log C)$
- **Space:** $O(C)$

<details>
<summary>Approach</summary>

#### General

**Preserving categories before sales**

Start from `Items` and left join `Orders`. This retains every item and therefore every category even when no matching order exists. Starting from orders or using an inner join would silently remove unsold categories.

**Pivoting weekdays with conditional aggregation**

For each weekday, sum a `CASE` expression that contributes `quantity` when `order_date` belongs to that day and zero otherwise. SQLite `strftime('%w', order_date)` numbers Sunday as `'0'` through Saturday as `'6'`; the native MySQL query uses `WEEKDAY`, which numbers Monday as `0` through Sunday as `6`.

**Why null joined rows become zeros**

An unsold item receives a left-joined row with null order fields. No weekday predicate matches, so all seven expressions contribute zero. Sold and unsold items sharing a category are grouped together, and the zero contributions do not alter real totals.

**Grouping at category level**

Group only by `item_category`; grouping by item would split a required category row. Each order joins to its item, contributes its quantity to exactly one weekday expression, and belongs to exactly one category group. Explicit ordering then produces the required deterministic row sequence.

#### Complexity detail

With ordinary indexed or hash join and grouping execution, scanning item and order rows costs $O(I+O)$. Sorting the $C$ grouped rows costs $O(C\log C)$. Seven totals per category require $O(C)$ aggregate state.

#### Alternatives and edge cases

- **Seven correlated subqueries:** Correct, but repeatedly scans sales for every category and can grow quadratically.
- **Inner join:** Omits categories that have items but no orders.
- **Group by item first:** Can be aggregated again, but creates an unnecessary intermediate level.
- **Dynamic pivot:** Unnecessary because the seven output weekdays are fixed.
- **No orders:** Preserve the category and return seven zeros.
- **Multiple items or orders:** Sum every quantity into the shared category and weekday.
- **Sunday mapping:** SQLite and MySQL use different weekday indices; the two artifacts account for that.
- **Output order:** Grouped SQL results have no implicit order, so `ORDER BY Category` is required.

</details>
