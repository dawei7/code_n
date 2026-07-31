# Count Array Pairs Divisible by K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2183 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Counting, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-array-pairs-divisible-by-k/) |

## Problem Description

### Goal

Given a zero-indexed integer array `nums` and a positive integer `k`, examine
every pair of distinct array positions in increasing index order. A pair
$(i,j)$ is eligible only when $0\le i<j<n$, so each unordered choice of two
positions is considered exactly once.

Count the eligible pairs for which the product of the two stored values,
`nums[i] * nums[j]`, is divisible by `k`. The values themselves need not be
divisible by `k`; complementary factors from the two values may combine to
supply all factors required by `k`.

### Function Contract

**Inputs**

- `nums`: an array of positive integers.
- `k`: the positive divisor used to test each pair's product.

The inputs satisfy
$1\le\lvert\texttt{nums}\rvert\le10^5$ and
$1\le\texttt{nums[i]},\texttt{k}\le10^5$.

**Return value**

Return the number of index pairs $(i,j)$ with $i<j$ and
$\texttt{nums[i]}\texttt{nums[j]}$ divisible by `k`.

### Examples

**Example 1**

- Input: `nums = [1,2,3,4,5]`, `k = 2`
- Output: `7`

**Example 2**

- Input: `nums = [1,2,3,4]`, `k = 5`
- Output: `0`

**Example 3**

- Input: `nums = [2,3]`, `k = 6`
- Output: `1`
