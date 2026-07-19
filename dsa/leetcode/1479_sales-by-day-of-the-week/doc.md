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
