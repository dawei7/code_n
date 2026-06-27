# K-th Nearest Obstacle Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3275 |
| Difficulty | Medium |
| Topics | Array, Heap (Priority Queue) |
| Official Link | [k-th-nearest-obstacle-queries](https://leetcode.com/problems/k-th-nearest-obstacle-queries/) |

## Problem Description & Examples
### Goal
Given a sequence of 2D coordinates representing obstacles appearing one by one, determine the distance of the k-th nearest obstacle from the origin (0, 0) after each new obstacle is added. The distance is defined as the Manhattan distance: |x| + |y|. If there are fewer than k obstacles currently present, the result for that step is -1.

### Function Contract
**Inputs**

- `queries`: A list of lists where each sub-list contains two integers `[x, y]` representing the coordinates of an obstacle.
- `k`: An integer representing the rank of the distance to track.

**Return value**

- A list of integers where the i-th element is the k-th smallest Manhattan distance after processing the first i+1 queries.

### Examples
**Example 1**

- Input: `queries = [[1,2],[3,4],[2,3],[-3,0]]`, `k = 2`
- Output: `[-1, 7, 5, 3]`

**Example 2**

- Input: `queries = [[5,5],[4,4],[3,3]]`, `k = 1`
- Output: `[10, 8, 6]`

**Example 3**

- Input: `queries = [[1,2],[3,4],[2,3],[-3,0]]`, `k = 3`
- Output: `[-1, -1, 6, 5]`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Max-Heap**. By maintaining a max-heap of size `k`, we ensure that the root of the heap always represents the largest distance among the `k` closest obstacles found so far. When a new obstacle is added, if the heap size is less than `k`, we push the distance. If the heap size is `k` and the new distance is smaller than the current maximum in the heap, we pop the maximum and push the new distance.

---

## Complexity Analysis
- **Time Complexity**: `O(N log k)`, where `N` is the number of queries. Each insertion and deletion operation in the heap takes `O(log k)` time.
- **Space Complexity**: `O(k)`, as we only store at most `k` distances in the heap at any given time.
