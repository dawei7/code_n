# Count Ways to Group Overlapping Ranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2580 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Count Ways to Group Overlapping Ranges](https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/) |

## Problem Description

### Goal

You are given an array `ranges`, where `ranges[i] = [start_i, end_i]` represents the closed interval containing every integer from `start_i` through `end_i`, inclusive.

Assign every range to exactly one of two possibly empty, distinguished groups. Whenever two ranges overlap, they must be assigned to the same group. Two closed ranges overlap when they contain at least one common integer, so sharing an endpoint counts as overlap.

Return the total number of valid assignments modulo $10^9+7$.

### Function Contract

**Inputs**

- `ranges`: A non-empty list of closed integer ranges `[start, end]`.

The number of ranges is between $1$ and $10^5$. Every range satisfies $0 \leq \texttt{start} \leq \texttt{end} \leq 10^9$.

**Return value**

- The number of valid assignments to the two groups, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `ranges = [[6,10],[5,15]]`
- **Output:** `2`
- **Explanation:** The ranges overlap and must stay together; their component can be placed in either group.

#### Example 2

- **Input:** `ranges = [[1,3],[10,20],[2,5],[4,8]]`
- **Output:** `4`
- **Explanation:** The first, third, and fourth ranges form one overlap-connected component, while `[10,20]` forms another. Each component independently chooses one of two groups.
