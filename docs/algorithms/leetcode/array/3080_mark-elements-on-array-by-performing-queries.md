# Mark Elements on Array by Performing Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3080 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sorting, Heap (Priority Queue), Simulation |
| Official Link | [mark-elements-on-array-by-performing-queries](https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/) |

## Problem Description & Examples
### Goal
Given an array of integers and a sequence of queries, you must maintain a "marked" status for each index. For each query `(index, k)`, you first mark the element at the specified index (if not already marked). Then, you identify the `k` smallest unmarked elements in the array (breaking ties by index) and mark them as well. After each query, calculate the sum of all currently unmarked elements.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial array.
- `queries`: A list of lists, where each inner list contains two integers `[index, k]`.

**Return value**

- A list of integers representing the sum of unmarked elements after each query is processed.

### Examples
**Example 1**

- Input: `nums = [1, 2, 2, 1, 2, 3, 1]`, `queries = [[1, 2], [3, 3], [4, 2]]`
- Output: `[8, 6, 0]`

**Example 2**

- Input: `nums = [1, 4, 2, 3]`, `queries = [[0, 1]]`
- Output: `[7]`

**Example 3**

- Input: `nums = [1, 1, 1]`, `queries = [[0, 1], [1, 2]]`
- Output: `[2, 0]`

---

## Underlying Base Algorithm(s)
The problem is solved using a Min-Heap (Priority Queue) to efficiently retrieve the smallest unmarked elements. We store tuples of `(value, index)` in the heap. A boolean array (or set) tracks which indices have been marked to ensure we skip already marked elements during the heap extraction process.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N + Q log N)`, where `N` is the length of `nums` and `Q` is the number of queries. Sorting the initial array takes `O(N log N)`, and each query involves heap operations that take `O(log N)`.
- **Space Complexity**: `O(N)`, required to store the heap, the marked status array, and the initial array values.
