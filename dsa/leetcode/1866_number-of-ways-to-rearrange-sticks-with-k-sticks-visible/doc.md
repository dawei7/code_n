# Number of Ways to Rearrange Sticks With K Sticks Visible

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1866 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/) |

## Problem Description
### Goal
There are $n$ sticks with distinct integer lengths $1$ through $n$. Arrange all
sticks in a row. A stick is visible when viewed from the left exactly when no
longer stick occurs anywhere before it; equivalently, it establishes a new
maximum length while scanning the arrangement from left to right.

Count the permutations in which exactly $k$ sticks are visible. Return the
count modulo $10^9+7$.

### Function Contract
**Inputs**

- `n`: the number of uniquely sized sticks, with $1 \le n \le 1000$.
- `k`: the required number visible from the left, with $1 \le k \le n$.

**Return value**

The number of permutations of lengths $1,\ldots,n$ having exactly $k$ visible
sticks, reduced modulo $1{,}000{,}000{,}007$.

### Examples
**Example 1**

- Input: `n = 3, k = 2`
- Output: `3`

**Example 2**

- Input: `n = 5, k = 5`
- Output: `1`

Only the strictly increasing arrangement exposes every stick.

**Example 3**

- Input: `n = 20, k = 11`
- Output: `647427950`
