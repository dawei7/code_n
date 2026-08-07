[TOC]

## Summary

We have to find the minimum sum of numbers over a path from the top left to the bottom right of the given matrix .

## Solution

---
### Approach 1: Brute Force

The Brute Force approach involves recursion. For each element, we consider two paths, rightwards and downwards and find the minimum sum out of those two. It specifies whether we need to take a right step or downward step to minimize the sum.

$$
\mathrm{cost}(i, j)=\mathrm{grid}[i][j] + \min \big(\mathrm{cost}(i+1, j), \mathrm{cost}(i, j+1) \big)
$$



```python
class Solution:
    def calculate(self, grid: List[List[int]], i: int, j: int) -> int:
        if i == len(grid) or j == len(grid[0]):
            return float("inf")
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j]
        return grid[i][j] + min(
            self.calculate(grid, i + 1, j), self.calculate(grid, i, j + 1)
        )

    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.calculate(grid, 0, 0)
```


**Complexity Analysis**

* Time complexity : $$O\big(2^{m+n}\big)$$. For every move, we have at most 2 options.
* Space complexity : $$O(m+n)$$. Recursion of depth $$m+n$$.

---

### Approach 2: Dynamic Programming 2D

**Algorithm**

We use an extra matrix $$dp$$ of the same size as the original matrix. In this matrix, $$dp(i, j)$$ represents the minimum sum of the path from the index $$(i, j)$$ to
the bottom rightmost element. We start by initializing the bottom rightmost element
of $$dp$$ as the last element of the given matrix. Then for each element starting from
the bottom right, we traverse backwards and fill in the matrix with the required
minimum sums. Now, we need to note that at every element, we can move either
rightwards or downwards. Therefore, for filling in the minimum sum, we use the
equation:

$$
dp(i, j)= \mathrm{grid}(i,j)+\min\big(dp(i+1,j),dp(i,j+1)\big)
$$

taking care of the boundary conditions.

The following figure illustrates the process:
<!--![Minimum Path Sum](images/64_Minimum_Path_Sum.gif)-->


![Slide 1](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide1.PNG)

![Slide 2](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide2.PNG)

![Slide 3](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide3.PNG)

![Slide 4](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide4.PNG)

![Slide 5](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide5.PNG)

![Slide 6](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide6.PNG)

![Slide 7](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide7.PNG)

![Slide 8](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide8.PNG)

![Slide 9](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide9.PNG)

![Slide 10](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide10.PNG)

![Slide 11](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide11.PNG)

![Slide 12](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide12.PNG)

![Slide 13](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide13.PNG)

![Slide 14](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide14.PNG)

![Slide 15](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide15.PNG)

![Slide 16](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide16.PNG)

![Slide 17](images/slideshow_64_Minimum_Path_Sum_64_Minimum_Path_SumSlide17.PNG)




```python
class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j != n - 1:
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
                elif j == n - 1 and i != m - 1:
                    dp[i][j] = grid[i][j] + dp[i + 1][j]
                elif j != n - 1 and i != m - 1:
                    dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
                else:
                    dp[i][j] = grid[i][j]
        return dp[0][0]
```


**Complexity Analysis**

* Time complexity : $$O(mn)$$. We traverse the entire matrix once.

* Space complexity : $$O(mn)$$. Another matrix of the same size is used.

---

### Approach 3: Dynamic Programming 1D

**Algorithm**

In the previous case, instead of using a 2D matrix for dp, we can do the same
work using a $$dp$$ array of the row size, since for making the current entry all we need is the dp entry for the bottom and
 the right element. Thus,
we start by initializing only the last element of the array as the last element of the given matrix.
The last entry is the bottom rightmost element of the given matrix. Then, we start
moving towards the left and update the entry $$dp(j)$$ as:

$$
dp(j)=\mathrm{grid}(i,j)+\min\big(dp(j),dp(j+1)\big)
$$

We repeat the same process for every row as we move upwards. At the end $$dp(0)$$ gives the
 required minimum sum.



```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [0 for _ in range(len(grid[0]))]
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1 and j != len(grid[0]) - 1:
                    dp[j] = grid[i][j] + dp[j + 1]
                elif j == len(grid[0]) - 1 and i != len(grid) - 1:
                    dp[j] = grid[i][j] + dp[j]
                elif i != len(grid) - 1 and j != len(grid[0]) - 1:
                    dp[j] = grid[i][j] + min(dp[j], dp[j + 1])
                else:
                    dp[j] = grid[i][j]
        return dp[0]
```


**Complexity Analysis**

* Time complexity : $$O(mn)$$. We traverse the entire matrix once.

* Space complexity : $$O(n)$$. Another array of row size is used.

---

### Approach 4: Dynamic Programming (Without Extra Space)

**Algorithm**

This approach is same as [Approach 2](#approach-2-dynamic-programming-2d), with a slight difference. Instead of using
another $$dp$$ matrix. We can store the minimum sums in the original matrix itself,
since we need not retain the original matrix here. Thus, the governing equation
now becomes:

$$
\mathrm{grid}(i, j)=\mathrm{grid}(i,j)+\min \big(\mathrm{grid}(i+1,j), \mathrm{grid}(i,j+1)\big)
$$


```python
# Python solution
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in reversed(range(len(grid))):
            for j in reversed(range(len(grid[0]))):
                if i == len(grid) - 1 and j != len(grid[0]) - 1:
                    grid[i][j] += grid[i][j + 1]
                elif j == len(grid[0]) - 1 and i != len(grid) - 1:
                    grid[i][j] += grid[i + 1][j]
                elif j != len(grid[0]) - 1 and i != len(grid) - 1:
                    grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])
        return grid[0][0]
```


**Complexity Analysis**

* Time complexity : $$O(mn)$$. We traverse the entire matrix once.

* Space complexity : $$O(1)$$. No extra space is used.