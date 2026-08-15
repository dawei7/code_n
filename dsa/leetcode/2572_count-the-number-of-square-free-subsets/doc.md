# Count the Number of Square-Free Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2572 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Bit Manipulation, Number Theory, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Count the Number of Square-Free Subsets](https://leetcode.com/problems/count-the-number-of-square-free-subsets/) |

## Problem Description

### Goal

You are given a 0-indexed array `nums` of positive integers. A subset is square-free when the product of its selected elements is not divisible by any perfect square greater than $1$. Equivalently, no prime may occur more than once across the combined prime factorizations of the selected values.

Count the non-empty square-free subsets of `nums`. Subsets are distinguished by their selected indices, so equal values at different positions represent different choices. Return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers satisfying $1 \le n \le 1000$ and $1 \le \texttt{nums[i]} \le 30$.

**Return value**

Return the number of non-empty index subsets whose element product is square-free, modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `nums = [3, 4, 4, 5]`
- **Output:** `3`
- **Explanation:** The valid index subsets produce `[3]`, `[5]`, and `[3, 5]`. Each `4` already contains the square factor $2^2$.

#### Example 2

- **Input:** `nums = [1]`
- **Output:** `1`
- **Explanation:** The single selected value has product $1$, which is square-free.

#### Example 3

- **Input:** `nums = [2, 3, 5]`
- **Output:** `7`
- **Explanation:** The values have distinct prime factors, so every non-empty subset is valid.
