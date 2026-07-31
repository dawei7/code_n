# Range Product Queries of Powers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2438 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Range Product Queries of Powers](https://leetcode.com/problems/range-product-queries-of-powers/) |

## Problem Description

### Goal

Every positive integer `n` can be written uniquely as a sum of distinct powers of two. Among all arrays of powers of two whose sum is `n`, let `powers` be the one with the fewest elements, arranged in non-decreasing order. Equivalently, `powers` contains one value $2^b$ for every set bit $b$ in the binary representation of `n`.

For each query `[left, right]`, multiply the consecutive entries `powers[left]` through `powers[right]`, including both endpoints. Return the answers in the same order as the queries, reducing every product modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `n`: A positive integer with $1 \le n \le 10^9$.
- `queries`: A list of $q$ inclusive index ranges, where $1 \le q \le 10^5$.

Each query is `[left, right]`, with $0 \le \texttt{left} \le \texttt{right} < \lvert\texttt{powers}\rvert$.

**Return value**

- A list of $q$ integers. Entry $i$ is the product selected by `queries[i]`, modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `n = 15, queries = [[0, 1], [2, 2], [0, 3]]`
- Output: `[2, 4, 64]`
- Explanation: The minimum decomposition is `powers = [1, 2, 4, 8]`. The three inclusive products are `1 * 2`, `4`, and `1 * 2 * 4 * 8`.

**Example 2**

- Input: `n = 2, queries = [[0, 0]]`
- Output: `[2]`
- Explanation: The only set bit contributes `powers = [2]`, so the sole range contains that value.
