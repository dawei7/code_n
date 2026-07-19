# Maximum Product Difference Between Two Pairs

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-product-difference-between-two-pairs/) |
| Frontend ID | 1913 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

The product difference between pairs $(a,b)$ and $(c,d)$ is $ab-cd$. Given a positive integer array `nums`, select four distinct indices `w`, `x`, `y`, and `z`, using `nums[w]` and `nums[x]` for the product that is added and `nums[y]` and `nums[z]` for the product that is subtracted.

Maximize this difference and return its value. Equal values at different indices remain distinct selectable elements, but no single array position may be used in both pairs.

### Function Contract

**Inputs**

- `nums`: a list of $N$ positive integers.
- $4 \le N \le 10^4$.
- $1 \le \texttt{nums[i]} \le 10^4$.

**Return value**

- Return the maximum value of `nums[w] * nums[x] - nums[y] * nums[z]` over four distinct indices.

### Examples

**Example 1**

- Input: `nums = [5,6,2,7,4]`
- Output: `34`

The two largest values give `6 * 7`, and the two smallest remaining values give `2 * 4`.

**Example 2**

- Input: `nums = [4,2,5,9,7,4,8]`
- Output: `64`

The maximum is `9 * 8 - 2 * 4 = 64`.

**Example 3**

- Input: `nums = [1,2,3,4]`
- Output: `10`

All four values are used: `4 * 3 - 1 * 2 = 10`.
