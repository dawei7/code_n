# Calculate Orders Within Each Interval

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2893 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/calculate-orders-within-each-interval/) |

## Problem Description

### Goal

The `Orders` table records the number of orders received during each numbered minute. The `minute` value uniquely identifies a row, and the table contains a multiple of six rows.

Partition the timeline into consecutive six-minute intervals: minutes $1$ through $6$ form interval $1$, minutes $7$ through $12$ form interval $2$, and the same pattern continues. For every interval, add the six `order_count` values. Return each interval number with its total orders, ordered by `interval_no` in ascending order.

### Function Contract

**Inputs**

- `Orders(minute, order_count)`: `minute` is the integer primary key, and `order_count` is the integer number of orders received during that minute.

Let $M$ be the number of rows in `Orders` and $I = M / 6$ the number of six-minute intervals.

**Return value**

Return two columns: `interval_no`, the one-based six-minute bucket number, and `total_orders`, the sum of `order_count` within that bucket. Sort the $I$ rows by `interval_no` ascending.

### Examples

#### Example 1

- **Input:** `Orders = [(1, 0), (2, 2), (3, 4), (4, 6), (5, 1), (6, 4), (7, 1), (8, 2), (9, 4), (10, 1), (11, 4), (12, 6)]`
- **Output:** `[(1, 17), (2, 18)]`
- **Explanation:** The first six counts sum to `17`; the next six sum to `18`.

#### Example 2

- **Input:** `Orders = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]`
- **Output:** `[(1, 0)]`

#### Example 3

- **Input:** `Orders = [(1, 5), (2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 10), (8, 10), (9, 0), (10, 0), (11, 1), (12, 1), (13, 7), (14, 6), (15, 5), (16, 4), (17, 3), (18, 2)]`
- **Output:** `[(1, 15), (2, 22), (3, 27)]`
