# Regions Cut By Slashes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 959 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Depth-First Search, Breadth-First Search, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [regions-cut-by-slashes](https://leetcode.com/problems/regions-cut-by-slashes/) |

## Problem Description

### Goal

An $N\times N$ grid is made of unit squares. Every square contains either a forward slash `/`, a backslash `\`, or a blank space. A slash divides its square diagonally, while a blank leaves the square undivided.

The drawn segments and the outer boundary partition the grid into contiguous regions. Given the rows as `grid`, count all resulting regions. In serialized string data a backslash is escaped, but it represents one diagonal character in the corresponding square.

### Function Contract

**Inputs**

- `grid`: an $N\times N$ list of strings, where $1 \le N \le 30$.
- Every character is `/`, `\`, or a space.

**Return value**

Return the number of connected regions created by the diagonals and blank squares.

### Examples

**Example 1**

- Input: `grid = [" /","/ "]`
- Output: `2`

**Example 2**

- Input: `grid = [" /","  "]`
- Output: `1`

**Example 3**

- Input: `grid = ["/\\","\\/"]`
- Output: `5`

### Required Complexity

- **Time:** $O(N^2)$
- **Space:** $O(N^2)$

<details>
<summary>Approach</summary>

#### General

**Replace geometry with ordinary grid connectivity.** Expand every original square into a $3\times3$ block. A forward slash blocks the three pixels `(0,2)`, `(1,1)`, and `(2,0)` within its block; a backslash blocks `(0,0)`, `(1,1)`, and `(2,2)`. A blank blocks nothing.

**Why three pixels are enough.** Each diagonal becomes a continuous one-pixel barrier from one corner of its expanded block to the opposite corner. Neighboring blocks meet along full pixel edges, so barriers connect at shared corners without accidentally sealing a blank passage or allowing movement through a slash.

**Count open connected components.** Scan the expanded board. Whenever an unblocked, unvisited pixel is found, increment the region count and flood fill through its four-directionally adjacent open pixels. Every geometric region contains exactly one such open component, and no flood fill crosses a drawn diagonal, so the component count equals the requested number of regions.

#### Complexity detail

The expanded board has $9N^2$ pixels. Marking barriers, scanning pixels, and flood filling each open pixel once all take $O(N^2)$ time. The board, visited state, and flood-fill stack use $O(N^2)$ space.

#### Alternatives and edge cases

- **Four triangles per square:** Split each cell into top, right, bottom, and left triangles, union triangles according to its character, and union adjacent cells. This also runs in $O(N^2)$ time and space.
- **Planar cycle counting:** Union lattice-point endpoints of each diagonal and count every edge that closes a cycle. This is compact but requires careful treatment of the shared outer boundary.
- **Global neighbor search:** During flood fill, scan every expanded pixel to locate the current pixel's four neighbors. It remains correct but raises runtime to $O(N^4)$.
- **Blank grid:** With no barriers, every square belongs to one region.
- **One slash:** A slash in a single cell divides it into two regions.
- **Escaped backslash:** A source literal may contain `"\\"`, but the grid cell contains one backslash character.

</details>
