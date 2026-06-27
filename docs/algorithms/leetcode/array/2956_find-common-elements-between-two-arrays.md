# Find Common Elements Between Two Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2956 |
| Difficulty | Easy |
| Topics | Array, Hash Table |
| Official Link | [find-common-elements-between-two-arrays](https://leetcode.com/problems/find-common-elements-between-two-arrays/) |

## Problem Description & Examples
### Goal
Given two integer arrays, determine how many elements from the first array exist in the second array, and conversely, how many elements from the second array exist in the first array. The result should be a pair of counts representing these two values.

### Function Contract
**Inputs**

- `nums1`: A list of integers.
- `nums2`: A list of integers.

**Return value**

- A list of two integers `[count1, count2]`, where `count1` is the number of indices `i` such that `nums1[i]` exists in `nums2`, and `count2` is the number of indices `j` such that `nums2[j]` exists in `nums1`.

### Examples
**Example 1**

- Input: `nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]`
- Output: `[3,4]`

**Example 2**

- Input: `nums1 = [3,4,2,3], nums2 = [1,5]`
- Output: `[0,0]`

**Example 3**

- Input: `nums1 = [1,1], nums2 = [1,1]`
- Output: `[2,2]`

---

## Underlying Base Algorithm(s)
The problem is solved using Hash Sets for O(1) average-time complexity lookups. By converting both input arrays into sets, we can iterate through each array once and check for the existence of each element in the set representation of the other array.

---

## Complexity Analysis
- **Time Complexity**: O(N + M), where N is the length of `nums1` and M is the length of `nums2`. We iterate through each array once to build sets and once to count occurrences.
- **Space Complexity**: O(N + M) to store the unique elements of both arrays in hash sets.
