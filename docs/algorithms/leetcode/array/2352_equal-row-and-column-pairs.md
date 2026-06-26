# Equal Row and Column Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2352 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Matrix, Simulation |
| Official Link | [equal-row-and-column-pairs](https://leetcode.com/problems/equal-row-and-column-pairs/) |

## Problem Description & Examples
### Goal
Given an `n x n` integer matrix, the task is to determine the total number of pairs `(row_index, col_index)` such that the elements of the `row_index`-th row are identical to the elements of the `col_index`-th column, when read as sequences. In other words, we need to count how many times a row vector in the matrix matches a column vector in the matrix.

### Function Contract
**Inputs**

- `grid`: `List[List[int]]` - An `n x n` matrix of integers. `n` is the number of rows and also the number of columns.

**Return value**

- `int` - The total count of equal row-column pairs.

### Examples
**Example 1**

- Input: `grid = [[3,2,1],[1,7,6],[2,7,7]]`
- Output: `1`
- Explanation: The only equal pair is (row 2, column 1) because `grid[2]` is `[2,7,7]` and the 1st column is `[2,7,7]`.

**Example 2**

- Input: `grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]`
- Output: `3`
- Explanation: There are three equal pairs:
    - (row 0, column 0): `[3,1,2,2]`
    - (row 2, column 2): `[2,4,2,2]`
    - (row 3, column 2): `[2,4,2,2]`

**Example 3**

- Input: `grid = [[11,1],[1,11]]`
- Output: `2`
- Explanation:
    - (row 0, column 0): `[11,1]`
    - (row 1, column 1): `[1,11]`

---

## Underlying Base Algorithm(s)
The problem can be efficiently solved using **Hash Tables (or Frequency Maps)**. The core idea is to:
1.  **Extract and count frequencies of all unique rows**: Iterate through each row of the matrix, convert it into a hashable format (e.g., a tuple), and store its frequency in a hash map.
2.  **Extract and count frequencies of all unique columns**: Iterate through each column of the matrix, convert it into a hashable format (e.g., a tuple), and store its frequency in a separate hash map.
3.  **Calculate total pairs**: Iterate through the unique row types and their frequencies. For each unique row type, check its frequency in the column frequency map. The number of pairs for that specific row type is `(frequency of row type) * (frequency of same vector as column type)`. Sum these products to get the total count.

This approach avoids `O(N^3)` direct comparisons of every row with every column, which would involve `N^2` comparisons, each taking `N` time. By pre-counting frequencies, we reduce the comparison phase significantly.

## Complexity Analysis
Let `n` be the dimension of the `n x n` grid.

-   **Time Complexity**: `O(n^2)`
    -   **Extracting and counting rows**: We iterate through `n` rows. For each row, we convert it to a tuple (which takes `O(n)` time) and then update its count in a hash map. Hash map operations (insertion/lookup) for a key of size `n` take `O(n)` time in the worst case (due to hashing the tuple elements), but are often amortized `O(1)` for fixed-size keys. Given `n` rows, this phase takes `n * O(n) = O(n^2)` time.
    -   **Extracting and counting columns**: Similarly, we iterate through `n` columns. For each column, we construct it by iterating `n` elements (`O(n)` time), convert it to a tuple (`O(n)` time), and update its count in a hash map (`O(n)` time). This phase also takes `n * O(n) = O(n^2)` time.
    -   **Calculating total pairs**: We iterate through at most `n` unique row types (the number of entries in the `row_counts` hash map). For each unique row type, we perform a lookup in the `col_counts` hash map. Each lookup takes `O(n)` time (for hashing the tuple key). Thus, this phase takes `n * O(n) = O(n^2)` time.
    -   Combining these, the total time complexity is `O(n^2) + O(n^2) + O(n^2) = O(n^2)`.

-   **Space Complexity**: `O(n^2)`
    -   **`row_counts` hash map**: In the worst case, all `n` rows could be unique. Each row is stored as a tuple of `n` integers. So, `n` tuples, each of size `O(n)`, leading to `O(n * n) = O(n^2)` space.
    -   **`col_counts` hash map**: Similarly, in the worst case, all `n` columns could be unique. Each column is stored as a tuple of `n` integers. So, `n` tuples, each of size `O(n)`, leading to `O(n * n) = O(n^2)` space.
    -   The total space complexity is `O(n^2) + O(n^2) = O(n^2)`.
