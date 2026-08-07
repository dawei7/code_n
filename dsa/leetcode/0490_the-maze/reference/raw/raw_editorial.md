[TOC]

## Solution

---

### Overview

We are given a 2D `maze`. Each cell of `maze` represents an empty space or wall denoted by `0` and `1` respectively.

Our task is to determine whether the ball can travel from the `start` cell to the `destination` cell by rolling up, down, left, or right through the empty spaces.

It should be noted that the ball will continue to roll in the same direction until it hits a wall. We can only change the direction of the ball once it hits a wall and comes to a halt.

---

### Approach 1: Depth First Search

#### Intuition

The problem gives a 2D `maze` in which we can move in any of the four directions (left, top, right, and bottom) until we hit a wall. This 2D maze, in addition to permitting movement in any of the four directions, prompts us to consider describing the problem as a graph.

The 2D `maze` can be modelled as a directed graph. Each empty cell corresponds to a node in such a graph. We add four directed edges from an empty cell in all four directions (left, top, right, and bottom) to the cells to which the ball will roll if rolled in these four ways from the present cell.

Here's how the directed edges will look for the two highlighted cells `(3, 1)` and `(4, 4)` in the following maze where the yellow cells represent walls:

![img](images/490-1.png)

> The problem is now reduced to finding whether a path exists in this graph from the `start` cell to the `destination` cell.

We can use a graph traversal algorithm like depth-first search or breadth-first search to check if a path exists from the source node to the destination node. In this approach, we will solve the problem using DFS.

In DFS, we use a recursive function to explore nodes as far as possible along each branch. Upon reaching the end of a branch, we backtrack to the previous node and continue exploring the next branches.

Once we encounter an unvisited node, we will take one of its neighbor nodes (if exists) as the next node on this branch. Recursively call the function to take the next node as the 'starting node' and solve the subproblem.

