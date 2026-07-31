# Minimum Number of Primes to Sum to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3610 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/) |

## Problem Description
### Goal

Consider the first `m` prime numbers in increasing order. Select a multiset from those primes whose elements sum to exactly `n`. A prime may be selected any number of times, including more than once in the same sum.

Because the selection is a multiset, only the chosen values and their multiplicities matter; their order does not. Determine the fewest selected primes that can produce the target. If no such multiset exists, return `-1`.

### Function Contract

**Inputs**

- `n`: The required target sum.
- `m`: The number of initial prime numbers available for selection.

The constraints are $1 \le \texttt{n} \le 1000$ and $1 \le \texttt{m} \le 1000$.

**Return value**

Return the minimum number of available primes whose sum is `n`, allowing repetitions, or `-1` when the target cannot be formed.

### Examples

**Example 1**

- Input: `n = 10, m = 2`
- Output: `4`
- Explanation: The available primes are `2` and `3`; `2 + 2 + 3 + 3 = 10` uses four terms.

**Example 2**

- Input: `n = 15, m = 5`
- Output: `3`
- Explanation: Three copies of `5` form the target.

**Example 3**

- Input: `n = 7, m = 6`
- Output: `1`
- Explanation: Since `7` is one of the first six primes, it forms the target by itself.
