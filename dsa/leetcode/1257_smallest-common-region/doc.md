# Smallest Common Region

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1257 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Tree, Depth-First Search, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-common-region/) |

## Problem Description

### Goal

Regions form a containment hierarchy. Each list in `regions` starts with a parent region, followed by regions it directly contains. Containment is transitive: if one region contains a second and the second contains a third, then the first also contains the third.

Given two distinct region names, return the smallest region that contains both of them. A region contains itself for this purpose, so one query region may be the answer when it contains the other. The input describes a valid rooted hierarchy, both query names occur in it, and a common containing region is guaranteed.

### Function Contract

**Inputs**

- `regions`: hierarchy lists in which `regions[i][0]` directly contains every later name in that list.
- `region1`: the first region name.
- `region2`: the second, distinct region name.
- Let $R=\sum_{g\in\texttt{regions}}\lvert g\rvert$ be the total number of region-name occurrences in the hierarchy lists.

**Return value**

- Return the lowest region in the hierarchy that contains both `region1` and `region2`.

### Examples

**Example 1**

- Input: `regions = [["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]]`, `region1 = "Quebec"`, `region2 = "New York"`
- Output: `"North America"`

**Example 2**

- Input: the same hierarchy, `region1 = "Canada"`, `region2 = "South America"`
- Output: `"Earth"`

**Example 3**

- Input: the same hierarchy, `region1 = "North America"`, `region2 = "Quebec"`
- Output: `"North America"`
