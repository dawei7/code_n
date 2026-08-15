# Remove Trailing Zeros From a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2710 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/remove-trailing-zeros-from-a-string/) |

## Problem Description

### Goal

A positive integer is provided as its decimal string `num`. Remove every consecutive `'0'` character at the end of the representation and return the remaining digits as a string.

Zeros elsewhere in the number must remain unchanged. If the final digit is already nonzero, return the same sequence of digits. Because the input represents a positive integer and has no leading zeros, at least one nonzero digit remains after the trailing suffix is removed.

### Function Contract

**Inputs**

- `num`: A digit-only string of length $n$, where $1 \le n \le 1000$, representing a positive integer without leading zeros.

**Return value**

Return the prefix ending at the last nonzero digit of `num`.

### Examples

#### Example 1

- **Input:** `num = "51230100"`
- **Output:** `"512301"`
- **Explanation:** Exactly two zeros form the trailing suffix; the interior zero remains.

#### Example 2

- **Input:** `num = "123"`
- **Output:** `"123"`
- **Explanation:** The string already ends with a nonzero digit.

#### Example 3

- **Input:** `num = "1000"`
- **Output:** `"1"`
- **Explanation:** Removing the three trailing zeros leaves the first digit.
