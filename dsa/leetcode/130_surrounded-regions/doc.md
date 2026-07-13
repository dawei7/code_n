# Surrounded Regions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 130 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/surrounded-regions/) |

## Problem Description
### Goal
Given a rectangular board containing only `"X"` and `"O"`, identify regions of `"O"` cells connected through shared horizontal or vertical sides. A region is surrounded when none of its cells lies on the board boundary and no cell in the region can reach a boundary `"O"` through such connections.

Capture every surrounded region by changing all of its cells to `"X"` in place. Any boundary `"O"`, along with every `"O"` connected to it, must remain unchanged because that region is open to the outside. Diagonal contact does not connect regions, and the function returns no separate replacement board.

### Function Contract
**Inputs**

- `board`: a rectangular matrix containing only `"X"` and `"O"`

**Return value**

`None`; mutate `board` in place to capture all surrounded regions.

### Examples
**Example 1**

- Input: `board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]`
- Output board: `[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]`

**Example 2**

- Input: `board = [["X"]]`
- Output board: `[["X"]]`

**Example 3**

- Input: `board = [["O","O"],["X","O"]]`
- Output board unchanged

### Required Complexity

- **Time:** $O(mn)$
- **Space:** $O(mn)$

<details>
<summary>Approach</summary>

#### General

**Boundary reachability characterizes exactly the cells that survive**

A region is captured precisely when it has no four-directional path to the boundary. Instead of testing every interior region for enclosure, identify the complement: all `O` cells reachable from any boundary `O`. Those and only those cells must survive.

**Mark safe cells at enqueue time**

Inspect the first/last row and first/last column. When a boundary `O` is found, replace it with a temporary safe marker before enqueueing it. During BFS, do the same for each unmarked orthogonal `O` neighbor.

Marking at enqueue time prevents corner cells or converging searches from entering the queue repeatedly. The marker must differ from both `O` and `X` so safe cells are neither revisited nor mistaken for captured cells.

**One final pass distinguishes enclosed and proven-safe cells**

After flood fill, every remaining literal `O` lacks a boundary path and becomes `X`. Restore every safe marker to `O`. Existing `X` cells remain unchanged throughout.

**The marked region is exactly the discovered boundary-connected component union**

Every marked cell is boundary-connected through original `O` cells. Every queued cell has been marked, and all processed marked cells have had each neighbor considered.

**Trace a boundary cell connected through the interior**

In the standard example, the bottom-row `O` is itself safe but has no adjacent `O`, so only it is marked and restored. The interior `O` group cannot be reached from any boundary seed and is therefore still literal `O` during finalization, causing the whole group to flip.

**Boundary reachability is the exact escape criterion**

An `O` region is preserved exactly when some four-directional path connects it to a boundary `O`. Flood fill from every boundary seed reaches all such cells and cannot cross water into a surrounded region.

After marking, every remaining literal `O` lacks a boundary path and must be captured, while every marker witnesses such a path and must be restored. Finalization therefore changes precisely the surrounded regions.

#### Complexity detail

Each of the `mn` cells is inspected a constant number of times, giving $O(mn)$ time. In the worst case the queue contains $O(mn)$ boundary-connected cells.

#### Alternatives and edge cases

- **Run a search from every `O`:** repeats region work and can become quadratic in cell count.
- **Union-find:** is correct but stores more structure than one flood fill needs.
- **Flip all interior `O` cells:** fails when an interior cell connects to the boundary through a winding path.
- Boards with fewer than three rows or columns cannot contain a surrounded cell; the general flood-fill method still leaves them unchanged.
- Connectivity is four-directional. Diagonal contact with a safe cell does not preserve a region.

</details>
