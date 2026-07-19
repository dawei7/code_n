# Low-Quality Problems

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2026 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/low-quality-problems/) |

## Problem Description

### Goal

The `Problems` table records the numbers of likes and dislikes received by
each problem. A problem is considered low quality when its likes form strictly
less than 60% of all votes cast for it.

Return the identifiers of every low-quality problem, ordered by `problem_id`
in ascending order. A problem whose like percentage is exactly 60% does not
qualify. The result contains no vote-count columns.

### Function Contract

Let $P$ be the number of rows in `Problems`.

**Inputs**

- `Problems(problem_id, likes, dislikes)`, where `problem_id` is the primary
  key and the other columns contain the vote counts.

**Return value**

- A table with one column, `problem_id`, containing qualifying identifiers in
  ascending order.

### Examples

**Example 1**

- Input: problems `1`, `6`, `7`, `10`, `11`, and `13` with their supplied
  like and dislike counts
- Output: problem IDs `7`, `10`, `11`, and `13`
- Explanation: Each returned problem has a like percentage below 60%; problems
  `1` and `6` are above the threshold.

**Example 2**

- Input: one problem with `likes = 3` and `dislikes = 2`
- Output: no rows
- Explanation: Its like percentage is exactly 60%, not strictly below it.

**Example 3**

- Input: problem `9` with one like and nine dislikes
- Output: problem ID `9`

### Required Complexity

- **Time:** $O(P\log P)$
- **Space:** $O(P)$

<details>
<summary>Approach</summary>

#### General

**Express the threshold without division**

The required comparison is

$$
\frac{\text{likes}}{\text{likes}+\text{dislikes}} < \frac{3}{5}.
$$

Because vote totals are positive, cross multiplication preserves the
inequality. Test `5 * likes < 3 * (likes + dislikes)`. The strict `<` operator
correctly excludes exactly 60%, and integer arithmetic avoids rounding near
the boundary.

**Filter first, then impose the required order**

Select only `problem_id` from rows satisfying that inequality and sort the
result by `problem_id` ascending. Each row is evaluated independently, so it
is returned exactly when its like proportion meets the definition; the final
ordering clause establishes the required output sequence.

#### Complexity detail

Scanning and filtering $P$ rows takes $O(P)$ time. Without relying on a useful
index, sorting as many as $P$ qualifying identifiers takes
$O(P\log P)$ time and $O(P)$ working space. A database may exploit the primary
key order and use less sorting work, but the stated bounds cover the general
plan.

#### Alternatives and edge cases

- **Decimal division:** Comparing a computed ratio with `0.6` is readable but
  can introduce type-dependent rounding or integer-division mistakes.
- **Correlated rank ordering:** Sorting by counting how many IDs precede each
  row is correct but repeatedly scans the table and can take $O(P^2)$ time.
- The threshold is strict; exactly 60% is not low quality.
- Input row order does not determine output order.
- A qualifying set may be empty, but the result still has the
  `problem_id` column.

</details>
