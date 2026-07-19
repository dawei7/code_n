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

### Required Complexity

- **Time:** $O(n+q)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Reducing a query to its enclosing candles**

For a query `[left, right]`, the relevant boundaries are the first candle at or after `left` and the last candle at or before `right`. Plates outside those two candles are not enclosed within the query, while every plate strictly between them is enclosed.

Precompute the nearest candle to the right of every index with a right-to-left pass and the nearest candle to the left with a left-to-right pass. If either boundary is missing or the first candle is not before the last, the answer is zero.

**Counting the interior in constant time**

Build a prefix array where `plates[i]` counts plate characters before index `i`. Once the two candle indices are known, subtract their prefix values to count exactly the plates between them. The candles themselves contribute nothing, so no endpoint adjustment is needed.

The chosen candles discard precisely the unenclosed prefix and suffix of each queried substring. Every remaining plate lies after a candle and before another candle within the range, and the prefix subtraction counts all and only those plates.

#### Complexity detail

The three preprocessing arrays are built in $O(n)$ time. Each of the $q$ queries performs constant-time boundary lookups and one subtraction, for $O(n+q)$ total time. The prefix and nearest-candle arrays use $O(n)$ space; the returned answer uses $O(q)$ output space.

#### Alternatives and edge cases

- **Candle positions plus binary search:** Store only candle indices and binary-search each query's two boundaries, using prefix counts for the result. This uses $O(n)$ space and $O(n+q\log n)$ time.
- **Scan every query substring:** Finding both candles and counting plates separately per query is correct but can cost $O(nq)$.
- A query with fewer than two candles has answer zero.
- Plates before the first in-range candle or after the last in-range candle are excluded.
- Query endpoints are inclusive and may themselves be candles or plates.

</details>
