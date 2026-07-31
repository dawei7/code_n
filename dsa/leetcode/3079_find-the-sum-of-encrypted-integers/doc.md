# Find the Sum of Encrypted Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3079 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-sum-of-encrypted-integers/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers. Define the encryption of a number $x$ by finding the largest digit that occurs in $x$ and replacing every digit of $x$ with that largest digit. The number of digits does not change. For example, `523` encrypts to `555`, while `213` encrypts to `333`.

Encrypt every element of `nums` independently, then return the sum of all the encrypted values.

### Function Contract

**Inputs**

- `nums`: A list of positive integers.

The list length satisfies $1 \leq \lvert\texttt{nums}\rvert \leq 50$, and every value satisfies $1 \leq \texttt{nums[i]} \leq 1000$.

Let $d_i$ be the number of decimal digits in `nums[i]`, and define

$$
D = \sum_i d_i.
$$

**Return value**

- The sum of the encrypted values of all elements in `nums`.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `6`
- Explanation: Each one-digit value is unchanged, so the encrypted values are `[1, 2, 3]` and their sum is `6`.

**Example 2**

- Input: `nums = [10, 21, 31]`
- Output: `66`
- Explanation: The encrypted values are `[11, 22, 33]`, whose sum is `66`.
