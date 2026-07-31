# Maximum Number of Subsequences After One Inserting

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3628 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming, Greedy, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/) |

## Problem Description
### Goal

You are given a string `s` made of uppercase English letters. You may insert at most one uppercase English letter at any position, including before the first character or after the last character.

After that optional insertion, count the subsequences equal to `"LCT"`. A subsequence keeps the original relative order of its chosen characters but does not require them to be adjacent. Return the largest possible number of `"LCT"` subsequences obtainable by choosing the inserted letter and its position optimally.

### Function Contract
**Inputs**

- `s`: A string of length $n$, where $1 \le n \le 10^5$, containing only uppercase English letters.

**Return value**

Return the maximum number of `"LCT"` subsequences after inserting at most one uppercase letter.

### Examples
**Example 1**

- Input: `s = "LMCT"`
- Output: `2`
- Explanation: Insert `"L"` at the beginning so either L can begin the subsequence.

**Example 2**

- Input: `s = "LCCT"`
- Output: `4`
- Explanation: Inserting another `"L"` at the beginning creates two choices for L and two for C.

**Example 3**

- Input: `s = "L"`
- Output: `0`
- Explanation: One inserted character is insufficient to form all three required letters.
