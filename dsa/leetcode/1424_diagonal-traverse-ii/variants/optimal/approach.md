## General

**A diagonal is identified by row plus column**

Use zero-based coordinates `(i, j)`. Moving one step upward and one step right changes them to `(i - 1, j + 1)`. Their sum stays constant:

$$
(i-1)+(j+1)=i+j.
$$

Therefore, every cell on one requested diagonal has the same value of $i+j$, and different requested diagonals have different sums. The top-left cell has sum zero, and traversal proceeds through increasing sums.

This property works for a ragged list just as it does for a rectangle. Rows may have different lengths, but every existing cell still has well-defined row and column indices.

**Encode both ordering rules in a tuple**

The nested loops visit every real cell:

```python
for i, row in enumerate(nums):
    for j, v in enumerate(row):
        arr.append((i + j, j, v))
```

Each tuple stores:

1. `i + j`, the diagonal identifier.
2. `j`, the position-order key within that diagonal.
3. `v`, the value to return.

Python sorts tuples lexicographically. It compares the first component, then the second only when the first ties, then the third only if both earlier components tie.

The first component places all cells from diagonal zero before all cells from diagonal one, and so on. It also groups cells on the same diagonal next to each other.

**Why increasing column gives the required within-diagonal direction**

For a fixed diagonal identifier $d$, row and column satisfy:

$$
i=d-j.
$$

As `j` increases, `i` decreases. Thus sorting a diagonal by increasing column visits cells from larger row indices to smaller row indices: bottom-left toward top-right. That is exactly the required direction.

For the main three-by-three example, diagonal $d=2$ contains:

| Coordinate | Tuple key | Value |
|---|---|---:|
| `(2, 0)` | `(2, 0)` | 7 |
| `(1, 1)` | `(2, 1)` | 5 |
| `(0, 2)` | `(2, 2)` | 3 |

Sorting by the second tuple component produces 7, 5, 3.

No two distinct cells can share both `i+j` and `j` because those two numbers uniquely determine `i`. Therefore, the value component never has to break a meaningful coordinate tie. Including `v` as the third tuple element is convenient storage, not an additional intended ordering rule.

**Sort once and project the values**

`arr.sort()` applies the two ordering rules simultaneously. After sorting, the comprehension:

```python
return [v[2] for v in arr]
```

extracts the third component of every tuple and discards the coordinate keys. The variable name `v` in this comprehension refers to a whole tuple, so `v[2]` is the original cell value.

**Trace across the first diagonals**

For `nums = [[1,2,3],[4,5,6],[7,8,9]]`, the coordinate tuples begin:

```text
(0, 0, 1)
(1, 1, 2)
(2, 2, 3)
(1, 0, 4)
(2, 1, 5)
...
```

After tuple sorting, the order becomes:

```text
(0, 0, 1)
(1, 0, 4), (1, 1, 2)
(2, 0, 7), (2, 1, 5), (2, 2, 3)
(3, 1, 8), (3, 2, 6)
(4, 2, 9)
```

Projecting the values gives `[1,4,2,7,5,3,8,6,9]`.

**Why ragged rows are handled safely**

The implementation never assumes a uniform column count. The inner `enumerate(row)` generates only coordinates that actually exist in that row. Sorting those real coordinates by diagonal and column naturally skips missing cells.

In the second example, some later rows are short and others become long again. A diagonal may therefore have gaps in potential rectangular coordinates, but only actual cells produce tuples. Their relative bottom-to-top order still follows increasing `j`.

**Why the result is correct**

Every input element contributes exactly one tuple, so no cell is lost or duplicated. Sorting first by $i+j$ orders all diagonals correctly. Among equal diagonal identifiers, sorting by $j$ orders row indices in decreasing order, which is the specified traversal direction. Extracting tuple values preserves that sorted cell order. Hence the returned list contains all and only the input elements in diagonal order.

## Complexity detail

Let $N$ be the total number of integers across all rows. Building `arr` takes $O(N)$ time and space. Sorting $N$ tuples takes $O(N\log N)$ comparison time, and the final projection takes $O(N)$ time and creates an $O(N)$ output list. The exact stored source therefore runs in $O(N\log N)$ time and uses $O(N)$ additional storage.

The manifest advertises $O(N)$ time. That bound belongs to an alternative that groups cells by diagonal while iterating rows bottom-up, or to the BFS traversal described in the editorial. The protected implementation explicitly calls `arr.sort()`, so an accurate explanation cannot claim linear time for this exact code.

## Alternatives and edge cases

- **Hash-map diagonal groups:** Iterate rows from bottom to top, append each value to group `i+j`, then concatenate groups by identifier. This achieves $O(N)$ expected time and $O(N)$ space.
- **Breadth-first traversal:** Start at coordinate `(0,0)` and enqueue the next row start before the next column cell. Careful enqueue rules visit each ragged-grid cell once in output order.
- **Sort by diagonal and negative row:** Tuple `(i+j, -i, v)` expresses the same order directly because rows should decrease within a diagonal.
- **Sort by diagonal only:** This would rely on sort stability and the original collection order, which is top-to-bottom and therefore wrong within each diagonal.
- **One cell:** Its only tuple sorts trivially and its value is returned.
- **One row:** Diagonal identifiers increase with the column, so output matches left-to-right row order.
- **Rows of length one:** Each cell has column zero, so diagonals follow increasing row order.
- **Highly ragged shape:** Missing rectangular positions are never materialized and have no effect.
- **Duplicate values:** Coordinate keys, not values, determine order, so equal cell values cause no ambiguity.
- **Manifest distinction:** The sorting source is correct but not linear; achieving the advertised time requires changing the implementation technique.
