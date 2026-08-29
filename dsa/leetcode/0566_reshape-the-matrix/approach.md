## General

Reshaping changes row and column boundaries but must preserve the single row-major sequence of elements. The solution assigns every element a flat position and converts that same position into coordinates in both shapes.

Let the original dimensions be `m` rows and `n` columns. The original element count is `m * n`, while the requested count is `r * c`.

**Reject an impossible shape immediately.** If these products differ, some elements would need to be lost or invented. The method returns the original `mat` object unchanged.

Matching dimensions individually is not required. Shapes such as two-by-two and one-by-four are compatible because both contain four cells.

**Allocate the legal target.** When counts match, `ans = [[0] * c for _ in range(r)]` creates `r` independent rows of `c` placeholders.

The comprehension is important in Python: it avoids making every row reference the same inner list.

**Use one flat index for row-major order.** The loop visits:

`i = 0, 1, ..., m * n - 1`.

For an array with `q` columns, flat row-major index `i` maps to:

- row `i // q`;
- column `i % q`.

Integer division counts how many complete rows precede the position, and remainder gives the offset inside its row.

Therefore the source coordinate is:

`mat[i // n][i % n]`,

because the original has `n` columns.

The destination coordinate is:

`ans[i // c][i % c]`,

because the new shape has `c` columns.

Assigning source to destination at the same flat index preserves the complete traversal order.

For `[[1,2],[3,4]]` reshaped to one-by-four:

- flat zero maps source `(0,0)` to destination `(0,0)`;
- flat one maps `(0,1)` to `(0,1)`;
- flat two maps `(1,0)` to `(0,2)`;
- flat three maps `(1,1)` to `(0,3)`.

The output is `[[1,2,3,4]]`.

For a four-by-one target, the same flat sequence produces one value per new row.

**Why every source element is used exactly once.** The flat loop covers every integer in the valid element range once. The division/remainder mapping is a bijection between that range and every valid coordinate of a rectangular matrix.

**Why every destination cell is filled exactly once.** Equal element counts give the destination the same flat-index range. Different `i` values cannot map to the same quotient/remainder pair, and every pair from row zero through `r - 1` and column zero through `c - 1` corresponds to one `i = row * c + column`.

**Why order is preserved across old row boundaries.** When `i % n` reaches `n - 1`, the next source coordinate moves to the next row at column zero. Destination boundaries are determined independently by `c`, but flat `i` still increases by one. Thus only grouping changes, never sequence.

The source matrix is read-only. For a legal reshape, a new matrix is returned; for an illegal reshape, the exact original object is returned as specified.

It is useful to write the flat-order invariant explicitly. Immediately before loop iteration `i`, destination flat positions zero through `i - 1` contain the same values as source flat positions zero through `i - 1`, in the same order. The assignment copies source position `i` into destination position `i`, extending the invariant by one. After the final iteration, it covers the complete matrices.

For a less symmetric example, reshape `[[1,2,3],[4,5,6]]` from two-by-three into three-by-two. The shared flat sequence is `1,2,3,4,5,6`. Destination row boundaries occur after values two and four, producing `[[1,2],[3,4],[5,6]]`. Notice that source neighbors three and four cross an old row boundary but become neighbors in one destination row; their flat order is still unchanged.

The coordinate formulas are inverses of flattening. Original coordinate `(u, v)` has flat index `u * n + v`; applying division and remainder by `n` recovers `(u, v)`. The same flat index interpreted with divisor `c` gives its unique target coordinate. This mathematical bijection is why no special logic is needed when row sizes have no common factor.

Returning `mat` immediately on failure also avoids an unnecessary copy. Callers receive the same valid original shape and data rather than a partially filled or merely equal replacement.

## Complexity detail

For a legal reshape, let $N=mn=rc$. Allocation and the flat loop each take $O(N)$ time, so time is $O(mn)$.

The returned matrix stores $rc$ elements, giving $O(rc)$ result space, matching the manifest. Beyond output storage, the algorithm uses only constant scalar state.

For an illegal reshape, checking products and returning the input takes $O(1)$ time and auxiliary space.

On a legal reshape, output allocation is unavoidable because the result needs a different nested row structure even though scalar values are preserved.

## Alternatives and edge cases

- **Flatten then regroup:** Building a separate one-dimensional list is clear but adds another $O(mn)$ temporary buffer.
- **Nested source loops with destination pointers:** It is equivalent but requires manually updating row and column counters.
- **Different element counts:** Return the original matrix without partial allocation.
- **Same shape:** The code creates an equivalent new matrix because the reshape is legal.
- **One-row target:** Flat positions become consecutive columns.
- **One-column target:** Every flat position becomes a separate row.
- **Single element:** Any legal one-cell shape is one by one.
- **Negative or zero values:** Values are copied without interpretation.
- **Independent destination rows:** The list comprehension avoids shared-row aliasing.
- **Input immutability:** Legal reshaping copies references/values into a new outer structure.
- **Row-major guarantee:** One flat index is the invariant connecting both coordinate systems.
