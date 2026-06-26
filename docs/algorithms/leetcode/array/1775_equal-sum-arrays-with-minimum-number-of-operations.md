# Equal Sum Arrays With Minimum Number of Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1775 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Counting |
| Official Link | [equal-sum-arrays-with-minimum-number-of-operations](https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/) |

## Problem Description & Examples
### Goal
Two arrays contain values from `1` to `6`. In one operation, change any one value in either array to another value from `1` to `6`. Find the fewest operations needed to make the two array sums equal.

### Function Contract
**Inputs**

- `nums1`: the first array of dice-like values.
- `nums2`: the second array of dice-like values.

**Return value**

Return the minimum number of operations, or `-1` if equal sums are impossible.

### Examples
**Example 1**

- Input: `nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]`
- Output: `3`

**Example 2**

- Input: `nums1 = [1,1,1,1,1,1,1], nums2 = [6]`
- Output: `-1`

**Example 3**

- Input: `nums1 = [6,6], nums2 = [1]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Compare the sums. Each element in the smaller-sum array can increase by `6 - value`, and each element in the larger-sum array can decrease by `value - 1`. Count how many changes of each possible gain `1..5` are available, then greedily apply the largest gains until the sum gap is closed.

---

## Complexity Analysis
- **Time Complexity**: `O(n + m)`
- **Space Complexity**: `O(1)`
