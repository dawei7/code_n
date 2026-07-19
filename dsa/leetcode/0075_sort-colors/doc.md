# Sort Colors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 75 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-colors/) |

## Problem Description
### Goal
An array `nums` contains only the values `0`, `1`, and `2`, representing red, white, and blue. Sort the colors so all zeroes come first, followed by all ones and then all twos, while preserving the number of occurrences of each value.

The native method must modify the array in place, make one pass, and avoid a library sorting routine; it returns no value. The app adapter returns the same mutated array for inspection. Inputs of one color or one element remain unchanged apart from satisfying the same ordering.

### Function Contract
**Inputs**

- `nums`: a nonempty `List[int]` containing only 0, 1, and 2

**Return value**

The sorted array in the app; LeetCode's `sortColors` method returns nothing.

### Examples
**Example 1**

- Input: `nums = [2,0,2,1,1,0]`
- Output: `[0,0,1,1,2,2]`

**Example 2**

- Input: `nums = [2,0,1]`
- Output: `[0,1,2]`

**Example 3**

- Input: `nums = [1]`
- Output: `[1]`
