# Find the XOR of Numbers Which Appear Twice

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3158 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/) |

## Problem Description

### Goal

You are given an integer array `nums` in which every distinct value occurs either once or twice. Classify each value by its total frequency in the complete array. Values with one occurrence do not contribute to the result, while each value with two occurrences contributes that value once; the two copies are not XORed separately.

Return the bitwise XOR of all values selected by that rule. Their positions and encounter order do not change the result. When every value is unique, the selected set is empty, so return $0$.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1 \le n \le 50$ and $1 \le \texttt{nums[i]} \le 50$. Every distinct value appears once or twice.

**Return value**

Return the bitwise XOR of all distinct values that appear twice, or $0$ if no value appears twice.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 1, 3]`
- **Output:** `1`
- **Explanation:** Only `1` appears twice.

#### Example 2

- **Input:** `nums = [1, 2, 3]`
- **Output:** `0`
- **Explanation:** Every value appears once.

#### Example 3

- **Input:** `nums = [1, 2, 2, 1]`
- **Output:** `3`
- **Explanation:** The repeated values are `1` and `2`, and `1 ^ 2` equals `3`.
