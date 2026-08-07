[TOC]

## Solution

--- 

### Overview

As shown in the picture below, we have found 8 valid paths. Note that:
- A cell itself is also a valid path, so each cell in the grid stands for a unique path.
- The path must be **strictly** increasing, so the paths colored in red are invalid.

![img](images/1.png)

 

---

### Approach 1: Sorting + DP.

#### Intuition   

Let's build an auxiliary array `dp` of the same size as `grid` to represent the number of paths that end at each cell. Initially, the value of each `dp[i][j]` cell is `1`, which stands for the path made by `grid[i][j]` cell itself.

![img](images/2.png)

Then, for each cell `grid[i][j]`, we need to look for its neighbor cells in 4 directions, if there exists a neighbor cell (let's say `grid[i + 1][j]`) that is larger than `grid[i][j]`, it means every path that ends at `grid[i][j]` can be extended to `grid[i + 1][j]`. Therefore, the number of paths ending at `grid[i + 1][j]` should be incremented by `grid[i][j]`.


However, if we traverse all cells by arbitrary order, we might need many repeated updates, as described below.

![img](images/wrong.png)

It implies that we should iterate over all cells by value. If we sort these cells by value, then traverse over them from the smallest. This ensures that the number of paths ending at each cell in `dp` is updated only once.


Please refer to the following slide for an example. 



![Slide 1](images/slideshow_s1_s1.png)

![Slide 2](images/slideshow_s1_s2.png)

![Slide 3](images/slideshow_s1_s3.png)

![Slide 4](images/slideshow_s1_s4.png)

![Slide 5](images/slideshow_s1_s5.png)

![Slide 6](images/slideshow_s1_s6.png)





<br>

#### Algorithm

1) Initialize `dp`, a 2-d array of the same size as `grid`, and set every value as `1`.
2) Sort all cells by value and iterate over the sorted cells.
3) For each cell `grid[i][j]`, check its 4-direction neighbor cells, if a neighbor cell `grid[curr_i][curr_j]` has a larger value, then increment `dp[curr_i][curr_j]` by `dp[i][j]`.
4) Return the sum of all cells of `dp` when the iteration ends.

#### Implementation


```python
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10 ** 9 + 7
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        # Initialize dp, 1 stands for the path made by a cell itself.
        dp = [[1] * n for _ in range(m)]

        # Sort all cells by value.
        cell_list = [[i, j] for i in range(m) for j in range(n)]
        cell_list.sort(key = lambda x: grid[x[0]][x[1]])
        
        # Iterate over the sorted cells, for each cell grid[i][j]: 
        for i, j in cell_list:
            # Check its four neighbor cells, if a neighbor cell grid[curr_i][curr_j] has a
            # larger value, increment dp[curr_i][curr_j] by dp[i][j]
            for di, dj in directions:
                curr_i, curr_j = i + di, j + dj
                if 0 <= curr_i < m and 0 <= curr_j < n and grid[curr_i][curr_j] > grid[i][j]:
                    dp[curr_i][curr_j] += dp[i][j]
                    dp[curr_i][curr_j] %= mod
        
        # Sum over dp[i][j].
        return sum(sum(row) % mod for row in dp) % mod
```



#### Complexity Analysis

Let $$m \times n$$ be the size of the input array `grid`.

* Time complexity: $$O(m\cdot n \cdot\log(m\cdot n))$$

    - We sort all cells by value, it takes $$O(k\log k)$$ to sort an array of size $$O(k)$$, so it takes $$O(m\cdot n \cdot\log(m\cdot n))$$ time.
    - The iteration over sorted cells has $$O(m \cdot n)$$ steps, each step consists of checking at most four neighbor cells, thus it takes $$O(m \cdot n)$$ time.
    - For initialization of `dp` and the calculation of `answer` we iterate over all the cells of the `dp` array, which also takes $$O(m \cdot n)$$ time.
    - To sum up, the overall time complexity is $$O(m\cdot n \cdot\log(m\cdot n))$$.

* Space complexity: $$O(m\cdot n)$$

    - We used two arrays, `cellList` and `dp`, they both contain $$O(m \cdot n)$$ elements.

<br/>



---

### Approach 2: DFS with Memoization


#### Intuition   

In the previous approach, we have to sort all cells first to avoid repeated computation. Here, we introduce a better method that doesn't need traversing by order.

We define a function `dfs(i, j)` to calculate the number of increasing paths ending at `grid[i][j]`. `dfs(i, j)` consists of **at most** 5 parts:


