# Find Anagram Mappings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 760 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-anagram-mappings/) |

## Problem Description

### Goal

Given integer arrays `nums1` and `nums2` containing the same values with the same multiplicities, construct an index mapping from the first array into the second.

For every index `i` in `nums1`, choose an index `j` such that `nums1[i] = nums2[j]`, and return all chosen `j` values in first-array order. When a value occurs more than once, any occurrence with that value is an acceptable mapping; the problem does not require a unique assignment among duplicates.

### Function Contract

**Inputs**

- `nums1`: the source integer array.
- `nums2`: an anagram of `nums1`, possibly with duplicate values.

**Return value**

- A list `mapping` of the same length where `nums1[i] = nums2[mapping[i]]` for every index `i`.

### Examples

**Example 1**

- Input: `nums1 = [12,28,46,32,50]`, `nums2 = [50,12,32,46,28]`
- Output: `[1,4,3,2,0]`
- Explanation: Each returned index locates the corresponding value from `nums1` in `nums2`.

**Example 2**

- Input: `nums1 = [1,2,1]`, `nums2 = [1,1,2]`
- Output: `[1,2,1]`
- Explanation: Either index `0` or `1` is valid for either occurrence of value `1`, so other valid mappings exist.
