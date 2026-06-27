# First Completely Painted Row or Column

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2661 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Matrix |
| Official Link | [first-completely-painted-row-or-column](https://leetcode.com/problems/first-completely-painted-row-or-column/) |

## Problem Description & Examples
### Goal
You are given a sequence of numbers to be "painted" and a grid (matrix) containing distinct numbers. Your task is to determine the earliest point in the painting sequence (represented by its 0-indexed position `k`) at which either an entire row or an entire column in the grid has all its numbers painted. You should return this minimum index `k`.

### Function Contract
**Inputs**

- `arr`: A `List[int]` representing the 0-indexed sequence of numbers to be painted. Its length is `m * n`.
- `mat`: A `List[List[int]]` representing the `m x n` grid of distinct numbers.

**Return value**

- An `int`, which is the smallest 0-indexed `k` from `arr` such that after painting `arr[0]` through `arr[k]`, at least one row or one column in `mat` is completely painted.

### Examples
**Example 1**

- Input: `arr = [1, 3, 4, 2]`, `mat = [[1, 2], [3, 4]]`
- Output: `1`
- Explanation:
    - `k = 0`, `arr[0] = 1`: `mat[0][0]` is painted. No complete row/column.
    - `k = 1`, `arr[1] = 3`: `mat[1][0]` is painted. Now, column 0 (`[1, 3]`) is completely painted. The earliest index is `1`.

**Example 2**

- Input: `arr = [2, 8, 7, 4, 1, 3, 5, 6, 9]`, `mat = [[3, 2, 5], [1, 4, 6], [8, 7, 9]]`
- Output: `3`
- Explanation:
    - `k = 0`, `arr[0] = 2`: `mat[0][1]` painted.
    - `k = 1`, `arr[1] = 8`: `mat[2][0]` painted.
    - `k = 2`, `arr[2] = 7`: `mat[2][1]` painted.
    - `k = 3`, `arr[3] = 4`: `mat[1][1]` painted. At this point, column 1 (`[2, 4, 7]`) is completely painted. The earliest index is `3`.

**Example 3**

- Input: `arr = [1, 2, 3, 4, 5, 6]`, `mat = [[1, 2, 3], [4, 5, 6]]`
- Output: `2`
- Explanation:
    - `k = 0`, `arr[0] = 1`: `mat[0][0]` painted.
    - `k = 1`, `arr[1] = 2`: `mat[0][1]` painted.
    - `k = 2`, `arr[2] = 3`: `mat[0][2]` painted. At this point, row 0 (`[1, 2, 3]`) is completely painted. The earliest index is `2`.

---

## Underlying Base Algorithm(s)
The problem can be efficiently solved using a combination of **Hash Tables** (dictionaries) for quick lookups and **Counters** (arrays) to track the completion status of rows and columns.

1.  **Pre-processing with a Hash Map:** To quickly find the grid coordinates (`(row, col)`) for any number in `arr`, we first iterate through the `mat` matrix and build a hash map. This map will store `number -> (row_index, col_index)` pairs. This allows for O(1) average-time lookup of a number's position.

2.  **Row and Column Counters:** We maintain two arrays: `row_counts` and `col_counts`.
    *   `row_counts[i]` will store the number of unpainted elements remaining in row `i`. Initially, each `row_counts[i]` is set to `n` (the number of columns).
    *   `col_counts[j]` will store the number of unpainted elements remaining in column `j`. Initially, each `col_counts[j]` is set to `m` (the number of rows).

3.  **Iterative Painting and Checking:** We then iterate through the `arr` sequence from `k = 0` onwards. For each number `arr[k]`:
    *   We use the pre-computed hash map to find its `(r, c)` coordinates in `mat`.
    *   We decrement `row_counts[r]` by 1.
    *   We decrement `col_counts[c]` by 1.
    *   After decrementing, we check if `row_counts[r]` has become `0` or `col_counts[c]` has become `0`. If either is true, it means that row `r` or column `c` (or both) is now completely painted. Since we are iterating through `arr` in order, the current index `k` is the smallest such index, so we return `k`.

This approach avoids repeatedly scanning the matrix or checking all rows/columns, making it efficient.

---

## Complexity Analysis
- **Time Complexity**: `O(m * n)`
    - Building the `pos_map`: We iterate through each of the `m * n` elements in the `mat` matrix once. Each insertion into a hash map takes `O(1)` on average. So, `O(m * n)`.
    - Iterating through `arr`: In the worst case, we iterate through all `m * n` elements of `arr`. For each element, we perform a hash map lookup (`O(1)` average) and two array updates (`O(1)`). So, `O(m * n)`.
    - The dominant factor is `O(m * n)`.
- **Space Complexity**: `O(m * n)`
    - `pos_map`: Stores `m * n` key-value pairs, where each key is an integer and each value is a tuple of two integers. This requires `O(m * n)` space.
    - `row_counts`: An array of size `m`, requiring `O(m)` space.
    - `col_counts`: An array of size `n`, requiring `O(n)` space.
    - The dominant factor is `O(m * n)`.
