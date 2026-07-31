# Sum of Numbers With Units Digit K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2310 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming, Greedy, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/) |

## Problem Description
### Goal
Given `num` and the decimal digit `k`, form a collection of positive integers
such that every chosen integer has units digit `k` and all chosen values sum to
`num`. Repeated instances of the same value are permitted despite the
statement's use of the word set.

Return the smallest possible number of chosen integers. If no such collection
can produce `num`, return `-1`. The empty collection has sum zero, so `num = 0`
requires no integers. A units digit is the rightmost decimal digit.

### Function Contract
**Inputs**

- `num`: The nonnegative target sum.
- `k`: The required units digit of every positive summand.

The contract guarantees $0\le\texttt{num}\le3000$ and
$0\le\texttt{k}\le9$.

**Return value**

The minimum collection size producing `num`, zero for the empty target, or
`-1` when no valid sum exists.

### Examples
**Example 1**

- Input: `num = 58`, `k = 9`
- Output: `2`
- Explanation: `9 + 49 = 58`, and both summands end in 9.

**Example 2**

- Input: `num = 37`, `k = 2`
- Output: `-1`
- Explanation: No count of positive integers ending in 2 can have this sum.

**Example 3**

- Input: `num = 0`, `k = 7`
- Output: `0`
- Explanation: The empty collection supplies the zero sum.
