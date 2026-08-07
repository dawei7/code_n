### Approach: Enumerate Each Layer

#### Intuition

For a matrix $\textit{grid}$ of size $m \times n$, the number of layers is $\min(m / 2, n / 2)$. We can simulate the cyclic rotation operation by enumerating each layer from the outside to the inside.

For convenience, we traverse the elements of each layer in a counterclockwise direction starting from the top-left corner. We divide this traversal into four parts, where each part processes one edge of the layer while excluding the last element to avoid duplication.

We store the row indices, column indices, and values of these elements in the corresponding arrays $r$, $c$, and $\textit{val}$, respectively. Let $\textit{total}$ denote the number of elements in the current layer, which is equal to the length of $\textit{val}$. If we perform $\textit{total}$ rotations, the layer remains unchanged. Therefore, the effective number of rotations is $\textit{kk} = k \bmod \textit{total}$.

After rotation, the value at the $i$-th position in the traversal corresponds to the value at index $(i - \textit{kk} + \textit{total}) \bmod \textit{total}$ in the $\textit{val}$ array. Adding $\textit{total}$ before taking the modulus ensures that the index remains non-negative.

Finally, we iterate over the stored coordinates and update the corresponding positions in $\textit{grid}$. Once all layers are processed, $\textit{grid}$ represents the rotated matrix.

#### Implementation

```python
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        nlayer = min(m // 2, n // 2)  # level count
        # enumerate each layer counterclockwise starting from the top-left corner
        for layer in range(nlayer):
            r = []  # row index of each element
            c = []  # column index of each element
            val = []  # value of each element
            for i in range(layer, m - layer - 1):  # down
                r.append(i)
                c.append(layer)
                val.append(grid[i][layer])
            for j in range(layer, n - layer - 1):  # right
                r.append(m - layer - 1)
                c.append(j)
                val.append(grid[m - layer - 1][j])
            for i in range(m - layer - 1, layer, -1):  # up
                r.append(i)
                c.append(n - layer - 1)
                val.append(grid[i][n - layer - 1])
            for j in range(n - layer - 1, layer, -1):  # left
                r.append(layer)
                c.append(j)
                val.append(grid[layer][j])
            total = len(val)  # total number of elements in each layer
            kk = k % total  # equivalent number of rotations
            # find the value at each index after rotation
            for i in range(total):
                idx = (
                    i + total - kk
                ) % total  # the index corresponding to the value after rotation
                grid[r[i]][c[i]] = val[idx]
        return grid
```

#### Complexity Analysis

Let $m$ and $n$ be the number of rows and columns of $\textit{grid}$, respectively.

- Time complexity: $O(mn)$，

  We traverse all elements of $\textit{grid}$ once during the process.

- Space complexity: $O(m + n)$.

  Auxiliary arrays are used to store the coordinates and values of each layer. Note that this can be optimized to $O(1)$ using in-place rotation, but that approach is less intuitive, so it is not included here.

---