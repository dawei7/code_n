# Convert 1D Array Into 2D Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2022 |
| Difficulty | Easy |
| Topics | Array, Matrix, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-1d-array-into-2d-array/) |

## Problem Description

### Goal

Given a zero-indexed one-dimensional integer array `original` and positive
integers `m` and `n`, construct a matrix with exactly `m` rows and `n` columns
using every source element.

Preserve row-major order: indices `0` through `n - 1` form the first row,
indices `n` through `2 * n - 1` form the second row, and so forth. If the
requested dimensions cannot hold exactly all elements, return an empty matrix.

### Function Contract

Let $L$ be the length of `original`.

**Inputs**

- `original`: a list of $L$ integers, where $1 \le L \le 5 \cdot 10^4$ and
  every value is between $1$ and $10^5$, inclusive.
- `m`: the requested number of rows, where $1 \le m \le 4 \cdot 10^4$.
- `n`: the requested number of columns, where $1 \le n \le 4 \cdot 10^4$.

**Return value**

- An `m`-by-`n` list of lists in row-major order when $L = mn$; otherwise, an
  empty list.

### Examples

**Example 1**

- Input: `original = [1, 2, 3, 4], m = 2, n = 2`
- Output: `[[1, 2], [3, 4]]`

**Example 2**

- Input: `original = [1, 2, 3], m = 1, n = 3`
- Output: `[[1, 2, 3]]`

**Example 3**

- Input: `original = [1, 2], m = 1, n = 1`
- Output: `[]`
- Explanation: One cell cannot contain both source elements.

### Required Complexity

- **Time:** $O(L)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

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

#### Complexity detail

Here $L$ is the number of source elements, and a valid result satisfies
$L = mn$. Copying the consecutive row slices visits each value once, taking
$O(L)$ time. The returned matrix contains $L$ values and uses $O(L)$ space;
apart from the output, only constant auxiliary state is needed.

#### Alternatives and edge cases

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

</details>