If you are new to Depth First Search, please see our [Leetcode Explore Card](https://leetcode.com/explore/featured/card/graph/619/depth-first-search-in-graph/3882/) for more information on it!

We begin a DFS traversal from the `start` cell, treating it as a node. We determine which cells the ball will roll into until it strikes a wall in each of the four directions, and then we run the DFS recursively from these cells. We continue traversing in this fashion recursively until we reach the `destination` cell or there are no more unvisited cells.

To figure out which cell the ball will roll out of, we can keep travelling in that direction using a `while` loop until we reach a cell with a wall. The ball will roll to the preceding cell.

#### Algorithm

1. Create two variables, `m` and `n`, to store the number of rows and columns respectively in the given `maze`.
2. Create a 2D array called `visit` to keep track of visited cells.
3. We use the `dfs` function to perform the traversal. For each call, pass `m`, `n`, `maze`, `curr`, `destination` and `visit` as the parameters where `curr` corresponds to the current cell. The `dfs` function returns a boolean indicating whether a path exists between the `curr` and `destination` cells. We begin the DFS traversal from `start` and proceed as follows:
    - If the `curr` cell is already visited, we return `false` because we have already traversed this cell and could not reach `destination`.
    - If the `curr` cell is the same as `destination`, we return `true`.
    - Otherwise, mark `curr` as visited.
    - We create two arrays `dirX` and `dirY` of size `4` to help us iterate over the four directions.
    - We use a loop to go through all four directions. We create two variables `r = curr[0]` and `c = curr[1]` to move along a specific direction. We use a `while` loop and keep updating `r += dirX[i]` and `c = dirY[i]` as long as we don't go out of bounds or hit a wall. Once the `while` loop breaks, it means `r` and `c` form a cell that has a wall. Reverting the last move, i.e., `r - dirX[i]` and `r - dirY[i]` would give the cell to which the ball rolls. We recursively call `dfs` from cell `(r - dirX[i], c - dirY[i])`. If any DFS call returns `true`, we return `true` from the main call as we got a path to reach the `destination` cell.
4. There is no way to reach the `destination` cell, return `false`.

#### Implementation


```python
class Solution:
    def dfs(self, m, n, maze, curr, destination, visit):
        if visit[curr[0]][curr[1]]:
            return False
        if curr[0] == destination[0] and curr[1] == destination[1]:
            return True

        visit[curr[0]][curr[1]] = True
        dirX = [0, 1, 0, -1]
        dirY = [-1, 0, 1, 0]

        for i in range(4):
            r = curr[0]
            c = curr[1]
            # Move the ball in the chosen direction until it can.
            while r >= 0 and r < m and c >= 0 and c < n and maze[r][c] == 0:
                r += dirX[i]
                c += dirY[i]
            # Revert the last move to get the cell to which the ball rolls.
            if self.dfs(m, n, maze, [r - dirX[i], c - dirY[i]], destination, visit):
                return True
        return False

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        visit = [[False] * n for _ in range(m)]
        return self.dfs(m, n, maze, start, destination, visit)
```


#### Complexity Analysis

Here, $m$ and $n$ are the number of rows and columns in `maze`.

* Time complexity: $O(m \cdot n)$

    - Initializing the `visit` array takes $O(m \cdot n)$ time.
    - The function `dfs` visits each node at most once, resulting in $O(m \cdot n)$ calls. While each call involves rolling in four directions using while loops, the total rolling work across all calls is $O(m \cdot n)$ because each cell can only be traversed a constant number of times when considering all rolling operations together.

* Space complexity: $O(m \cdot n)$

    - The `visit` array takes $O(m \cdot n)$ space.
    - The recursion stack used by `dfs` can have no more than $O(m \cdot n)$ elements in the worst-case scenario. It would take up $O(m \cdot n)$ space in that case. 

---

### Approach 2: Breadth First Search

#### Intuition

As our task is to check if there exists a path from the `start` cell to the `destination` cell, we can use a breadth-first search (BFS) algorithm as well.

We can use a graph traversal algorithm like breadth-first search (BFS) to traverse over the islands. BFS is an algorithm for traversing or searching a graph. It traverses in a level-wise manner, i.e., all the nodes at the present level (say `l`) are explored before moving on to the nodes at the next level (`l + 1`), where a level's number is the distance from a starting node. BFS is implemented with a queue.

If you are not familiar with BFS traversal, we suggest you read our [Leetcode Explore Card](https://leetcode.com/explore/featured/card/graph/620/breadth-first-search-in-graph/).

Similar to a DFS traversal, we begin a BFS from the `start` cell, treating it as a node. We push `start` into the BFS queue. We determine which cells the ball will roll into until it strikes a wall in each of the four directions, and then push these cells into the BFS queue. We continue traversing in this fashion until we reach the `destination` cell or there are no more cells that can be visited.

#### Algorithm

1. Create two variables, `m` and `n`, to store the number of rows and columns respectively in the given `maze`.
2. Create a 2D array called `visit` to keep track of visited cells.
3. Create two arrays `dirX` and `dirY` of size `4` to help us iterate over the four directions.
4. Initialize a queue `q` of pair of integers.
5. We start the BFS traversal from the `start` cell by pushing it in the queue and marking it as visited.
6. While the queue is not empty, we perform the following:
    - We dequeue the first cell `curr` from the queue. If `curr == destination`, return `true`.
    - We use a loop to go through all four directions. We create two variables `r = curr[0]` and `c = curr[1]` to move along a specific direction. We use a `while` loop and keep updating `r += dirX[i]` and `c = dirY[i]` as long as we don't go out of bounds or hit a wall. Once the `while` loop breaks, it means `r` and `c` form a cell that has a wall. Reverting the last move, i.e., `r - dirX[i]` and `r - dirY[i]` would give the cell to which the ball rolls. Push the cell with coordinates `(r - dirX[i], c - dirY[i])` into the queue if it's not already visited.
7. There is no way to reach the `destination` cell, return `false`.

#### Implementation


```python
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        visit = [[False] * n for _ in range(m)]
        queue = deque()
        
        queue.append(start)
        visit[start[0]][start[1]] = True
        dirX = [0, 1, 0, -1]
        dirY = [-1, 0, 1, 0]

        while queue:
            curr = queue.popleft()
            if curr[0] == destination[0] and curr[1] == destination[1]:
                return True

            for i in range(4):
                r = curr[0]
                c = curr[1]
                # Move the ball in the chosen direction until it can.
                while r >= 0 and r < m and c >= 0 and c < n and maze[r][c] == 0:
                    r += dirX[i]
                    c += dirY[i]
                # Revert the last move to get the cell to which the ball rolls.
                r -= dirX[i]
                c -= dirY[i]
                if not visit[r][c]:
                    queue.append([r, c])
                    visit[r][c] = True
        return False
```


#### Complexity Analysis

Here, $m$ and $n$ are the number of rows and columns in `maze`.

* Time complexity: $O(m \cdot n)$

    - Initializing the `visit` array takes $O(m \cdot n)$ time.
    - Each queue operation in the BFS algorithm takes $O(1)$ time, and a single node can be pushed once, leading to $O(m \cdot n)$ operations for $m \cdot n$ nodes. While each dequeue involves rolling in four directions using while loops, the total rolling work across all BFS iterations is $O(m \cdot n)$ because each cell can only be traversed a constant number of times when considering all rolling operations together.

* Space complexity: $O(m \cdot n)$

    - The `visit` array takes $O(m \cdot n)$ space.
    - The BFS queue takes $O(m \cdot n)$ space in the worst-case because each node is added once.