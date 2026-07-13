# Pacific Atlantic Water Flow

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 417 |
| Difficulty | Medium |
| Topics | Array, Depth-First Search, Breadth-First Search, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/) |

## Problem Description
### Goal
Given a nonempty rectangular elevation matrix, water from a cell may move horizontally or vertically to an adjacent cell whose height is less than or equal to the current height. The Pacific borders the top and left edges, while the Atlantic borders the bottom and right edges.

Return every coordinate `[row, column]` from which some downhill-or-level route can reach both oceans, in any order. The two routes may differ and can leave through different boundary cells. Diagonal movement and uphill flow are forbidden. A cell touching both ocean boundaries qualifies directly, and repeated heights may form level-connected drainage regions.

### Function Contract
**Inputs**

- `heights`: a nonempty rectangular elevation matrix

**Return value**

- Return all `[row, column]` coordinates that can flow to both oceans, in any order.

### Examples
**Example 1**

- Input: `heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]`
- Output: `[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]`

**Example 2**

- Input: `heights = [[1]]`
- Output: `[[0,0]]`

**Example 3**

- Input: `heights = [[2,2],[2,2]]`
- Output: `[[0,0],[0,1],[1,0],[1,1]]`

### Required Complexity

- **Time:** $O(rc)$
- **Space:** $O(rc)$

<details>
<summary>Approach</summary>

#### General

**Reverse the direction of water flow**

Instead of starting from every cell and searching downhill, start from an ocean's boundary cells and move inland only to equal or higher neighbors. A reverse path from an ocean to a cell exists exactly when water can follow the same edges downhill from that cell to the ocean.

**Run one multi-source search per ocean**

Seed the Pacific search with all top-row and left-column cells. Seed the Atlantic search with all bottom-row and right-column cells. Each breadth-first search marks every cell reverse-reachable from its ocean, adding a cell only once.

**Intersect the two reachable sets**

After both searches, scan the matrix and emit coordinates present in both sets. Such a cell has a downhill path to each ocean; a cell absent from either set lacks the corresponding path.

**Why reverse reachability is complete**

Every legal forward edge goes from height `h` to a neighbor no higher than `h`. Reversing it permits movement from that neighbor to height `h`, exactly the nondecreasing rule used by the searches. Reversing complete paths establishes a one-to-one correspondence between downhill ocean paths and uphill boundary paths.

#### Complexity detail

Let `r` and `c` be the matrix dimensions. Each ocean search visits every cell at most once and examines four neighbors, so total time is $O(rc)$. The two visited sets and queues use $O(rc)$ space.

#### Alternatives and edge cases

- **Search downhill from every cell:** is correct but may revisit the matrix for each start and take $O((rc)^2)$ time.
- **Depth-first reverse searches:** use the same graph direction and bounds, with recursion-depth concerns on large grids.
- **Compare only row and column extrema:** misses winding paths and plateaus.
- A one-cell matrix touches both oceans.
- A single row or column lies on both opposing ocean boundaries.
- Equal-height plateaus allow flow in either direction.
- A high interior ridge may reach both oceans through different paths.

</details>
