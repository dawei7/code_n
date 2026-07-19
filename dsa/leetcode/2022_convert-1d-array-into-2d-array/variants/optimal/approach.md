## General
**Reject incompatible dimensions first**

An `m`-by-`n` matrix has exactly $mn$ cells. Using all source values exactly
once is therefore possible if and only if `len(original) == m * n`. Return the
empty matrix immediately when this equality fails; truncating or padding would
violate the contract.

**Partition the source into consecutive rows**

When the dimensions match, take consecutive chunks of `n` elements. The chunk
beginning at `row * n` becomes that row of the result. Thus source index `i`
appears in row `i // n` and column `i % n`, preserving its position in
row-major order.

The equality check guarantees exactly `m` complete chunks: no row is short and
no element remains. The index mapping assigns every source index to one unique
cell and reads the cells back in increasing source-index order. The returned
matrix therefore has the requested shape and ordering.

## Complexity detail
Here $L$ is the number of source elements, and a valid result satisfies
$L = mn$. Copying the consecutive row slices visits each value once, taking
$O(L)$ time. The returned matrix contains $L$ values and uses $O(L)$ space;
apart from the output, only constant auxiliary state is needed.

## Alternatives and edge cases
- **Index-by-index placement:** Preallocate `m` rows and append each value to
  row `i // n`; this has the same asymptotic costs but requires more explicit
  bookkeeping.
- **Repeated row concatenation:** Rebuilding a row with `row = row + [value]`
  copies its accumulated prefix each time and can take $O(L^2)$ time for one
  long row.
- Both too few and too many source elements require an empty result.
- With `m = 1`, the valid matrix contains one row holding the entire source.
- With `n = 1`, each source value becomes its own one-element row.
- Duplicate values are preserved independently and in their original order.
