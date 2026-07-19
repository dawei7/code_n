# Paint House II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 265 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/paint-house-ii/) |

## Problem Description
### Goal
Houses stand in a row, and the $n \times k$ matrix `costs` gives the price of painting each house with each of `k` available colors. Choose exactly one color per house, with adjacent houses required to use different colors.

Return the minimum total cost among all valid color assignments. A color's meaning is determined by its column and can be reused on nonadjacent houses. A locally cheapest choice may block a cheaper option for the next house, so all neighbor constraints must be satisfied together. Return `0` when there are no houses, and return only the optimal cost rather than the selected color sequence.

### Function Contract
**Inputs**

- `costs`: an `n × k` matrix of painting costs

**Return value**

The minimum cost of a valid coloring, or zero when there are no houses.

### Examples
**Example 1**

- Input: `costs = [[1,5,3],[2,9,4]]`
- Output: `5`

**Example 2**

- Input: `costs = [[8,2,6,4]]`
- Output: `2`

**Example 3**

- Input: `costs = []`
- Output: `0`
