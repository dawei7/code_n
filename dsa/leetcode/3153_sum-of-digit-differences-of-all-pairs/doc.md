# Sum of Digit Differences of All Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3153 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers, and every value has the same number of decimal digits. For two values, their **digit difference** is the number of positions where the digits are unequal. Positions are compared directly: units with units, tens with tens, and so on.

Consider every unordered pair of distinct array positions. Return the sum of the digit differences for all those pairs. Equal values and repeated values remain separate array elements, although a pair of equal values contributes zero.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $2 \le n \le 10^5$, $1 \le \texttt{nums[i]} < 10^9$, and every value has the same digit count $D$.

**Return value**

Return the sum, over every pair of indices $i<j$, of the number of digit positions at which `nums[i]` and `nums[j]` differ.

### Examples

#### Example 1

- **Input:** `nums = [13,23,12]`
- **Output:** `4`
- **Explanation:** The three pairwise digit differences are $1$, $1$, and $2$, which sum to $4$.

#### Example 2

- **Input:** `nums = [10,10,10,10]`
- **Output:** `0`
- **Explanation:** Every pair contains identical values, so no digit position differs.

#### Example 3

- **Input:** `nums = [1,2,3,1]`
- **Output:** `5`
- **Explanation:** Five of the six unordered pairs contain different one-digit values.
