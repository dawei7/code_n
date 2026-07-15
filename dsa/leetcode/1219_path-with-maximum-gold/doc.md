# Path with Maximum Gold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1219 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/path-with-maximum-gold/) |

## Problem Description

### Goal

You are given a gold mine represented by a grid. Each cell contains a nonnegative integer: a positive value is the amount of gold in that cell, while `0` represents an empty cell. Whenever you enter a gold cell, you collect all of its gold.

From a cell, you may walk one step left, right, up, or down. A path may never enter a `0` cell and may not visit the same cell more than once. You may choose any gold cell as the starting point and may stop at any gold cell.

Return the maximum amount of gold that can be collected along one valid path.

### Function Contract

**Inputs**

- `grid`: An $m\times n$ matrix, where $1\le m,n\le15$ and $0\le\texttt{grid[r][c]}\le100$.

Let $g$ be the number of cells containing gold. The input guarantees $g\le25$.

**Return value**

- The greatest total gold obtainable from one path that obeys all movement and visitation rules.

### Examples

**Example 1**

- Input: `grid = [[0,6,0],[5,8,7],[0,9,0]]`
- Output: `24`

The path `9 -> 8 -> 7` collects `24` gold.

**Example 2**

- Input: `grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]`
- Output: `28`

The path `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7` collects `28` gold.

**Example 3**

- Input: `grid = [[10]]`
- Output: `10`

### Required Complexity

- **Time:** $O(mn\cdot3^g)$
- **Space:** $O(g)$

<details>
<summary>Approach</summary>

#### General

**Try every permitted starting cell.** A maximum path may begin anywhere, including an interior cell whose two directions lead to unequal totals. Launch a depth-first search from each positive grid cell and keep the largest collected sum.

**Mark the current path in place.** On entering a cell, save its gold and temporarily replace the grid value with `0`. Recursive calls then use the ordinary empty-cell check to reject both original empty cells and cells already on the current path. Explore all four neighboring coordinates, add the best continuation to the saved gold, and restore the cell before returning so another path may use it.

**Why backtracking finds the optimum.** At any visited cell, a valid path either stops or continues through exactly one unvisited positive neighbor. The recursive maximum considers every such next choice, while the temporary mark enforces the no-revisit rule. Induction on the remaining available cells therefore makes each call return the best path beginning at its cell. Taking the maximum over every legal start covers every valid path and yields the global optimum.

#### Complexity detail

There are at most $mn$ starting positions. After the first move, the cell just left is marked, so a search step has at most three forward choices; with at most $g$ gold cells, the broad worst-case time bound is $O(mn\cdot3^g)$. A path contains at most $g$ cells, so the recursion stack uses $O(g)$ space. In-place marking adds only constant storage per frame.

#### Alternatives and edge cases

- **Copy a visited collection for every branch:** This preserves correctness but adds path-length copying or membership work to every recursive state; in-place marking is simpler and cheaper.
- **Dynamic programming by cell alone:** The best continuation depends on the entire set of already visited cells, so coordinates alone do not identify a reusable state.
- **Bitmask memoization:** Mapping gold cells to bits can memoize `(cell, visited)` states, but it may require $O(g2^g)$ storage and is unnecessary under the small $g$ bound.
- **No gold cells:** No path can start, so the answer is `0`.
- **One gold cell:** Starting and stopping there collects its full value.
- **Disconnected components:** A path stays within one component, but trying every start naturally compares their best totals.
- **Stopping early:** A search may stop whenever no beneficial legal continuation exists; because gold values are positive, taking any available neighbor is beneficial, but the neighbor choice still matters.
- **Grid restoration:** Every recursive return must restore the saved value so sibling branches and later starting points see the original mine.

</details>
