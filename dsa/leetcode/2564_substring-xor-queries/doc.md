# Substring XOR Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2564 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [substring-xor-queries](https://leetcode.com/problems/substring-xor-queries/) |

## Problem Description

### Goal

You are given a binary string `s` and a list `queries`, where each query contains two non-negative integers `[first, second]`. Every non-empty contiguous substring of `s` represents a binary number; leading zeroes are allowed when interpreting that value.

For each query, find a substring whose decimal value `val` satisfies `val ^ first == second`. Among all valid substrings, choose one with the fewest characters. If several shortest substrings work, choose the one with the smallest starting index. Return its inclusive, zero-based endpoints `[left, right]`, or `[-1, -1]` when no substring has the required value. Answers must remain in the same order as the queries.

### Function Contract

**Inputs**

- `s`: A binary string of length $n$, where $1 \le n \le 10^4$.
- `queries`: A list of $q$ pairs `[first, second]`, where $1 \le q \le 10^5$ and $0 \le \texttt{first}, \texttt{second} \le 10^9$.

**Return value**

- A list containing one inclusive endpoint pair `[left, right]` per query. Each pair identifies the required shortest substring with the smallest possible `left`, or is `[-1, -1]` if no match exists.

### Examples

**Example 1**

- Input: `s = "101101", queries = [[0, 5], [1, 2]]`
- Output: `[[0, 2], [2, 3]]`
- Explanation: `"101"` represents $5$, while `"11"` represents $3$ and $3 \mathbin{\mathtt{\char94}} 1 = 2$.

**Example 2**

- Input: `s = "0101", queries = [[12, 8]]`
- Output: `[[-1, -1]]`
- Explanation: The required value is $12 \mathbin{\mathtt{\char94}} 8 = 4$, but no substring represents binary `100`.

**Example 3**

- Input: `s = "1", queries = [[4, 5]]`
- Output: `[[0, 0]]`
- Explanation: The one-character substring represents $1$, and `1 ^ 4 == 5`.
