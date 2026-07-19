# Sum Of Special Evenly-Spaced Elements In Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1714 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/) |

## Problem Description
### Goal

You are given an integer array `nums` and a list of queries. Each query is `[x, y]`. Its special sum starts at index `x` and includes `nums[x]`, `nums[x + y]`, `nums[x + 2 * y]`, and so on while the selected index remains inside the array.

Return the special sum for every query in its original order, with each result reduced modulo $10^9+7$. Queries do not modify `nums`, and repeated starting positions or step sizes must each produce their own output.

### Function Contract
**Inputs**

- `nums`: a list of $n$ non-negative integers
- `queries`: a list of $q$ pairs `[x, y]`, where `x` is a valid array index and $y \ge 1$
- $1 \le n \le 5\cdot 10^4$ and $1 \le q \le 1.5\cdot 10^5$
- every value and query step is at most $10^9$ and $5\cdot10^4$, respectively

Let $S=\lfloor\sqrt n\rfloor+1$.

**Return value**

A length-$q$ list whose entry for `[x, y]` is

$$
\left(\sum_{\substack{k\ge0\\x+ky<n}}\texttt{nums[x + k * y]}\right)
\bmod (10^9+7).
$$

### Examples
**Example 1**

- Input: `nums = [0, 1, 2, 3, 4, 5, 6, 7], queries = [[0, 3], [5, 1], [4, 2]]`
- Output: `[9, 18, 10]`

The selected index sequences are `(0, 3, 6)`, `(5, 6, 7)`, and `(4, 6)`.

**Example 2**

- Input: `nums = [100, 200, 101, 201, 102, 202, 103, 203], queries = [[0, 7]]`
- Output: `[303]`

The query selects indices `0` and `7`.

**Example 3**

- Input: `nums = [1, 2, 3, 4, 5], queries = [[0, 2], [1, 2], [4, 1]]`
- Output: `[9, 6, 5]`

Different starts with the same step reuse the same evenly spaced suffix relation.
