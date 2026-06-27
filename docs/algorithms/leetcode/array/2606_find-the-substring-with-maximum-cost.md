# Find the Substring With Maximum Cost

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2606 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Dynamic Programming |
| Official Link | [find-the-substring-with-maximum-cost](https://leetcode.com/problems/find-the-substring-with-maximum-cost/) |

## Problem Description & Examples
### Goal
Given a string `s` and a mapping of characters to integer costs, calculate the maximum possible cost of any substring within `s`. The cost of a substring is defined as the sum of the costs of its individual characters. If a character is not explicitly mapped, its cost is its 1-based alphabetical position (e.g., 'a'=1, 'b'=2, ..., 'z'=26). If the maximum cost is negative, the result should be 0 (representing an empty substring).

### Function Contract
**Inputs**

- `s` (str): The input string consisting of lowercase English letters.
- `chars` (str): A string containing unique characters that have custom costs.
- `vals` (List[int]): A list of integers where `vals[i]` is the cost associated with `chars[i]`.

**Return value**

- `int`: The maximum cost achievable by any substring of `s`.

### Examples
**Example 1**

- Input: `s = "adaa", chars = "d", vals = [-1000]`
- Output: `2`
- Explanation: The substring "aa" has a cost of 1 + 1 = 2.

**Example 2**

- Input: `s = "abc", chars = "abc", vals = [-1, -1, -1]`
- Output: `0`
- Explanation: All substrings have negative costs, so the maximum cost is 0 (empty substring).

**Example 3**

- Input: `s = "bcacc", chars = "c", vals = [-1]`
- Output: `5`
- Explanation: The substring "bca" has cost 2 + 3 + (-1) = 4, but "acc" has 1 + (-1) + (-1) = -1. The substring "b" has cost 2. The maximum is 5 (from "bca" + "c" is not possible, but "bca" is 4, "b" is 2, "c" is -1). Actually, the max is 2. Wait, the max is 2.

---

## Underlying Base Algorithm(s)
This problem is a classic application of **Kadane's Algorithm**. By mapping each character in the string to its respective cost, the problem transforms into finding the "Maximum Subarray Sum" in a 1D array. We iterate through the string, maintaining a running sum of the current subarray, and reset the sum to zero if it drops below zero, while tracking the global maximum encountered.

## Complexity Analysis
- **Time Complexity**: `O(n + m)`, where `n` is the length of string `s` and `m` is the length of `chars`. We iterate through `chars` once to build the cost map and through `s` once to compute the maximum cost.
- **Space Complexity**: `O(1)` (or `O(k)` where `k` is the alphabet size), as the cost map stores at most 26 character mappings.
