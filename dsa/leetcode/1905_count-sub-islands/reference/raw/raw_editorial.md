[TOC]

## Solution

--- 

### Overview

We are given two binary matrices, `grid1` and `grid2`, both of size `m x n`, where 1 represents land and 0 represents water. An island is a group of connected 1s, connected horizontally or vertically. The task is to find how many islands in `grid2` are also sub-islands of `grid1`. An island in `grid2` is considered a sub-island if every land cell of the island is part of an island in `grid1`.

![slide1a](images/Slide-1a.png)

<br />

If we overlap this image with `grid1`, we can see all the land cells of the island of `grid2` lie on one island in grid1.

![slide1b](images/Slide-1b.png)

<br />

Let's consider another island of the `grid2`, now, is this a sub-island?

![slide1c](images/Slide-1c.png)

<br />

If we overlap this image with `grid1`, we can see two land cells are lying on the water cell, thus this island can't be considered a sub-island.

![slide1d](images/Slide-1d.png)

<br />

The above images hint that; to check whether an island of `grid2` is a sub-island in `grid1`, we can start traversing on each land cell of the current island of `grid2` and for each land cell there should be a land cell in `grid1` at the same position (at same `(x, y)` index in grids).

Each grid cell is connected to its adjacent neighbors 4-directionally (horizontal or vertical), this grid problem can be visualized as a graph traversal problem, where each cell is a node and the 4-directions are edges connecting those nodes.

![slide1e](images/Slide-1e.png)

<br />

We will iterate on each cell of the `grid2`, if the current cell is a land cell we traverse the whole island of `grid2` containing the current land cell. While traversing over the entire island we keep track if, for each land cell of the island of `grid2`, the `grid1` also has a land cell at the respective position using a boolean variable. After iteration on the current island is completed this boolean variable will denote if the island is a sub-island or not.

<br />

The following slideshow will give you an idea about this approach:

!?!../Documents/1905/slideshow1.json:1900,1600!?!

