# Number of Excellent Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2354 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-excellent-pairs/) |

## Problem Description

### Goal

Given a 0-indexed array `nums` of positive integers and a positive integer
`k`, count the distinct ordered value pairs $(a,b)$ whose two values both
occur somewhere in `nums` and satisfy the required bit condition. Add the
number of set bits in $a\mathbin{\mathrm{OR}}b$ to the number in
$a\mathbin{\mathrm{AND}}b$; the pair is excellent when that sum is at least
`k`.

Pairs are distinguished by their values and their order, not by source-array
indices. Thus duplicates in `nums` do not multiply the count, while $(a,b)$
and $(b,a)$ are different when $a\ne b$. A self-pair $(a,a)$ is allowed as
long as `a` occurs at least once; it does not require two occurrences.

### Function Contract

**Inputs**

- `nums`: A positive integer array with
  $1 \le \lvert\texttt{nums}\rvert \le 10^5$ and
  $1 \le \texttt{nums[i]} \le 10^9$.
- `k`: The minimum combined set-bit count, where $1 \le k \le 60$.

**Return value**

The number of distinct ordered excellent value pairs.

### Examples

**Example 1**

- Input: `nums = [1,2,3,1]`, `k = 3`
- Output: `5`
- Explanation: The qualifying ordered pairs are `(3,3)`, `(2,3)`, `(3,2)`,
  `(1,3)`, and `(3,1)`. The duplicate `1` creates no additional value pair.

**Example 2**

- Input: `nums = [5,1,1]`, `k = 10`
- Output: `0`
- Explanation: Neither unique value supplies enough set bits with the other.

**Example 3**

- Input: `nums = [1]`, `k = 2`
- Output: `1`
- Explanation: `(1,1)` is valid because the single set bit contributes once
  through OR and once through AND.
