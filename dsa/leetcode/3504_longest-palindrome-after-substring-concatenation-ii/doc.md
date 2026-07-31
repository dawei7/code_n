# Longest Palindrome After Substring Concatenation II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3504 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Two Pointers, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/) |

## Problem Description

### Goal

Given lowercase strings `s` and `t`, select one contiguous substring from `s` and one contiguous substring from `t`. Either selection may be empty. Form a new string by placing the chosen part of `s` before the chosen part of `t`; the two inputs cannot be swapped or internally reordered.

Return the maximum possible length when the resulting concatenation is a palindrome. The optimum may combine both inputs, or it may be a palindromic substring lying wholly within one input while the other contributes nothing. The larger limits require avoiding explicit enumeration of all substring pairs.

### Function Contract

**Inputs**

- `s`: A nonempty lowercase English string of length $n$.
- `t`: A nonempty lowercase English string of length $m$.

The constraints are $1 \le n,m \le 1000$.

**Return value**

Return the greatest length of any palindrome representable as `s[i:j] + t[k:l]`, allowing either slice to be empty.

### Examples

**Example 1**

- Input: `s = "a", t = "a"`
- Output: `2`
- Explanation: The two one-character selections form `"aa"`.

**Example 2**

- Input: `s = "abc", t = "def"`
- Output: `1`
- Explanation: No cross-string pair matches, but every individual character is palindromic.

**Example 3**

- Input: `s = "b", t = "aaaa"`
- Output: `4`
- Explanation: Select an empty substring from `s` and all of `t`.

**Example 4**

- Input: `s = "abcde", t = "ecdba"`
- Output: `5`
- Explanation: Choosing `"abc"` and `"ba"` produces `"abcba"`.
