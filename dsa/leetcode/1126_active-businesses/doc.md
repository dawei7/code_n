# Active Businesses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1126 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/active-businesses/) |

## Problem Description

### Goal

The `Events` table records, for each `(business_id, event_type)` pair, how many times that event occurred at the business. Its composite primary key makes every business-and-event pair unique. For a particular `event_type`, define its average activity as the average `occurrences` among all businesses that have a row for that event type; businesses without that event are not included in its average.

A business is active when it has more than one event type whose own `occurrences` value is strictly greater than the average activity for that same event type. Find the identifiers of all active businesses and return them in any order. Equality with an event's average does not qualify as above average.

### Function Contract

**Input table**

- `Events(business_id, event_type, occurrences)`: one row per business and event type, with `(business_id, event_type)` as the primary key.

Let $R$ be the number of rows in `Events`.

**Return value**

A result table with one column, `business_id`, containing every business that is strictly above its event-type average for at least two event types. Row order is not significant.

### Examples

**Example 1**

`Events`

| business_id | event_type | occurrences |
|---:|---|---:|
| 1 | reviews | 7 |
| 3 | reviews | 3 |
| 1 | ads | 11 |
| 2 | ads | 7 |
| 3 | ads | 6 |
| 1 | page views | 3 |
| 2 | page views | 12 |

Output:

| business_id |
|---:|
| 1 |

The averages are $5$ for `reviews`, $8$ for `ads`, and $7.5$ for `page views`. Business `1` is strictly above average for both `reviews` and `ads`, so it is active.