There are different techniques to traverse a graph, in this article we will cover some of them in brief, we assume you already have a good knowledge about them,     
if you are new to the graph traversal algorithms we recommend you read the following Leetcode articles before proceeding:
- [Breadth-First Search](https://leetcode.com/explore/learn/card/graph/620/breadth-first-search-in-graph/3883/)
- [Depth-First Search](https://leetcode.com/explore/learn/card/graph/619/depth-first-search-in-graph/3882/)
- [Union Find](https://leetcode.com/discuss/general-discussion/1072418/Disjoint-Set-Union-(DSU)Union-Find-A-Complete-Guide)

---

### Approach 1: Breadth-First Search (BFS)

#### Intuition

Breadth-first search is used to traverse graphs level by level, and in this problem, each cell in the grid represents a node, with 4-directional connections as edges. In this context, each cell in the grid represents a node, and the horizontal and vertical connections between cells are the edges. The goal is to check if an island in `grid2` is a sub-island of `grid1`. We start BFS from each unvisited land cell in `grid2` and verify if all corresponding cells in `grid1` are also land cells. If we encounter a land cell in `grid2` where the corresponding cell in `grid1` is water, the island in `grid2` is not a sub-island.

We iterate through each cell in `grid2`, initiating BFS from each unvisited land cell to explore the island. During the traversal, we use a boolean flag `isSubIsland` to track if all corresponding cells in `grid1` are land. If the flag remains `true` after the traversal, we increment our sub-island count.

#### Algorithm

1. Create an array of `directions` storing the up, down, left, and right direction movements which is the change in the `(x, y)` position value of the cell while moving.
2. Create a helper method `isCellLand(x, y, grid)` which returns a boolean value indicating whether the cell at position `(x, y)` in `grid` is a land cell or not.
3. Create a helper method `isSubIsland(x, y, grid1, grid2, visited)` which returns a boolean value indicating whether the island of `grid2` containing cell at position `(x, y)` is a sub-island in `grid1` or not. This method will utilize the BFS algorithm to traverse all cells of the island of the `grid2`:
    - Initialize a variable `isSubIsland` to `true`, indicating whether the island of `grid2` is a sub-island or not.
    - Initialize a queue, push the starting cell `(x, y)` in queue and mark it as visited.
    - While the queue is not empty:
        - Pop the current cell from the queue.
        - If the cell in `grid1` at the same position as the current cell of `grid2` is not a land cell then this island can't be a sub-island so we will mark the `isSubIsland` flag as `false`.
        - Next, we move in all 4 directions one by one using the `directions` array. If the cell at the next position `(nextX, nextY)` lies inside the `grid2`, was not visited earlier, and is also a land cell, then we will traverse on this cell, hence, push it in the queue and mark it as visited. 
    - When we traverse all cells of the current island we return `isSubIsland`.
4. Initialize a boolean `visited` matrix of the same size as the `grid2` matrix to mark visited land cells.
5. Initialize a variable `subIslandsCount` to `0`, to count the total number of islands in `grid2` which are also sub-islands.
6. Iterate on all cells of the `grid2` using nested for loop, if the current cell is never visited, is a land cell in `grid2`, and is a sub-island then increment the `subIslandsCount` by `1`.
7. At the end return, `subIslandsCount`. 

#### Implementation


```python
class Solution:
    # Directions in which we can traverse inside the grids.
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Helper method to check if the cell at the position (x, y) in the 'grid'
    # is a land cell.
    def is_cell_land(self, x, y, grid):
        return grid[x][y] == 1

    # Traverse all cells of island starting at position (x, y) in 'grid2',
    # and check this island is a sub-island in 'grid1'.
    def is_sub_island(self, x, y, grid1, grid2, visited):
        total_rows = len(grid2)
        total_cols = len(grid2[0])

        is_sub_island = True

        pending_cells = deque()
        # Push the starting cell in the queue and mark it as visited.
        pending_cells.append((x, y))
        visited[x][y] = True

        # Traverse on all cells using the breadth-first search method.
        while pending_cells:
            curr_x, curr_y = pending_cells.popleft()

            # If the current position cell is not a land cell in 'grid1',
            # then the current island can't be a sub-island.
            if not self.is_cell_land(curr_x, curr_y, grid1):
                is_sub_island = False

            for direction in self.directions:
                next_x = curr_x + direction[0]
                next_y = curr_y + direction[1]
                # If the next cell is inside 'grid2', is never visited and
                # is a land cell, then we traverse to the next cell.
                if (
                    0 <= next_x < total_rows
                    and 0 <= next_y < total_cols
                    and not visited[next_x][next_y]
                    and self.is_cell_land(next_x, next_y, grid2)
                ):
                    # Push the next cell in the queue and mark it as visited.
                    pending_cells.append((next_x, next_y))
                    visited[next_x][next_y] = True
        return is_sub_island

    def countSubIslands(
        self, grid1: List[List[int]], grid2: List[List[int]]
    ) -> int:
        total_rows = len(grid2)
        total_cols = len(grid2[0])

        visited = [[False] * total_cols for _ in range(total_rows)]
        sub_island_counts = 0

        # Iterate on each cell in 'grid2'
        for x in range(total_rows):
            for y in range(total_cols):
                # If cell at the position (x, y) in the 'grid2' is not visited,
                # is a land cell in 'grid2', and the island
                # starting from this cell is a sub-island in 'grid1', then we
                # increment the count of sub-islands.
                if (
                    not visited[x][y]
                    and self.is_cell_land(x, y, grid2)
                    and self.is_sub_island(x, y, grid1, grid2, visited)
                ):
                    sub_island_counts += 1

        # Return total count of sub-islands.
        return sub_island_counts
```


#### Complexity Analysis

Let $m$ and $n$ represent the number of rows and columns, respectively.

* Time complexity: $O(m * n)$

    We iterate on each grid cell and perform BFS to traverse all land cells of all the islands. Each land cell is only traversed once. In the worst case, we may traverse all cells of the grid.

    Thus, in the worst case time complexity will be $O(m * n)$.

* Space complexity: $O(m * n)$    

    We create an additional grid `visited` of size $m * n$ and push the land cells in the queue.

    Thus, in the worst case space complexity will be $O(m * n)$.

---

### Approach 2: Depth-First Search

#### Intuition

Depth-first search (DFS) explores as far as possible along each branch before backtracking, making it effective for checking if an island in `grid2` is a sub-island of `grid1`. 

We start by iterating through each cell in `grid2`. Upon encountering an unvisited land cell, we initiate a DFS to mark all connected land cells as visited. During the traversal, we compare each cell in `grid2` with the corresponding cell in `grid1`. If any land cell in `grid2` maps to a water cell in `grid1`, the island is disqualified. If the island passes the check, it is counted as a sub-island.

DFS is ideal for this task because it efficiently handles deep, recursive exploration, avoiding the need for additional data structures like a queue.

#### Algorithm

1. Create an array `directions` for the four movement directions: up, down, left, and right, representing changes in `(x, y)` coordinates.
2. Define a helper method `isCellLand(x, y, grid)` to check if the cell at `(x, y)` in `grid` is a land cell.
3. Define a helper method `isSubIsland(x, y, grid1, grid2, visited)` to determine if the island in `grid2` containing cell `(x, y)` is a sub-island of `grid1`. This method uses DFS to:
    - Initialize `isSubIsland` as `true`.
    - Check if the corresponding cell in `grid1` is land; if not, set `isSubIsland` to `false`.
    - Move in all four directions. For each valid, unvisited land cell in `grid2`, recursively check if it’s part of a sub-island and update `isSubIsland` accordingly.
    - Return `isSubIsland` after traversing the island.
4. Initialize a boolean `visited` matrix of the same size as `grid2` to keep track of visited cells.
5. Initialize `subIslandsCount` to `0` to count sub-islands.
6. Iterate through all cells of `grid2`. For each unvisited land cell, use `isSubIsland` to check if it's a sub-island of `grid1`. Increment `subIslandsCount` if it is.
7. Return `subIslandsCount`.

#### Implementation


```python
class Solution:
    # Directions in which we can traverse inside the grids.
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Helper method to check if the cell at the position (x, y) in the 'grid'
    # is a land cell.
    def is_cell_land(self, x, y, grid):
        return grid[x][y] == 1

    # Traverse all cells of island starting at position (x, y) in 'grid2',
    # and check if this island is a sub-island in 'grid1'.
    def is_sub_island(self, x, y, grid1, grid2, visited):
        total_rows = len(grid2)
        total_cols = len(grid2[0])
        # Traverse on all cells using the depth-first search method.
        is_sub_island = True

        # If the current cell is not a land cell in 'grid1', then the current island can't be a sub-island.
        if not self.is_cell_land(x, y, grid1):
            is_sub_island = False

        # Traverse on all adjacent cells.
        for direction in self.directions:
            next_x = x + direction[0]
            next_y = y + direction[1]
            # If the next cell is inside 'grid2', is not visited, and is a land cell,
            # then we traverse to the next cell.
            if (
                0 <= next_x < total_rows
                and 0 <= next_y < total_cols
                and not visited[next_x][next_y]
                and self.is_cell_land(next_x, next_y, grid2)
            ):
                # Mark the next cell as visited.
                visited[next_x][next_y] = True
                next_cell_is_part_of_sub_island = self.is_sub_island(
                    next_x, next_y, grid1, grid2, visited
                )
                is_sub_island = (
                    is_sub_island and next_cell_is_part_of_sub_island
                )
        return is_sub_island

    def countSubIslands(
        self, grid1: List[List[int]], grid2: List[List[int]]
    ) -> int:
        total_rows = len(grid2)
        total_cols = len(grid2[0])

        visited = [[False] * total_cols for _ in range(total_rows)]
        sub_island_counts = 0

        # Iterate over each cell in 'grid2'.
        for x in range(total_rows):
            for y in range(total_cols):
                # If the cell at position (x, y) in 'grid2' is not visited,
                # is a land cell in 'grid2', and the island starting from this cell is a sub-island in 'grid1',
                # then increment the count of sub-islands.
                if not visited[x][y] and self.is_cell_land(x, y, grid2):
                    visited[x][y] = True
                    if self.is_sub_island(x, y, grid1, grid2, visited):
                        sub_island_counts += 1

        # Return total count of sub-islands.
        return sub_island_counts
```


#### Complexity Analysis

Let $m$ and $n$ represent the number of rows and columns, respectively.

* Time complexity: $O(m * n)$

    We iterate on each grid cell and perform DFS to traverse all land cells of all the islands. Each land cell is only traversed once. In the worst case, we may traverse all cells of the grid. 

    Thus, in the worst case time complexity will be $O(m * n)$.

* Space complexity: $O(m * n)$

    We create an additional grid `visited` of size $m * n$ and push the land cells in the recursive stack. 

    Thus, in the worst case space complexity will be $O(m * n)$.

---

### Approach 3: Union-Find

#### Intuition

Union-Find, or Disjoint Set Union (DSU), is a data structure that efficiently manages disjoint subsets, supporting quick union and find operations. It’s well-suited for problems where you need to determine if elements are in the same subset or to merge subsets. The key idea is to treat each island as a separate set and unite these sets based on connectivity.

In the context of this problem, we start by representing each land cell in both grids as a node in a graph. The main challenge is to determine whether an island in `grid2` is a sub-island of `grid1`, which means all cells of an island in `grid2` must also belong to the corresponding island in `grid1`. To implement this, we can follow these steps:

First, we initialize a Union-Find data structure where each cell initially belongs to its own set. As we iterate through the grid, we union adjacent land cells (cells with value `1`) in `grid2`. This results in a partitioning of the grid into distinct islands, where each island is represented by its parent node in the Union-Find structure.

After unionizing all possible cells within each grid, the next step is to compare the islands in `grid2` with the corresponding islands in `grid1`. As we discussed in the overview section, for each land cell in `grid2` there should be a corresponding land cell at the same position in `grid1` as well. If any land cell in an island of `grid2` does not have a corresponding land cell in `grid1`, the entire island containing that land cell is disqualified as a sub-island and we mark the parent cell of that island of `grid2` as not a sub-island.

Union-Find allows us to efficiently manage and compare these islands by providing quick union operations to group cells and find operations to identify the root of any given cell. Additionally, the process is optimized by two key techniques: path compression and union by rank. Path compression ensures that during the find operation, each node on the path to the root directly connects to the root, making future find operations faster. Union by rank helps to keep the tree representing each set shallow by always attaching the smaller tree under the root of the larger tree during union operations.

By the end of the process, the number of valid sub-islands can be determined by counting how many islands in `grid2` satisfy the condition of being entirely contained within the corresponding islands in `grid1`.

#### Algorithm

1. Create an array of `directions` storing the up, down, left, and right direction movements which is the change in the `(x, y)` position value of the cell while moving.
2. Create a helper method `isCellLand(x, y, grid)` which returns a boolean value indicating whether the cell at position `(x, y)` in `grid` is a land cell or not.
3. Create a class `UnionFind` which initialized two arrays `rank` and `parent` with size `n`. Initially rank of all elements is `0` and the parent is the element itself.
    - Create a method `int find(int u)`, which returns the `parent` of element `u` using the path compression technique.
    - Create a method `void unionSets(int u, int v)`, which joins two components of elements `u` and `v` into one based on their parent's ranks. 
4. Create a helper method `convertToIndex(int x, int y, int totalCols)` which converts and returns the 2-dimensional position to a 1-dimensional index.
5. Initialize a `UnionFind` object `uf` with size the same as `grid2`.
6. Iterate on all land cells of the `grid2` using nested for loop, and join the adjacent cells to the current land cell if they are also a land cell.
7. Initialize a boolean array `isSubIsland` with the size same as `grid2` initially storing `true`.
8. Iterate on all land cells of the `grid2` and if the respective cell in the `grid1` isn't a land cell then mark the `parent` node of the current land cell's island as `false` in the `isSubIsland` array.
9. Iterate on all land cells of the `grid2` and if `isSubIsland` for the parent cell is `true` count the sub-island, i.e. increment `subIslandsCount` by `1` and mark it as `false` to prevent counting it multiple times.
10. At the end return, `subIslandsCount`. 

#### Implementation


```python
class Solution:
    # Directions in which we can traverse inside the grids.
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Helper method to check if the cell at the position (x, y) in the 'grid'
    # is a land cell.
    def is_cell_land(self, x, y, grid):
        return grid[x][y] == 1

    # Union-Find class.
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n

        # Find the root of element 'u', using the path-compression technique.
        def find(self, u):
            if self.parent[u] != u:
                self.parent[u] = self.find(self.parent[u])
            return self.parent[u]

        # Union two components of elements 'u' and 'v' respectively based on their ranks.
        def union_sets(self, u, v):
            root_u = self.find(u)
            root_v = self.find(v)
            if root_u != root_v:
                if self.rank[root_u] > self.rank[root_v]:
                    self.parent[root_v] = root_u
                elif self.rank[root_u] < self.rank[root_v]:
                    self.parent[root_u] = root_v
                else:
                    self.parent[root_v] = root_u
                    self.rank[root_u] += 1

    # Helper method to convert (x, y) position to a 1-dimensional index.
    def convert_to_index(self, x, y, total_cols):
        return x * total_cols + y

    def countSubIslands(
        self, grid1: List[List[int]], grid2: List[List[int]]
    ) -> int:
        total_rows = len(grid2)
        total_cols = len(grid2[0])
        uf = self.UnionFind(total_rows * total_cols)

        # Traverse each land cell of 'grid2'.
        for x in range(total_rows):
            for y in range(total_cols):
                if self.is_cell_land(x, y, grid2):
                    # Union adjacent land cells with the current land cell.
                    for direction in self.directions:
                        next_x = x + direction[0]
                        next_y = y + direction[1]
                        if (
                            0 <= next_x < total_rows
                            and 0 <= next_y < total_cols
                            and self.is_cell_land(next_x, next_y, grid2)
                        ):
                            uf.union_sets(
                                self.convert_to_index(x, y, total_cols),
                                self.convert_to_index(
                                    next_x, next_y, total_cols
                                ),
                            )

        # Traverse 'grid2' land cells and mark that cell's root as not a sub-island
        # if the land cell is not present at the respective position in 'grid1'.
        is_sub_island = [True] * (total_rows * total_cols)
        for x in range(total_rows):
            for y in range(total_cols):
                if self.is_cell_land(x, y, grid2) and not self.is_cell_land(
                    x, y, grid1
                ):
                    root = uf.find(self.convert_to_index(x, y, total_cols))
                    is_sub_island[root] = False

        # Count all the sub-islands.
        sub_island_counts = 0
        for x in range(total_rows):
            for y in range(total_cols):
                if self.is_cell_land(x, y, grid2):
                    root = uf.find(self.convert_to_index(x, y, total_cols))
                    if is_sub_island[root]:
                        sub_island_counts += 1
                        # One cell can be the root of multiple land cells, so to
                        # avoid counting the same island multiple times, mark it as false.
                        is_sub_island[root] = False

        return sub_island_counts
```


#### Complexity Analysis

Let $m$ and $n$ represent the number of rows and columns, respectively.

* Time complexity: $O(m * n)$

    We iterate on each land cell of the grid and perform union operations with its adjacent cells. In the worst case, we may traverse all cells of the grid. 

    Thus, in the worst case time complexity will be $O(m * n)$.

* Space complexity: $O(m * n)$    

    We create an additional object `uf` and a boolean array `isSubIsland` of size $m * n$.
    
    Thus, in the worst case space complexity will be $O(m * n)$.