# Divide Intervals Into Minimum Number of Groups

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2406 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum |
| Official Link | [divide-intervals-into-minimum-number-of-groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/) |

## Problem Description & Examples
### Goal
Given a collection of closed intervals, determine the minimum number of groups required to partition these intervals such that no two intervals within the same group overlap. Two intervals are considered overlapping if they share any common point.

### Function Contract
**Inputs**

- `intervals`: A list of lists, where each inner list `[left, right]` represents the start and end points of an interval.

**Return value**

- An integer representing the minimum number of groups needed to accommodate all intervals without overlap.

### Examples
**Example 1**

- Input: `intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]`
- Output: `3`

**Example 2**

- Input: `intervals = [[1,3],[5,6],[8,10],[11,13]]`
- Output: `1`

**Example 3**

- Input: `intervals = [[1,1],[2,2],[3,3]]`
- Output: `1`

---

## Underlying Base Algorithm(s)
The problem can be solved using a **Sweep Line** algorithm. By treating the start of an interval as an event that increases the number of active groups and the end of an interval as an event that decreases the number of active groups, we can track the maximum number of concurrent intervals at any point in time. Sorting the start and end points independently allows us to calculate the peak concurrency efficiently.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of intervals, due to the sorting of start and end points.
- **Space Complexity**: `O(N)` to store the sorted start and end points.
