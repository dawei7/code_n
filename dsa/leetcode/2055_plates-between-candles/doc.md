# Plates Between Candles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2055 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Binary Search, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/plates-between-candles/) |

## Problem Description

### Goal

A long table is represented by a string `s` containing only plates `'*'` and candles `'|'`. Each query `[left, right]` selects the inclusive substring from `left` through `right`.

For every query, count the plates that have at least one candle to their left and at least one candle to their right within that same selected substring. Candles outside the query cannot enclose a plate. Return the counts in the original query order.

### Function Contract

**Inputs**

- `s`: a string of length $n$, where $3 \le n \le 10^5$, consisting only of `'*'` and `'|'`.
- `queries`: an array of $q$ inclusive ranges `[left, right]`, where $1 \le q \le 10^5$ and $0 \le left \le right < n$.

**Return value**

- Return an integer array of length $q$ whose entry at index `i` is the number of plates enclosed by candles inside `queries[i]`.

### Examples

**Example 1**

- Input: `s = "**|**|***|", queries = [[2,5],[5,9]]`
- Output: `[2,3]`
- Explanation: The candles at indices `2` and `5` enclose two plates; those at `5` and `9` enclose three.

**Example 2**

- Input: `s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]`
- Output: `[9,0,0,0,0]`
