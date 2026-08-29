## General

**Classify a cell by its coordinates**

An X-Matrix has two diagonals:

- the main diagonal from the top-left corner to the bottom-right corner;
- the secondary diagonal from the top-right corner to the bottom-left corner.

For zero-based coordinates `(i, j)` in an `n x n` matrix, a cell lies on the main diagonal exactly when `i == j`. It lies on the secondary diagonal exactly when `i + j == n - 1`.

Every matrix position belongs to one of two required categories. If either diagonal condition holds, its value must be nonzero. If neither holds, its value must be zero. The solution checks this classification directly for every cell.

**Visit every row and every value**

The outer loop uses `enumerate(grid)` to obtain row index `i` and the row itself. The inner `enumerate(row)` obtains column index `j` and value `v`. This visits coordinates in ordinary row-major order, although correctness does not depend on that particular traversal order.

The diagonal branch is

`if i == j or i + j == len(grid) - 1`.

The logical OR is important because a position on either diagonal has the same nonzero requirement. In an odd-sized matrix, the central cell lies on both diagonals, but it is still one cell and is checked once by this combined condition.

If a diagonal value is zero, the method immediately returns `False`. One violation is enough to disqualify the matrix, so no remaining cells need examination.

**Require zero everywhere else**

The `elif v` branch runs only when neither diagonal condition held. In Python, an integer is truthy exactly when it is nonzero. Therefore `elif v` means “this off-diagonal value is nonzero.” Such a value violates the second X-Matrix condition, so the method returns `False`.

An off-diagonal zero is falsy, so no return occurs and scanning continues. The code could spell this as `elif v != 0`; the shorter truthiness test is equivalent under the integer-valued grid contract.

Only after every coordinate satisfies its category requirement does execution reach `return True`.

**Why checking both kinds of violation is necessary**

It is not enough to verify that both diagonals are nonzero. A matrix could have correct diagonals and also contain a nonzero value elsewhere, which would fail the definition.

It is also not enough to verify that all off-diagonal values are zero. A zero on either diagonal would fail the first condition.

The two branches cover these complementary failure types. Diagonal zero and off-diagonal nonzero are exactly all possible violations because every coordinate is either on at least one diagonal or off both.

**A coordinate-level correctness argument**

Suppose the method returns `True`. Then it did not encounter a zero at any position satisfying a diagonal equation, so every diagonal element is nonzero. It also did not encounter a truthy value outside both diagonals, so every other element is zero. Both defining conditions hold, and the grid is an X-Matrix.

Suppose instead that the grid is an X-Matrix. Every coordinate satisfying `i == j` or `i + j == n - 1` has a nonzero value, so the first failure return is never triggered. Every other coordinate has value zero, so the `elif v` return is never triggered. The loops finish and return `True`.

Finally, if the grid is not an X-Matrix, at least one of the two defining conditions fails. A diagonal zero is found by the first branch, while an off-diagonal nonzero is found by the second. The method returns `False` when that violating coordinate is reached. These directions establish exact equivalence between the method's result and the definition.

**The center of an odd matrix needs no special case**

When `n` is odd, coordinate `((n-1)/2, (n-1)/2)` satisfies both diagonal equations. The OR branch treats it as diagonal and requires it to be nonzero once. The definition also speaks about elements in the diagonals, not about counting diagonal memberships, so one check is correct.

When `n` is even, the diagonals cross between cells and no coordinate belongs to both. The same formulas still classify every diagonal position correctly.

## Complexity detail

Let `n` be the side length. In the worst case, the nested loops inspect all `n^2` cells. Each inspection performs constant-time index comparisons and a value test, so worst-case running time is `O(n^2)`. An invalid matrix may return earlier—possibly after its first cell—but asymptotic worst-case analysis must include a valid matrix or a violation at the final inspected cell.

The method stores only loop variables and reuses references to existing rows and values. It creates no second matrix, coordinate set, or diagonal arrays, so auxiliary space is `O(1)`.

The input grid is read but never modified. `len(grid) - 1` is recomputed inside the condition, but Python list length is constant time; storing it once could reduce a small constant without changing complexity.

## Alternatives and edge cases

- **Check the two diagonals first, then all other cells:** This can work, but avoiding double-checks of diagonal coordinates in the second pass requires the same coordinate classification. A single pass is simpler.
- **Build a set of diagonal coordinates:** Precompute all `(i, i)` and `(i, n-1-i)` pairs, then test membership for every cell. This uses `O(n)` extra space for formulas that are already constant-time.
- **Count nonzero cells:** An X-Matrix has `2n` nonzero diagonal positions when `n` is even and `2n-1` when odd, but the count alone cannot prove that the nonzeros are in the correct locations.
- **Sum diagonal values:** Nonzero values can cancel if negatives were allowed, and even with nonnegative values a sum does not verify off-diagonal zeros. Per-cell conditions are direct and reliable.
- **Use only `i == j`:** This checks the main diagonal but misses the secondary diagonal from top right to bottom left.
- **Use `i + j == n`:** Zero-based secondary-diagonal coordinates sum to `n - 1`, not `n`. The latter is an off-by-one error.
- **Logical AND between diagonal tests:** A cell needs to be on either diagonal, not both. AND would classify only the odd-sized center as diagonal.
- **Odd-sized center:** It belongs to both diagonals and must simply be nonzero; the OR condition handles it once.
- **Even-sized matrix:** There is no shared center cell, but both formulas still identify exactly `2n` diagonal positions.
- **Zero on a diagonal corner:** The first inspected corner may cause immediate failure. Corners `(0,0)` and `(0,n-1)` lie on the two diagonals.
- **Nonzero beside a diagonal:** Even if all diagonal entries are correct, any such off-diagonal value causes `False`.
- **All-zero matrix:** It satisfies the off-diagonal condition but fails at the first diagonal cell, so it is not an X-Matrix.
- **All-nonzero matrix:** It satisfies the diagonal condition but fails as soon as an off-diagonal cell is inspected.
- **Truthiness of negative values:** The source values are nonnegative, but Python would also treat a negative integer as nonzero, which is the correct requirement for either category test.
- **Square-shape guarantee:** The coordinate formulas use `len(grid)` for both dimensions. The contract guarantees every row has that length; a ragged or rectangular input is outside scope.
- **Input mutation:** Enumeration reads existing rows and values only, leaving `grid` unchanged.
