## Solution

---

### Approach 1: Rotate Groups of Four Cells

**Intuition**

Observe how the cells move in groups when we rotate the image.

![The corners all move](images/48_angles.png)

We can iterate over each group of four cells and rotate them.

**Implementation**

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
```

**Complexity Analysis**

Let $M$ be the number of cells in the matrix.

* Time complexity: $\mathcal{O}(M)$, as each cell is getting read once and written once.

* Space complexity: $\mathcal{O}(1)$ because we do not use any other additional data structures.

<br/>

---

### Approach 2: Reverse on the Diagonal and then Reverse Left to Right

**Intuition**

The most elegant solution for rotating the matrix is to first reverse the matrix around the main diagonal, and then reverse it from left to right. These operations are called **transpose** and **reflect** in linear algebra.

> **Bonus Question:** What would happen if you reflect and *then* transpose? Would you still get the correct answer?

Even though this approach does twice as many reads and writes as approach 1, most people would consider it a better approach because the code is simpler, and it is built with standard matrix operations that can be found in any matrix library.

**Implementation**

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = (
                    matrix[i][-j - 1],
                    matrix[i][j],
                )
```

**Complexity Analysis**

Let $M$ be the number of cells in the grid.

* Time complexity: $\mathcal{O}(M)$. We perform two steps; transposing the matrix, and then reversing each row. Transposing the matrix has a cost of $\mathcal{O}(M)$ because we're moving the value of each cell once. Reversing each row also has a cost of $\mathcal{O}(M)$, because again we're moving the value of each cell once.

* Space complexity: $\mathcal{O}(1)$ because we do not use any other additional data structures.

<br/>

> **Bonus Question:** If you're not too confident with matrices and linear algebra, get some more practice by also coding a method that transposes the matrix on the *other* diagonal, and another that reflects from top to bottom. You can test your functions by printing out the matrix before and after each operation. Finally, use your functions to find *three more solutions to this problem*. Each solution uses two matrix operations.

<br/>

> **Interview Tip**: Terrified of being asked this question in an interview? Many people are: it can be intimidating due to the fiddly logic. Unfortunately, if you do a lot of interviewing, the probability of seeing it at least once is high, and some people have claimed to have seen it multiple times! This is one of the few questions that I recommend practicing until you can confidently code it and explain it without thinking too much.
