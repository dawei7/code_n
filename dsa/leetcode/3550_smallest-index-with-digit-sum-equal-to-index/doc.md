# Smallest Index With Digit Sum Equal to Index

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3550 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/) |

## Problem Description

### Goal

Given an array `nums` of nonnegative integers, inspect each position using zero-based indexing. A position $i$ qualifies when adding the decimal digits of the value stored at that position, `nums[i]`, produces exactly $i$.

Return the smallest qualifying index. If no array element has a digit sum equal to its own index, return `-1`. The digits of the array value are summed; the condition does not ask for the digit sum of the index itself.

### Function Contract

**Inputs**

- `nums`: A nonempty array of integers.

The constraints are $1 \le \lvert\texttt{nums}\rvert \le 100$ and $0 \le \texttt{nums[i]} \le 1000$.

**Return value**

Return the smallest index `i` satisfying `digit_sum(nums[i]) == i`, or `-1` if no such index exists.

### Examples

**Example 1**

- Input: `nums = [1,3,2]`
- Output: `2`
- Explanation: The value at index `2` is `2`, whose digit sum is also $2$.

**Example 2**

- Input: `nums = [1,10,11]`
- Output: `1`
- Explanation: Values at indices `1` and `2` have digit sums $1$ and $2$ respectively, so the smaller qualifying index is `1`.

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `-1`
- Explanation: None of the three stored values has a digit sum equal to its position.

---
