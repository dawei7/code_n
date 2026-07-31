## General

**Find every legal stamp in constant time**

Build a two-dimensional prefix sum of occupied cells. The sum inside any
axis-aligned stamp rectangle is then available in $O(1)$ time. Enumerate every
in-bounds top-left position; a rectangle whose sum is zero is a legal stamp
placement.

Because stamps may overlap and there is no limit on their number, placing
every legal stamp can never hurt. If this maximal collection fails to cover an
empty cell, no smaller collection can cover it either.

**Accumulate coverage without painting each rectangle**

Record every legal placement as four corner updates in a two-dimensional
difference grid. A prefix sum over that grid converts all updates into the
number of legal stamps covering each cell. Finally, inspect the original grid:
every `0` must have positive coverage. Occupied cells need no coverage and, by
construction, no recorded stamp includes one.

The rectangle prefix sum proves every recorded placement is valid, while the
difference-grid prefix sum exactly represents their union. Testing that union
therefore establishes both necessity and sufficiency.

## Complexity detail

Let $m$ and $n$ be the grid dimensions. Building the occupied prefix sum,
enumerating candidate top-left positions, accumulating coverage, and checking
cells each take $O(mn)$ time. The prefix and difference grids use $O(mn)$
space.

## Alternatives and edge cases

- **Paint every valid stamp rectangle:** This is correct but can take
  $O(mn\cdot\textit{stampHeight}\cdot\textit{stampWidth})$ time.
- **Test every empty cell separately:** Searching for a covering placement per
  cell repeats overlapping rectangle work and can be much slower than linear.
- If the stamp exceeds either grid dimension, success is possible only when
  the grid has no empty cells.
- A `1`-by-`1` stamp can cover every empty cell independently.
- Overlap is sometimes essential near the ends of an empty region.
- An all-occupied grid succeeds without placing any stamp.
