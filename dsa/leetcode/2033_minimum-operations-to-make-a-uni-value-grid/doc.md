# Minimum Operations to Make a Uni-Value Grid

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2033 |
| Difficulty | Medium |
| Topics | Array, Math, Sorting, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/) |

## Problem Description

### Goal

An integer grid has $M$ rows and $N$ columns. In one operation, choose one cell
and either add `x` to its value or subtract `x` from it. Operations affect only
the selected cell and may be repeated.

Make every grid cell contain the same integer using as few operations as
possible. Return that minimum count when a common value is reachable; if the
step size prevents some cells from ever becoming equal, return `-1`.

### Function Contract

Let $P = MN$ be the number of cells.

**Inputs**

- `grid`: a nonempty $M$-by-$N$ rectangular integer matrix with
  $1 \le P \le 10^5$ and cell values from $1$ through $10^4$.
- `x`: the positive amount added or subtracted by one operation, where
  $1 \le x \le 10^4$.

**Return value**

- The minimum operation count needed to make all $P$ values equal, or `-1`
  when no common value is reachable.

### Examples

**Example 1**

- Input: `grid = [[2, 4], [6, 8]], x = 2`
- Output: `4`
- Explanation: Targeting `4` costs one operation for `2`, none for `4`, one
  for `6`, and two for `8`.

**Example 2**

- Input: `grid = [[1, 5], [2, 3]], x = 1`
- Output: `5`

**Example 3**

- Input: `grid = [[1, 2], [3, 4]], x = 2`
- Output: `-1`

### Required Complexity

- **Time:** $O(P\log P)$
- **Space:** $O(P)$

<details>
<summary>Approach</summary>

#### General

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

#### Complexity detail

Flattening $P$ cells and checking remainders takes $O(P)$ time. Sorting takes
$O(P\log P)$ time, and summing distances takes another $O(P)$ time. The
flattened sorted list occupies $O(P)$ space.

#### Alternatives and edge cases

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

</details>
