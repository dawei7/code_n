# Create a Session Bar Chart

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1435 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open Problem](https://leetcode.com/problems/create-a-session-bar-chart/) |

## Problem Description

### Goal

The `Sessions` table stores the duration of each session in seconds. Build a four-row bar-chart summary that counts sessions lasting less than 5 minutes, from 5 minutes through less than 10 minutes, from 10 minutes through less than 15 minutes, and at least 15 minutes.

Return every prescribed bin even when its count is zero. The output labels must be exactly `[0-5>`, `[5-10>`, `[10-15>`, and `15 or more`. The bracket notation denotes half-open minute intervals, so a duration exactly on a 5-, 10-, or 15-minute boundary belongs to the bin beginning at that boundary.

### Function Contract

**Inputs**

- `Sessions(session_id, duration)`: one row per session.
- `session_id` uniquely identifies a session.
- `duration` is the session length in seconds.

**Return value**

- A relation with columns `bin` and `total` containing exactly the four required labels and the number of sessions in each interval.

### Examples

**Example 1**

- Input: `Sessions = [(1,30),(2,199),(3,299),(4,580),(5,1000)]`
- Output: `[("[0-5>",3),("[5-10>",1),("[10-15>",0),("15 or more",1)]`

**Example 2**

- Input: `Sessions = [(1,299),(2,300),(3,599),(4,600),(5,899),(6,900)]`
- Output: `[("[0-5>",1),("[5-10>",2),("[10-15>",2),("15 or more",1)]`

**Example 3**

- Input: `Sessions = [(1,42),(2,120)]`
- Output: `[("[0-5>",2),("[5-10>",0),("[10-15>",0),("15 or more",0)]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Translate minutes into exact second boundaries.** Five, ten, and fifteen minutes correspond to 300, 600, and 900 seconds. Classify each `duration` with a `CASE` expression using `< 300`, `< 600`, `< 900`, and an `ELSE` branch. Testing in ascending order makes the boundary ownership explicit.

**Aggregate the observed classifications once.** Group the classified rows by their label and compute `COUNT(*)`. Each session enters exactly one branch of the `CASE` expression, so it contributes once to one count and cannot be double-counted at a boundary.

**Materialize the complete bin dimension.** A grouped query alone omits a label when no session falls in that interval. Create a four-row `bins` common table expression containing every exact label and a numeric display order, then left join the observed counts onto it. Replace a missing aggregate with zero using `COALESCE`.

**Why the result has exactly the required rows.** The left side of the final join contains one row for each required bin and no other labels. Classification maps every source row to one of those labels, so each joined count is complete. A missing match means the bin truly received no sessions, and `COALESCE(..., 0)` supplies its required zero. Ordering by the hidden numeric key produces a stable bar-chart sequence without adding that key to the output.

#### Complexity detail

The classification and grouping scan the $n$ session rows once. Joining at most four aggregate rows to four fixed bin rows is constant work, so the logical query cost is $O(n)$ time. The grouping domain and result both contain exactly four rows, giving $O(1)$ auxiliary state apart from database-engine execution details.

#### Alternatives and edge cases

- **Four independent conditional queries:** Combining four `COUNT(*)` statements with `UNION ALL` is correct and still linear because the number of bins is fixed, but it scans `Sessions` four times.
- **Group only by the CASE label:** This is concise but fails the contract by omitting empty bins.
- **Correlated counting per session:** Repeatedly scanning `Sessions` from each source row can take $O(n^2)$ time before aggregation.
- **Exact 300 seconds:** It belongs to `[5-10>`, not `[0-5>`.
- **Exact 600 seconds:** It belongs to `[10-15>`.
- **Exact 900 seconds:** It belongs to `15 or more`.
- **Zero sessions in a bin:** Preserve the label and return `0` rather than dropping the row.
- **Units:** Compare seconds to 300, 600, and 900; do not compare the stored values directly with 5, 10, and 15.

</details>
