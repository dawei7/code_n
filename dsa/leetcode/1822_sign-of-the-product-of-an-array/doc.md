# Sign of the Product of an Array

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/sign-of-the-product-of-an-array/) |
| Frontend ID | 1822 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Define the sign of a number to be `1` when it is positive, `-1` when it is negative, and `0` when it equals zero. The integer array `nums` determines a product formed from all of its elements.

Return the sign of that complete product. Only the three-way sign classification is requested, not the potentially very large product itself. A single zero makes the product zero; otherwise, its sign depends on whether the number of negative factors is even or odd.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 1000$.
- Every value satisfies $-100 \le \texttt{nums[i]} \le 100$.

**Return value**

- Return `1` if the product of all values is positive, `-1` if it is negative, or `0` if it is zero.

### Examples

**Example 1**

- Input: `nums = [-1,-2,-3,-4,3,2,1]`
- Output: `1`

Four negative factors give the nonzero product a positive sign.

**Example 2**

- Input: `nums = [1,5,0,2,-3]`
- Output: `0`

The zero factor makes the complete product zero.

**Example 3**

- Input: `nums = [-1,1,-1,1,-1]`
- Output: `-1`

There are three negative factors, so the product is negative.
