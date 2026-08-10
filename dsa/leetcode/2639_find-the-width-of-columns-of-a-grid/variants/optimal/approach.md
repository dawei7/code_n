## General

**Width is the length of the decimal text**

The problem's length rule is exactly what Python's ordinary string conversion produces for valid integers:

- `str(333)` is `"333"`, length three;
- `str(-15)` is `"-15"`, length three because the minus sign counts;
- `str(0)` is `"0"`, length one.

Therefore, there is no need to count digits with logarithms or add a special sign adjustment. `len(str(x))` directly computes the required width contribution of cell value $x$.

**Transpose rows into columns lazily**

The matrix is stored as a list of rows, but the answer is defined column by column.

`zip(*grid)` conceptually transposes the matrix for iteration:

- `*grid` passes each row as one positional iterable to `zip`;
- the first produced tuple contains every row's column-zero value;
- the second contains every row's column-one value;
- this continues for all columns.

For a rectangular $m\times n$ grid, exactly $n$ tuples are produced, each with $m$ integers.

Python's `zip` iterator is lazy. It creates one column tuple at a time rather than building a complete second matrix.

**Compute one maximum per column**

For each tuple `col`, the generator expression:

`len(str(x)) for x in col`

produces the decimal representation length of every value in that column.

`max(...)` retains the greatest length. Because every column contains $m\ge1$ values, the maximum is always defined.

The outer list comprehension collects these maxima in the order `zip` produces columns, which is increasing column index. Hence output position $j$ corresponds exactly to grid column $j$.

**Trace the mixed-sign example**

For:

`[[-15,1,3],[15,7,12],[5,6,-2]]`,

`zip(*grid)` yields conceptual columns:

- `(-15,15,5)`;
- `(1,7,6)`;
- `(3,12,-2)`.

Their string lengths are:

- $(3,2,1)$, maximum three;
- $(1,1,1)$, maximum one;
- $(1,2,2)$, maximum two.

The result is `[3,1,2]`.

The numerical maximum of the first column is 15, but its width is two, while negative 15 has width three. This shows why comparing numerical magnitudes alone is not identical to comparing text lengths when signs are present.

**Why direct string conversion is robust**

A mathematical digit formula often starts with:

$$
\lfloor\log_{10}|x|\rfloor+1.
$$

That formula needs separate handling for:

- zero, because logarithm of zero is undefined;
- negative values, because absolute value removes a sign that must be counted;
- floating-point boundary precision near powers of ten.

String conversion already follows the language's exact integer formatting and avoids all three traps. With values bounded by $10^9$, its cost is small and well-defined.


Fix output column index $j$. The $j$-th tuple from `zip(*grid)` contains exactly:

$$
\texttt{grid[0][j]},\texttt{grid[1][j]},\ldots,\texttt{grid[m-1][j]}.
$$

For each such value, `len(str(x))` equals its defined integer length. Taking their maximum therefore equals the definition of column $j$'s width.

The list comprehension performs this calculation for every $j$ in order, so the entire returned array is correct.

**Why every cell must be inspected**

Any cell can be the one with the longest representation in its column. Without examining a particular cell, an algorithm cannot rule out that it determines the answer.

The exact solution visits every cell once through the column tuples. This matches the natural $\Omega(mn)$ lower bound for arbitrary input.

**Memory behavior of the compact expression**

The returned answer has $n$ integers. During evaluation, `zip` materializes a tuple of $m$ references for the current column. The inner generator does not build a separate list of all lengths; it feeds them to `max` one at a time.

So although the manifest states $O(n)$ space for the result, Python's transposed iteration also has a temporary $O(m)$ column tuple. Peak total beyond input is $O(n+m)$ including output, not a full $O(mn)$ transposed copy.

**Input preservation**

Neither `zip`, `str`, nor `max` modifies the matrix or its integers. The original row structure remains unchanged.

**Constraints and rectangular shape**

`zip` stops at the shortest iterable. That could silently drop cells for jagged rows. The contract guarantees `grid[i].length = n` for every row, so all rows have equal length and no truncation occurs.

The one-line implementation is safe because these shape guarantees are part of the problem.

## Complexity detail

Every one of the $mn$ cells is converted to a short decimal string and measured. With integer magnitude bounded by $10^9$, each conversion is constant-bounded work, so total time is $O(mn)$.

The required answer uses $O(n)$ space. `zip` creates one $m$-element column tuple at a time, giving $O(m)$ temporary space. Precise peak additional space including output is $O(n+m)$; it is often summarized as output $O(n)$ plus streaming temporary storage.

## Alternatives and edge cases

- **Nested row/column loops:** Maintain an $n$-entry maximum array while scanning rows, avoiding the temporary column tuple and retaining $O(n)$ space.
- **Logarithmic digit counting:** Works with special cases but is more error-prone for zero, signs, and numeric boundaries.
- **Build an explicit transpose:** Correct but wastes $O(mn)$ extra space.
- **Negative value:** Its minus sign contributes one to width.
- **Zero:** Its representation has width one.
- **Positive power of ten:** String length naturally captures the new digit.
- **One-row grid:** Each column width is simply that row's value length.
- **One-column grid:** The single result is the maximum across all rows.
- **Jagged rows:** `zip` would truncate, but the rectangular contract excludes them.
- **Input preservation:** Conversion and iteration are read only.
