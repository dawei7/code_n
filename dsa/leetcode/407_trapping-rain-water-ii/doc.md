# Trapping Rain Water II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 407 |
| Difficulty | Hard |
| Topics | Array, Breadth-First Search, Heap (Priority Queue), Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/trapping-rain-water-ii/) |

## Problem Description
### Goal
Given a nonempty rectangular matrix of nonnegative terrain heights, imagine rain falling over every cell. Water can spread between horizontally or vertically adjacent cells and escapes whenever it reaches the map's outer boundary.

Return the total number of unit cubes of water that remain trapped above the terrain after levels stabilize. Boundary cells cannot hold water above themselves, while interior capacity depends on the lowest enclosing route to the outside rather than only immediate neighbors. Sum retained depth over all cells. Diagonal barriers do not directly block or connect flow, and the function returns volume rather than a final water-level matrix.

### Function Contract
**Inputs**

- `height_map`: a nonempty matrix of nonnegative terrain heights

**Return value**

- Return the total trapped-water volume above all cells.

### Examples
**Example 1**

- Input: `height_map = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]`
- Output: `4`

**Example 2**

- Input: `height_map = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]`
- Output: `10`

**Example 3**

- Input: `height_map = [[1,2,3,4]]`
- Output: `0`

### Required Complexity

- **Time:** $O(rc \log(rc))$
- **Space:** $O(rc)$

<details>
<summary>Approach</summary>

#### General

**Flood inward from every escape boundary**

All boundary cells can release water directly, so mark them visited and insert them into one min-heap keyed by their effective boundary height. This creates a multi-source frontier around the unprocessed interior.

**Always expand the lowest known containment wall**

Pop the frontier cell with minimum effective height. For each unvisited neighbor, that wall can hold water up to its height. If the neighbor's terrain is lower, add the difference to the volume. The neighbor then joins the frontier at `max(wall_height, terrain_height)` because trapped water raises its effective surface to the wall.

**Why a later route cannot lower a finalized level**

The heap processes effective boundaries in nondecreasing order. When a cell is first reached from the minimum frontier, every alternate path to the exterior must cross either that frontier height or a boundary not yet popped and therefore no lower. Its assigned level is thus the minimum possible maximum elevation on any escape path—the exact water surface limit for that cell.

**Visit each cell only once**

Mark a neighbor when it enters the heap, not when it leaves. Its first candidate comes from the globally smallest available boundary and is already optimal by the minimax argument, so duplicate entries and later relaxation are unnecessary.

#### Complexity detail

Let `r` and `c` be the matrix dimensions. Each of the `rc` cells enters and leaves the heap once, with $O(\log(rc))$ heap work, for $O(rc \log(rc))$ time. The heap and visited matrix use $O(rc)$ space.

#### Alternatives and edge cases

- **Independent minimax search from every interior cell:** computes correct escape levels but repeats graph work and can take $O((rc)^2 \log(rc))$ time.
- **Iterative level-by-level flooding:** can revisit the grid once per height level and depends on the numeric height range.
- **Apply one-dimensional trapping by rows and columns:** is incorrect because water can escape along winding two-dimensional paths.
- Fewer than three rows or columns cannot enclose water.
- Boundary cells never trap water above themselves.
- A low boundary leak can drain an otherwise high basin.
- Nested terrain walls are handled by propagated effective heights.

</details>
