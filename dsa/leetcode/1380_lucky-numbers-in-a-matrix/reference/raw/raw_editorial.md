## Solution

---

### Approach 1: Simulation

#### Intuition

We are given a matrix of size $M X N$ with distinct integers. We need to return the list of lucky numbers in the matrix. An integer in the matrix is lucky if it is the maximum integer in its column and it is the minimum value in its row.

In this approach, we will simulate the process by iterating over each integer in the matrix, checking if it is the minimum in its row and the maximum in its column. If it meets both criteria, we will add it to the list of lucky numbers, `luckyNumbers`.

The naive approach to check the criteria for each integer involves iterating over each integer in the current row and column to verify the minimum and maximum criteria, requiring $M + N$ operations per integer. A more efficient method is to precompute the minimum of each row and the maximum of each column before processing the matrix. This allows us to check the criteria for each integer in constant time. We iterate over each row to store the minimum in `rowMin` and each column to store the maximum in `colMax`.

#### Algorithm

1. Iterate over each row and store the minimum of the `ith` row at the `ith` position in the list `rowMin`.
2. Iterate over each column and store the maximum of the `ith` column at the `ith` position in the list `colMax`.
3. Iterate over each integer in the matrix and for each integer at `(i, j)`, check if the integer is equal to `rowMin[i]` and `colMax[j]`. If yes, add it to the list `luckyNumbers`.
4. Return `luckyNumbers`.

#### Implementation


```python
class Solution:
    def luckyNumbers(self, matrix):
        N = len(matrix)
        M = len(matrix[0])

        rowMin = []
        for i in range(N):
            rMin = float('inf')
            for j in range(M):
                rMin = min(rMin, matrix[i][j])
            rowMin.append(rMin)

        colMax = []
        for i in range(M):
            cMax = float('-inf')
            for j in range(N):
                cMax = max(cMax, matrix[j][i])
            colMax.append(cMax)

        luckyNumbers = []
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == rowMin[i] and matrix[i][j] == colMax[j]:
                    luckyNumbers.append(matrix[i][j])

        return luckyNumbers
```


#### Complexity Analysis

Here, $N$ is the number of rows in the matrix and $M$ is the number of columns in the matrix.

* Time complexity: $O(N * M)$.

  To store the minimum of each row, we require $N * M$ operations and the same for storing the maximum of each column. In the end, to find the lucky numbers we again iterate over each integer. Hence, the total time complexity is equal to $O(N * M)$.

* Space complexity: $O(N + M)$.

  We require two lists, `rowMin` and `colMax` of size $N$ and $M$ respectively. Hence the total space complexity is equal to $O(N + M)$.
---

### Approach 2: Greedy

#### Intuition

In the previous approach, we didn't observe a key observation that there can be at most one lucky number in the matrix. Let's first try to prove that there cannot be more than one lucky number in the matrix by contradiction.

Suppose we have an integer `X` in the row `r1` and column `c1` as shown below, the integer `X` is the minimum in its row and maximum in its column and hence is a lucky number. Let's say there's another integer `Y` in the column `r2` and column `c2` let's assume that `Y` is also a lucky number. The below figure shows the expressions we have based on these assumptions that lead us to a contradictory expression.

![fig](images/1380A.png)

Hence, we can conclude that there can be at most one lucky number. If it exists, it can be found as follows: the lucky number is the minimum element in its row and the maximum element in its column. Therefore, we first find the minimum element of each row and then determine the maximum of these minimums as `rowMinMax`. Similarly, we find the maximum of each column and then determine the minimum of these maximums as `colMaxMin`. If `rowMinMax` equals `colMaxMin`, then this value is the lucky number; otherwise, we return an empty list.

#### Algorithm

1. Iterate over each row and find the minimum as `rMin`, then find the maximum of these minimum elements in each row as `rMinMax`.
2. Iterate over each column and find the maximum as `rMax`, then find the minimum of these maximum elements in each column as `cMaxMin`.
3. If the values `rMinMax` and `cMaxMin` are equal then return `rMinMax` or `cMaxMin`.
4. Otherwise, return an empty list.

#### Implementation


```python
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        N, M = len(matrix), len(matrix[0])

        r_min_max = float('-inf')
        for i in range(N):
            r_min = min(matrix[i])  
            r_min_max = max(r_min_max, r_min)

        c_max_min = float('inf')
        for i in range(M):
            c_max = max(matrix[j][i] for j in range(N))
            c_max_min = min(c_max_min, c_max)

        if r_min_max == c_max_min:
            return [r_min_max]
        else:
            return []
```


#### Complexity Analysis

Here, $N$ is the number of rows in the matrix and $M$ is the number of columns in the matrix.

* Time complexity: $O(N * M)$.

  To find the value `rMinMax` and `cMaxMin` we are iterating over each integer in the matrix. Hence, the total time complexity is equal to $O(N * M)$.

* Space complexity: $O(1)$.

  No extra space is required apart from the few variables. Hence the total space complexity is constant.
---