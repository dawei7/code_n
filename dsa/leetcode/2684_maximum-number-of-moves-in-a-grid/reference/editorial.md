## Solution

---

### Overview

We have an `M x N` matrix called `grid`, filled with positive integers. The challenge is to start from any cell in the first column and find out how many moves we can make to the right while following specific rules.

From any cell `(i, j)` in the first column, we can move to the next column in one of three ways:
1. Directly right to the cell $(i, j + 1)$.
2. Diagonally up-right to the cell $(i - 1, j + 1)$.
3. Diagonally down-right to the cell $(i + 1, j + 1)$.

However, there's an important condition: we can only make a move if the value in the destination cell is greater than the value in the current cell.

Our goal is to determine the maximum number of moves we can make, starting from any cell in the first column.

![fig](images/2684A.png)

---

### Approach 1: Breadth-First Search (BFS)

#### Intuition

Let's consider the scenario with a single starting point from the first column. To solve the problem, the most intuitive approach is to explore the possible cells (those with a greater value) from the current cell and continue moving until there are no further options. The maximum number of moves made during this process would be our answer. In this case, we would track the cells we have visited to ensure that each cell is not visited more than once.

However, tracking visited cells raises a question: is it possible to reach the same cell from different starting points with different numbers of moves? If so, we would need to revisit a cell for each starting point to find the maximum move count. We can prove that this is not possible. The number of moves required to reach a particular cell from different starting points would always be the same. This is because, in each move, the column index strictly increases (as we move from a cell in column `j` to a cell in column $j + 1$). Therefore, reaching cell `(i, j)` from any starting cell in the first column (say `(x, 0)`) requires exactly `j` moves, and it's not possible to reach it in more or fewer moves.

To extend this approach for starting from any cell in the first column, we can use a traversal method known as Breadth-First Search (BFS). A variation of BFS that starts with multiple initial sources is called Multi-Source BFS. In this case, the approach remains similar to the single-source scenario, except that all cells in the first column are used as starting points in the BFS queue. We then explore the possible next cells that have not been visited yet and have a value greater than the current cell. We keep track of the number of moves made so far, and each time we process a cell from the queue, we update the maximum moves recorded. At the end, this value represents the maximum possible moves.

#### Algorithm

1. Initialize Variables:
- Get the dimensions of the grid: `M` (number of rows) and `N` (number of columns).
- Create a queue `q` for BFS traversal.
- Create a 2D list `vis` of size `M x N` initialized to False to keep track of visited cells.
- Define possible directions for movement to adjacent rows in the next column as $dirs = [-1, 0, 1]$.
2. Enqueue Starting Cells:
- For each row in the first column ($col = 0$):
- Mark the cell as visited.
- Enqueue the cell along with the initial move count `0`.
3. Perform BFS Traversal:
- Initialize `maxMoves` to `0` to store the maximum number of moves made.
- While the queue is not empty:
- Get the size of the current queue (`sz`) representing the number of cells to process at this level.
- For each cell in the current level:
- Dequeue the cell and extract its row, column, and move count.
- Update `maxMoves` as the maximum between `maxMoves` and the current move count.
- Explore Possible Moves:
-  For each direction (`dir`) in `dirs`:
-  Calculate the new row as $newRow = row + dir$ and the new column as $newCol = col + 1$.
- Check if the new cell is within bounds, not yet visited, and its value is greater than the current cell's value.
- If valid, mark the new cell as visited, and enqueue it with the incremented move count ($count + 1$).
4. After processing all cells, return `maxMoves`.

#### Implementation

```python
class Solution:
    # The three possible directions for the next column.
    dirs = [-1, 0, 1]

    def maxMoves(self, grid):
        M, N = len(grid), len(grid[0])

        q = deque()
        vis = [[False] * N for _ in range(M)]

        # Enqueue the cells in the first column.
        for i in range(M):
            vis[i][0] = True
            q.append((i, 0, 0))

        max_moves = 0
        while q:
            sz = len(q)

            for _ in range(sz):
                row, col, count = q.popleft()

                # Update the maximum moves made so far.
                max_moves = max(max_moves, count)

                for dir in self.dirs:
                    # Next cell after the move.
                    new_row, new_col = row + dir, col + 1

                    # If the next cell isn't visited yet and is greater than
                    # the current cell value, add it to the queue with the
                    # incremented move count.
                    if (
                        0 <= new_row < M
                        and 0 <= new_col < N
                        and not vis[new_row][new_col]
                        and grid[row][col] < grid[new_row][new_col]
                    ):
                        vis[new_row][new_col] = True
                        q.append((new_row, new_col, count + 1))

        return max_moves
```

#### Complexity Analysis

