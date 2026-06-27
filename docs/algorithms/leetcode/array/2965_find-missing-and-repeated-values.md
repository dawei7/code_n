# Find Missing and Repeated Values

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2965 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Math, Matrix |
| Official Link | [find-missing-and-repeated-values](https://leetcode.com/problems/find-missing-and-repeated-values/) |

## Problem Description & Examples
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

## Underlying Base Algorithm(s)
The problem can be solved using frequency counting. By flattening the matrix and tracking the occurrence of each number using a hash map or a frequency array of size $n^2 + 1$, we can identify the number that appears twice and the number that appears zero times. Alternatively, mathematical summation formulas for the sum of integers and the sum of squares can be used to solve for the two unknowns in $O(1)$ extra space.

---

## Complexity Analysis
- **Time Complexity**: $O(n^2)$, where $n^2$ is the total number of elements in the matrix, as we must traverse every cell exactly once.
- **Space Complexity**: $O(n^2)$ if using a frequency array or hash map to store counts, or $O(1)$ if using the mathematical summation approach.
