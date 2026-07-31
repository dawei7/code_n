# Find X-Sum of All K-Long Subarrays I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3318 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/) |

## Problem Description

### Goal

For any integer array, define its x-sum by counting each distinct value and retaining every occurrence of the $x$ values with the highest frequencies. When two values have equal frequencies, the larger numeric value ranks higher. Sum all retained occurrences; if fewer than $x$ distinct values exist, this is simply the sum of the whole array.

Given `nums`, examine every contiguous subarray of exactly length $k$. Return an array of length $n-k+1$ whose entry at index `i` is the x-sum of `nums[i..i + k - 1]`. Each window is ranked from its own frequencies, so the selected values can change as the window moves.

### Function Contract

**Inputs**

- `nums`: An array of $n$ integers, where $1\leq n\leq50$ and $1\leq\texttt{nums[i]}\leq50$.
- `k`: The subarray length, with $1\leq k\leq n$.
- `x`: The number of distinct frequency groups to retain, with $1\leq x\leq k$.

**Return value**

Return the x-sum of each length-$k$ subarray in left-to-right starting-index order.

### Examples

**Example 1**

- Input: `nums = [1, 1, 2, 2, 3, 4, 2, 3], k = 6, x = 2`
- Output: `[6, 10, 12]`

In the first window, values 1 and 2 each occur twice and contribute $2+4=6$. In the second, value 2 occurs three times; among the remaining one-time values, 4 wins the value tie.

**Example 2**

- Input: `nums = [3, 8, 7, 8, 7, 5], k = 2, x = 2`
- Output: `[11, 15, 15, 15, 12]`

Because `x == k`, every value in each two-element window is retained.

**Example 3**

- Input: `nums = [1, 1, 1, 1], k = 2, x = 1`
- Output: `[2, 2, 2]`
