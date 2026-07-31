# Maximum Elegance of a K-Length Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2813 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Stack, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/) |

## Problem Description

### Goal

You are given `n` items, each represented as `[profit, category]`, and an integer `k`. Select exactly `k` items. Because a subsequence may retain any chosen indices in their original order, every size-`k` subset of items is a valid choice.

The elegance of a selection is its total profit plus the square of its number of distinct categories. Return the maximum elegance among all selections of exactly `k` items. Repeated categories contribute every selected profit to the total but count only once toward the squared diversity bonus.

### Function Contract

**Inputs**

- `items`: A list of $n$ pairs `[profit, category]`, with $1 \leq n \leq 10^5$ and both values between $1$ and $10^9$.
- `k`: The exact number of items to select, where $1 \leq k \leq n$.

**Return value**

Return the maximum possible value of `total_profit + distinct_categories ** 2` for exactly `k` selected items.

### Examples

**Example 1**

- Input: `items = [[3,2],[5,1],[10,1]]`, `k = 2`
- Output: `17`
- Explanation: Selecting profits `3` and `10` gives total profit $13$ and two categories, for $13+2^2=17$.

**Example 2**

- Input: `items = [[3,1],[3,1],[2,2],[5,3]]`, `k = 3`
- Output: `19`
- Explanation: Selecting profits `3`, `2`, and `5` covers three categories and yields $10+3^2=19$.

**Example 3**

- Input: `items = [[1,1],[2,1],[3,1]]`, `k = 3`
- Output: `7`
- Explanation: All items are required, producing profit $6$ and one distinct category.
