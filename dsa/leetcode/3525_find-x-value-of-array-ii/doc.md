# Find X Value of Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3525 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-x-value-of-array-ii/) |

## Problem Description

### Goal

You are given an array of positive integers `nums`, a positive integer `k`, and a list of queries. A query `[index, value, start, x]` first assigns `nums[index] = value`; this update persists and affects every later query. It then requires the prefix `nums[0..start - 1]` to be removed, where `start = 0` means removing an empty prefix.

After that required removal, choose a suffix to remove while leaving at least one element. The query's x-value is the number of choices whose remaining prefix of `nums[start..]` has a product congruent to $x$ modulo $k$. Return one x-value per query. This version counts prefixes of the selected suffix range, rather than all subarrays as in Find X Value of Array I.

### Function Contract

**Inputs**

- `nums`: An array of positive integers updated in place conceptually across queries.
- `k`: The modulus used for all product remainders.
- `queries`: A list whose entries are `[index, value, start, x]`.

The constraints are $1 \le \lvert\texttt{nums}\rvert \le 10^5$, $1 \le k \le 5$, and $1 \le \lvert\texttt{queries}\rvert \le 2 \cdot 10^4$. Array and update values are between $1$ and $10^9$; indices and starts are valid array positions, and $0 \le x < k$.

**Return value**

- An integer array in query order, containing the requested x-value after each persistent update.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3, 4, 5], k = 3, queries = [[2, 2, 0, 2], [3, 3, 3, 0], [0, 1, 0, 1]]`
- **Output:** `[2, 2, 2]`

#### Example 2

- **Input:** `nums = [1, 2, 4, 8, 16, 32], k = 4, queries = [[0, 2, 0, 2], [0, 2, 0, 1]]`
- **Output:** `[1, 0]`

#### Example 3

- **Input:** `nums = [1, 1, 2, 1, 1], k = 2, queries = [[2, 1, 0, 1]]`
- **Output:** `[5]`
