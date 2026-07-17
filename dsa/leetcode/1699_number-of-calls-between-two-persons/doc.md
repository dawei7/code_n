# Number of Calls Between Two Persons

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1699 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-calls-between-two-persons/) |

## Problem Description
### Goal

The `Calls` table records one phone call per row with a caller `from_id`, a different recipient `to_id`, and the call's `duration`. The table has no primary key and may contain duplicate rows. Direction identifies who initiated a row, but the requested report treats calls in both directions as interactions between the same pair of people.

Produce one row for each unordered pair that appears in the table. Name the smaller identifier `person1` and the larger identifier `person2`, so `person1 < person2`. Report the number of call rows between them as `call_count` and the sum of their durations as `total_duration`. Return the pair rows in any order.

### Function Contract
**Inputs**

- `Calls(from_id, to_id, duration)`: all directed call records, with `from_id != to_id`; duplicate rows remain separate calls

Let $R$ be the number of rows in `Calls`.

**Return value**

A table with columns `person1`, `person2`, `call_count`, and `total_duration`, containing one row for every unordered participant pair.

### Examples
**Example 1**

- Input: calls `1 -> 2` for 59 and `2 -> 1` for 11
- Output: pair `(1, 2)` with `call_count = 2, total_duration = 70`

Reversing caller and recipient does not create a second report group.

**Example 2**

- Input: calls between 3 and 4 with durations 100, 200, 200, and 499
- Output: pair `(3, 4)` with `call_count = 4, total_duration = 999`

The two equal 200-duration rows are separate calls and both contribute.

**Example 3**

- Input: one call `7 -> 2` lasting 30
- Output: `(2, 7, 1, 30)`

The smaller ID is always projected first, regardless of call direction.

### Required Complexity

- **Time:** $O(R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Canonicalize direction before grouping**

For every call row, compute `person1` as the smaller of `from_id` and `to_id`, and `person2` as the larger. SQL `CASE` expressions implement this portably. Both directions between the same participants now yield the identical key `(person1, person2)`, while the strict identifier inequality guarantees the two projected values differ.

**Aggregate every call row in its canonical pair**

Group by the two canonical expressions. `COUNT(*)` gives the number of calls, including duplicate source rows, and `SUM(duration)` gives their combined duration. Do not apply `DISTINCT`: identical rows still represent multiple table records and must contribute multiple times.

Each source row maps to exactly one unordered pair, and every pair present in the input has a group. Canonicalization makes opposite directions share that group, so its count and sum cover exactly all calls between those two people. The problem permits any result order, so sorting is unnecessary.

#### Complexity detail

A hash aggregation examines each of the $R$ call rows once, computes a constant-size canonical key, and updates two aggregates in expected $O(1)$ time, for expected $O(R)$ total time. There can be at most $R$ distinct pairs, so the aggregation state uses $O(R)$ space.

#### Alternatives and edge cases

- **Union both directions:** duplicating rows with reversed endpoints before grouping is unnecessary and would double-count unless followed by extra correction.
- **Group by directed IDs:** grouping directly on `(from_id, to_id)` incorrectly separates calls in opposite directions.
- **Correlated subqueries per row:** repeatedly scanning for the reverse pair can take quadratic time and still needs deduplication of output pairs.
- **Duplicate call rows:** every row counts as a call and contributes its full duration; no `DISTINCT` belongs in either aggregate.
- **Only reverse-direction rows:** canonical expressions still place the smaller ID in `person1`.
- **Several partners for one person:** each distinct second participant forms its own unordered pair group.
- **Output order:** any row order is valid and is compared as an unordered table.

</details>
