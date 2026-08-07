### Approach: Simulate Rotation Operation

#### Hint

Rotating a matrix by 90 degrees clockwise four times results in the matrix being identical to its original form.

#### Intuition

According to the **Hint**, we can simulate up to $4$ rotations of $\textit{mat}$ by 90 degrees clockwise, and compare it with $\textit{target}$ after each rotation.

The rotation operation can be implemented either using an extra array or by performing an in-place rotation. The details of these methods and their derivations can be found in the [48. Rotate Image Editorial](https://leetcode.com/problems/rotate-image/editorial/)。

In this article, we implement the rotation using an in-place method.

#### Implementation


```python
class Solution:
    def findRotation(
        self, mat: List[List[int]], target: List[List[int]]
    ) -> bool:
        n = len(mat)
        # at most 4 rotations
        for k in range(4):
            # rotation operation
            for i in range(n // 2):
                for j in range((n + 1) // 2):
                    (
                        mat[i][j],
                        mat[n - 1 - j][i],
                        mat[n - 1 - i][n - 1 - j],
                        mat[j][n - 1 - i],
                    ) = (
                        mat[n - 1 - j][i],
                        mat[n - 1 - i][n - 1 - j],
                        mat[j][n - 1 - i],
                        mat[i][j],
                    )

            if mat == target:
                return True
        return False
```


#### Complexity Analysis

Let $n$ be the side length of $\textit{mat}$.

- Time complexity: $O(n^2)$.
  
  We perform at most $4$ rotations and comparisons, each taking $O(n^2)$ time.

- Space complexity: $O(1)$.

---