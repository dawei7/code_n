# Maximize Active Section with Trade II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3501 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Binary Search, Segment Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-active-section-with-trade-ii/) |

## Problem Description

### Goal

A binary string `s` represents active sections with `'1'` and inactive sections with `'0'`. You may make at most one trade inside a specified substring. The trade first changes a contiguous block of `'1'`s surrounded by `'0'`s into `'0'`s, then changes a contiguous block of `'0'`s surrounded by `'1'`s into `'1'`s.

Each query `[l, r]` independently restricts both conversions to `s[l:r + 1]`. For that query, conceptually place an extra `'1'` immediately before and after the substring; those artificial sections establish its boundary surroundings but do not count toward the result. After choosing the optimal valid trade—or skipping it—report the number of active sections in the entire original string `s`, including unchanged positions outside the queried substring. Return one result per query in the original order.

### Function Contract

**Inputs**

- `s`: A binary string of length $n$.
- `queries`: A list of inclusive index pairs `[l, r]`, each describing `s[l:r + 1]`.

The constraints are $1 \le n \le 10^5$, $1 \le \lvert\texttt{queries}\rvert \le 10^5$, and $0 \le l \le r < n$. Every character of `s` is `'0'` or `'1'`.

**Return value**

Return a list whose $i$th value is the maximum whole-string active count after an optimal trade restricted to the $i$th query substring.

### Examples

**Example 1**

- Input: `s = "01", queries = [[0,1]]`
- Output: `[1]`
- Explanation: The substring contains no active block surrounded by inactive blocks, so no trade is possible.

**Example 2**

- Input: `s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]]`
- Output: `[4,3,1,1]`
- Explanation: The first two substrings contain the middle active block and zero sections on both sides, while the final two do not contain a valid first conversion.

**Example 3**

- Input: `s = "1000100", queries = [[1,5],[0,6],[0,4]]`
- Output: `[6,7,2]`
- Explanation: Results count the whole string. For `[1,5]`, the trade activates its five-character substring and preserves the active section at index `0`, producing `6`.

**Example 4**

- Input: `s = "01010", queries = [[0,3],[1,4],[1,3]]`
- Output: `[4,4,2]`
- Explanation: The first two ranges contain an eligible one run with zero sections on both sides; the last substring `"101"` does not.
