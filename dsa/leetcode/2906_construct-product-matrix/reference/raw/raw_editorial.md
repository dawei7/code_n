### Approach: Suffix Product

#### Intuition

The product matrix $p$ of the matrix $\textit{grid}$ is defined as follows:

+ Each element $p[i][j]$ is equal to the product of all elements in the matrix except $\textit{grid}[i][j]$, taken modulo $12345$.

If the matrix were one-dimensional, this problem would reduce to "[238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)". Using the same idea, we can treat the two-dimensional matrix as a flattened array and compute the product of elements to the left and right of each position separately.

This allows us to compute, for each position, a **prefix product** and a **suffix product**, whose product gives the desired result.

The computation of each element $p[i][j]$ proceeds as follows:

* First, compute the **suffix product**, which is the product of all elements after $\textit{grid}[i][j]$ up to $\textit{grid}[n - 1][m - 1]$. Denote this as $\textit{suffix}[i][j]$. We can compute this by traversing the matrix in reverse order starting from $\textit{grid}[n - 1][m - 1]$.

* Next, compute the **prefix product**, which is the product of all elements before $\textit{grid}[i][j]$, starting from $\textit{grid}[0][0]$. Denote this as $\textit{prefix}[i][j]$. This can be computed by traversing the matrix in forward order.

Thus, we have:

$$
p[i][j] = \textit{prefix}[i][j] \cdot \textit{suffix}[i][j]
$$

To optimize space, we do not explicitly store both arrays. Instead:

* During the reverse traversal, we store the suffix product directly in $p[i][j]$.
* During the forward traversal, we maintain a running prefix product in a variable $\textit{prefix}$ and multiply it with $p[i][j]$ to obtain the final result.

#### Implementation


```python
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        p = [[0] * m for _ in range(n)]

        suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = suffix
                suffix = (suffix * grid[i][j]) % MOD

        prefix = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = (p[i][j] * prefix) % MOD
                prefix = (prefix * grid[i][j]) % MOD

        return p
```


#### Complexity Analysis

Let $n$ and $m$ be the number of rows and columns of the matrix, respectively.

- Time complexity: $O(nm)$.
  
  We traverse the entire matrix twice, so the total time complexity is $O(nm)$.

- Space complexity: $O(1)$.
  
  No additional space is used apart from the output matrix.

---