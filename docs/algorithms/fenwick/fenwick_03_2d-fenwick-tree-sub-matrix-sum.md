# 2D Fenwick Tree (Sub-matrix Sum)

| | |
|---|---|
| **ID** | `fenwick_03` |
| **Category** | fenwick |
| **Complexity (required)** | $O(log N * log M)$ Query/Update |
| **Difficulty** | 7/10 |
| **Interview relevance** | 3/10 |
| **LeetCode Equivalent** | [Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/) |

## Problem statement

Given a 2D matrix of dimensions N x M, implement a 2-Dimensional Fenwick Tree to support:
1. `update(row, col, value)`: Update the matrix at `(row, col)` to the new `value`.
2. `query(row1, col1, row2, col2)`: Return the sum of the elements inside the rectangle defined by its upper-left corner `(row1, col1)` and lower-right corner `(row2, col2)`.

Both operations must be strictly faster than $O(N)$ time.

**Input:** A 2D matrix, and a series of `update` and `query` operations.
**Output:** The results of the range queries.

## When to use it

- When you have a massive grid (e.g., an image, a game map) with constantly changing values, and you need to query area sums.
- This is the mutable version of the standard "2D Prefix Sum" matrix. A standard 2D prefix sum answers queries in $O(1)$ but takes $O(N \times M)$ to update a single pixel! A 2D Fenwick updates in fractions of a millisecond.

## Approach

A 1D Fenwick Tree is an array where `BIT[x]` holds the sum of a horizontal range.
A 2D Fenwick Tree is simply a 2D array (matrix) where `BIT[x][y]` holds the sum of a **rectangle** ending at `(x, y)`. The width of the rectangle is determined by the lowest set bit of `x`, and the height is determined by the lowest set bit of `y`!

**2D Point Update:**
Instead of a single `while` loop, we use two nested `while` loops!
For a given `(row, col)` update with `delta`:
We loop `x` upwards through the rows. Inside that loop, we loop `y` upwards through the columns, adding `delta` to `BIT[x][y]`.

**2D Prefix Query:**
To get the sum of the rectangle from `(0,0)` to `(row, col)`:
We loop `x` downwards. Inside that loop, we loop `y` downwards, accumulating `BIT[x][y]`.

**2D Range Query:**
Just like 2D Prefix Sums, querying a sub-matrix `(r1, c1)` to `(r2, c2)` uses the Inclusion-Exclusion Principle:
`Area = Prefix(r2, c2) - Prefix(r1-1, c2) - Prefix(r2, c1-1) + Prefix(r1-1, c1-1)`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for fenwick_03: 2D Fenwick Tree (Sub-matrix Sum).

Build a 2D Binary Indexed Tree on an n x n matrix,
"""


def solve(matrix, n, updates, queries, q):
    """2D BIT with point updates and sub-matrix sum queries.

    1-based BIT indexing internally (so cell (r, c) maps to
    BIT[r+1][c+1]).
    """
    if n == 0:
        return [0] * q
    # Build BIT.
    bit = [[0] * (n + 1) for _ in range(n + 1)]
    work = [row[:] for row in matrix]

    def update(r, c, delta):
        r += 1
        c += 1
        i = r
        while i <= n:
            j = c
            while j <= n:
                bit[i][j] += delta
                j += j & -j
            i += i & -i

    def prefix(r, c):
        # Sum over (0,0) .. (r,c) inclusive. Caller must clamp
        # r, c to -1 (which yields 0).
        if r < 0 or c < 0:
            return 0
        r += 1
        c += 1
        s = 0
        i = r
        while i > 0:
            j = c
            while j > 0:
                s += bit[i][j]
                j -= j & -j
            i -= i & -i
        return s

    # Build the BIT by inserting each cell's initial value.
    for r in range(n):
        for c in range(n):
            if matrix[r][c] != 0:
                update(r, c, matrix[r][c])

    # Apply updates.
    for r, c, delta in updates:
        work[r][c] += delta
        update(r, c, delta)

    # Answer queries.
    out = []
    for r1, c1, r2, c2 in queries:
        s = (prefix(r2, c2)
             - prefix(r1 - 1, c2)
             - prefix(r2, c1 - 1)
             + prefix(r1 - 1, c1 - 1))
        out.append(s)
    return out
```

</details>

## Walk-through

*(Conceptual)*
`matrix = [[1, 2], [3, 4]]`

1. **Query Region (0,0) to (1,1):**
   - We need `Pref(2,2) - Pref(0,2) - Pref(2,0) + Pref(0,0)`.
   - `Pref(0, x)` and `Pref(x, 0)` naturally return `0` because the `while i > 0` loop immediately terminates.
   - We calculate `Pref(2,2)` by accumulating `BIT` values downward.
   - Result: 1 + 2 + 3 + 4 = 10. ✓

2. **Update(0, 1, value=5):**
   - Old value is 2. New is 5. `delta = 3`.
   - `_add(1, 2, delta=3)`
   - Loop `i` from 1 to `rows`. Inside, loop `j` from 2 to `cols`.
   - `BIT[1][2] += 3`.
   - `BIT[2][2] += 3`.
   - The tree instantly reflects the 2D mutation! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(N * M)$ |
| **Average** | $O(log N * log M)$ | $O(N * M)$ |
| **Worst** | $O(log N * log M)$ | $O(N * M)$ |

Because of the two nested `while` loops manipulating bits, the operations take $O(log N x log M)$ time. For a 1000 x 1000 matrix, this is about 10 x 10 = 100 operations, which is incredibly fast!
Space complexity is $O(N \times M)$ to store the 2D BIT arrays.

## Variants & optimizations

- **3D Fenwick Tree:** The logic extends infinitely! You can just nest a third `while` loop for the Z-axis to query 3D volumes in space in $O(log N x log M x log Z)$ time.

## Real-world applications

- **Computer Vision & Graphics:** Instantly adjusting brightness/contrast patches in image editors and calculating the average luminosity of bounded pixel rectangles.
- **Spatial Indexing:** Fast querying of density/populations in rectangular coordinate boundaries on dynamic grid-based maps.

## Related algorithms in cOde(n)

- **[fenwick_02 - Range Sum Query](fenwick_02_range-sum-query-bit.md)** — The 1D precursor.
- **[dynamic_10 - Max Maximal Square](../dynamic/dp_10_unique-paths.md)** *(Conceptual link)* — Standard 2D DP/Prefix matrices rely on the exact same inclusion-exclusion geometry.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
