# Split With Minimum Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2578 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Split With Minimum Sum](https://leetcode.com/problems/split-with-minimum-sum/) |

## Problem Description

### Goal

Given a positive integer `num`, redistribute all of its decimal digits between two non-negative integers `num1` and `num2`. Across the two results, every digit must occur exactly as many times as it does in `num`; their digit order does not need to match the original order.

Either constructed integer may contain leading zeroes. The input itself has no leading zeroes.

Return the minimum possible value of `num1 + num2`.

### Function Contract

**Inputs**

- `num`: A positive integer satisfying $10 \leq \texttt{num} \leq 10^9$.

Let $d$ be the number of decimal digits in `num`, so $2 \leq d \leq 10$.

**Return value**

- The smallest sum obtainable by distributing every digit of `num` between two non-negative integers.

### Examples

**Example 1**

- Input: `num = 4325`
- Output: `59`
- Explanation: The digits can form `24` and `35`, whose sum is $59$.

**Example 2**

- Input: `num = 687`
- Output: `75`
- Explanation: The digits can form `68` and `7`, whose sum is $75$.
