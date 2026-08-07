[TOC]

## Solution

---

### Overview

We are given a binary grid where each cell represents either land (1) or water (0). Each day, we can convert any single land cell to a water cell. Our task is to determine the minimum number of days required to modify the grid such that it either:

- Contains no islands, or
- Contains more than one island.

An island is a maximal group of horizontally or vertically connected land cells.

In this article, we will explore the applications of the Flood-Fill Algorithm, Tarjan's Algorithm, and Articulation Points, focusing on their practical uses rather than their fundamental principles. If you are unfamiliar with these algorithms, please refer to the foundational materials for a comprehensive understanding:

1. [Flood-Fill Algorithm](https://leetcode.com/problems/flood-fill/description/)
2. [Tarjan's Algorithm and Articulation Points](https://leetcode.com/problems/critical-connections-in-a-network/editorial/)
    
---

### Approach 1: Brute Force

#### Intuition

The binary grid can initially be in one of three states:
1. No islands (all cells are water).
2. One island.
3. More than one island.

We only need to modify the grid in the second case, aiming to reach either the first or third state with minimal changes.

A brute force approach would involve flipping each land cell one by one to achieve the desired conditions. However, this could generate up to $2^{30}$ states, which will not satisfy the problem constraints. 

To reduce this complexity, we can identify a pattern. The most effective way to split an island into two parts is to find the thinnest cross-section and change those cells to water. In a binary grid, even for uniform shapes like squares or circles, the thinnest cross-section comprises at most 2 squares. Examples can be seen here:

![two flips are enough](images/two_is_enough.png)

First, we should determine if the grid already satisfies the conditions (zero or more than one island). If so, we can immediately return 0.

To check if we can meet the conditions in 1 step, we systematically flip each island cell to water and evaluate the resulting configuration. We iterate over each cell in the grid, temporarily changing it to water, and use a `countIslands` function to determine the number of islands in the modified grid. When we encounter a land cell, we use the [flood-fill algorithm](https://en.wikipedia.org/wiki/Flood_fill) to count the entire island. The total number of flood-fill calls indicates the number of islands.

If removing one land cell does not achieve the goal, the only remaining option is to return 2.

#### Algorithm

- Define an array `DIRECTIONS` that contain the directions for moving right, left, down, and up.

Main method `minDays`:

- Set `rows` and `cols` as the number of rows and columns in `grid`.
- Initialize a variable `initialIslandCount` and set it to the initial number of islands in the grid by calling the `countIslands` method. 
- Check if `initialIslandCount` is not equal to `1` (i.e. the island is already disconnected):
  - If `true`, return `0`.
- Iterate through each cell `(row, col)` of the grid:
  - If the cell is water, skip it.
  - Set `grid[row][col]` to `0`.
  - Find the `newIslandCount` by calling `countIslands`.
  - If `newIslandCount` is not equal to `1`, return `1`.
  - Set  `grid[row][col]` back to `1`.
- Return `2`.
  
Helper method `countIslands`:

- Define a method `countIslands` with parameter: the `grid`.
- Initialize:
  - `rows` and `cols` as the number of rows and columns in the `grid`.
  - a boolean array `visited` to track visited cells.
  - a variable `islandCount` set to `0`.
- Iterate through each cell `(row, col)` of the `grid`:
  - If the cell has not been visited and its value is `1`:  
    - Call `exploreIsland` on `(row, col)`.
    - Increment `islandCount`.
- Return `islandCount`.

Helper method `exploreIsland`:

- Define a method `exploreIsland` with parameters: `grid`, the `row` and `col` indices, and the `visited` array.
- Set `visited[row][col]` to `true`.
- For each `direction` in `DIRECTIONS`:
  - Set `newRow` to `row + direction[0]`.
  - Set `newCol` to `col + direction[1]`.
  - Check if the `(newRow, newCol)` is valid using `isValidLandCell`:
    - If `true`, call `exploreIsland` on `(newRow, newCol)`.

Helper method `isValidLandCell`:

- Define a method `isValidLandCell` with parameters: `grid`, the `row` and `col` indices, and the `visited` array.
- Return `true` if the cell is within the `grid` bounds, `grid[row][col]` is `1` and has not been visited yet.
- Else, return `false`.

#### Implementation


```python
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def _count_islands():
            visited = set()
            count = 0
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        _explore_island(i, j, visited)
                        count += 1
            return count

        def _explore_island(i, j, visited):
            if (
                i < 0
                or i >= rows
                or j < 0
                or j >= cols
                or grid[i][j] == 0
                or (i, j) in visited
            ):
                return
            visited.add((i, j))
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                _explore_island(i + di, j + dj, visited)

        # Check if already disconnected
        if _count_islands() != 1:
            return 0

        # Check if can be disconnected in 1 day
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if _count_islands() != 1:
                        return 1
                    grid[i][j] = 1

        # If can't be disconnected in 0 or 1 day, return 2
        return 2
```


#### Complexity Analysis

Let $m$ be the number of rows and $n$ be the number of columns in the `grid`.

- Time complexity: $O((m \cdot n)^2)$

    The main operation in this algorithm is the `countIslands` function, which is called multiple times. `countIslands` in turn calls the `exploreIslands` method, which performs a depth-first search on the grid. The DFS in the worst case can explore all the cells in the grid, resulting in a time complexity of $O(m \cdot n)$.

    The `countIslands` method may be called a maximum of $1 + m \cdot n$ times.

    Thus, the overall time complexity of the algorithm is $O((m \cdot n) \cdot (1 + m \cdot n))$, which simplifies to $O((m \cdot n)^2)$.

- Space complexity: $O(m \cdot n)$

    The main space usage comes from the `visited` array in the `countIslands` function, which has a size of $m \times n$.

    The recursive call stack in the DFS (`exploreIsland` function) can go as deep as $m \cdot n$ in the worst case.

    Therefore, the space complexity of the algorithm is $O(m \cdot n)$.  

---

### Approach 2: Tarjan's Algorithm

#### Intuition

An articulation point is a cell that will split an island in two when it is changed from land to water. If a given grid has an articulation point, we can disconnect the island in one day. Tarjan's algorithm efficiently finds articulation points in a graph.

The algorithm uses three key pieces of information for each node (cell): discovery time, lowest reachable time, and parent. The discovery time is when a node is first visited during the DFS. The lowest reachable time is the minimum discovery time of any node that can be reached from the subtree rooted at the current node, including the current node itself. The parent is the node from which the current node was discovered during the DFS.

A node can be an articulation point in two cases:
1. A non-root node is an articulation point if it has a child whose lowest reachable time is greater than or equal to the node's discovery time. This condition means that the child (and its subtree) cannot reach any ancestor of the current node without going through the current node, making it critical for connectivity.
2. The root node of the DFS tree is an articulation point if it has more than one child. Removing the root would disconnect these children from each other.

If no articulation points are found, the grid cannot be disconnected by removing a single land cell. In that case, we return 2.

#### Algorithm
 
- Define a constant array `DIRECTIONS` that contains the directions for moving right, down, left, and up.

Main method `minDays`:

- Set `rows` and `cols` as the number of rows and columns in the `grid`.
- Initialize an `ArticulationPointInfo` object `apInfo` with `hasArticulationPoint` set to `false` and `time` set to `0`.
- Initialize variables:
  - `landCells` to count the number of land cells in the grid.
  - `islandCount` to count the number of islands in the grid.
- Initialize arrays `discoveryTime`, `lowestReachable`, and `parentCell` with default values of `-1`. These arrays store information about each cell during DFS traversal.
- Loop through each cell `(i, j)` of the `grid`:
  - If the cell is land (`1`):
    - Increment the `landCells` count.
    - If the cell has not been visited (`discoveryTime[i][j]` = `-1`):
      - Call `findArticulationPoints` on `(i, j)` to find if articulation point exists.
      - Increment `islandCount`.
- If there is zero or more than one island, return `0`
- If there is only one land cell, return `1`.
- If there is an articulation point, return `1`.
- Otherwise, return `2`.

Helper method `findArticulationPoints`:

- Define a method `findArticulationPoints` with parameters: `grid`, the `row` and `col` indices, `discoveryTime`, `lowestReachable`, `parentCell`, and `apInfo`.
- Set `rows` and `cols` as the number of rows and columns in the `grid`.
- Set `discoveryTime` of the current cell to `apInfo.time`.
- Increment the `time` in `apInfo`.
- Set the `lowestReachable` time of the current cell to its `discoveryTime`.
- Initialize a variable `children` to count the number of child nodes in the DFS tree.
- To explore adjacent cells, loop through each `direction` in `DIRECTIONS`:
  - Calculate `newRow` as `row + direction[0]`.
  - Calculate `newCol` as `col + direction[1]`.
  - If `(newRow, newCol)` is a valid cell:
    - If the `discoveryTime` of the new cell is `-1`:
      - Increment `children`.
      - Set the `parentCell` of the new cell to the current cell.
      - Recursively call `findArticulationPoints` for the new cell.
      - Update the `lowestReachable` time for the current cell to the minimum of `lowestReachable[row][col]` and `lowestReachable[newRow][newCol]`.
      - If `lowestReachable` of `(newRow, newCol)` is greater than or equal to `discoveryTime` of `(row, col)`, and `(row, col)` has a parent:
        - Set `hasArticulationPoint` of `apInfo` to `true`.
    - Else if `(newRow, newCol)` is not the parent of `(row, col)`:
        - Set `lowestReachable` time of `(row, col)` to the minimum of `lowestReachable[row][col]` and `discoveryTime[newRow][newCol]`.
- Check if `(row, col)` is the root of the DFS tree and has more than 1 `children`:
  - Set `hasArticulationPoint` of `apInfo` to `true`.

Helper method `isValidLandCell`:

- Define a method `isValidLandCell` with parameters: `grid`, and the `row` and `col` indices.
- Return `true` if the given cell is within the bounds of the grid and is a land cell (`1`).
- Else, return `false`.

Helper class `ArticulationPointInfo`:

- Define a class `ArticulationPointInfo` with fields: `hasArticulationPoint` and `time`.
- Override the default constructor to initialize `hasArticulationPoint` and `time`.

#### Implementation


```python
class Solution:
    # Directions for adjacent cells: right, down, left, up
    DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def minDays(self, grid):
        rows, cols = len(grid), len(grid[0])
        ap_info = {"has_articulation_point": False, "time": 0}
        land_cells = 0
        island_count = 0

        # Arrays to store information for each cell
        discovery_time = [
            [-1] * cols for _ in range(rows)
        ]  # Time when a cell is first discovered
        lowest_reachable = [
            [-1] * cols for _ in range(rows)
        ]  # Lowest discovery time reachable from the subtree rooted at this cell
        parent_cell = [
            [-1] * cols for _ in range(rows)
        ]  # Parent of each cell in DFS tree

        def _find_articulation_points(row, col):
            discovery_time[row][col] = ap_info["time"]
            ap_info["time"] += 1
            lowest_reachable[row][col] = discovery_time[row][col]
            children = 0

            # Explore all adjacent cells
            for direction in self.DIRECTIONS:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and grid[new_row][new_col] == 1
                ):
                    if discovery_time[new_row][new_col] == -1:
                        children += 1
                        parent_cell[new_row][new_col] = (
                            row * cols + col
                        )  # Set parent
                        _find_articulation_points(new_row, new_col)

                        # Update lowest reachable time
                        lowest_reachable[row][col] = min(
                            lowest_reachable[row][col],
                            lowest_reachable[new_row][new_col],
                        )

                        # Check for articulation point condition
                        if (
                            lowest_reachable[new_row][new_col]
                            >= discovery_time[row][col]
                            and parent_cell[row][col] != -1
                        ):
                            ap_info["has_articulation_point"] = True
                    elif new_row * cols + new_col != parent_cell[row][col]:
                        # Update lowest reachable time for back edge
                        lowest_reachable[row][col] = min(
                            lowest_reachable[row][col],
                            discovery_time[new_row][new_col],
                        )

            # Root of DFS tree is an articulation point if it has more than one child
            if parent_cell[row][col] == -1 and children > 1:
                ap_info["has_articulation_point"] = True

        # Traverse the grid to find islands and articulation points
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    land_cells += 1
                    if discovery_time[i][j] == -1:  # If not yet visited
                        # Start DFS for a new island
                        _find_articulation_points(i, j)
                        island_count += 1

        # Determine the minimum number of days to disconnect the grid
        if island_count == 0 or island_count >= 2:
            return 0  # Already disconnected or no land
        if land_cells == 1:
            return 1  # Only one land cell
        if ap_info["has_articulation_point"]:
            return 1  # An articulation point exists
        return 2  # Need to remove any two land cells
```


#### Complexity Analysis

Let $m$ be the number of rows and $n$ be the number of columns in the `grid`.

* Time complexity: $O(m \cdot n)$

    Initializing the arrays `discoveryTime`, `lowestReachable`, and `parentCell` takes $O(m \cdot n)$ time each.

    The DFS traversal by the `findArticulationPoints` method visits each cell exactly once, taking $O(m \cdot n)$ time.

    Thus, the overall time complexity of the algorithm is $O(m \cdot n)$.

* Space complexity: $O(m \cdot n)$

    The arrays `discoveryTime`, `lowestReachable`, and `parentCell` each take $O(m \cdot n)$ space.

    The recursive call stack for the DFS traversal can go as deep as the number of land cells in the worst case. If all cells are land, the depth of the recursive call stack can be $O(m \cdot n)$.

    Thus, the total space complexity of the algorithm is $O(m \cdot n) + O(m \cdot n) = O(m \cdot n)$.

---