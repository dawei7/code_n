# Number of Subarrays Having Even Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2495 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-subarrays-having-even-product/) |

## Problem Description

### Goal

Given a 0-indexed integer array `nums`, count its non-empty contiguous subarrays whose element product is even.

The product itself may become extremely large, but only its parity matters: a product is even exactly when at least one selected element is even. Return the total number of subarrays satisfying that condition.

A subarray must use consecutive positions and contain at least one element; selecting scattered values or the empty range does not count. Each distinct pair of start and end indices defines a separate subarray, even when its values match another range.

### Function Contract

**Inputs**

- `nums`: A list of positive integers, with $1 \leq \lvert\texttt{nums}\rvert \leq 10^5$ and $1 \leq \texttt{nums[i]} \leq 10^5$.

**Return value**

Return an integer equal to the number of non-empty contiguous subarrays of `nums` having an even product.

### Examples

#### Example 1

- **Input:** `nums = [9, 6, 7, 13]`
- **Output:** `6`
- **Explanation:** Exactly the subarrays containing the value `6` have even products.

#### Example 2

- **Input:** `nums = [7, 3, 5]`
- **Output:** `0`
- **Explanation:** Every element is odd, so every subarray product is odd.

#### Example 3

- **Input:** `nums = [2, 4, 6]`
- **Output:** `6`
- **Explanation:** Every non-empty subarray contains an even element, so all $3 \cdot 4 / 2 = 6$ subarrays qualify.
