# Get the Maximum Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1537 |
| Difficulty | Hard |
| Topics | Array, Two Pointers, Dynamic Programming, Greedy |
| Official Link | [get-the-maximum-score](https://leetcode.com/problems/get-the-maximum-score/) |

## Problem Description & Examples
### Goal
Walk through two strictly increasing arrays, switching from one array to the
other only at shared values, and maximize the sum of visited values.

### Function Contract
**Inputs**

- `nums1`: the first strictly increasing array.
- `nums2`: the second strictly increasing array.

**Return value**

The maximum score modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `nums1 = [2, 4, 5, 8, 10], nums2 = [4, 6, 8, 9]`
- Output: `30`

**Example 2**

- Input: `nums1 = [1, 3, 5, 7, 9], nums2 = [3, 5, 100]`
- Output: `109`

**Example 3**

- Input: `nums1 = [1, 2, 3, 4, 5], nums2 = [6, 7, 8, 9, 10]`
- Output: `40`

---

## Underlying Base Algorithm(s)
Use two pointers and accumulate segment sums between common values. When a common
value is reached, add the larger of the two segment sums plus the shared value,
then reset both segment sums. After the scan, add the larger remaining segment.

---

## Complexity Analysis
- **Time Complexity**: `O(n + m)`.
- **Space Complexity**: `O(1)`.
