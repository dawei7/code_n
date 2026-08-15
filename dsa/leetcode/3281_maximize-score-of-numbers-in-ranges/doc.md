# Maximize Score of Numbers in Ranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3281 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Maximize Score of Numbers in Ranges](https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/) |

## Problem Description

### Goal

Each element `start[i]` defines a closed integer interval from `start[i]` through `start[i] + d`. Choose exactly one integer from every interval. Different intervals may overlap or even have the same starting point, and their chosen values do not need to remain associated with the input order when reasoning about their spacing.

The score of a complete choice is the minimum absolute difference between any pair of chosen integers. Find the greatest score that can be achieved by coordinating all choices. A score of zero is possible when the intervals cannot provide distinct values.

### Function Contract

**Inputs**

- `start`: A list of $n$ interval starts, each between $0$ and $10^9$.
- `d`: The common nonnegative interval width, at most $10^9$.

The number of intervals satisfies $2 \le n \le 10^5$. Let $R=\max(\texttt{start})+d-\min(\texttt{start})$ be the total available coordinate span.

**Return value**

Return the maximum possible minimum absolute difference among all pairs of selected integers.

### Examples

#### Example 1

- **Input:** `start = [6, 0, 3], d = 2`
- **Output:** `4`
- **Explanation:** Choosing `8`, `0`, and `4` yields pairwise minimum distance `4`.

#### Example 2

- **Input:** `start = [2, 6, 13, 13], d = 5`
- **Output:** `5`
- **Explanation:** One optimal sorted selection is `2`, `7`, `13`, and `18`.

#### Example 3

- **Input:** `start = [4, 4, 4], d = 0`
- **Output:** `0`
- **Explanation:** Every interval contains only the value `4`.
