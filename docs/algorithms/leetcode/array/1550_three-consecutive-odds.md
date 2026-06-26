# Three Consecutive Odds

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1550 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [three-consecutive-odds](https://leetcode.com/problems/three-consecutive-odds/) |

## Problem Description & Examples
### Goal
Determine whether the array contains three odd numbers in a row.

### Function Contract
**Inputs**

- `arr`: an integer array.

**Return value**

`true` if there are three consecutive odd elements; otherwise `false`.

### Examples
**Example 1**

- Input: `arr = [2, 6, 4, 1]`
- Output: `false`

**Example 2**

- Input: `arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]`
- Output: `true`

**Example 3**

- Input: `arr = [1, 3, 5]`
- Output: `true`

---

## Underlying Base Algorithm(s)
Scan once while keeping a streak count of consecutive odd values. Reset the
streak on an even value and return true as soon as the streak reaches three.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(1)`.
