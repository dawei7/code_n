# Points That Intersect With Cars

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2848 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [points-that-intersect-with-cars](https://leetcode.com/problems/points-that-intersect-with-cars/) |

## Problem Description & Examples
### Goal
Given a list of intervals representing the range of coordinates occupied by various cars on a number line, determine the total number of unique integer coordinates that are covered by at least one car.

### Function Contract
**Inputs**

- `nums`: A list of lists, where each inner list `[start, end]` represents the inclusive range of coordinates covered by a car.

**Return value**

- An integer representing the count of distinct integer points covered by the union of all given intervals.

### Examples
**Example 1**

- Input: `nums = [[3,6],[1,5],[4,7]]`
- Output: `7`

**Example 2**

- Input: `nums = [[1,3],[5,8]]`
- Output: `6`

**Example 3**

- Input: `nums = [[1,2],[3,4],[5,6]]`
- Output: `6`

---

## Underlying Base Algorithm(s)
The problem can be solved using a **Set** to track unique integers or a **Difference Array/Prefix Sum** approach. Given the constraints (coordinates up to 100), a boolean array or a set is highly efficient. The set approach iterates through each interval, adds every integer in the range to a hash set, and returns the set's size.

---

## Complexity Analysis
- **Time Complexity**: `O(N * L)`, where `N` is the number of intervals and `L` is the average length of the intervals. In the worst case, this is bounded by the range of coordinates.
- **Space Complexity**: `O(M)`, where `M` is the total number of unique integer points covered, as we store them in a set.
