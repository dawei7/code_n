# Find Palindrome With Fixed Length

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2217 |
| Difficulty | Medium |
| Topics | Array, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/find-palindrome-with-fixed-length/) |

## Problem Description
### Goal

For a positive digit length `intLength`, consider all positive palindromes having exactly that many decimal digits, ordered from smallest to largest. A palindrome reads identically from left to right and right to left, and it cannot begin with zero.

For every one-based rank in `queries`, return the palindrome at that position in the ordered collection. If fewer than `queries[i]` palindromes of the required length exist, place `-1` at the corresponding answer position.

### Function Contract
**Inputs**

- `queries`: A nonempty list of positive one-based ranks.
- `intLength`: A positive integer giving the exact required decimal length.

Let $q=\lvert\texttt{queries}\rvert$ and $\ell=\texttt{intLength}$.

**Return value**

Return a list of $q$ integers in query order, using `-1` for each rank outside the available fixed-length palindromes.

### Examples
**Example 1**

- Input: `queries = [1, 2, 3, 4, 5, 90], intLength = 3`
- Output: `[101, 111, 121, 131, 141, 999]`

**Example 2**

- Input: `queries = [2, 4, 6], intLength = 4`
- Output: `[1111, 1331, 1551]`

**Example 3**

- Input: `queries = [1, 10], intLength = 1`
- Output: `[1, -1]`
