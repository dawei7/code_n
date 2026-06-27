# Find the Maximum Number of Marked Indices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2576 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Greedy, Sorting |
| Official Link | [find-the-maximum-number-of-marked-indices](https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/) |

## Problem Description & Examples
### Goal
Given an array of non-negative integers, determine the maximum number of indices that can be "marked." An index `i` can be marked if there exists another index `j` such that `i != j` and `2 * nums[i] <= nums[j]`. Each index can be used in at most one marking pair.

### Function Contract
**Inputs**

- `nums`: A list of non-negative integers.

**Return value**

- An integer representing the maximum total count of marked indices.

### Examples
**Example 1**

- Input: `nums = [3, 5, 2, 4]`
- Output: `2`
- Explanation: We can mark index 2 (value 2) and index 0 (value 3) because 2 * 2 <= 3 is false, but 2 * 2 <= 4 is true. We mark indices 2 and 3.

**Example 2**

- Input: `nums = [9, 2, 5, 4]`
- Output: `4`
- Explanation: We can pair (2, 4) and (5, 9). All 4 indices are marked.

**Example 3**

- Input: `nums = [7, 6, 8]`
- Output: `0`
- Explanation: No pair satisfies the condition.

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach combined with Two Pointers**. By sorting the array, we can optimally pair the smallest available elements with the smallest possible valid larger elements. We split the sorted array into two halves: the first half (potential "small" elements) and the second half (potential "large" elements). We iterate through the first half and attempt to match each element with the smallest available element in the second half that satisfies the condition.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)` due to the initial sorting of the input array, where `n` is the length of `nums`. The two-pointer traversal takes `O(n)`.
- **Space Complexity**: `O(1)` or `O(n)` depending on the sorting implementation's space requirements.