Here, $M$ is the number of rows and $N$ is the number of columns in the given matrix `grid`.

- Time complexity: $O(M \cdot N)$

  We will always be visiting a cell only once due to the visited array. We started from the cells in the first column and might end up in visiting all the cells in the matrix. Hence the time complexity is equal to $O(M \cdot N)$.

- Space complexity: $O(M \cdot N)$

  We need the visited array as the size of the given matrix `grid` to keep track of each cell. Also, the queue used in the BFS will have the $M$ number of entries at max, i.e. one for each row. Hence, the total space complexity is equal to $O(M \cdot N)$.

---

### Approach 2: Top-Down Dynamic Programming

#### Intuition

This approach uses a similar idea but with a different strategy. As discussed earlier, one method is to explore the possible cells from the current cell and continue until no further options remain. This works well when there is a single starting cell.

However, in the given problem, there are multiple starting cells, and repeating the process for each one independently might be inefficient. This is because we could end up traversing the same cells multiple times from different starting points. The key insight for using dynamic programming here is that the number of moves possible from a cell is fixed, regardless of how we reach that cell. In other words, once we have calculated the number of moves for a cell, we can reuse that value whenever we encounter that cell again, rather than recalculating it.

To solve the problem, we'll perform a recursive process to explore the possible cells for each starting point in the first column and determine the maximum number of moves we can make. After calculating the moves for each starting cell, we will return the highest value as the maximum possible moves. During this process, we'll use memoization to store the number of moves for each cell, allowing us to return the result directly if we revisit that cell, thus avoiding redundant recursion

#### Algorithm

1. Define possible directions for movement to adjacent rows in the next column as $dirs = [-1, 0, 1]$.
2. Define DFS Function:
- The DFS function takes `row`, `col`, `grid`, and `dp` array as parameters.
- Get the dimensions `M` (number of rows) and `N` (number of columns).
- Check Memoized Result: If $\text{dp}[row][col]$ is not `-1`, return its value, as the maximum moves for this cell have already been computed.
- Initialize $\text{max}_{moves}$ to `0` to track the maximum moves possible from this cell.
- Explore All Directions:
- For each direction in dirs:
- Compute the next cell position as $\text{new}_{row} = row + dir$ and $\text{new}_{col} = col + 1$.
- Check Validity: Ensure that the new position is within grid bounds and the next cell value is greater than the current cell's value.
- If valid, recursively call DFS on the new position and update $\text{max}_{moves}$ as max($\text{max}_{moves}$, $1 + DFS(\text{new}_{row}, \text{new}_{col}, grid, dp)$).
- Store the computed $\text{max}_{moves}$ for $\text{dp}[row][col]$ and return it.
3. Call the above function for all the cells in the first column and find the maximum returned value as `maxMoves`.
4. Return `maxMoves`.

#### Implementation

```python
class Solution:
    # The three possible directions for the next column.
    dirs = [-1, 0, 1]

    def DFS(self, row, col, grid, dp):
        M, N = len(grid), len(grid[0])

        # If we have already calculated the moves required for this cell, return the answer.
        if dp[row][col] != -1:
            return dp[row][col]

        max_moves = 0
        for dir in self.dirs:
            # Next cell after the move.
            new_row, new_col = row + dir, col + 1

            # If the next cell is valid and greater than the current cell value,
            # perform recursion to that cell with updated value of moves.
            if (
                0 <= new_row < M
                and 0 <= new_col < N
                and grid[row][col] < grid[new_row][new_col]
            ):
                max_moves = max(
                    max_moves, 1 + self.DFS(new_row, new_col, grid, dp)
                )

        dp[row][col] = max_moves
        return max_moves

    def maxMoves(self, grid):
        M, N = len(grid), len(grid[0])

        # Initialize the dp array with -1 indicating uncomputed cells.
        dp = [[-1] * N for _ in range(M)]

        max_moves = 0
        # Start DFS from each cell in the first column.
        for i in range(M):
            moves_required = self.DFS(i, 0, grid, dp)
            max_moves = max(max_moves, moves_required)

        return max_moves
```

#### Complexity Analysis

Here, $M$ is the number of rows and $N$ is the number of columns in the given matrix `grid`.

- Time complexity: $O(M \cdot N)$

  We will always be the calculating the moves for each cell only once due to the `dp` array. We might end up finding all the states in the `dp` that are $M \cdot N$ and hence the time complexity is equal to $O(M \cdot N)$.

- Space complexity: $O(M \cdot N)$

  The size of array `dp` is same as the size of the given matrix `grid` to keep the answer of each cell. There will also be some stack space required to keep all the active stack calls which can be at max equal to number of columns as there can be one active stack call for each move. Hence, the total space complexity is equal to $O(M \cdot N)$.

