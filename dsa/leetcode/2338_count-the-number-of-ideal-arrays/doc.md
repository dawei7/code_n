# Count the Number of Ideal Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2338 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Combinatorics, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-ideal-arrays/) |

## Problem Description

### Goal

An ideal array is a 0-indexed integer array `arr` of length `n`. Every entry
must lie between 1 and `maxValue`, inclusive. In addition, each entry after the
first must be divisible by the entry immediately before it: for every
$1 \le i < n$, `arr[i]` is divisible by `arr[i - 1]`.

Count the distinct ideal arrays satisfying both rules. Equal adjacent values
are allowed because every positive integer divides itself. Since the number of
arrays can be large, return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: The array length, where $2 \le n \le 10^4$.
- `maxValue`: The inclusive upper bound for every entry, where
  $1 \le \texttt{maxValue} \le 10^4$.

**Return value**

The number of distinct length-`n` ideal arrays, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `n = 2`, `maxValue = 5`
- **Output:** `10`
- **Explanation:** There are five arrays beginning with 1, two beginning with 2,
  and one beginning with each of 3, 4, and 5.

#### Example 2

- **Input:** `n = 5`, `maxValue = 3`
- **Output:** `11`
- **Explanation:** Nine valid arrays begin with 1; the constant all-2 and all-3
  arrays contribute the other two.
