# Prime Palindrome

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 866 |
| Difficulty | Medium |
| Topics | Math, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/prime-palindrome/) |

## Problem Description
### Goal
Given an integer `n`, find the smallest integer greater than or equal to `n` that is both prime and a palindrome. A prime has exactly two positive divisors, `1` and itself; in particular, `1` is not prime. A palindrome has the same decimal digit sequence when read from left to right or right to left.

Return the first integer satisfying both properties. The tests guarantee that an answer exists between `2` and $2\cdot10^8$, inclusive, while the input itself satisfies $1 \leq n \leq 10^8$.

### Function Contract
**Inputs**

- `n`: the inclusive lower bound for the search, where $1 \leq n \leq 10^8$.

Let $A$ denote the returned prime palindrome. For `n > 11`, let $P$ be the number of odd-length palindrome candidates generated from the starting decimal prefix through $A$, including any first candidate that falls just below `n`.

**Return value**

Return the smallest prime palindrome $A$ such that $A\geq n$.

### Examples
**Example 1**

- Input: `n = 6`
- Output: `7`

**Example 2**

- Input: `n = 8`
- Output: `11`

**Example 3**

- Input: `n = 13`
- Output: `101`

Every two-digit palindrome after `11` is composite, so the search continues to `101`.
