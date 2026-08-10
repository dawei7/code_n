## General

**Search the value, not the cells**

An `m * n` multiplication table can contain hundreds of millions of cells, so constructing and sorting all products is infeasible.

Every value lies between one and `m * n`. The solution binary-searches this numeric range and asks:

“How many table entries are less than or equal to candidate `mid`?”

If at least `k` entries are no larger than `mid`, then `mid` is large enough to reach the `k`th rank. Otherwise, the answer must be larger.

**Count one row without generating it**

Row `i` contains:

`i, 2i, 3i, ..., ni`.

An entry `i * j` is at most `mid` exactly when:

`j <= mid // i`.

Therefore, the row has `mid // i` qualifying columns, except that a row contains only `n` columns. The exact contribution is:

`min(mid // i, n)`.

Summing this quantity for row indices one through `m` gives the total number of table cells whose products are at most `mid`.

This counts cells, not distinct product values. That is correct because repeated values occupy multiple positions and count multiple times in the sorted table.

**Why the count predicate is monotone**

As the candidate value increases, no previously qualifying cell stops qualifying. The count can only stay the same or increase.

Define `enough(x)` to mean that at least `k` table entries are at most `x`. Then:

- below the `k`th smallest value, `enough` is false;
- at the `k`th smallest value and above, `enough` is true.

This false-then-true shape is exactly what lower-bound binary search requires.

**Binary-search updates**

The initial interval is `left = 1` and `right = m * n`. It contains every possible table value.

While `left < right`:

1. Compute `mid = (left + right) // 2`. The source uses right shift by one, which is equivalent for nonnegative integers.
2. Count entries at most `mid`.
3. If `cnt >= k`, the answer is at most `mid`, so set `right = mid`.
4. Otherwise, fewer than `k` entries reach `mid`, so the answer is strictly larger; set `left = mid + 1`.

Each step removes at least half of the remaining value interval. When the bounds meet, they identify the smallest value for which `cnt >= k`.

**Why the smallest sufficient value is the answer**

Sort all table cells conceptually, including duplicates. Let the `k`th value be `A`.

For any `x < A`, fewer than `k` cells can be at most `x`, so the predicate is false. At `x = A`, the first `k` sorted cells are all at most `A`, so the predicate is true.

Therefore, `A` is exactly the first true value. Lower-bound binary search returns that value even if several cells equal `A` or if some integers in the numeric range never occur in the table.

**A three-by-three example**

The table contains rows:

- `[1, 2, 3]`;
- `[2, 4, 6]`;
- `[3, 6, 9]`.

For candidate three:

- row one contributes `min(3 // 1, 3) = 3`;
- row two contributes `min(3 // 2, 3) = 1`;
- row three contributes `min(3 // 3, 3) = 1`.

The total is five, so three is sufficient for `k = 5`. Candidate two has only three qualifying cells, so it is insufficient. The smallest sufficient value is three.

**Why table symmetry can improve the loop**

An `m * n` multiplication table has the same multiset of products if rows and columns are swapped. The exact source always iterates over `m` rows and caps each row at `n`.

If `m > n`, swapping them before the search would make each counting pass iterate over the smaller dimension. That optimization is not present in the literal code but explains the stronger manifest expression involving `min(m, n)`.

**No overflow issue in Python**

The upper bound `m * n` and all counts fit easily in Python's arbitrary-precision integers. In fixed-width languages, the constraints still fit within common 32-bit signed range for the product, but using a wider type for `left + right` is a safe binary-search practice.

## Complexity detail

The binary search performs `O(log(m * n))` iterations because it halves the value range from one through `m * n`.

The exact counting loop visits all `m` rows in every iteration. Its literal time complexity is:

`O(m * log(m * n))`.

The manifest states `O(min(m, n) * log(mn))`. That bound is achieved by swapping dimensions so the counting loop uses the smaller one. Since the exact source does not swap, its bound only simplifies to the manifest when `m <= n`.

The algorithm stores only search bounds, midpoint, count, and row index, so auxiliary space is `O(1)`. It never materializes the table.

Integer division and arithmetic are treated as constant-time under the standard bounded-integer model.

## Alternatives and edge cases

- **Swap dimensions first:** If `m > n`, exchange them. The same products are represented, and counting then costs `O(min(m, n))` per binary-search step.

- **Materialize and sort the table:** This uses `O(mn)` space and `O(mn log(mn))` time, which is prohibitive at the maximum constraints.

- **Min-heap row merge:** Treat each row as a sorted list and repeatedly extract the next product. It uses `O(m)` heap space and roughly `O(k log m)` time, which is too slow when `k` is large.

- **Binary search table indices:** The target rank is over values with duplicates across rows, so a single row or column index does not identify the answer. Searching the value domain with a count predicate is simpler.

- **`k = 1`:** Candidate one is the first sufficient value, so the result is one.

- **`k = m * n`:** Only the maximum product makes every cell count, so the result is `m * n`.

- **One row:** The table is `[1, 2, ..., n]`, and the count formula reduces naturally to `min(mid, n)`.

- **One column:** Each row contributes zero or one, and binary search returns the corresponding row value.

- **Duplicate products:** Values such as six can appear as `2 * 3` and `3 * 2`. Both cells are counted, as required by order statistics.

- **Candidate smaller than a row index:** `mid // i` is zero, so that row contributes no cells.

- **Candidate beyond a row maximum:** The `min` cap prevents counting more than `n` cells in that row.

- **Missing numeric values:** Binary search may test integers that do not occur in the table. The monotone count still guides it to the first occurring value at the required rank.

- **Use `cnt > k` instead of `cnt >= k`:** This would mishandle the boundary where exactly `k` entries are at most the answer. “At least `k`” is the correct predicate.

- **Move `left = mid` on an insufficient candidate:** This can stall when bounds are adjacent. `mid + 1` guarantees progress because `mid` is proven too small.

- **Return any sufficient value:** Only the smallest sufficient value is the `k`th order statistic. Lower-bound updates preserve that requirement.
