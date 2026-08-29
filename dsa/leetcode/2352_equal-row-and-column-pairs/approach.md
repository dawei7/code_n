## General

**Check every ordered row-column pair directly**

There are `n` rows and `n` columns, so there are `n^2` candidate pairs `(i,j)`. The exact solution tries each one.

For a fixed row `i` and column `j`, their entries at sequence position `k` are:

- row entry `grid[i][k]`;
- column entry `grid[k][j]`.

The row and column are equal exactly when these values match for every `k` from zero through `n - 1`.

**Use all to express universal equality**

The generator

`grid[i][k] == grid[k][j] for k in range(n)`

produces one Boolean comparison per sequence position. `all(...)` returns `True` only when every comparison is true.

It short-circuits on the first mismatch. A pair that differs in its first position costs only one comparison, while an equal pair or one differing at the end requires all `n` comparisons.

The Boolean result is added directly to `ans`. In Python, `True` has integer value one and `False` zero, so each equal pair increases the count by one and every unequal pair adds nothing.

**Pair identity includes both indices**

If two rows have identical contents and both match the same column, they are two different `(row,column)` pairs and must both count. The nested loops naturally visit both row indices.

Likewise, two identical columns matching one row create two pairs. The method counts index pairs, not merely distinct sequence values.

For the second example, rows two and three are identical and both equal column two. They contribute separately, in addition to row zero matching column zero.

**Why direct comparison is correct**

For any candidate `(i,j)`, `all` is true if and only if

`grid[i][0] = grid[0][j], grid[i][1] = grid[1][j], ..., grid[i][n-1] = grid[n-1][j]`.

That list of equalities is exactly the definition that row `i` and column `j` contain the same elements in the same order.

The nested loops enumerate every possible row and every possible column once. Therefore every valid pair contributes one and no invalid pair contributes. The final total is exact.

**No row or column object needs to be built**

The method indexes the existing matrix during comparison. It does not transpose the matrix or allocate column lists.

This saves auxiliary storage, though it repeats row-column comparisons when many sequences are identical. The tradeoff is constant extra space for cubic worst-case time.

**The exact implementation differs from the manifest summary**

The manifest describes counting row tuples in a hash map and looking up each constructed column tuple, which runs in `O(n^2)` time and uses `O(n^2)` space.

The provided Optimal source is the direct triple-nested logic: two explicit loops plus the generator's `k` loop. Its literal worst-case time is `O(n^3)` and its auxiliary state is constant. Documentation must follow that source rather than claiming the hash-map behavior.

**A small trace**

For row `[2,7,7]` and column one `[2,7,7]`, all three comparisons succeed and one is added. For the same row against column zero `[3,1,2]`, the first comparison `2 == 3` fails, `all` stops, and zero is added.

The traversal order does not affect the answer because each pair's equality is independent.

## Complexity detail

There are `n^2` row-column candidates. In the worst case, each requires `n` element comparisons, giving `O(n^3)` time. Short-circuiting can reduce actual work on mismatching data but not the worst case, such as a matrix where many rows and columns match through their final positions.

The algorithm stores loop indices, `ans`, and a generator frame, all independent of `n`, so auxiliary space is `O(1)`. The required input matrix is not counted and is not modified.

Integer comparisons are constant time under the bounded values. The maximum answer is `n^2`.

## Alternatives and edge cases

- **Row-frequency hash map:** Convert every row to a tuple, then build each column tuple and add its row frequency. This improves time to `O(n^2)` at the cost of `O(n^2)` stored tuple data.
- **Trie of rows:** Insert every row sequence and query each column sequence. It also uses `O(n^2)` time and space but has more implementation overhead.
- **Transpose then compare:** Materialize columns as rows and count matching sequences. This still needs a frequency strategy to avoid quadratic sequence comparisons.
- **One-by-one matrix:** Its only row equals its only column, so the answer is one.
- **All entries equal:** Every row equals every column and the answer is `n^2`, realizing the cubic comparison worst case.
- **No matching pair:** Every `all` call eventually fails and the result is zero.
- **Duplicate rows:** Each row index contributes independently when a column matches.
- **Duplicate columns:** Each column index likewise contributes independently.
- **Same multiset but different order:** The elementwise sequence comparison rejects it.
- **Short-circuit behavior:** An early mismatch saves work but does not change correctness.
- **Boolean arithmetic:** `True` adds one and `False` adds zero in Python; other languages may require an explicit conditional.
- **Input preservation:** Only indexed reads occur.
