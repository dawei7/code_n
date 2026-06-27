# Find the Length of the Longest Common Prefix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3043 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Trie |
| Official Link | [find-the-length-of-the-longest-common-prefix](https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/) |

## Problem Description & Examples
### Goal
Given two arrays of positive integers, identify the length of the longest prefix shared by any integer from the first array and any integer from the second array. A prefix is defined as the leading sequence of digits of an integer.

### Function Contract
**Inputs**

- `arr1`: A list of positive integers.
- `arr2`: A list of positive integers.

**Return value**

- An integer representing the maximum length of a common prefix found between any pair of numbers $(x, y)$ where $x \in arr1$ and $y \in arr2$. If no common prefix exists, return 0.

### Examples
**Example 1**

- Input: `arr1 = [1, 10, 100], arr2 = [1000]`
- Output: `3`
- Explanation: The longest common prefix is "100", which has length 3.

**Example 2**

- Input: `arr1 = [1, 2, 3], arr2 = [4, 5, 6]`
- Output: `0`
- Explanation: No common prefixes exist.

**Example 3**

- Input: `arr1 = [12, 34, 56], arr2 = [123, 456]`
- Output: `2`
- Explanation: The longest common prefix is "12", which has length 2.

---

## Underlying Base Algorithm(s)
The problem is efficiently solved using a **Hash Set** to store all possible prefixes of numbers in the first array. By iterating through each number in `arr1` and generating all its prefixes, we can perform $O(1)$ lookups. We then iterate through `arr2`, generate its prefixes, and check for existence in the set to find the maximum length.

---

## Complexity Analysis
- **Time Complexity**: $O(N \cdot L + M \cdot L)$, where $N$ and $M$ are the lengths of `arr1` and `arr2` respectively, and $L$ is the maximum number of digits in an integer (at most 10).
- **Space Complexity**: $O(N \cdot L)$ to store the prefixes of all numbers in `arr1` in the hash set.
