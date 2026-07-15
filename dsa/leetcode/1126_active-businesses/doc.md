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

### Required Complexity

- **Time:** $O(R \log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Compare each row with the correct peer group.** Use `AVG(occurrences) OVER (PARTITION BY event_type)` to attach the average for an event type to every row of that type. The partition excludes businesses that have no row for the event, matching the definition directly.

**Filter before counting.** Keep only rows satisfying `occurrences > average_occurrences`. The strict operator is essential: a row equal to its event average contributes nothing toward active status.

**Count qualifying event types per business.** Because `(business_id, event_type)` is unique, every surviving row represents one distinct qualifying event type. Group those rows by `business_id` and retain groups with `COUNT(*) > 1`. Thus every returned business has at least two above-average event types, while every active business necessarily contributes at least two surviving rows and is returned.

#### Complexity detail

The window calculation partitions and may sort the $R$ rows, giving a conservative logical bound of $O(R \log R)$ time; the final filter and grouping are linear after that organization. Window and grouping state can require $O(R)$ space. A database optimizer may use indexes, hashing, or external storage, so physical costs can differ.

#### Alternatives and edge cases

- **Grouped averages joined back:** Compute one average per `event_type`, join those averages to `Events`, then filter and group; this has the same semantics and may be preferable on engines without window functions.
- **Correlated average subquery:** Recomputing the matching event average for every row is concise but can repeatedly scan `Events` and degrade toward $O(R^2)$ without optimizer decorrelation or a useful index.
- **Exactly average:** `occurrences = average_occurrences` is not strictly greater and must be excluded.
- **Only one qualifying event:** A business above average for exactly one type is not active because the requirement is more than one.
- **Event recorded by one business:** Its occurrence count equals that event's average, so that row can never qualify.

</details>
