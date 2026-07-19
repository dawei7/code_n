# Count Ways to Make Array With Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1735 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Combinatorics, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-ways-to-make-array-with-product/) |

## Problem Description

### Goal

Each query `[n,k]` asks about ordered arrays of $n$ positive integers. Count how many different arrays have a product exactly equal to $k$. Values may repeat, but every entry must be positive. Placing the same factors in different positions can produce different arrays because their order matters.

Queries are independent and their answers must remain in the original order. Because a count may be large, return each result modulo $10^9+7$.

### Function Contract

**Inputs**

- `queries`: a list of between $1$ and $10^4$ pairs `[n,k]`, with $1 \le n,k \le 10^4$.

Let $Q$ be the number of queries and

$$
K = \max_{[n,k] \in \texttt{queries}} k.
$$

**Return value**

- Return a length-$Q$ integer list whose $i$th value is the answer for `queries[i]` modulo $10^9+7$.

### Examples

**Example 1**

- Input: `queries = [[2,6],[5,1],[73,660]]`
- Output: `[4,1,50734910]`
- Explanation: Product $6$ can be split across two positions as `(1,6)`, `(2,3)`, `(3,2)`, or `(6,1)`; product $1$ forces every entry to be $1$.

**Example 2**

- Input: `queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]`
- Output: `[1,2,3,10,5]`
- Explanation: Every query is counted independently, including prime and prime-power products.

**Example 3**

- Input: `queries = [[4,8],[3,12],[2,36]]`
- Output: `[20,18,9]`
- Explanation: The prime exponents of each product are distributed independently among the requested positions.
