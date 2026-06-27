# Alternating Groups III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3245 |
| Difficulty | Hard |
| Topics | Array, Binary Indexed Tree, Ordered Set |
| Official Link | [alternating-groups-iii](https://leetcode.com/problems/alternating-groups-iii/) |

## Problem Description & Examples
### Goal
Given a circular binary array representing colors, determine the number of contiguous subarrays of length `k` that consist of alternating colors (0 and 1). Additionally, handle dynamic updates where specific indices in the array change their color, and query the total count of such alternating groups after each update.

### Function Contract
**Inputs**

- `colors`: A list of integers (0 or 1) representing the circular array.
- `queries`: A list of queries, where each query is either `[1, k]` (count alternating groups of length `k`) or `[2, i, c]` (update `colors[i]` to `c`).

**Return value**

- A list of integers containing the results for every type-1 query.

### Examples
**Example 1**

- Input: `colors = [0, 1, 0, 1, 0], queries = [[2, 1, 0], [1, 4]]`
- Output: `[2]`
- Explanation: After updating index 1 to 0, the array becomes `[0, 0, 0, 1, 0]`. The alternating groups of length 4 are checked.

**Example 2**

- Input: `colors = [0, 0, 1, 0, 1], queries = [[1, 3], [2, 3, 0], [1, 3]]`
- Output: `[2, 0]`

**Example 3**

- Input: `colors = [1, 0, 1, 0, 1], queries = [[1, 2], [2, 0, 0], [1, 2]]`
- Output: `[5, 4]`

---

## Underlying Base Algorithm(s)
The problem is solved by maintaining the "breaks" in the alternating pattern (where `colors[i] == colors[i+1]`). A Binary Indexed Tree (BIT) or Fenwick Tree is used to store the lengths of contiguous alternating segments. Specifically, we track the lengths of segments of alternating colors and use the BIT to calculate how many segments of length at least `k` exist, accounting for the circular nature of the array by duplicating the array or handling the wrap-around index.

---

## Complexity Analysis
- **Time Complexity**: `O((n + q) log n)`, where `n` is the length of the array and `q` is the number of queries. Each update and query operation takes logarithmic time using the BIT.
- **Space Complexity**: `O(n)`, required to store the BIT and the current state of the array.
