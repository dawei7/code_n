# Subtract the Product and Sum of Digits of an Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1281 |
| Difficulty | Easy |
| Topics | Math |
| Official Link | [LeetCode](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/) |

## Problem Description
### Goal
Given a positive integer `n`, consider the digits in its ordinary decimal representation. Use every digit exactly once to form two quantities: multiply the digits together to obtain their product, and add the same digits together to obtain their sum. A zero digit therefore makes the product zero while contributing zero to the sum.

Return the difference obtained by subtracting the digit sum from the digit product. The input is always positive, so its representation contains at least one digit and no sign character needs to be considered.

### Function Contract
**Inputs**

- `n`: an integer satisfying $1 \le n \le 10^5$.
- Let $d$ be the number of decimal digits in `n`.

**Return value**

An integer equal to the product of `n`'s decimal digits minus their sum.

### Examples
**Example 1**

- Input: `n = 234`
- Output: `15`
- Explanation: The digit product is $2 \cdot 3 \cdot 4 = 24$, while the digit sum is $2 + 3 + 4 = 9$; their difference is $15$.

**Example 2**

- Input: `n = 4421`
- Output: `21`
- Explanation: The product is $32$ and the sum is $11$.

**Example 3**

- Input: `n = 10`
- Output: `-1`
- Explanation: A zero digit makes the product $0$, while the sum is $1$.
