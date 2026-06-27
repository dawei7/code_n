# Find Building Where Alice and Bob Can Meet

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2940 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Stack, Binary Indexed Tree, Segment Tree, Heap (Priority Queue), Monotonic Stack |
| Official Link | [find-building-where-alice-and-bob-can-meet](https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/) |

## Problem Description & Examples
### Goal
Given an array representing the heights of buildings, determine the leftmost building index where two people, Alice and Bob, can meet. A person at index `i` can move to index `j` if `j > i` and `heights[j] > heights[i]`. For a set of queries, each containing two starting indices, find the smallest index `k` such that both people can reach `k` from their respective starting positions. If no such building exists, return -1.

### Function Contract
**Inputs**

- `heights`: A list of integers representing the height of each building.
- `queries`: A list of lists, where each inner list contains two integers `[a, b]` representing the starting indices of Alice and Bob.

**Return value**

- A list of integers where the `i`-th element is the index of the meeting building for the `i`-th query, or -1 if no meeting is possible.

### Examples
**Example 1**

- Input: `heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]`
- Output: `[2,5,-1,5,2]`

**Example 2**

- Input: `heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]`
- Output: `[7,6,-1,4,6]`

**Example 3**

- Input: `heights = [1,2,1,2], queries = [[0,0]]`
- Output: `[0]`

---

## Underlying Base Algorithm(s)
The problem is solved using an offline query processing approach combined with a Min-Heap. By sorting queries based on their rightmost index in descending order, we can process buildings from right to left. We maintain a Min-Heap of queries that are waiting for a building of a certain height to be found. As we iterate through the buildings, we check if the current building's height satisfies the requirements of the queries in the heap.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N + Q log Q)`, where `N` is the number of buildings and `Q` is the number of queries. Sorting the queries takes `O(Q log Q)`, and each query is pushed/popped from the heap at most once, taking `O(Q log Q)`. Iterating through buildings takes `O(N)`.
- **Space Complexity**: `O(N + Q)` to store the queries, the heap, and the results.
