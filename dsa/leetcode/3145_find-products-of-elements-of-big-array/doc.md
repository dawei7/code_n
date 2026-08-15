# Find Products of Elements of Big Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3145 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-products-of-elements-of-big-array/) |

## Problem Description

### Goal

The powerful array of a non-negative integer `x` is the shortest sorted list of powers of two whose sum is `x`. Equivalently, it contains one value $2^b$ for every set bit $b$ in `x`; this representation is unique.

Build the infinite zero-indexed array `big_nums` by concatenating the powerful arrays of the positive integers $1,2,3,\ldots$ in that order. Each query is `[from, to, mod]`. For every query, multiply the inclusive range from `big_nums[from]` through `big_nums[to]`, reduce the product modulo `mod`, and return the query results in their original order.

### Function Contract

**Inputs**

- `queries`: A list of triples `[from, to, mod]` describing inclusive sequence ranges and their moduli.

Let $q = \lvert\texttt{queries}\rvert$ and let $U$ be one plus the largest `to` value. The constraints are $1 \le q \le 500$, $0 \le \texttt{from} \le \texttt{to} \le 10^{15}$, and $1 \le \texttt{mod} \le 10^5$.

**Return value**

Return a length-$q$ integer list. Entry $i$ is the product of the requested inclusive `big_nums` range modulo the modulus in query $i$.

### Examples

#### Example 1

- **Input:** `queries = [[1, 3, 7]]`
- **Output:** `[4]`
- **Explanation:** `big_nums[1:4]` is `[2, 1, 2]`, whose product is $4$; reducing modulo $7$ leaves $4$.

#### Example 2

- **Input:** `queries = [[2, 5, 3], [7, 7, 4]]`
- **Output:** `[2, 2]`
- **Explanation:** The first range is `[1, 2, 4, 1]`, with product $8 \equiv 2 \pmod 3$. The second range contains only `2`, which is also $2$ modulo $4$.
