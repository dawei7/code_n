## General

**Decide whether one move suffices.** A rook attacks the queen immediately
when they share a row or column, unless the bishop lies strictly between them
on that same line. A bishop attacks immediately when the absolute row and
column differences to the queen are equal, unless the rook lies strictly
between them on the same diagonal.

Diagonal collinearity must preserve the correct diagonal direction. Squares
on one diagonal share `row - column`; squares on the other share
`row + column`. Checking one of these invariants together with strict row
betweenness distinguishes a genuine blocker from a rook on the crossing
diagonal.

Return 1 if either direct attack is unobstructed. Otherwise return 2: the rook
can always move to a clear square in the queen's row or column and capture on
its following move. Thus no result larger than two is necessary.

## Complexity detail

The method performs a fixed number of coordinate comparisons on a fixed
$8\times8$ board. It therefore uses $O(1)$ time and $O(1)$ auxiliary space.
The complete legal domain is finite, so this bound is verified by a strict
bounded-domain certificate rather than artificial runtime scaling.

## Alternatives and edge cases

- **Directional ray simulation:** Walking all rook and bishop rays is correct, but direct coordinate relations are shorter and remain constant-time.
- **Full move search:** Breadth-first search can find the answer, but the proof that the result is always 1 or 2 makes it unnecessary.
- **Rook blocker:** The bishop blocks only when it lies strictly between the rook and queen on their shared row or column.
- **Bishop blocker:** Matching an absolute diagonal distance alone is insufficient; the rook must occupy the same diagonal invariant and lie between the endpoints.
- **Crossing diagonal:** A rook equally far from the bishop in row and column may lie on the opposite diagonal and must not be treated as a blocker.
