# Create Maximum Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 321 |
| Difficulty | Hard |
| Topics | Array, Two Pointers, Stack, Greedy, Monotonic Stack |
| Official Link | [create-maximum-number](https://leetcode.com/problems/create-maximum-number/) |

## Problem Description & Examples
### Goal
Given two arrays of digits representing two separate numbers, select a total of `k` digits from both arrays while maintaining the relative order of digits from their original sources. The objective is to construct the largest possible number (represented as a list of digits) that can be formed by merging these selected digits.

### Function Contract
**Inputs**

- `nums1`: A list of integers representing the first sequence of digits.
- `nums2`: A list of integers representing the second sequence of digits.
- `k`: An integer representing the total number of digits to select and merge.

**Return value**

- A list of integers representing the digits of the largest possible number of length `k`.

### Examples
**Example 1**

- Input: `nums1 = [3, 4, 6, 5], nums2 = [9, 1, 2, 5, 8, 3], k = 5`
- Output: `[9, 8, 6, 5, 3]`

**Example 2**

- Input: `nums1 = [6, 7], nums2 = [6, 0, 4], k = 5`
- Output: `[6, 7, 6, 0, 4]`

**Example 3**

- Input: `nums1 = [3, 9], nums2 = [8, 9], k = 3`
- Output: `[9, 8, 9]`

---

## Underlying Base Algorithm(s)
The problem is solved by decomposing it into three sub-problems:
1. **Monotonic Stack**: For a single array, find the largest subsequence of length `i` by maintaining a decreasing stack. If the current digit is larger than the stack top and we have enough remaining digits to reach length `i`, we pop the stack.
2. **Merge Strategy**: Given two sequences, merge them into the largest possible sequence by comparing the sequences lexicographically at each step (greedy choice).
3. **Brute Force Combination**: Iterate through all possible counts `i` (where `0 <= i <= k`) to take from `nums1`, and `k-i` from `nums2`, then find the maximum result among all valid combinations.

---

## Complexity Analysis
- **Time Complexity**: `O(k * (n + m + k))`, where `n` and `m` are the lengths of `nums1` and `nums2`. Generating subsequences takes `O(n+m)`, and merging takes `O(k^2)`. Since we iterate `k` times, the complexity is dominated by the merge and subsequence generation.
- **Space Complexity**: `O(n + m + k)` to store the intermediate subsequences and the final result.
