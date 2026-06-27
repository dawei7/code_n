# Fruits Into Baskets III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3479 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Segment Tree, Ordered Set |
| Official Link | [fruits-into-baskets-iii](https://leetcode.com/problems/fruits-into-baskets-iii/) |

## Problem Description & Examples
### Goal
You are given a list of fruits with specific sizes and a list of baskets, each with a maximum capacity. Each fruit must be placed into a basket sequentially. A fruit can only be placed in a basket if the basket's capacity is greater than or equal to the fruit's size, and the basket is currently empty. Among all valid baskets that satisfy the capacity requirement, you must choose the one with the smallest index. If no such basket exists for a fruit, the fruit is discarded. The goal is to determine the total number of fruits that are successfully placed into baskets.

### Function Contract
**Inputs**

- `fruits`: A list of integers representing the sizes of the fruits in the order they arrive.
- `baskets`: A list of integers representing the maximum capacity of each basket.

**Return value**

- An integer representing the total count of fruits that were successfully placed into a basket.

### Examples
**Example 1**

- Input: `fruits = [4, 2, 5, 3], baskets = [3, 5, 4, 7]`
- Output: `3`

**Example 2**

- Input: `fruits = [1, 1, 1], baskets = [1, 1, 1]`
- Output: `3`

**Example 3**

- Input: `fruits = [5, 1, 2, 3, 4], baskets = [4, 3, 2, 1, 5]`
- Output: `2`

---

## Underlying Base Algorithm(s)
The problem requires efficient range queries to find the first index `i` such that `baskets[i] >= fruit_size`. A Segment Tree is the optimal data structure here, where each node stores the maximum capacity in its range. By traversing the tree, we can perform a "find first" operation in O(log N) time. Once a basket is used, its capacity is updated to -1 to mark it as unavailable.

---

## Complexity Analysis
- **Time Complexity**: O(F log B), where F is the number of fruits and B is the number of baskets. Each fruit requires a O(log B) segment tree search and update.
- **Space Complexity**: O(B) to store the segment tree nodes.
