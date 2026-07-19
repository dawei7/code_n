# Tuple with Same Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1726 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/tuple-with-same-product/) |

## Problem Description

### Goal

You are given an array `nums` containing distinct positive integers. Form an ordered tuple `(a, b, c, d)` by choosing four distinct elements from the array. The tuple is valid when the products of its first and second pairs are equal:

$$
a b = c d.
$$

Return the total number of valid ordered tuples. Order matters: exchanging the values within either pair or exchanging the two pairs produces a different tuple, provided the same four distinct array elements still satisfy the product equality.

### Function Contract

**Inputs**

- `nums`: an array of $n$ distinct positive integers, where $1 \le n \le 1000$ and $1 \le \texttt{nums[i]} \le 10^4$.

**Return value**

- Return the number of ordered tuples `(a, b, c, d)` made from four distinct elements such that $ab=cd$.

### Examples

**Example 1**

- Input: `nums = [2,3,4,6]`
- Output: `8`
- Explanation: The unordered pairs `{2,6}` and `{3,4}` share product $12$. Swapping within each pair and exchanging the pair positions creates eight ordered tuples.

**Example 2**

- Input: `nums = [1,2,4,5,10]`
- Output: `16`
- Explanation: Products $10$ and $20$ each arise from two different unordered pairs, and each collision contributes eight tuples.

**Example 3**

- Input: `nums = [2,3,5,7]`
- Output: `0`
- Explanation: No two unordered pairs have the same product.
