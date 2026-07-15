# Rotting Oranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 994 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/rotting-oranges/) |

## Problem Description

### Goal

You are given an $m\times n$ grid in which `0` represents an empty cell, `1` represents a fresh orange, and `2` represents a rotten orange. During each minute, every fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes required until no cell contains a fresh orange. If one or more fresh oranges can never be reached by this spreading process, return `-1`. When the grid initially has no fresh oranges, the required time is zero.

### Function Contract

**Inputs**

- `grid`: an $m\times n$ matrix whose entries are `0`, `1`, or `2`, where $1\le m,n\le10$.

Define the grid area as $A=mn$.

**Return value**

- The minimum elapsed minutes needed to rot every fresh orange, or `-1` if that is impossible.

### Examples

**Example 1**

- Input: `grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]`
- Output: `4`

**Example 2**

- Input: `grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]`
- Output: `-1`
- Explanation: The fresh orange in the lower-left corner has no 4-directional path from a rotten orange.

**Example 3**

- Input: `grid = [[0, 2]]`
- Output: `0`
- Explanation: No fresh orange exists at minute zero.

### Required Complexity

- **Time:** $O(A)$
- **Space:** $O(A)$

<details>
<summary>Approach</summary>

#### General

**Start from every rotten orange at once:** Scan the grid once, enqueue all initially rotten cells, and count the fresh oranges. These sources form minute zero of a multi-source breadth-first search. Processing them together is essential because rotting from every source occurs simultaneously.

**Advance one breadth-first layer per minute:** For each queued cell, inspect its four neighbors. When a neighbor is fresh, change it to rotten immediately, decrement the remaining-fresh count, and enqueue it with the next minute. Immediate marking prevents two sources from enqueuing the same orange. The greatest minute assigned to any newly rotten orange is the elapsed time.

Breadth-first search reaches each orange by the shortest 4-directional path from any initial rotten source, so its layer number is exactly the earliest minute when that orange can rot. After the queue empties, a positive fresh count proves that barriers or disconnected cells made complete rotting impossible.

#### Complexity detail

The initial scan and breadth-first traversal each inspect $O(A)$ cells, and every cell is enqueued at most once, so time is $O(A)$. The queue can hold $O(A)$ cells, giving $O(A)$ space.

#### Alternatives and edge cases

- **Rescan the entire grid each minute:** Simulating simultaneous changes with repeated full-grid scans is correct, but a long narrow propagation path can require $O(A^2)$ time.
- **Depth-first search from each source:** DFS does not naturally preserve earliest arrival times and may revisit cells unless distances are repeatedly relaxed.
- **No fresh oranges:** Return zero even if the grid contains only empty cells and rotten oranges.
- **No initial rotten orange:** Return `-1` when any fresh orange exists because propagation cannot begin.
- **Disconnected fresh region:** Empty cells block movement, and diagonal contact does not spread rot.

</details>
