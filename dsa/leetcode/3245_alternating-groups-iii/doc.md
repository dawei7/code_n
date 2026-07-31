# Alternating Groups III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3245 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Indexed Tree, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/alternating-groups-iii/) |

## Problem Description

### Goal

Red and blue tiles form a circle. The array `colors` records the current color of every tile: `0` denotes red and `1` denotes blue. Because the arrangement is circular, the last tile is adjacent to the first.

An alternating group of size $s$ consists of $s$ consecutive circular tiles in which every consecutive pair inside the group has different colors. Process two kinds of query in order:

- `[1, s]` asks how many starting positions produce an alternating group of exactly size $s$.
- `[2, index, color]` changes the tile at `index` to the specified color; assigning its existing color is allowed and changes nothing.

Return the answers to type-1 queries in their original order. Update queries do not add entries to the result.

### Function Contract

**Inputs**

- `colors`: A binary array describing a circular arrangement of $n$ tiles, where $4 \le n \le 5 \cdot 10^4$.
- `queries`: Between 1 and $5 \cdot 10^4$ count or update operations. A count size satisfies $3 \le s \le n-1$; an update uses a valid index and binary color.

**Return value**

- The alternating-group count produced by each type-1 query, in order.

### Examples

**Example 1**

- Input: `colors = [0,1,1,0,1], queries = [[2,1,0],[1,4]]`
- Output: `[2]`

**Example 2**

- Input: `colors = [0,0,1,0,1,1], queries = [[1,3],[2,3,0],[1,5]]`
- Output: `[2,0]`

**Example 3**

- Input: `colors = [0,1,0,1,0,1], queries = [[1,3],[2,4,1],[1,3]]`
- Output: `[6,3]`
