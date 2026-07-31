# Minimum Swaps to Sort by Digit Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3551 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/) |

## Problem Description

### Goal

You are given an array `nums` containing distinct positive integers. Rearrange it into increasing order according to each number's decimal digit sum: a number with a smaller digit sum must come first. When two numbers have the same digit sum, the smaller number must come first.

One swap exchanges the values at two distinct array positions. Return the minimum number of swaps needed to transform `nums` into the uniquely determined order above.

### Function Contract

**Inputs**

- `nums`: An array of distinct positive integers.

The constraints are $1 \le \lvert\texttt{nums}\rvert \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.

**Return value**

Return the minimum number of pairwise swaps required to arrange all values by `(digit sum, value)` in increasing lexicographic order.

### Examples

**Example 1**

- Input: `nums = [37,100]`
- Output: `1`
- Explanation: The digit sums are $10$ and $1$, so the target is `[100,37]`; one swap reaches it.

**Example 2**

- Input: `nums = [22,14,33,7]`
- Output: `0`
- Explanation: Their digit sums are $4,5,6,7$, so the array already has the required order.

**Example 3**

- Input: `nums = [18,43,34,16]`
- Output: `2`
- Explanation: The target is `[16,34,43,18]`. Swapping `18` with `16`, then `43` with `34`, reaches it.

---
