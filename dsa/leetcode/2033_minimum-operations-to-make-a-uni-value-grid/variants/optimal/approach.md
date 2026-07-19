## General
**Check whether a common value is reachable**

Adding or subtracting `x` never changes a value's remainder modulo `x`.
Therefore, all cells can become equal only if every flattened value has the
same remainder. If any remainder differs from the first, return `-1`.

**Choose a median target**

When the remainder condition holds, divide every difference by `x`; each cell
then lies on the same integer step lattice. For a proposed target, the number
of operations is the sum of absolute lattice distances to that target. A
median of the flattened values minimizes this sum.

Sort the values, select either middle value as the median, and add
`abs(value - median) // x` for every cell. Each term is integral because all
remainders match.

The remainder test is necessary because operations cannot cross residue
classes, and it is sufficient because any two same-remainder values differ by
an integer multiple of `x`. For reachable inputs, moving a target toward the
median cannot increase the number of values on the nearer side more than on
the farther side; the standard median absolute-deviation argument proves that
no other target uses fewer operations.

## Complexity detail
Flattening $P$ cells and checking remainders takes $O(P)$ time. Sorting takes
$O(P\log P)$ time, and summing distances takes another $O(P)$ time. The
flattened sorted list occupies $O(P)$ space.

## Alternatives and edge cases
- **Linear-time selection:** A selection algorithm can find a median in
  expected or worst-case $O(P)$ time, followed by a linear distance sum, but
  it is more involved than sorting.
- **Evaluate every cell value as target:** This is correct after the remainder
  check but recomputes $P$ distances for $P$ targets and takes $O(P^2)$ time.
- A single-cell grid already needs zero operations.
- Equal values need zero operations regardless of `x`.
- For an even number of cells, either middle value minimizes the total.
- Matching remainders matter; merely having pairwise differences smaller than
  `x` does not make conversion possible.
- The result counts step operations, so each absolute difference is divided
  by `x`.
