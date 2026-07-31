## General

Blanks may change position, but pieces never pass one another. Consequently,
removing every `_` from both strings must leave the same sequence of `L` and
`R` pieces. The remaining question is whether each paired piece can travel from
its initial index to its requested index.

**Pair pieces without storing them**

Keep one pointer in each string. Advance each pointer past blanks, then compare
the next two pieces. Different piece types make the transformation impossible.
For a matched `L`, the initial index must be at least the target index because
that piece can move only left. For a matched `R`, the initial index must be at
most the target index because it can move only right.

After a valid pair, advance both pointers and repeat. At the end, both strings
must run out of pieces together.

These conditions are also sufficient. Matching the nonblank sequences preserves
piece order. Process the paired pieces from left to right: every `L` has enough
blank space on its left to reach its no-later target, and every `R` has enough
blank space on its right to reach its no-earlier target. Since the paired order
is unchanged, those moves can be scheduled without forcing two pieces to cross.

## Complexity detail

Each pointer advances monotonically through a length-$n$ string, so the scan
takes $O(n)$ time. Only the two indices are stored, giving $O(1)$ auxiliary
space.

## Alternatives and edge cases

- **Remove blanks and store positions:** Comparing filtered piece strings and
  two position arrays expresses the same conditions in $O(n)$ time, but uses
  $O(n)$ additional space.
- **Search the state graph:** Breadth-first search over all reachable strings
  is useful as an exhaustive oracle for tiny inputs, but the number of
  arrangements grows exponentially.
- **Piece order:** Matching counts alone is insufficient; the complete
  left-to-right sequence of `L` and `R` must agree.
- **Direction boundaries:** An `L` may remain still or move left, while an `R`
  may remain still or move right.
- **Only blanks:** Two all-blank strings are already equal and therefore
  transformable.
