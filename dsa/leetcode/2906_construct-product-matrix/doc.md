# Construct Product Matrix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2906 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [construct-product-matrix](https://leetcode.com/problems/construct-product-matrix/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/construct-product-matrix/).

### Goal
Given a 2D grid of integers, generate a new matrix of the same dimensions where each cell `(i, j)` contains the product of all elements in the original grid except for the element at `(i, j)`. Since the product can be very large, return the result modulo 12345.

### Function Contract
**Inputs**

- `grid`: A 2D list of integers (`List[List[int]]`) representing the input matrix of size `n x m`.

**Return value**

- A 2D list of integers (`List[List[int]]`) where each element is the product of all other elements in the input grid modulo 12345.

### Examples
**Example 1**

- Input: `grid = [[1, 2], [3, 4]]`
- Output: `[[24, 12], [8, 6]]`

**Example 2**

- Input: `grid = [[12345], [2]]`
- Output: `[[0], [0]]`

**Example 3**

- Input: `grid = [[1]]`
- Output: `[[0]]`

---

## Solution
### Approach
The problem is solved using the **Prefix and Suffix Product** technique. By flattening the 2D matrix into a 1D sequence, we can compute the product of all elements to the left of index `i` and all elements to the right of index `i`. The product of all elements excluding index `i` is simply `prefix[i-1] * suffix[i+1]`. This avoids division, which is problematic due to the modulo operation and potential zeros in the input.

### Complexity Analysis
- **Time Complexity**: `O(n * m)`, where `n` is the number of rows and `m` is the number of columns. We perform three linear passes over the total number of elements.
- **Space Complexity**: `O(n * m)` to store the resulting matrix and the auxiliary prefix/suffix arrays.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows = len(grid)
    cols = len(grid[0])
    n = rows * cols
    MOD = 12345

    # Flatten the grid into a 1D array for easier prefix/suffix calculation
    flat = [grid[r][c] for r in range(rows) for c in range(cols)]

    prefix = [1] * n
    suffix = [1] * n

    # Calculate prefix products
    curr = 1
    for i in range(n):
        prefix[i] = curr
        curr = (curr * flat[i]) % MOD

    # Calculate suffix products
    curr = 1
    for i in range(n - 1, -1, -1):
        suffix[i] = curr
        curr = (curr * flat[i]) % MOD

    # Construct the result matrix
    res = [[0] * cols for _ in range(rows)]
    for i in range(n):
        r, c = divmod(i, cols)
        res[r][c] = (prefix[i] * suffix[i]) % MOD

    return res
```
</details>