---

### Approach 3: Bottom-up Dynamic Programming

#### Intuition

This approach is similar to the previous one, but instead of using recursion, we calculate the state values iteratively in a `dp` array. This helps save space that would otherwise be used for the recursion stack. The process of filling the values in this approach is essentially the reverse of the previous method.

For each cell in the grid, the `dp` array stores the number of moves required to reach that cell when starting from any cell in the first column. We begin with the base case: the cells in the first column are initialized with a value of `1`. Although logically, the number of moves should be `0` since we can't move to a cell starting from itself, we assign a value of `1` to these cells as an indicator that they are reachable. Cells with a value of `0` in `dp` will represent those that cannot be reached from any starting point in the first column. We can adjust the extra `1` by subtracting it from the result before returning the final answer.

To calculate the values for the remaining cells, we iterate through the columns from `1` to $N - 1$, and within each column, we iterate over the rows from `0` to $M - 1$. This order is necessary because determining the value for cell `(i, j)` depends on the values of the cells in the previous column, namely $(i - 1, j - 1)$, $(i, j - 1)$, and $(i + 1, j - 1)$. Thus, when processing column `j`, we must already have the values for all rows in column $j - 1$.

For each cell `(i, j)`, we check the three potential cells from the previous column. If any of these cells have a value less than the current cell and their dp value is not zero (indicating that the cell is reachable), we update $\text{dp}[i][j]$ to be the maximum of its current value and one plus the value of the reachable cell:

> $\text {\text{dp}[i][j] = max(\text{dp}[i][j],  dp[i - 1][j - 1] + 1, \text{dp}[i][j - 1] + 1, dp[i + 1][j - 1] + 1)}$

This formula is used provided that the value of the previous cell is greater than the current cell and has a positive dp value. The maximum number of moves we can make from any cell in the first column will be the highest value in the `dp` array after subtracting the extra `1` that we initially added.

#### Algorithm

1. Initialize variables:
- Get the grid dimensions `M` (rows) and `N` (columns).
- Create a 2D dp array of size `M x N` initialized to `0` to store the maximum moves from each cell.
2. Set Initial reachable cells:
- For each cell in the first column ($col = 0$), set $\text{dp}[i][0] = 1$ for all rows `i`. This indicates that these cells are reachable as starting points.
3. Iterate over each cell in column major order, for each cell `(i, j)`
- Check the possible cells in the previous column:
- If the current cell $\text{grid}[i][j]$ is greater than the cell directly to its left $\text{grid}[i][j - 1]$ and $\text{dp}[i][j - 1] > 0$ (reachable):
- Update dp[i][j] with the maximum of its current value and dp[i][j - 1] + 1.
- If $i - 1$ (upper diagonal) is valid, and $\text{grid}[i][j]$ is greater than $grid[i - 1][j - 1]$ and $dp[i - 1][j - 1] > 0$:
- Update $\text{dp}[i][j]$ with the maximum of its current value and $dp[i - 1][j - 1] + 1$.
- If $i + 1$ (lower diagonal) is valid, and $\text{grid}[i][j]$ is greater than $grid[i + 1][j - 1]$ and $dp[i + 1][j - 1] > 0$:
- Update $\text{dp}[i][j]$ with the maximum of its current value and $dp[i + 1][j - 1] + 1$.
4. Find the maximum value of all $\text{dp}[i][j] - 1$ as `maxMoves`
5. Return `maxMoves`.

#### Implementation

```python
class Solution:
    def maxMoves(self, grid):
        M, N = len(grid), len(grid[0])

        # Create a 2D list for dp, initialized to 0.
        dp = [[0] * N for _ in range(M)]

        # Initialize the first column with moves as 1.
        for i in range(M):
            dp[i][0] = 1

        max_moves = 0
        for j in range(1, N):
            for i in range(M):
                # Check all three possible previous cells:
                # (i, j-1), (i-1, j-1), (i+1, j-1)
                if grid[i][j] > grid[i][j - 1] and dp[i][j - 1] > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1] + 1)
                if (
                    i - 1 >= 0
                    and grid[i][j] > grid[i - 1][j - 1]
                    and dp[i - 1][j - 1] > 0
                ):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                if (
                    i + 1 < M
                    and grid[i][j] > grid[i + 1][j - 1]
                    and dp[i + 1][j - 1] > 0
                ):
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 1)

                max_moves = max(max_moves, dp[i][j] - 1)

        return max_moves
```

#### Complexity Analysis

Here, $M$ is the number of rows and $N$ is the number of columns in the given matrix `grid`.

- Time complexity: $O(M \cdot N)$

  We will be finding the values for each cell in the array `dp` with size as $M \cdot N$ and hence the time complexity is equal to $O(M \cdot N)$.

