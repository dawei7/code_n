# Avoid Flood in The City

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1488 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Greedy, Heap (Priority Queue) |
| Official Link | [avoid-flood-in-the-city](https://leetcode.com/problems/avoid-flood-in-the-city/) |

## Problem Description & Examples
### Goal
Schedule dry days to prevent any lake from raining while it is already full. On rainy days the action is fixed; on dry days choose one full lake to dry.

### Function Contract
**Inputs**

- `rains`: `rains[i] > 0` means lake `rains[i]` receives rain that day; `0` means a dry day.

**Return value**

An action array where rainy days are `-1` and dry days name a lake to dry, or an empty list if flooding is unavoidable.

### Examples
**Example 1**

- Input: `rains = [1,2,3,4]`
- Output: `[-1,-1,-1,-1]`

**Example 2**

- Input: `rains = [1,2,0,0,2,1]`
- Output: `[-1,-1,2,1,-1,-1]`

**Example 3**

- Input: `rains = [1,2,0,1,2]`
- Output: `[]`

---

## Underlying Base Algorithm(s)
Greedy scheduling with ordered dry-day lookup. Track the last rainy day for each full lake; when a lake rains again, assign the earliest unused dry day after its previous rain.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)` with a balanced ordered set; list plus binary search may require extra shifting.
- **Space Complexity**: `O(n)`
