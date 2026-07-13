# Plates Between Candles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2055 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Binary Search, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [plates-between-candles](https://leetcode.com/problems/plates-between-candles/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/plates-between-candles/).

### Goal
For each substring query, count plates `'*'` that lie between two candles `'|'` inside the queried range.

### Function Contract
**Inputs**

- `s`: a string of plates and candles.
- `queries`: inclusive index ranges `[left, right]`.

**Return value**

Return one plate count per query.

### Examples
**Example 1**

- Input: `s = "**|**|***|", queries = [[2,5],[5,9]]`
- Output: `[2,3]`

**Example 2**

- Input: `s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]`
- Output: `[9,0,0,0,0]`

**Example 3**

- Input: `s = "|*|", queries = [[0,2],[1,1]]`
- Output: `[1,0]`

---

## Solution
### Approach
Precompute prefix plate counts, the nearest candle at or to the left of each index, and the nearest candle at or to the right of each index. A query uses the first candle inside the left bound and the last candle inside the right bound; prefix counts between them give the answer.

### Complexity Analysis
- **Time Complexity**: `O(n + q)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
