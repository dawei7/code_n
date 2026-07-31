# Largest Palindromic Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2384 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-palindromic-number/) |

## Problem Description

### Goal

Given a nonempty string `num` containing only decimal digits, select at least one of its digits and reorder the selected digits to form a palindrome. Each occurrence in the result must come from a distinct occurrence in `num`, but not every available digit has to be used.

Return the numerically largest palindromic integer that can be formed, represented as a string. A multi-digit result must not begin with `'0'`; therefore it cannot gain length merely by placing unused zeroes outside all nonzero digits. Repeated occurrences are significant, and a digit may occupy the center without a matching partner.

### Function Contract

**Inputs**

- `num`: A string of $n$ decimal digits, where $1 \le n \le 10^5$.

**Return value**

- Return the string representation of the largest valid palindromic integer.

**Construction rules**

- Digits may be reordered, and any subset containing at least one occurrence may be used.
- Every digit used outside the center requires a matching occurrence on the opposite side.
- The result has no leading zeroes unless the entire result is the single digit `"0"`.

### Examples

**Example 1**

- Input: `num = "444947137"`
- Output: `"7449447"`
- Explanation: The selected digits can be arranged with outer sevens, then fours, and a central nine.

**Example 2**

- Input: `num = "00009"`
- Output: `"9"`
- Explanation: Surrounding the nine with zeroes would create a leading zero, so the largest valid palindrome uses only the nine.
