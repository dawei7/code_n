# Clear Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3174 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Stack, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/clear-digits/) |

## Problem Description

### Goal

You are given a string `s`. Repeatedly locate the first digit still present, then delete that digit together with the closest non-digit character to its left. Continue until the string contains no digits, and return the remaining characters in their original relative order.

The operation cannot be applied when a digit has no non-digit character to its left. Every input is generated so that all digits can be removed successfully, which means each encountered deletion has an eligible character available.

### Function Contract

**Inputs**

- `s`: A string of length $n$, where $1 \le n \le 100$, containing only lowercase English letters and decimal digits.

The input guarantees that repeated legal operations can delete every digit.

**Return value**

- The string left after all digits and their paired non-digit characters have been removed.

### Examples

#### Example 1

- **Input:** `s = "abc"`
- **Output:** `"abc"`
- **Explanation:** The string contains no digit, so no operation is performed.

#### Example 2

- **Input:** `s = "cb34"`
- **Output:** `""`
- **Explanation:** Removing `3` with the closest letter `b` leaves `"c4"`; removing `4` with `c` then leaves the empty string.
