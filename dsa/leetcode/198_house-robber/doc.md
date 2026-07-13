# House Robber

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 198 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/house-robber/) |

## Problem Description
### Goal
Houses stand along one street, and `nums[i]` gives the nonnegative amount of money in house `i`. Robbing two directly adjacent houses on the same night triggers an alarm, so any chosen set of houses must leave at least one unrobbed position between consecutive choices.

Return the maximum total amount that can be collected without selecting adjacent indices. You may skip any house, including one with a smaller amount when doing so enables more valuable choices later. If every house contains zero, the result is zero. The function returns only the optimal sum, not the selected indices or a modified list of remaining amounts.

### Function Contract
**Inputs**

- `nums`: nonnegative amounts arranged along one street

**Return value**

The maximum sum of a subset containing no adjacent positions.

### Examples
**Example 1**

- Input: `[1,2,3,1]`
- Output: `4`

**Example 2**

- Input: `[2,7,9,3,1]`
- Output: `12`

**Example 3**

- Input: `[50]`
- Output: `50`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

For every prefix of the street, the last house creates two exhaustive choices:

- Skip it, keeping the optimum for the prefix ending at the previous house.
- Rob it, which forbids the previous house and adds its amount to the optimum ending two houses earlier.

If `dp[i]` is the best amount from houses through index `i`, the recurrence is

`dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])`.

Only the two preceding values are needed, so retain rolling totals instead of the full table. Before processing a new amount, let `previous` be the optimum for the processed prefix and `before_previous` the optimum for the prefix excluding its final house. Compute `current = max(previous, before_previous + amount)`, then shift the two variables forward together.

For `[2,7,9,3,1]`, the prefix optima are `2, 7, 11, 11, 12`. At value `9`, taking it plus the best before `7` gives $2 + 9 = 11$; at the final value, $11 + 1$ beats keeping `11`, producing `12`.

This is not safely greedy by local value. In `[2,3,2]`, selecting the largest single house gives `3`, while the two nonadjacent houses give `4`.

Consider an optimal selection for a prefix ending at house `i`. If it omits house `i`, its value is at most the optimum `dp[i - 1]`. If it includes house `i`, it must omit $i - 1$, and the remaining selected houses form an optimal-compatible subset of the prefix through $i - 2$, worth at most `dp[i - 2]`; adding `nums[i]` yields the second recurrence term. Both constructions are valid, so their maximum is exactly optimal. Induction over prefixes proves the final rolling value is the answer.

#### Complexity detail

Each house is processed once, giving $O(n)$ time. Two rolling prefix values and one temporary use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- A full `dp` array makes prefix states visible but uses $O(n)$ space unnecessarily.
- Plain recursive include/exclude search repeats subproblems exponentially; memoization restores linear time but retains linear state and call stack.
- Greedily choosing the largest available house can block a better sum of several nonadjacent houses.
- A single house returns its amount; two houses return their maximum.
- Zero-valued houses do not change the optimum, and a defensive implementation can treat an empty list as zero if the surrounding contract permits it.

</details>
