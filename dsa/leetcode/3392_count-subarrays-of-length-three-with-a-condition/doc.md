# Count Subarrays of Length Three With a Condition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3392 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/) |

## Problem Description

### Goal

Given an integer array `nums`, examine every contiguous subarray containing exactly three elements. A triplet is valid when the sum of its first and third values is exactly half of its middle value.

Count all valid length-three subarrays. Neighboring candidates overlap, so each possible starting index from zero through `len(nums) - 3` must be evaluated independently. The array may contain positive values, negative values, and zero.

### Function Contract

**Inputs**

- `nums`: A list of integers with length $n$, where $3\le n\le100$ and every value lies between $-100$ and $100$ inclusive.

**Return value**

- The number of indices $i$ for which the triplet `nums[i:i + 3]` satisfies

$$
2\bigl(\texttt{nums[i]}+\texttt{nums[i + 2]}\bigr)=\texttt{nums[i + 1]}.
$$

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 1, 4, 1]`
- **Output:** `1`

Only `[1, 4, 1]` is valid: the two endpoint values sum to 2, exactly half of the middle value 4.

#### Example 2

- **Input:** `nums = [1, 1, 1]`
- **Output:** `0`

The only triplet has endpoint sum 2, which is not half of its middle value 1.
