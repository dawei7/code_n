# Bitwise OR of Adjacent Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3173 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/bitwise-or-of-adjacent-elements/) |

## Problem Description

### Goal

Given an integer array `nums` of length $n$, construct a new array with one entry for every adjacent pair in `nums`.

For each index $i$ from $0$ through $n-2$, set `answer[i] = nums[i] | nums[i + 1]`, where `|` denotes bitwise OR. Return the resulting array of length $n-1$.

Consecutive output positions come from overlapping pairs: an interior value of `nums` participates once as the right member of a pair and once as the left member of the next pair. Each pair is evaluated independently, and its result remains in the same left-to-right order as that pair in the input.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers satisfying $2 \le n \le 100$ and $0 \le \texttt{nums[i]} \le 100$.

**Return value**

- A list `answer` of length $n-1$ in which `answer[i]` is the bitwise OR of the two consecutive values `nums[i]` and `nums[i + 1]`.

### Examples

#### Example 1

- **Input:** `nums = [1, 3, 7, 15]`
- **Output:** `[3, 7, 15]`
- **Explanation:** The adjacent OR values are `1 | 3 = 3`, `3 | 7 = 7`, and `7 | 15 = 15`.

#### Example 2

- **Input:** `nums = [8, 4, 2]`
- **Output:** `[12, 6]`
- **Explanation:** The two adjacent pairs produce `8 | 4 = 12` and `4 | 2 = 6`.

#### Example 3

- **Input:** `nums = [5, 4, 9, 11]`
- **Output:** `[5, 13, 11]`
- **Explanation:** Apply bitwise OR independently to each consecutive pair.