- Space complexity: $O(M \cdot N)$

  The size of array `dp` is same as the size of the given matrix `grid` to keep the answer of each cell. Hence, the total space complexity is equal to $O(M \cdot N)$.

---

### Approach 4: Space-Optimized Bottom-up Dynamic Programming

#### Intuition

In our previous solution, we used a `dp` array with a size of `M x N` to keep track of the number of moves possible for each cell in a grid. But if we dig a bit deeper, we’ll notice that for any cell `(i, j)`, the answer only depends on values from the previous column, $j - 1$, because any moves to `(i, j)` come from there.

This observation simplifies things a lot! Instead of storing results for every single cell in the grid, we can just keep track of two columns at a time: the previous column (for reference) and the current column (for updating values). As we move to the next column, we simply update our "previous column" values to reflect the new current column results. This way, we’re only using two arrays, one for each column we need, instead of the whole `M x N` grid. This small adjustment saves a lot of memory, giving us a big boost in efficiency.

#### Algorithm

1. Initialize Variables:
- Get the grid dimensions `M` (rows) and `N` (columns).
- Create a dp array of size `M x 2` initialized to `0` to store the maximum moves.
- dp[i][0] tracks moves for the current column.
- dp[i][1] tracks moves for the next column.
2. Set initial reachable cells:
- For each cell in the first column ($col = 0$), set $\text{dp}[i][0] = 1$ for all rows `i`, indicating that these cells are reachable starting points.
3. Iterate over each cell in column major order, for each cell `(i, j)`
- Check Possible Moves:
- If $\text{grid}[i][j]$ is greater than $\text{grid}[i][j - 1]$ and $\text{dp}[i][0] > 0$ (reachable):
- Update $\text{dp}[i][1]$ as $max(\text{dp}[i][1], \text{dp}[i][0] + 1)$.
- If $i - 1$ (upper diagonal) is valid and $\text{grid}[i][j]$ is greater than $grid[i - 1][j - 1]$ and $dp[i - 1][0] > 0$:
- Update $\text{dp}[i][1]$ as $max(\text{dp}[i][1], dp[i - 1][0] + 1)$.
- If $i + 1$ (lower diagonal) is valid and grid[i][j] is greater than $grid[i + 1][j - 1]$ and $dp[i + 1][0] > 0$:
- Update $\text{dp}[i][1]$ as $max(\text{dp}[i][1], dp[i + 1][0] + 1)$.
- Update `maxMoves` with $max(maxMoves, \text{dp}[i][1] - 1)$ to track the maximum number of moves so far.
4. After processing each column `j`, shift values from $\text{dp}[i][1]$ to $\text{dp}[i][0]$ for the next iteration, and reset $\text{dp}[i][1]$ to `0` for all rows `i`.
5. Return `maxMoves`.

#### Implementation

```python
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        # Create a dp array to store moves, with each cell having a size of 2.
        dp = [[0] * 2 for _ in range(M)]

        # Initialize the first column cells as reachable.
        for i in range(M):
            dp[i][0] = 1

        max_moves = 0

        # Iterate over each column starting from the second one.
        for j in range(1, N):
            for i in range(M):
                # Check if moving from the same row of the previous column is possible.
                if grid[i][j] > grid[i][j - 1] and dp[i][0] > 0:
                    dp[i][1] = max(dp[i][1], dp[i][0] + 1)

                # Check if moving from the upper diagonal is possible.
                if (
                    i - 1 >= 0
                    and grid[i][j] > grid[i - 1][j - 1]
                    and dp[i - 1][0] > 0
                ):
                    dp[i][1] = max(dp[i][1], dp[i - 1][0] + 1)

                # Check if moving from the lower diagonal is possible.
                if (
                    i + 1 < M
                    and grid[i][j] > grid[i + 1][j - 1]
                    and dp[i + 1][0] > 0
                ):
                    dp[i][1] = max(dp[i][1], dp[i + 1][0] + 1)

                # Update the maximum moves so far.
                max_moves = max(max_moves, dp[i][1] - 1)

            # Shift dp values for the next iteration.
            for k in range(M):
                dp[k][0] = dp[k][1]
                dp[k][1] = 0

        return max_moves
```

#### Complexity Analysis

Here, $M$ is the number of rows and $N$ is the number of columns in the given matrix `grid`.

- Time complexity: $O(M \cdot N)$

  We will be finding the values for each cell in the array `dp` with size as $M \cdot N$ and hence the time complexity is equal to $O(M \cdot N)$.

- Space complexity: $O(M)$

  The size of array `dp` is $2 * M$. Hence, the total space complexity is equal to $O(M)$.

---