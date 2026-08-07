[TOC]

## Solution

--- 

### Overview

Matrices such as this one are a type of **graph** representation. Standard graph traversal algorithms such as BFS and DFS can be used to solve this problem. If you aren't familiar with these algorithms, check out the [Explore Card on BFS](https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/).

The naive approach would be to check every cell - that is, iterate through every cell, and at each one, start a traversal that follows the problem's conditions. That is, find every cell that manages to reach both oceans.

This approach, however, is extremely slow, as it repeats a ton of computation. Instead of looking for every path from cell to ocean, let's start at the oceans and try to work our way to the cells. This will be much faster because when we start a traversal at a cell, whatever result we end up with can be applied to only that cell. However, when we start from the ocean and work backwards, we already know that every cell we visit must be connected to the ocean.

</br>

---

### Approach 1: Breadth First Search (BFS)

**Intuition**

If we start traversing from the ocean and flip the condition (check for higher height instead of lower height), then we know that every cell we visit during the traversal can flow into that ocean. Let's start a BFS traversal from every cell that is immediately beside the Pacific ocean, and figure out what cells can flow into the Pacific. Then, let's do the exact same thing with the Atlantic ocean. At the end, the cells that end up connected to both oceans will be our answer.



![Slide 1](images/slideshow_417_Pacific_Atlantic_417_1.png)

![Slide 2](images/slideshow_417_Pacific_Atlantic_417_2.png)

![Slide 3](images/slideshow_417_Pacific_Atlantic_417_3.png)

![Slide 4](images/slideshow_417_Pacific_Atlantic_417_4.png)

![Slide 5](images/slideshow_417_Pacific_Atlantic_417_5.png)

![Slide 6](images/slideshow_417_Pacific_Atlantic_417_6.png)



<br/>

**Algorithm**

1. If the input is empty, immediately return an empty array.

2. Initialize variables that we will use to solve the problem:
    - Number of rows and columns in our matrix;
    - 2 queues, one for the Atlantic Ocean and one for the Pacific Ocean that will be used for BFS;
    - 2 data structures, again one for each ocean, that we'll use to keep track of cells we already visited, to avoid infinite loops;
    - A small array `[(0, 1), (1, 0), (-1, 0), (0, -1)]` that will help with BFS.

3. Figure out all the cells that are adjacent to each ocean, and fill the respective data structures with them.

4. Perform BFS from each ocean. The data structure used to keep track of cells already visited has a double purpose - it also
contains every cell that can flow into that ocean.

5. Find the intersection, that is all cells that can flow into both oceans.

**Implementation**

Putting it all together for the final solution:


```python
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Check if input is empty
        if not matrix or not matrix[0]: 
            return []
            
        num_rows, num_cols = len(matrix), len(matrix[0])

        # Setup each queue with cells adjacent to their respective ocean
        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(num_rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, num_cols - 1))
        for i in range(num_cols):
            pacific_queue.append((0, i))
            atlantic_queue.append((num_rows - 1, i))
        
        def bfs(queue):
            reachable = set()
            while queue:
                (row, col) = queue.popleft()
                # This cell is reachable, so mark it
                reachable.add((row, col))
                for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # Check all 4 directions
                    new_row, new_col = row + x, col + y
                    # Check if the new cell is within bounds
                    if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue
                    # Check that the new cell hasn't already been visited
                    if (new_row, new_col) in reachable:
                        continue
                    # Check that the new cell has a higher or equal height,
                    # So that water can flow from the new cell to the old cell
                    if matrix[new_row][new_col] < matrix[row][col]:
                        continue
                    # If we've gotten this far, that means the new cell is reachable
                    queue.append((new_row, new_col))
            return reachable
        
        # Perform a BFS for each ocean to find all cells accessible by each ocean
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))
```



**Complexity Analysis**

* Time complexity: $$O(M \cdot N)$$, where $$M$$ is the number of rows and $$N$$ is the number of columns.
    
    In the worst case, such as a matrix where every value is equal, we would visit every cell twice. This is because we perform 2 traversals, and during each traversal, we visit each cell exactly once. There are $$M \cdot N$$ cells total, which gives us a time complexity of $$O(2 \cdot M \cdot N) = O(M \cdot N)$$.

* Space complexity: $$O(M \cdot N)$$, where $$M$$ is the number of rows and $$N$$ is the number of columns.
    
    The extra space we use comes from our queues, and the data structure we use to keep track of what cells have been visited. Similar to the time complexity, for a given ocean, the amount of space we will use scales linearly with the number of cells. For example, in the Java implementation, to keep track of what cells have been visited, we simply used 2 matrices that have the same dimensions as the input matrix.

    The same logic follows for the queues - we can't have more cells in the queue than there are cells in the matrix!

<br/>

---

### Approach 2: Depth First Search (DFS)

Intuitively, BFS makes more sense for this problem since water flows in the same manner. However, we can also use DFS, and it doesn't really make much of a difference. So, if you prefer DFS, then that's perfectly fine for this problem. Additionally, it's possible that your interviewer will ask you to implement the problem recursively instead of iteratively. Recursion must be DFS, not BFS.

**Algorithm**

DFS is very similar to BFS. Instead of using a queue and working iteratively, we'll use recursion. Our `dfs` method will be called for every reachable cell. Note: we could also work iteratively with DFS, in which case we would simply use a stack instead of a queue like in the Approach 1 code, with mostly everything else being identical to the BFS approach.

**Implementation**


```python
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Check if input is empty
        if not matrix or not matrix[0]: 
            return []
        
        # Initialize variables, including sets used to keep track of visited cells
        num_rows, num_cols = len(matrix), len(matrix[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(row, col, reachable):
            # This cell is reachable, so mark it
            reachable.add((row, col))
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # Check all 4 directions
                new_row, new_col = row + x, col + y
                # Check if the new cell is within bounds
                if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                    continue
                # Check that the new cell hasn't already been visited
                if (new_row, new_col) in reachable:
                    continue
                # Check that the new cell has a higher or equal height,
                # So that water can flow from the new cell to the old cell
                if matrix[new_row][new_col] < matrix[row][col]:
                    continue
                # If we've gotten this far, that means the new cell is reachable
                dfs(new_row, new_col, reachable)
        
        # Loop through each cell adjacent to the oceans and start a DFS
        for i in range(num_rows):
            dfs(i, 0, pacific_reachable)
            dfs(i, num_cols - 1, atlantic_reachable)
        for i in range(num_cols):
            dfs(0, i, pacific_reachable)
            dfs(num_rows - 1, i, atlantic_reachable)
        
        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))
```



**Complexity Analysis**

* Time complexity: $$O(M \cdot N)$$, where $$M$$ is the number of rows and $$N$$ is the number of columns.
    
    Similar to approach 1. The `dfs` function runs exactly once for each cell accessible from an ocean.

* Space complexity: $$O(M \cdot N)$$, where $$M$$ is the number of rows and $$N$$ is the number of columns.
    
    Similar to approach 1. Space that was used by our queues is now occupied by `dfs` calls on the recursion stack.

<br/>

---