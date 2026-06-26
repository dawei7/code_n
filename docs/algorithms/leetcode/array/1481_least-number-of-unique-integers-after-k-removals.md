# Least Number of Unique Integers after K Removals

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1481 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Sorting, Counting |
| Official Link | [least-number-of-unique-integers-after-k-removals](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/) |

## Problem Description & Examples
### Goal
Remove exactly `k` elements from the array so the number of distinct remaining integers is as small as possible.

### Function Contract
**Inputs**

- `arr`: a list of integers.
- `k`: number of elements to remove.

**Return value**

The minimum possible count of unique integers left.

### Examples
**Example 1**

- Input: `arr = [5,5,4], k = 1`
- Output: `1`

**Example 2**

- Input: `arr = [4,3,1,1,3,3,2], k = 3`
- Output: `2`

**Example 3**

- Input: `arr = [1,2,3], k = 2`
- Output: `1`

---

## Underlying Base Algorithm(s)
Frequency counting plus greedy removal. Remove values with the smallest frequencies first, because deleting all copies of one value reduces the unique count by one.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)` due to sorting frequencies.
- **Space Complexity**: `O(n)`
