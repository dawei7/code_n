# Find the Number of Subsequences With Equal GCD

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3336 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/) |

## Problem Description

### Goal

You are given an integer array `nums`. Form an ordered pair of non-empty subsequences `(seq1, seq2)` by assigning selected array elements to the first or second subsequence while preserving their original order. The two subsequences must be disjoint: no array index may contribute to both, even when equal values occur at different positions.

Count the ordered pairs for which the greatest common divisor of all elements in `seq1` equals the greatest common divisor of all elements in `seq2`. Reversing the two subsequences produces a distinct pair. Return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: A nonempty list of positive integers. Its length is $n$, where $1 \le n \le 200$, and every value is at most $200$.

Let $V=\max(\texttt{nums})$.

**Return value**

- The number of ordered, disjoint, non-empty subsequence pairs having equal GCD, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `10`
- Explanation: All ten valid ordered pairs have GCD $1$; exchanging the first and second subsequences counts separately.

**Example 2**

- Input: `nums = [10, 20, 30]`
- Output: `2`
- Explanation: The two valid ordered pairs both have GCD $10$ and differ by which side receives the index containing `10`.

**Example 3**

- Input: `nums = [1, 1, 1, 1]`
- Output: `50`
- Explanation: Every pair of non-empty disjoint subsequences has GCD $1$.