- 1, the path consisting of `grid[i][j]` itself.
- `dfs(i - 1, j)`, if `grid[i - 1][j]` exists and is smaller than `grid[i][j]`. 
- `dfs(i, j - 1)`, if `grid[i][j - 1]` exists and is smaller than `grid[i][j]`.
- `dfs(i + 1, j)`, if `grid[i + 1][j]` exists and is smaller than `grid[i][j]`.
- `dfs(i, j + 1)`, if `grid[i][j + 1]` exists and is smaller than `grid[i][j]`.

If a neighbor cell with a smaller value (For example, `grid[i + 1][j] < grid[i][j]`) exists, we can get the number of paths ending at this cell as `dfs(i + 1, j)`, and for all those paths we can extend the path with the current element, so we increment `dfs(i, j)` by `dfs(i + 1, j)`.


![img](images/3.png)

Remember to use the memoization method to avoid repeated computation. Similarly, we create an array `dp` of the same size as `grid`. Initially, each cell `dp[i][j]` is set to `-1`, which means **unvisited**. 


![img](images/4.png)

Once we get the number of paths ending at cell `grid[i][j]` and update `dp[i][j]`, it means the cell `grid[i][j]` is **visited** and the value of `dfs(i, j)` calculated for the first time. If we need `dfs(i, j)` in the further iteration, we don't bother repeating the DFS process to calculate `dfs(i, j)`, but return `dp[i][j]` since `dp[i][j] = dfs(i, j)`.

<br>

As shown in the picture below, suppose we have visited `grid[0][0]` and updated `dp[0][0]`. Now we are visiting `grid[1][0]`, `grid[0][0]` is smaller than `grid[1][0]`, according to the previous definition, we need a step `dfs(1, 0) += dfs(0, 0)`. However, there is no need to recalculate `dfs(0, 0)`, we can just return `dp[0][0]` which will take constant time!

![img](images/5.png)

We can tell that each cell in `dp[i][j]` is only calculated by once.

<br>

#### Algorithm

1) Initialize `dp`, an auxiliary 2-d array of the same size as `grid`, and set every value as `-1`.
2) Iterate over every cell `grid[i][j]` and get `dfs(i, j)`, the number of paths end at it:
    - If `dp[i][j]` is non-zero, it means we have visited this cell, just return `dp[i][j]` and repeat step 2.
    - Otherwise, set `dfs(i, j) = 1`, the path consisting of the cell itself.
    - Check its 4-direction neighbor cells, if a neighbor cell `(prev_i, prev_j)` has a smaller value, increment `dfs(i, j)` by `dfs(prev_i, prev_j)`
    - Update `dp[i][j]` as `dfs(i, j)`.
3) Once the iteration ends, return the sum of `dp`.

#### Implementation


```python
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10 ** 9 + 7
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        dp = [[-1] * n for _ in range(m)]
        
        def dfs(i, j):
            # If dp[i][j] is non-zero, it means we have got the value of dfs(i, j),
            # so just return dp[i][j].
            if dp[i][j] != -1:
                return dp[i][j]

            # Otherwise, set answer = 1, the path made of grid[i][j] itself.
            answer = 1

            # Check its four neighbor cells, if a neighbor cell grid[prevI][prevJ] has a
            # smaller value, we move to this cell and solve the subproblem: dfs(prevI, prevJ).
            for di, dj in directions:
                prev_i, prev_j = i + di, j + dj
                if 0 <= prev_i < m and 0 <= prev_j < n and grid[prev_i][prev_j] < grid[i][j]:
                    answer += dfs(prev_i, prev_j) % mod
            
            # Update dp[i][j], so that we don't recalculate its value later.
            dp[i][j] = answer
            return answer
        
        # Iterate over all cells grid[i][j] and sum over dfs(i, j).
        return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod
```



#### Complexity Analysis

Let $$m \times n$$ be the size of the input array `grid`.

* Time complexity: $$O(m\cdot n)$$

    - We used `dp` as memory to avoid repeated computation, so each cell is only visited and calculated once. 
    - Initialization of the `dp` array also takes $$O(m \cdot n)$$ time.
    

* Space complexity: $$O(m\cdot n)$$

    - We build the auxiliary array `dp` of the same size as `grid`.
    - The space complexity of recursive algorithm is proportional to the maximum depth of the recursion tree generated. There are at most $$m\cdot n$$ recursive call of `dfs` in the stack simultaneously, thus the stack takes $$O(m\cdot n)$$ space.
    - To sum up, the space complexity is $$O(m\cdot n)$$.

<br/>