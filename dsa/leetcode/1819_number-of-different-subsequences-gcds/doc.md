# Number of Different Subsequences GCDs

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/number-of-different-subsequences-gcds/) |
| Frontend ID | 1819 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Counting, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

The greatest common divisor (GCD) of a non-empty sequence is the greatest positive integer that divides every value in that sequence. A subsequence of `nums` is formed by deleting any number of elements while preserving the relative order of those retained; equal values at different positions remain independently selectable.

Consider every non-empty subsequence of the positive-integer array `nums`. Many subsequences may share a GCD, and the task concerns the distinct GCD values rather than the number of subsequences producing them. Return how many different positive integers occur as the GCD of at least one such subsequence.

### Function Contract

**Inputs**

- `nums`: an array of $n$ positive integers with $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 2\cdot10^5$.
- Let $M = \max(\texttt{nums})$.

**Return value**

- Return the number of distinct GCD values among all non-empty subsequences of `nums`.

### Examples

**Example 1**

- Input: `nums = [6,10,3]`
- Output: `5`

The attainable values are 6, 10, and 3 from single-element subsequences, 2 from `[6,10]`, and 1 from a subsequence containing 3 with either even value.

**Example 2**

- Input: `nums = [5,15,40,5,6]`
- Output: `7`

Repeated occurrences may form different subsequences, but they do not make an already attainable GCD count twice.
