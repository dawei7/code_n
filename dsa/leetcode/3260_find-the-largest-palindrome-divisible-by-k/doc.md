# Find the Largest Palindrome Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3260 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Dynamic Programming, Greedy, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/) |

## Problem Description

### Goal

An integer is $k$-palindromic when its decimal representation reads identically from left to right and right to left, and its value is divisible by \`k\`. Given the positive integers \`n\` and \`k\`, find the greatest $k$-palindromic integer whose decimal representation has exactly \`n\` digits.

Return that integer as a string so lengths up to $10^5$ are representable. Its first digit must be nonzero; leading zeroes cannot be used to pad a shorter palindrome to the requested length.

### Function Contract

**Inputs**

- \`n\`: The required number of decimal digits, where $1 \le n \le 10^5$.
- \`k\`: The divisor, where $1 \le k \le 9$.

**Return value**

- The lexicographically and numerically largest length-$n$ decimal palindrome with no leading zero whose remainder modulo $k$ is zero.

### Examples

#### Example 1

- **Input:** \`n = 3, k = 5\`
- **Output:** \`"595"\`

Among three-digit palindromes divisible by 5, 595 is the largest.

#### Example 2

- **Input:** \`n = 1, k = 4\`
- **Output:** \`"8"\`

The valid one-digit choices are 4 and 8.

#### Example 3

- **Input:** \`n = 5, k = 6\`
- **Output:** \`"89898"\`

The result is palindromic and divisible by both 2 and 3.
