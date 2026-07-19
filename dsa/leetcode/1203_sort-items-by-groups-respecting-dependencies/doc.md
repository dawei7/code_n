# Sort Items by Groups Respecting Dependencies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1203 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/) |

## Problem Description

### Goal

There are `n` zero-indexed items. Each item belongs either to one of `m` zero-indexed groups or to no group: `group[i]` gives item `i`'s group, while `-1` denotes an ungrouped item. A group is allowed to contain no items.

Produce an ordering of all items in which every item from the same group appears in one contiguous block. The dependency list `beforeItems[i]` contains every item that must occur to the left of item `i` in that ordering. Return any ordering satisfying both the dependency and contiguity requirements. If no such ordering exists, return an empty list.

### Function Contract

**Inputs**

- `n`: The number of items, labeled from `0` through `n - 1`, where $1\le n\le3\times10^4$.
- `m`: The number of original groups, where $1\le m\le n$.
- `group`: A length-$n$ array with `group[i]` between `-1` and `m - 1`.
- `beforeItems`: A length-$n$ dependency list. Each `beforeItems[i]` contains distinct item indices other than `i`.
- Let $e=\sum_{i=0}^{n-1}\lvert\texttt{beforeItems[i]}\rvert$ be the total number of dependency relations.
- Let $g$ be `m` plus the number of items whose original group is `-1`.

**Return value**

- Any permutation of all $n$ items that respects every dependency and keeps each group's items next to one another, or `[]` if none exists.

### Examples

**Example 1**

- Input: `n = 8`, `m = 2`, `group = [-1,-1,1,0,0,1,0,-1]`, `beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]`
- Output: `[6,3,4,1,5,2,0,7]`

Other valid orders may also be returned.

**Example 2**

- Input: `n = 8`, `m = 2`, `group = [-1,-1,1,0,0,1,0,-1]`, `beforeItems = [[],[6],[5],[6],[3],[],[4],[]]`
- Output: `[]`

Compared with the first example, item `4` must now precede item `6`; the resulting requirements cannot be satisfied while group `0` remains contiguous.
