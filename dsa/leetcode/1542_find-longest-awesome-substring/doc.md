# Find Longest Awesome Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1542 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-longest-awesome-substring/) |

## Problem Description
### Goal
You are given a nonempty string `s` consisting only of decimal digits. A substring is called awesome when its characters can be rearranged, using any number of swaps, to form a palindrome. The chosen characters must occupy one contiguous interval in the original string, but their order within that interval does not need to be preserved.

Return the maximum length of an awesome substring. A digit's identity matters only through how many times it occurs in the interval: every count must be even for an even-length palindrome, while an odd-length palindrome may have exactly one digit with an odd count. Any single character is therefore awesome.

### Function Contract
**Inputs**

- `s`: a digit string of length $n$, where $1 \le n \le 10^5$.

**Return value**

The greatest length of a contiguous substring whose digits can be permuted into a palindrome.

### Examples
**Example 1**

- Input: `s = "3242415"`
- Output: `5`
- Explanation: The substring `"24241"` can be rearranged as `"24142"`.

**Example 2**

- Input: `s = "12345678"`
- Output: `1`
- Explanation: Every longer substring contains multiple digits with odd frequency.

**Example 3**

- Input: `s = "213123"`
- Output: `6`
- Explanation: The whole string can be rearranged into a palindrome such as `"231132"`.
