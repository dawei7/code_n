# Find Missing and Repeated Values

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2965 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-missing-and-repeated-values](https://leetcode.com/problems/find-missing-and-repeated-values/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-missing-and-repeated-values/).

### Goal
Given an $n \times n$ matrix containing integers from $1$ to $n^2$, where exactly one number is repeated and exactly one number is missing, identify both the repeated value and the missing value.

### Function Contract
**Inputs**

- `grid`: A list of lists of integers representing an $n \times n$ matrix.

**Return value**

- A list of two integers: `[repeated_value, missing_value]`.

### Examples
**Example 1**

- Input: `grid = [[1,3],[2,2]]`
- Output: `[2,4]`

**Example 2**

- Input: `grid = [[9,1,7],[8,9,2],[3,4,6]]`
- Output: `[9,5]`

**Example 3**

- Input: `grid = [[1,1],[2,3]]`
- Output: `[1,4]`

---

## Solution
### Approach
The problem can be solved using frequency counting. By flattening the matrix and tracking the occurrence of each number using a hash map or a frequency array of size $n^2 + 1$, we can identify the number that appears twice and the number that appears zero times. Alternatively, mathematical summation formulas for the sum of integers and the sum of squares can be used to solve for the two unknowns in $O(1)$ extra space.

### Complexity Analysis
- **Time Complexity**: $O(n^2)$, where $n^2$ is the total number of elements in the matrix, as we must traverse every cell exactly once.
- **Space Complexity**: $O(n^2)$ if using a frequency array or hash map to store counts, or $O(1)$ if using the mathematical summation approach.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(grid: list[list[int]]) -> list[int]:
    n = len(grid)
    n_squared = n * n

    # Using a frequency array to track occurrences
    # Size is n^2 + 1 to accommodate values from 1 to n^2
    counts = [0] * (n_squared + 1)

    for row in grid:
        for val in row:
            counts[val] += 1

    repeated = -1
    missing = -1

    for i in range(1, n_squared + 1):
        if counts[i] == 2:
            repeated = i
        elif counts[i] == 0:
            missing = i

    return [repeated, missing]
```
</details>
