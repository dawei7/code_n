# Number of Divisible Triplet Sums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2964 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-divisible-triplet-sums/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and a positive integer `d`.
Choose three distinct indices in strictly increasing order, $i<j<k$.

Count the index triplets for which the sum of their three array values is
divisible by `d`:

$$
(\texttt{nums[i]}+\texttt{nums[j]}+\texttt{nums[k]})\bmod d=0.
$$

Triplets are distinguished by indices, so repeated values may participate in
several different choices.

### Function Contract

**Inputs**

- `nums`: the positive integer array supplying triplet values
- `d`: the divisor used to test each triplet sum

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees
$1\le N\le1000$, $1\le\texttt{nums[i]}\le10^9$, and $1\le d\le10^9$.

**Return value**

The number of index triples $i<j<k$ whose corresponding value sum is divisible
by `d`.

### Examples

#### Example 1

- **Input:** `nums = [3,3,4,7,8], d = 5`
- **Output:** `3`
- **Explanation:** The qualifying index triples are `(0,1,2)`, `(0,2,4)`, and `(1,2,4)`.

#### Example 2

- **Input:** `nums = [3,3,3,3], d = 3`
- **Output:** `4`
- **Explanation:** Every choice of three indices sums to nine, so all four possible triplets qualify.

#### Example 3

- **Input:** `nums = [3,3,3,3], d = 6`
- **Output:** `0`
- **Explanation:** Every triplet sum is nine, which is not divisible by six.
