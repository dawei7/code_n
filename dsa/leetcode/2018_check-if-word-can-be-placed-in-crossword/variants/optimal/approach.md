## General
**Treat blockers and board edges as slot boundaries.** Traverse every row and
every column. Accumulate cells until `#` or the line's end is reached; that
accumulation is one maximal non-blocked segment. A segment whose length differs
from `word` cannot be a legal slot because an adjacent non-blocked cell would
remain outside the placed word.

**Check both orientations with the same segment.** For an equal-length
segment, compare its cells with `word`, accepting a cell when it is blank or
matches the corresponding letter. Repeat against the reversed word. Return
immediately when either orientation matches.

Every horizontal or vertical placement belongs to exactly one maximal
non-blocked row or column segment. The boundary rule makes equal segment and
word lengths necessary, and the cellwise predicate is exactly the remaining
compatibility rule. Conversely, any segment passing one orientation check
provides an unblocked, fully bounded legal placement. Inspecting all row and
column segments is therefore complete.

## Complexity detail
Each of the $RC$ cells is visited once in its row and once in its column.
Compatibility checks across disjoint segments inspect at most the same total
number of cells, so time is $O(RC)$. The current segment stores at most
$\max(R,C)$ cells, giving $O(\max(R,C))$ space.

## Alternatives and edge cases
- **Try every start and direction:** Rechecking up to the word length from
  every cell is correct with boundary validation but can take
  $O(RC\lvert\texttt{word}\rvert)$ time.
- **Materialize a transposed board:** This simplifies shared row logic but uses
  $O(RC)$ additional space; column iterators avoid the copy.
- A matching prefix inside a longer unblocked run is invalid.
- Existing letters must match exactly, while spaces accept any letter.
- A one-cell word may occupy a one-cell slot bounded by edges or blockers.
