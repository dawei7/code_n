# How Many Numbers Are Smaller Than the Current Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1365 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Sorting, Counting Sort |
| Official Link | [how-many-numbers-are-smaller-than-the-current-number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) |

## Problem Description & Examples
### Goal
For each number in the input, count how many elements in the same array are strictly smaller than it.

### Function Contract
**Inputs**

- `nums`: a list of integers.

**Return value**

A list where each position contains the smaller-element count for the corresponding input value.

### Examples
**Example 1**

- Input: `nums = [8,1,2,2,3]`
- Output: `[4,0,1,1,3]`

**Example 2**

- Input: `nums = [6,5,4,8]`
- Output: `[2,1,0,3]`

**Example 3**

- Input: `nums = [7,7,7]`
- Output: `[0,0,0]`

---

## Underlying Base Algorithm(s)
Frequency prefix counts for bounded values, or sorting with rank assignment. The counting approach accumulates how many numbers occur below each value and answers each position by lookup.

---

## Complexity Analysis
- **Time Complexity**: `O(n + U)` where `U` is the value range; sorting alternative is `O(n log n)`.
- **Space Complexity**: `O(U)` for counting or `O(n)` for sorting metadata.
