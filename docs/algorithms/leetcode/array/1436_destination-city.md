# Destination City

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1436 |
| Difficulty | Easy |
| Topics | Array, Hash Table, String |
| Official Link | [destination-city](https://leetcode.com/problems/destination-city/) |

## Problem Description & Examples
### Goal
Given directed travel paths, find the city that never appears as a starting city. The path chain has exactly one such destination.

### Function Contract
**Inputs**

- `paths`: a list of `[fromCity, toCity]` directed paths.

**Return value**

The final destination city name.

### Examples
**Example 1**

- Input: `paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]`
- Output: `"Sao Paulo"`

**Example 2**

- Input: `paths = [["B","C"],["D","B"],["C","A"]]`
- Output: `"A"`

**Example 3**

- Input: `paths = [["A","Z"]]`
- Output: `"Z"`

---

## Underlying Base Algorithm(s)
Set difference. Collect all starting cities, then return the destination city that is not in that set.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
