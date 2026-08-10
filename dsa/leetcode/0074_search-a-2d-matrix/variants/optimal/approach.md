## General

**Recognize one sorted sequence hidden inside the rectangle**

Every row is sorted in non-decreasing order. In addition, the first value of each row is greater than the last value of the preceding row. The second property is what connects the rows: after reading the last cell of one row, the first cell of the next row is strictly larger. Therefore row-major order across the complete matrix is globally sorted.

The algorithm can treat the matrix as a virtual one-dimensional array without copying any values. If each row has `n` columns, virtual index `k` maps to

$$
\text{row}=\left\lfloor\frac{k}{n}\right\rfloor,
\qquad
\text{column}=k\bmod n.
$$

`divmod(k, n)` computes both values together. Every index from zero through `m * n - 1` maps to exactly one matrix cell, and every cell maps back to exactly one virtual index `row * n + column`. This is a representation change, not an allocation.

**Search for the leftmost value at least as large as the target**

The implementation uses a lower-bound-style binary search. It seeks the first virtual position whose value is greater than or equal to `target`. If that value equals the target, the target exists. If it is greater, then every later value is also too large and every earlier value is smaller, so the target is absent.

The search interval is inclusive: `left = 0` and `right = m * n - 1`. The constraints guarantee at least one row and one column, so both endpoints are valid. The loop continues while the endpoints differ.

`mid = (left + right) >> 1` chooses the lower middle because right shift by one divides the non-negative sum by two using integer floor division. `divmod(mid, n)` then locates the corresponding matrix value without flattening the matrix.

**Why each comparison discards a safe half**

If `matrix[x][y] >= target`, the current midpoint might be the first qualifying position. Every position to its right is unnecessary for finding an earlier qualifying value, so `right = mid` keeps `mid` and discards only later candidates.

If the midpoint value is smaller than `target`, global sortedness proves that every virtual index at or before `mid` is also too small. None can equal the target or be the lower bound, so `left = mid + 1` safely discards all of them.

The asymmetric updates match the lower-middle choice. In the first branch, `right` moves down to `mid`, which is strictly less than the old `right` whenever `left < right`. In the second branch, `left` moves above `mid`. Thus the interval strictly shrinks on every iteration and cannot loop forever.

**A precise invariant with the above-maximum case**

When some virtual value is at least `target`, the first such position always remains inside `[left, right]`. Initially the whole array is included. The comparison rules preserve that lower-bound candidate as just argued.

If no value is at least the target because the target exceeds the matrix maximum, a conventional lower-bound search with a one-past-end sentinel would return `m * n`. This source instead has no sentinel and converges to the final valid index. That does not create a false positive because it performs an equality check after convergence. The last value is still smaller than the target, so the result is false.

This nuance explains why the final expression checks equality rather than assuming the converged position is a match. The search finds the best candidate available in its closed interval; equality determines membership.

**Trace a cross-row search**

For a three-by-four matrix, virtual indices zero through three are row zero, four through seven are row one, and eight through eleven are row two. Virtual index five maps through `divmod(5, 4)` to `(1, 1)`. Binary search may move from a value in one row to another without any row-specific logic because the cross-row ordering makes the virtual sequence continuous and sorted.

Suppose the target is 13 in `[[1,3,5,7],[10,11,16,20],[23,30,34,60]]`. Comparisons narrow the lower-bound candidate to the position containing 16. Since 16 is the first value greater than 13 but is not equal to 13, the method returns false. For target 3, convergence reaches its exact virtual position and equality returns true.

**Why the final equality is sufficient**

At termination, `left == right`. If a value at least as large as the target exists, the maintained lower-bound invariant and interval shrinking make this the first such value. A sorted sequence contains `target` exactly when that first qualifying value equals it. In the no-qualifying-value case, the selected last element is smaller and also fails equality. Hence `matrix[left // n][left % n] == target` is correct in every case.

## Complexity detail

The virtual array has $mn$ positions. Each iteration reduces the candidate interval by roughly half and performs one matrix access plus constant arithmetic, so time is $O(\log(mn))$, matching the manifest. No row-major array is actually constructed.

The algorithm stores only dimensions, two boundaries, a midpoint, and its mapped coordinates. Their count does not depend on matrix size, so auxiliary space is $O(1)$, also matching the manifest.

## Alternatives and edge cases

- **Two binary searches:** First locate a possible row by comparing row boundaries, then search within that row. Its time is $O(\log m+\log n)$, algebraically equal to $O(\log(mn))$, but it requires two search contracts.
- **Half-open lower bound:** Search `[0, m * n)` and allow the answer to equal the one-past-end sentinel. It handles an above-maximum target more conventionally but needs a guard before matrix indexing.
- **Staircase search:** Starting at the top-right and eliminating a row or column takes $O(m+n)$ time. It works under weaker row-and-column sorting but does not meet this problem's requested logarithmic bound.
- **Physically flatten the matrix:** It makes indexing obvious but wastes $O(mn)$ space and copy time.
- **Single cell:** The loop is skipped and direct equality returns the answer.
- **Target below the minimum:** Search converges to index zero; equality distinguishes absence from a match.
- **Target above the maximum:** Search converges to the last valid index; equality returns false.
- **Duplicate values within a row:** Non-decreasing rows permit them, and lower bound finds the first occurrence.
- **Cross-row boundary:** The next row's first value is strictly larger than the previous row's last value, preserving global sortedness.
- **Negative values:** Ordering and index arithmetic are unaffected by value sign.
- **Nonempty guarantee:** Direct access to `matrix[0]` is safe only because the constraints require both dimensions to be at least one.
- **Input preservation:** The method reads cells and does not modify the matrix.
