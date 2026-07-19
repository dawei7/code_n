# Get Watched Videos by Your Friends

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1311 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Breadth-First Search, Graph Theory, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/get-watched-videos-by-your-friends/) |

## Problem Description
### Goal
There are $n$ people with IDs from 0 through $n-1$. For each person, `watchedVideos[i]` lists the videos that person watched, and `friends[i]` lists that person's friends. Friendship is mutual.

Starting from person `id`, consider only people whose shortest friendship-path distance is exactly `level`. Count every video occurrence in those people's watched lists. Return the distinct video names ordered by increasing frequency among that exact-level group; when two videos have the same frequency, order them in ascending alphabetical order.

### Function Contract
**Inputs**

- `watched_videos`: $n$ nonempty video lists, one for each person.
- `friends`: an undirected adjacency list of the same length, with no out-of-range IDs.
- $2\le n\le100$; each person has between 1 and 100 watched videos.
- Every video name is a nonempty string of at most 8 characters.
- `id`: the starting person's ID, where $0\le\texttt{id}<n$.
- `level`: the required shortest-path distance, where $1\le\texttt{level}<n$.

Let $E$ be the number of friendship edges, $S$ the total number of video entries watched by people at the target level, and $V$ the number of distinct titles among those entries.

**Return value**

The $V$ distinct target-level video titles, sorted first by increasing occurrence count and then alphabetically.

### Examples
**Example 1**

- Input: `watchedVideos = [["A","B"],["C"],["B","C"],["D"]]`, `friends = [[1,2],[0,3],[0,3],[1,2]]`, `id = 0`, `level = 1`
- Output: `["B","C"]`
- Explanation: People 1 and 2 are exactly one step away. `B` occurs once and `C` occurs twice.

**Example 2**

- Input: the same graph, `id = 0`, `level = 2`
- Output: `["D"]`

**Example 3**

- Input: `watchedVideos = [["self"],["B","A"],["A"]]`, `friends = [[1,2],[0],[0]]`, `id = 0`, `level = 1`
- Output: `["B","A"]`
- Explanation: `B` occurs once and `A` occurs twice, so frequency takes priority over alphabetical order.
