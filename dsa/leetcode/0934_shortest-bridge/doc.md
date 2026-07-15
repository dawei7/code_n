# Shortest Bridge

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 934 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [shortest-bridge](https://leetcode.com/problems/shortest-bridge/) |

## Problem Description

### Goal

An $n \times n$ binary `grid` uses `1` for land and `0` for water. An island is a maximal group of land cells connected vertically or horizontally; diagonal contact alone does not connect cells. The input contains exactly two islands.

You may change water cells from `0` to `1`. Return the smallest number of water cells that must be flipped so the two original islands become one four-directionally connected island. The bridge may pass through any water cells but must connect the existing land groups.

### Function Contract

**Inputs**

- `grid`: an $n \times n$ binary matrix, where $2 \le n \le 100$ and exactly two four-directionally connected islands are present.

**Return value**

Return the minimum number of water cells that must be changed to land to connect the two islands.

### Examples

**Example 1**

- Input: `grid = [[0,1],[1,0]]`
- Output: `1`

**Example 2**

- Input: `grid = [[0,1,0],[0,0,0],[0,0,1]]`
- Output: `2`

**Example 3**

- Input: `grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]`
- Output: `1`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Mark one complete island.** Find the first land cell and run depth-first or breadth-first search through its four-directional land neighbors. Mark every cell of this first island as visited and place all of them into a queue. Using the whole island as the initial frontier allows the bridge to begin from whichever shoreline cell is best.

**Expand through water in distance layers.** Run a multi-source breadth-first search from that queue. Unvisited water neighbors are marked and enqueued with distance one greater than their predecessor. The distance assigned to a water cell is exactly the minimum number of flips needed to connect it to the first island, because breadth-first search explores all positions requiring fewer flips before any position requiring more.

**Stop at the second island.** When expansion first reaches an unvisited land cell, that cell belongs to the other island. Return the distance of the cell from which it was reached: it counts precisely the intervening water cells, while neither original land endpoint needs a flip. Breadth-first ordering proves minimality—any bridge with fewer flips would have reached the second island in an earlier layer. Marking cells when they enter the queue prevents repeated work and leaves the input unchanged.

#### Complexity detail

The island-marking traversal and bridge expansion each visit any grid cell at most once and inspect four neighbors, so the total time is $O(n^2)$. The visited matrix, island frontier, and breadth-first queue can each hold $O(n^2)$ cells.

#### Alternatives and edge cases

- **Pairwise island-cell distances:** Label both islands and minimize Manhattan distance minus one over every cross-island cell pair. This is correct but may require $O(n^4)$ time when both islands contain quadratic area.
- **Start BFS from only one shoreline cell:** This can miss a shorter bridge beginning elsewhere; all first-island cells or all boundary cells must seed the search.
- **Diagonal islands:** Diagonal adjacency is not connectivity, but one intervening orthogonal water flip may connect the cells.
- **Nested islands:** One island may surround the other with a water ring; multi-source expansion still finds the ring's minimum thickness.
- **Visited timing:** Mark a water cell when enqueuing it, not when removing it, to avoid adding the same cell from several frontier cells.

</details>
