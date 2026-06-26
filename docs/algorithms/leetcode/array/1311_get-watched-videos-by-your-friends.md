# Get Watched Videos by Your Friends

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1311 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Breadth-First Search, Graph Theory, Sorting |
| Official Link | [get-watched-videos-by-your-friends](https://leetcode.com/problems/get-watched-videos-by-your-friends/) |

## Problem Description & Examples
### Goal
Find all friends exactly `level` friendship steps away from a given person. Count videos watched by those friends and return video names sorted by increasing frequency, then alphabetically.

### Function Contract
**Inputs**

- `watchedVideos`: `watchedVideos[i]` lists videos watched by person `i`.
- `friends`: undirected friendship adjacency list.
- `id`: starting person.
- `level`: exact friendship distance.

**Return value**

Video names sorted by frequency and lexicographic tie-break.

### Examples
**Example 1**

- Input: `watchedVideos = [["A","B"],["C"],["B","C"],["D"]]`, `friends = [[1,2],[0,3],[0,3],[1,2]]`, `id = 0`, `level = 1`
- Output: `["B","C"]`

**Example 2**

- Input: `watchedVideos = [["A","B"],["C"],["B","C"],["D"]]`, `friends = [[1,2],[0,3],[0,3],[1,2]]`, `id = 0`, `level = 2`
- Output: `["D"]`

**Example 3**

- Input: `watchedVideos = [["Z"],["A"],["A","B"]]`, `friends = [[1],[0,2],[1]]`, `id = 0`, `level = 2`
- Output: `["A","B"]`

---

## Underlying Base Algorithm(s)
Breadth-first search and frequency sorting.

---

## Complexity Analysis
- **Time Complexity**: `O(n + e + v log v)` where `v` is the number of distinct videos at the target level.
- **Space Complexity**: `O(n + v)`
