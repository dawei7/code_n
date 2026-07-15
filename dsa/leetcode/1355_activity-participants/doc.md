# Activity Participants

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1355 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open Problem](https://leetcode.com/problems/activity-participants/) |

## Problem Description

### Goal

The `Activities` table lists the available activities, each with an ID and unique name. Every row in `Friends` identifies a friend and records the activity that friend participates in. An activity's participant count is the number of friend rows naming it.

Return the names of all activities whose participant count is neither the maximum nor the minimum among the listed activities. Activities tied at either extreme are excluded. The result may be returned in any order.

### Function Contract

**Inputs**

- `Activities(id, name)`: the catalog of activities.
- `Friends(id, name, activity)`: friends and the activity name chosen by each friend.
- Let $A$ and $F$ be the table row counts, and let $N = A + F$.

**Return value**

- Return one column named `activity` containing every activity whose participant count is strictly between the global minimum and maximum counts.

### Examples

**Example 1**

- Participant counts: Eating has `3`, Singing has `2`, and Horse Riding has `1`.
- Output: `Singing`.

**Example 2**

- Participant counts: A has `1`, B has `1`, and C has `1`.
- Output: no rows, because every activity is tied for both extremes.

**Example 3**

- Participant counts: A has `0`, B has `2`, C has `3`, and D has `3`.
- Output: `B`.

### Required Complexity

- **Time:** $O(N \log N)$
- **Space:** $O(A)$

<details>
<summary>Approach</summary>

#### General

**Count participants for every catalog activity.** Left join `Activities` to `Friends` on the activity name and group by the activity identity. Counting `f.id`, rather than all joined rows, gives zero to an activity with no matching friend and the exact number of friends otherwise.

**Compute the popularity bounds once.** From the grouped counts, derive the minimum and maximum participant totals. Keep only rows whose count is strictly greater than the minimum and strictly less than the maximum. Strict inequalities exclude every tie at either extreme, as required.

The grouped relation contains one row for every listed activity. Its bounds are therefore the global popularity extremes, and the final predicate returns exactly the activities at neither extreme.

#### Complexity detail

In the general sort/group model, joining and grouping $N$ input rows takes $O(N \log N)$ time. Hash aggregation can make the expected time linear. The grouped counts and lookup state contain at most $A$ activities, giving $O(A)$ auxiliary space.

#### Alternatives and edge cases

- **Correlated count per activity:** Counting matching friends independently for every activity is correct but may take $O(AF)$ time without an index.
- **Window functions:** Applying `MIN` and `MAX` windows to grouped counts is equivalent, though the staged aggregate is often easier to read.
- **All counts equal:** The minimum equals the maximum, so no activity qualifies.
- **Ties at one extreme:** Every activity sharing the minimum or maximum must be excluded.
- **Zero participants:** A catalog activity with no friends has count zero and can define the minimum.
- **Only two popularity levels:** Every activity belongs to an extreme, leaving an empty result.

</details>
