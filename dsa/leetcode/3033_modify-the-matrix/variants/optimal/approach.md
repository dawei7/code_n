## General

**Process one column at a time.** Every cell containing $-1$ must be replaced by the maximum value from its own column. Columns are independent: a replacement in column $j$ never affects the maximum or output of another column. The exact source therefore loops over column index `j`, determines that column's maximum, and then performs all replacements in the same column.

For a fixed column, the expression

`max(matrix[i][j] for i in range(m))`

visits every row and returns the maximum original value in that column. The reference guarantees that each column contains at least one non-negative integer. Since every other value is at least $-1$, the maximum is non-negative and cannot be the sentinel $-1$.

**Why it is safe to mutate after finding the maximum.** The maximum is computed before any $-1$ in that column is overwritten. Thus it is exactly the maximum of the column as supplied. Replacing a sentinel with that maximum does not change what the maximum would be anyway. Even if one examined the column again afterward, the result would remain the same.

Previous columns may already have been changed, but that is irrelevant because the calculation for column $j$ reads only `matrix[i][j]`. There is no cross-column dependency.

**Replace exactly the sentinel cells.** The inner row loop checks

`if matrix[i][j] == -1`.

Only those cells receive `mx`. All nonnegative values remain untouched, including values smaller than the column maximum. The task is not to fill the entire column with its maximum; it specifically replaces missing/sentinel entries.

**The source returns the same matrix object.** Despite the statement's wording about creating `answer` equal to `matrix`, the protected implementation does not allocate a copy. It edits `matrix` in place and returns it. The numerical grid is correct, but callers will observe that their original nested list has changed.

This also means the local manifest summary—“Copies the matrix”—does not describe the exact source. The implementation's behavior and memory use must be documented as in-place mutation.

**A column trace.** Consider

`matrix = [[1, 2, -1], [4, -1, 6], [7, 8, 9]]`.

Column 0 has values 1, 4, and 7. Its maximum is 7, but there are no sentinels, so it remains unchanged.

Column 1 has 2, $-1$, and 8. The maximum is 8, so the middle sentinel becomes 8.

Column 2 has $-1$, 6, and 9. Its maximum is 9, so the first-row sentinel becomes 9.

The returned matrix is `[[1,2,9],[4,8,6],[7,8,9]]`.

**Why a two-pass structure per column is necessary.** If replacements were attempted while discovering the maximum from top to bottom, a sentinel seen before the true maximum would not yet know its correct value. It could be stored for later or revisited, but the simple solution is to complete the maximum scan first and the replacement scan second. Both passes are linear in the column height.
Fix any output position $(i,j)$. If its original value is not $-1$, the inner condition is false and the method preserves it, as required. If its original value is $-1$, the first scan for column $j$ has computed the maximum among all original column values, and the second scan writes that maximum at $(i,j)$. Because every cell belongs to exactly one processed column, this argument covers the whole matrix. Hence the returned values match the requested answer.

**Why the guarantee matters.** If a column consisted entirely of $-1$, its maximum would also be $-1$, and the phrase “maximum non-missing value” would have no useful replacement. The source does not need a special case because the input contract excludes that situation by guaranteeing at least one non-negative value in every column.

## Complexity detail

Let the matrix have $M$ rows and $N$ columns. Each column is traversed once to find its maximum and once to replace sentinels, for $2MN$ cell visits. Total time is $O(MN)$.

The generator passed to `max` is lazy and stores only its current row index and value. Apart from `m`, `n`, `j`, `i`, and `mx`, the method allocates no data structure proportional to the matrix. Its auxiliary space is $O(1)$.

The matrix itself is the caller-provided input and is mutated in place; the return value is a reference to that same object. Therefore the manifest's $O(MN)$ space bound would be appropriate for a copied answer grid, but it does not match this exact implementation. If output space is counted, there is still no new output allocation here.

## Alternatives and edge cases

- **Copy the matrix first:** A deep row-by-row copy would preserve the input and use $O(MN)$ extra space, matching the manifest summary. The protected source instead chooses in-place mutation.
- **Precompute all column maxima:** Store an $N$-element maxima array, then scan the matrix once for replacement. This also takes $O(MN)$ time but uses $O(N)$ extra space; computing one column at a time avoids it.
- **Row-wise processing:** A row maximum is irrelevant because replacements depend on columns. Any row-oriented approach must still maintain separate information for every column.
- **Replace while searching:** A sentinel encountered before the true maximum cannot be filled correctly yet. The exact two-pass-per-column structure avoids that ordering problem.
- **Several $-1$ values in one column:** They all receive the same precomputed column maximum.
- **No $-1$ in a column:** The maximum is still computed, but the replacement pass changes nothing.
- **Maximum equals zero:** Zero is non-negative and valid; every sentinel in that column becomes zero.
- **Other negative values:** The contract permits only $-1$ below zero, so there is no ambiguity between a real negative intensity and the sentinel.
- **All but one cell are $-1$:** The one non-negative entry is the maximum and is copied into every sentinel position in that column.
- **Input mutation:** Any outside reference to `matrix` observes the replacements, and `result is matrix` would be true in Python.
- **Column independence:** Changes already made in earlier columns cannot affect the maximum in the current column.
