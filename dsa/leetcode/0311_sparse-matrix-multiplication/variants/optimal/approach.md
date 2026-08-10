## General

Let `mat1` have $m$ rows and $k$ columns, and let `mat2` have $k$ rows and $n$ columns. Their shared dimension $k$ makes multiplication possible. The product has $m$ rows, inherited from `mat1`, and $n$ columns, inherited from `mat2`.

The exact source uses the direct dense definition of matrix multiplication. For every output coordinate `(i, j)`, it computes the dot product of row `i` from `mat1` and column `j` from `mat2`:

$$
\texttt{ans}[i][j]
=
\sum_{t=0}^{k-1}\texttt{mat1}[i][t]\cdot\texttt{mat2}[t][j].
$$

The local manifest describes indexing nonzero entries of the right matrix, but `solution.py` does not implement any sparse representation or zero-skipping condition. This explanation follows the executable three-loop method exactly.

**Why the dimensions line up**

For a fixed output row `i`, `mat1[i]` contains $k$ values. For a fixed output column `j`, taking `mat2[0][j]`, `mat2[1][j]`, through `mat2[k - 1][j]` also gives $k$ values.

The shared index selects corresponding positions along that row and column. Multiplying each pair and adding all $k$ products produces one scalar output cell.

The problem guarantees `len(mat1[0]) == len(mat2)`, so every access `mat1[i][k]` has a matching `mat2[k][j]`. No dimension validation is needed in the method.

**Creating the output**

The source reads

- `m = len(mat1)` for the output row count;
- `n = len(mat2[0])` for the output column count.

It creates `ans` as $m$ distinct rows, each containing $n$ zeros. Starting with zero is necessary because every output cell is built as a running sum of products.

The list comprehension creates a new inner list for each row. This avoids aliasing: changing `ans[i][j]` affects only that row rather than accidentally modifying the same shared row object several times.

**The three nested loops**

The outer loop chooses output row `i` from 0 through $m-1$. The middle loop chooses output column `j` from 0 through $n-1$. Together, these loops visit every one of the $mn$ output coordinates exactly once.

For one fixed `(i, j)`, the inner loop iterates over every shared-dimension index from 0 through `len(mat2) - 1`. At each index it adds

`mat1[i][k] * mat2[k][j]`

to the current output cell.

When the inner loop begins, `ans[i][j]` is zero. After its first iteration, it contains the contribution through shared index 0. After shared index `t`, it contains

$$
\sum_{q=0}^{t}\texttt{mat1}[i][q]\cdot\texttt{mat2}[q][j].
$$

After the final iteration, this is exactly the complete dot-product formula. The next `(i, j)` cell starts from its own independent zero.

Although `k` is also conventionally used as the name of the shared dimension, in the Python source it is the loop variable. `len(mat2)` supplies the dimension size, and the loop variable takes each valid shared index in turn.

**Tracing the example**

For

`mat1 = [[1,0,0],[-1,0,3]]`

and

`mat2 = [[7,0,0],[0,0,0],[0,0,1]]`,

the top-left output is the dot product of `[1, 0, 0]` with the first column `[7, 0, 0]`:

$$
1\cdot7+0\cdot0+0\cdot0=7.
$$

The first row's other two dot products are zero, producing `[7, 0, 0]`.

For the second output row:

$$
(-1)\cdot7+0\cdot0+3\cdot0=-7,
$$

$$
(-1)\cdot0+0\cdot0+3\cdot0=0,
$$

and

$$
(-1)\cdot0+0\cdot0+3\cdot1=3.
$$

The completed product is `[[7,0,0],[-7,0,3]]`.

The numerous multiplications by zero illustrate the missed sparse optimization: they do not change the sum, but the exact source still executes them.

**Why every output value is correct**

For each output coordinate, matrix multiplication is defined as one particular row-column dot product. The outer and middle loops select every coordinate. The inner loop visits every term in that coordinate's defining sum once, using the same shared index for the row value and column value.

No term is skipped, duplicated, or assigned to another output cell. Because each `ans[i][j]` starts at zero and receives precisely its required terms, all output entries match the mathematical product.

## Complexity detail

There are $m$ choices for `i`, $n$ choices for `j`, and $k$ shared indices for each pair. The exact number of multiply-add iterations is $mnk$, so time complexity is $O(mnk)$ regardless of how many matrix entries are zero.

The returned matrix contains $mn$ values and therefore uses $O(mn)$ output space. Apart from this required result, the algorithm stores only dimensions and loop indices, so auxiliary space is $O(1)$.

The manifest's $O(mk+kn+z)$ time and $O(kn)$ sparse-index space do not apply to this implementation. Here, no preprocessing scans into sparse buckets, and $z$—the number of compatible nonzero products—does not control executed work.

## Alternatives and edge cases

- **Skip zero values from `mat1`:** Reorder loops as row `i`, shared index `t`, then output column `j`. If `mat1[i][t]` is zero, skip the entire column loop. This helps when the left matrix is sparse while retaining dense storage.
- **Compress both matrices by row:** Store only `(column, value)` pairs for every nonzero entry. For each nonzero `mat1[i][t]`, propagate products through nonzero entries in row `t` of `mat2`. This realizes the sparse behavior described by the manifest.
- **CSR for `mat1` and CSC for `mat2`:** Intersect sorted shared indices for each output row-column pair. This avoids zero products but adds compression and two-pointer machinery.
- **Transpose `mat2`:** Turning its columns into contiguous rows can make each dot product easier to express and can improve memory locality, but it still performs $O(mnk)$ arithmetic unless zeros are skipped.
- **Return a sparse product:** The contract requires a dense $m\times n$ list, so even a sparse multiplication strategy must eventually materialize zero output entries.
- **All-zero matrix:** Every multiply-add contributes zero, and the initialized output is returned unchanged.
- **One-by-one matrices:** The loops execute once and return the product of the two scalar entries.
- **Negative entries:** Ordinary signed multiplication and addition naturally handle negative contributions and cancellation.
- **Cancellation to zero:** An output zero may result from nonzero positive and negative products canceling, so a sparse algorithm cannot infer output sparsity merely from input positions.
- **Dense inputs:** The direct method performs the asymptotically expected $mnk$ work, and sparse metadata would offer little arithmetic reduction.
- **Sparse inputs:** The exact method still performs all $mnk$ multiplications, including products containing zero; this is its main limitation relative to the problem's title.
- **Compatible dimensions:** The source assumes at least one row and column and a matching shared dimension, all guaranteed by the constraints.
- **No input mutation:** The method only reads both matrices and writes a newly allocated result.
- **Integer magnitude:** Products and sums remain exact in Python integers, including negative totals.
