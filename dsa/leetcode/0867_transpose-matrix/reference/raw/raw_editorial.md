[TOC]

## Solution
---
### Approach 1: Copy Directly

**Intuition and Algorithm**

The transpose of a matrix `A` with dimensions `R x C` is a matrix `ans` with dimensions `C x R` for which `ans[c][r] = A[r][c]`.

Let's initialize a new matrix `ans` representing the answer.  Then, we'll copy each entry of the matrix as appropriate.


```python
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]] :
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in range(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans

        #Alternative Solution:
        #return list(zip(*A))
```


**Complexity Analysis**

* Time Complexity:  $$O(R * C)$$, where $$R$$ and $$C$$ are the number of rows and columns in the given matrix `A`.

* Space Complexity:  $$O(R * C)$$, the space used by the answer.
<br />
<br />