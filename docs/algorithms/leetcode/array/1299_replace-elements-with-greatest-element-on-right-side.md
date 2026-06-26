# Replace Elements with Greatest Element on Right Side

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1299 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [replace-elements-with-greatest-element-on-right-side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/) |

## Problem Description & Examples
### Goal
Replace every element with the greatest element strictly to its right. The final element becomes `-1`.

### Function Contract
**Inputs**

- `arr`: integer array.

**Return value**

The transformed array.

### Examples
**Example 1**

- Input: `arr = [17,18,5,4,6,1]`
- Output: `[18,6,6,6,1,-1]`

**Example 2**

- Input: `arr = [400]`
- Output: `[-1]`

**Example 3**

- Input: `arr = [1,2,3]`
- Output: `[3,3,-1]`

---

## Underlying Base Algorithm(s)
Right-to-left suffix maximum scan.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` extra space if modifying in place.
