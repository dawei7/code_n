# Unpopular Books

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1098 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [unpopular-books](https://leetcode.com/problems/unpopular-books/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/unpopular-books/).

### Goal
Using `2019-06-23` as the reference date, report books that have been available for at least one month and sold fewer than `10` copies during the previous year.

### Query Contract
**Input tables**

- `Books(book_id, name, available_from)`: Book catalog.
- `Orders(order_id, book_id, quantity, dispatch_date)`: Book orders.

**Output columns**

- `book_id`
- `name`

### Examples
**Example 1**

`Books`

| book_id | name | available_from |
|---:|---|---|
| 1 | Old Quiet Book | 2018-01-01 |
| 2 | Popular Book | 2018-01-01 |
| 3 | New Book | 2019-06-10 |

`Orders`

| order_id | book_id | quantity | dispatch_date |
|---:|---:|---:|---|
| 10 | 1 | 3 | 2019-01-01 |
| 11 | 2 | 12 | 2019-02-01 |

Output:

| book_id | name |
|---:|---|
| 1 | Old Quiet Book |

---

## Solution
### Approach
Filter out books whose `available_from` date is after `2019-05-23`, because those books have not been available for a full month by the reference date. For the remaining books, left join orders from the one-year window ending on `2019-06-23`, sum quantities, and keep books whose total is less than `10`.

Use `COALESCE` so books with no qualifying orders count as `0` sold.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query filters books, joins relevant orders, and groups by book.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
