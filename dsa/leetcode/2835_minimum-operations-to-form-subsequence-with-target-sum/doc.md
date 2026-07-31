# Minimum Operations to Form Subsequence With Target Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2835 |
| Difficulty | Hard |
| Topics | Array, Greedy, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/) |

## Problem Description
### Goal

You receive a 0-indexed array `nums` whose elements are powers of two and a positive integer `target`. One operation selects an element greater than $1$, removes it, and appends two copies of half that value. Because every input value is a power of two, both new values remain valid powers of two and their combined sum is unchanged.

Find the minimum number of these split operations needed until the resulting array contains a subsequence whose elements sum to exactly `target`. A subsequence may discard any elements while preserving the relative order of those retained; therefore only the availability of a suitable subset of values matters. Return $-1$ when no sequence of splits can make the target sum possible.

### Function Contract
**Inputs**

- `nums`: A list of length $n$, where $1 \le n \le 1000$. Every element is a power of two and satisfies $1 \le \texttt{nums[i]} \le 2^{30}$.
- `target`: The required subsequence sum, where $1 \le \texttt{target} < 2^{31}$.

**Return value**

Return the minimum number of split operations required to make some subsequence sum to `target`, or $-1$ if this is impossible.

### Examples
**Example 1**

- Input: `nums = [1, 2, 8], target = 7`
- Output: `1`
- Explanation: Split `8` into two `4` values. The resulting array contains `[1, 2, 4]`, whose sum is $7$.

**Example 2**

- Input: `nums = [1, 32, 1, 2], target = 12`
- Output: `2`
- Explanation: Splitting `32` into two `16` values and then one `16` into two `8` values makes `[1, 1, 2, 8]` available.

**Example 3**

- Input: `nums = [1, 32, 1], target = 35`
- Output: `-1`
- Explanation: The entire array sums to $34$, and splitting never changes that total.
