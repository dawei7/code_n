# Unique Paths III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 980 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Backtracking, Bit Manipulation, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/unique-paths-iii/) |

## Problem Description

### Goal

An $M\times N$ integer grid contains exactly one starting square marked `1` and exactly one ending square marked `2`. Empty squares marked `0` may be walked over, while obstacles marked `-1` cannot be entered.

Count the four-directional walks from the starting square to the ending square that visit every non-obstacle square exactly once. Each step moves up, down, left, or right to an edge-adjacent square; diagonal movement is not allowed. A walk is valid only if it reaches the ending square after covering the start, every empty square, and the end itself without revisiting any of them.

### Function Contract

**Inputs**

- `grid`: an $M\times N$ integer matrix with $1\le M,N\le20$, $1\le MN\le20$, values from `-1` through `2`, and exactly one start and one end.

Let $V$ be the number of non-obstacle squares.

**Return value**

- The number of four-directional start-to-end walks that visit all $V$ usable squares exactly once.

### Examples

**Example 1**

- Input: `grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]`
- Output: `2`

**Example 2**

- Input: `grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]`
- Output: `4`

**Example 3**

- Input: `grid = [[0, 1], [2, 0]]`
- Output: `0`
- Explanation: no walk covers both empty squares exactly once before ending.

### Required Complexity

- **Time:** $O(V2^V)$
- **Space:** $O(V2^V)$

<details>
<summary>Approach</summary>

#### General

**Encode the usable grid as a graph:** Assign a bit index to every non-obstacle square. Two vertices are adjacent when their grid squares share an edge. A bitmask then records exactly which squares a partial walk has visited.

**Memoize position and visited set:** Define a state by the current vertex `position` and the `visited` mask. From that state, try every adjacent vertex whose bit is not set and add the counts returned after setting it. Different walk prefixes can arrive at the same vertex with the same visited set; their possible suffixes are identical, so caching prevents those suffixes from being explored repeatedly.

**Accept the end only after full coverage:** If the current vertex is the end, return one exactly when `visited` equals the mask containing all $V$ usable squares; otherwise return zero immediately. This prevents a walk from reaching the end early, leaving other squares unvisited, and later treating that prefix as valid.

Every legal walk corresponds to one sequence of recursive transitions because each move follows a graph edge and sets one previously clear bit. Conversely, every counted transition sequence is four-directional, never revisits a square, covers the full mask, and finishes at the end. The state sum therefore counts precisely the required walks.

#### Complexity detail

There are at most $V2^V$ pairs of current vertex and visited mask. Each state examines at most four grid neighbors, so the bound remains $O(V2^V)$ time. The memo table can store $O(V2^V)$ results, and recursion uses at most $O(V)$ additional stack depth.

#### Alternatives and edge cases

- **Plain backtracking:** Marking cells in place uses only $O(V)$ stack space, but it can recompute the same position-and-visited-set suffix many times and has an exponential $O(3^V)$ upper bound.
- **Permute usable squares:** Generating orders and checking adjacency explores up to $V!$ candidates and ignores the grid graph until too late.
- **Reach the end early:** Such a path contributes zero because every other usable square must already have been visited.
- **Obstacles:** They receive no bit and no graph edges, so they are neither visited nor included in the full-coverage mask.
- **No Hamiltonian walk:** The recurrence naturally returns zero when every branch either gets stuck or reaches the end with an incomplete mask.

</details>
