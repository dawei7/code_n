
## Solution
---

The question seems to be pretty simple but the trick here is that we need to modify the given matrix in place i.e. our space complexity needs to $O(1)$.

We will go through two different approaches to the question. The first approach makes use of additional memory while the other does not.
<br/>
<br/>

---

### Approach 1: Additional Memory Approach

**Intuition**

If any cell of the matrix has a zero we can record its row and column number. All the cells of this recorded row and column can be marked zero in the next iteration.

**Algorithm**

1. We make a pass over our original array and look for zero entries.
2. If we find that an entry at `[i, j]` is 0, then we need to record somewhere the row `i` and column `j`.
3. So, we use two `sets`, one for the rows and one for the columns.
    <pre>
    if cell[i][j] == 0 {
        row_set.add(i)
        column_set.add(j)
    }</pre>

4. Finally, we iterate over the original matrix. For every cell we check if the row `r` or column `c` had been marked earlier. If any of them was marked, we set the value in the cell to 0.
    <pre>
    if r in row_set or c in column_set {
        cell[r][c] = 0
    }</pre>

```python
class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again and using the rows and cols sets, update the elements
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0
```

**Complexity Analysis**

* Time Complexity: $O(M \times N)$ where M and N are the number of rows and columns respectively.

* Space Complexity: $O(M + N)$.
<br/>
<br/>

---

### Approach 2: $\mathcal{O}(1)$ Space, Efficient Solution

**Intuition**

Rather than using additional variables to keep track of rows and columns to be reset, we use the matrix itself as the *indicators*.

> The idea is that we can use the **first cell** of every row and column as a **flag**. This flag would determine whether a row or column has been set to zero. This means for every cell instead of going to $M+N$ cells and setting it to zero we just set the flag in two cells.

<pre>
if cell[i][j] == 0 {
    cell[i][0] = 0
    cell[0][j] = 0
}
</pre>

 These flags are used later to update the matrix. If the first cell of a row is set to zero this means the row should be marked zero. If the first cell of a column is set to zero this means the column should be marked zero.

**Algorithm**

1. We iterate over the matrix and we mark the first cell of a row `i` and first cell of a column `j`, if the condition in the pseudo code above is satisfied. i.e. if $\text{cell}[i][j] = 0$.

2. The first cell of row and column for the first row and first column is the same i.e. $\text{cell}[0][0]$. Hence, we use an additional variable to tell us if the first column had been marked or not and the $\text{cell}[0][0]$ would be used to tell the same for the first row.

3. Now, we iterate over the original matrix starting from second row and second column i.e. $\text{matrix}[1][1]$ onwards. For every cell we check if the row `r` or column `c` had been marked earlier by checking the respective first row cell or first column cell. If any of them was marked, we set the value in the cell to 0. Note the first row and first column serve as the $\text{row}_{set}$ and $\text{column}_{set}$ that we used in the first approach.

5. We then check if $\text{cell}[0][0] = 0$, if this is the case, we mark the first row as zero.

6. And finally, we check if the first column was marked, we make all entries in it as zeros.

![Slide 1](images/slideshow_73_Matrix_Zeroes_MatrixZeros_1.png)

![Slide 2](images/slideshow_73_Matrix_Zeroes_MatrixZeros_2.png)

![Slide 3](images/slideshow_73_Matrix_Zeroes_MatrixZeros_3.png)

![Slide 4](images/slideshow_73_Matrix_Zeroes_MatrixZeros_4.png)

![Slide 5](images/slideshow_73_Matrix_Zeroes_MatrixZeros_5.png)

![Slide 6](images/slideshow_73_Matrix_Zeroes_MatrixZeros_6.png)

![Slide 7](images/slideshow_73_Matrix_Zeroes_MatrixZeros_7.png)

![Slide 8](images/slideshow_73_Matrix_Zeroes_MatrixZeros_8.png)

![Slide 9](images/slideshow_73_Matrix_Zeroes_MatrixZeros_9.png)

![Slide 10](images/slideshow_73_Matrix_Zeroes_MatrixZeros_10.png)

![Slide 11](images/slideshow_73_Matrix_Zeroes_MatrixZeros_11.png)

![Slide 12](images/slideshow_73_Matrix_Zeroes_MatrixZeros_12.png)

![Slide 13](images/slideshow_73_Matrix_Zeroes_MatrixZeros_13.png)

![Slide 14](images/slideshow_73_Matrix_Zeroes_MatrixZeros_14.png)

![Slide 15](images/slideshow_73_Matrix_Zeroes_MatrixZeros_15.png)

![Slide 16](images/slideshow_73_Matrix_Zeroes_MatrixZeros_16.png)

![Slide 17](images/slideshow_73_Matrix_Zeroes_MatrixZeros_17.png)

![Slide 18](images/slideshow_73_Matrix_Zeroes_MatrixZeros_18.png)

In the above animation we iterate all the cells and mark the corresponding first row/column cell incase of a cell with zero value.

<center>
<img src="images/MatrixZeros_18_1.png" width="400"/>
</center>

We iterate the matrix we got from the above steps and mark respective cells zeroes.

<center>
<img src="images/MatrixZeros_18_2.png" width="400"/>
</center>

<br>

```python
class Solution(object):
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well
        if is_col:
            for i in range(R):
                matrix[i][0] = 0
```

**Complexity Analysis**

* Time Complexity : $O(M \times N)$
* Space Complexity : $O(1)$