# Count Servers that Communicate

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1267 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-servers-that-communicate/) |

## Problem Description

### Goal

A server center is represented by an $m \times n$ integer matrix `grid`. A cell containing `1` holds a server, while a cell containing `0` is empty.

Two servers can communicate when they occupy the same row or the same column; no requirement is imposed on the cells between them. Count the servers that can communicate with at least one other server. Each qualifying server contributes once even if it shares both a row and a column with other servers.

### Function Contract

**Inputs**

- `grid`: an $m \times n$ binary matrix, where $1 \le m,n \le 250$.

Let $V=mn$ be the number of cells in the server-center map.

**Return value**

- Return the number of cells containing a server that shares its row or column with another server.

### Examples

**Example 1**

- Input: `grid = [[1,0],[0,1]]`
- Output: `0`

**Example 2**

- Input: `grid = [[1,0],[1,1]]`
- Output: `3`

**Example 3**

- Input: `grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]`
- Output: `4`

### Required Complexity

- **Time:** $O(V)$
- **Space:** $O(m+n)$

<details>
<summary>Approach</summary>

#### General

**Count occupancy before classifying servers**

Create one counter per row and one per column. Scan every cell once; whenever `grid[row][col] == 1`, increment both corresponding counters. These counts summarize all possible communication partners without building explicit edges between servers.

**Test the communication condition directly**

Scan the matrix again. A server communicates precisely when its row counter exceeds one or its column counter exceeds one. Count that cell once when either condition holds. The test is sufficient because a count above one guarantees a distinct server on the same line. It is also necessary: if both counts equal one, the current cell is the only server in its row and column, so it has no possible partner.

The logical `or` prevents double-counting a server that communicates along both axes, while servers on an otherwise empty line can still qualify through the other axis.

#### Complexity detail

Each of the two scans examines all $V$ cells and performs constant work, for $O(V)$ time. The row and column counters contain $m+n$ integers, giving $O(m+n)$ auxiliary space.

#### Alternatives and edge cases

- **Rescan each server's row and column:** It uses no counter arrays but repeats work and can take $O(V(m+n))$ time.
- **Graph traversal:** Connecting servers that share a line and counting non-singleton components is correct, but materializing or exploring those relationships is unnecessary.
- **Union-find:** Rows and columns can be joined through servers, yet the additional structure solves a more general connectivity problem than this direct count requires.
- **Single server:** Its row and column counts are both one, so it is excluded.
- **All-empty grid:** No counters increase and the answer is `0`.
- **Several partners on both axes:** A server still contributes exactly once.
- **Servers with empty cells between them:** Sharing a row or column is sufficient; intervening zeros do not block communication.

</details>
