# Check if Any Element Has Prime Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3591 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Counting, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-any-element-has-prime-frequency/) |

## Problem Description

### Goal

Given an integer array `nums`, count how often each distinct value occurs. Determine whether at least one of those occurrence counts is a prime number.

The frequency of a value is its total number of appearances in the entire array. A frequency is prime only when it is greater than $1$ and has exactly two positive factors: $1$ and itself. Return `true` as soon as any distinct value satisfies that condition; return `false` when every frequency is non-prime.

### Function Contract

**Inputs**

- `nums`: An integer array with $1 \leq \lvert\texttt{nums}\rvert \leq 100$ and $0 \leq \texttt{nums[i]} \leq 100$.

**Return value**

Return `true` if some distinct element has a prime frequency, and `false` otherwise.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 4, 5, 4]`
- Output: `true`
- Explanation: The value `4` occurs twice, and $2$ is prime.

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `false`
- Explanation: Every value occurs once, and $1$ is not prime.

**Example 3**

- Input: `nums = [2, 2, 2, 4, 4]`
- Output: `true`
- Explanation: The frequencies are $3$ and $2$, both of which are prime.
