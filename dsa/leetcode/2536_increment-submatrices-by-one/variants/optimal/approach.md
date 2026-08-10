## General

**Avoid touching every cell for every query**

A direct implementation would loop over every row and column inside each rectangle. With up to $10^4$ queries and a $500\times500$ matrix, that repeats too much work.

A two-dimensional difference array records only where a rectangle's effect begins and ends. After all queries are marked, one two-dimensional prefix-sum pass reconstructs the value of every cell.

The source reuses `mat` first as the difference array and then transforms it in place into the returned matrix.

**Mark one inclusive rectangle with four corners**

For rectangle

$$
[x_1,x_2]\times[y_1,y_2],
$$

the method applies:

- `+1` at `(x1,y1)` to begin the effect;
- `-1` at `(x2+1,y1)` to stop it below the rectangle;
- `-1` at `(x1,y2+1)` to stop it to the right;
- `+1` at `(x2+1,y2+1)` to restore the region subtracted twice below and right.

The last three updates are performed only when their coordinates remain inside the `n x n` array.

This is the two-dimensional version of marking an inclusive one-dimensional interval with `diff[left]+=1` and `diff[right+1]-=1`.

**Why the bottom-right correction is positive**

Imagine reconstructing prefixes after placing the first three markers. The below-stop marker removes the effect from every cell below `x2`, and the right-stop marker removes it from every cell right of `y2`.

Cells both below and right lie in both removed regions, so they receive $-2$ even though the original `+1` should be canceled only once. Adding one at the bottom-right outer corner corrects this double subtraction.

This is inclusion-exclusion:

$$
+\text{start}
-\text{below}
-\text{right}
+\text{below-and-right}.
$$

**Queries add linearly**

Every query places its four signed markers into the same matrix. Difference arrays are additive: prefix-reconstructing the sum of marker patterns equals summing the reconstructed rectangle increments.

Overlapping rectangles therefore produce values two, three, or higher automatically. No query ordering matters because addition is commutative.

**Reconstruct with a two-dimensional prefix recurrence**

When visiting cell `(i,j)` in row-major order, the code adds:

- prefix value above, `mat[i-1][j]`;
- prefix value to the left, `mat[i][j-1]`.

The upper-left prefix `mat[i-1][j-1]` was included in both of those totals, so it is subtracted once.

The recurrence is

$$
\texttt{mat}[i][j]
\mathrel{+}=
\texttt{top}
+\texttt{left}
-\texttt{diagonal}.
$$

Boundary `if` statements omit nonexistent neighbors in the first row or first column.

After this update, `mat[i][j]` equals the sum of every difference marker in rectangle `[0,i]\times[0,j]`. A query contributes one to that prefix exactly when `(i,j)` lies inside its original rectangle.

**Trace the first query**

For `n=3` and rectangle `[1,1,2,2]`:

- add one at `(1,1)`;
- the below marker would be row 3 and is outside;
- the right marker would be column 3 and is outside;
- the correction is also outside.

Prefix reconstruction spreads the one from `(1,1)` through rows 1–2 and columns 1–2, exactly the desired bottom-right submatrix.

For a rectangle not touching boundaries, all four markers confine the spread to both inclusive coordinate ranges.


For one rectangle, the signed-corner pattern's prefix sum is one inside the rectangle and zero outside; the start activates both dimensions, stop markers deactivate each exceeded boundary, and correction fixes their overlap.

By linearity, summing marker patterns for all queries makes each cell equal the number of rectangles containing it. Since every containing query increments that cell once, this is exactly the final matrix value.

**No separate output allocation after marking**

`mat` has the required output shape from the beginning. In-place prefix reconstruction replaces marker values that are no longer needed with final cell values, because row-major order ensures top, left, and diagonal prefixes are already complete.

The temporary negative markers are not final negative cell values; reconstruction combines them with their matching starts before the matrix is returned.

## Complexity detail

Let $q$ be the number of queries. Each query performs at most four constant-time updates, costing $O(q)$.

The reconstruction visits all $n^2$ cells once, so total time is $O(q+n^2)$.

The matrix uses $O(n^2)$ space and is also the required output. Excluding output storage, only loop variables use $O(1)$ additional space; including the constructed result, space is $O(n^2)$.

## Alternatives and edge cases

- **Direct rectangle loops:** They can cost $O(qn^2)$ in the worst case.
- **Row-wise difference arrays:** Mark each affected row separately, costing $O(qn+n^2)$.
- **Full-matrix query:** Only the top-left start marker lies inside; its prefix spread covers everything.
- **Single-cell query:** Four corner updates isolate exactly that cell.
- **Bottom or right boundary:** Out-of-range stop markers are omitted safely.
- **Overlapping queries:** Their marker contributions add.
- **Inclusive coordinates:** Stops occur at `x2+1` and `y2+1`.
- **Diagonal subtraction:** It prevents double-counting the shared upper-left prefix.
- **In-place reconstruction:** Difference markers become final values.
- **Query order:** It cannot affect the additive result.
