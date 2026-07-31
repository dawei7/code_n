## General

**Reject invalid lengths before comparing equality.** A valid triangle must
satisfy all three strict inequalities: $A+B>C$, $A+C>B$, and $B+C>A$.
Checking only `A + B > C` incorrectly assumes that `C` is the largest side,
which the table does not guarantee. If any pair sum is less than or equal to
the remaining side, return `Not A Triangle` immediately.

**Classify only the surviving rows.** When `A = B` and `B = C`, all three
sides are equal and the result is `Equilateral`. Otherwise, if any one of the
three equality pairs holds, exactly two sides are equal and the result is
`Isosceles`. A valid row with no equal pair is `Scalene`.

This CASE order is complete and mutually exclusive. Validity is decided
first, so equal but degenerate lengths cannot be mislabeled; the equality
branches then partition every valid triangle into exactly one class.

## Complexity detail

Let $n$ be the number of rows. Each row receives a constant number of integer
additions and comparisons, giving $O(n)$ time. The query needs $O(1)$
auxiliary space apart from the required result table. Because one output row
is required per input row, the linear time bound is asymptotically optimal.

## Alternatives and edge cases

- **Sort each row's sides first:** Sorting three values is constant work and allows one inequality check, but SQL row-wise sorting is less direct than stating all three inequalities.
- **Check equality before validity:** This can label a degenerate row such as `(0, 0, 0)` as equilateral instead of rejecting it.
- **Check only one pair sum:** This fails whenever the largest side is not in the assumed column.
- A pair sum equal to the third side is `Not A Triangle`; the inequality is strict.
- Isosceles equality may occur in any of the three column pairs.
- Output order is unrestricted, but row multiplicity must be preserved.
