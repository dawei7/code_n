# Create Target Array in the Given Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1389 |
| Difficulty | Easy |
| Topics | Array, Simulation |
| Official Link | [create-target-array-in-the-given-order](https://leetcode.com/problems/create-target-array-in-the-given-order/) |

## Problem Description & Examples
### Goal
Build a target array from left to right. At step `i`, insert `nums[i]` at position `index[i]` in the current target array.

### Function Contract
**Inputs**

- `nums`: values to insert.
- `index`: insertion positions for the corresponding values.

**Return value**

The final target array after all insertions.

### Examples
**Example 1**

- Input: `nums = [0,1,2,3,4], index = [0,1,2,2,1]`
- Output: `[0,4,1,3,2]`

**Example 2**

- Input: `nums = [1,2,3,4,0], index = [0,1,2,3,0]`
- Output: `[0,1,2,3,4]`

**Example 3**

- Input: `nums = [1], index = [0]`
- Output: `[1]`

---

## Underlying Base Algorithm(s)
Simulation with list insertion. Process pairs in order and insert each value at its requested position.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)` because middle insertions shift existing elements.
- **Space Complexity**: `O(n)`
