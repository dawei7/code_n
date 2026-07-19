## General
**Prove impossible multiplicities before exploring paths**

Count characters in the board and target. If any target multiplicity exceeds the board's supply, no path can exist and exponential search is unnecessary. Also reject when the word is longer than the number of cells.

A valid path can be traversed in reverse. Therefore, if the word's final character occurs less often on the board than its first character, reverse the search word. This preserves existence while reducing the number of starting cells and often the early branching factor.

**Mark a cell only for the lifetime of its current path**

At a candidate cell, first reject out-of-bounds coordinates, a character mismatch, or a cell already marked by the current path. If it matches the final word position, return true. Otherwise replace the board character with a sentinel unavailable value, recurse to four orthogonal neighbors, and restore the original character before returning.

Restoration must occur on both failure and success paths unless the function immediately abandons the board forever after success. A structured save/restore step avoids leaking mutation into other starting-cell searches or the caller-visible input.

**The recursion path is simple and spells exactly one prefix**

At recursion index `i`, marked cells form a simple orthogonally adjacent path spelling `word[:i]`, and the candidate cell is not among them. Accepting a matching candidate extends this path by one distinct cell. Marking prevents an immediate reversal or any later cycle from reusing a cell.

**Trace a route that must not reuse its predecessor**

For `ABCCED`, begin at the top-left A, move right through B and C, down to the second C, then left/down through E and D. Marks prevent the search from returning through an already used cell.

**Every valid path is one restored DFS branch**

A successful branch matches the required character at every depth, moves only to a four-directional neighbor, and marks each used cell until that branch returns. It therefore witnesses a legal board path spelling the word.

Conversely, any legal path begins at one scanned cell and chooses one of the neighbors explored at each depth. Because its cells are distinct, none is blocked by the path-local marks, so DFS follows the entire sequence. Restoring each cell on return ensures failed or successful alternatives do not remove choices from later branches.

## Complexity detail
There are `mn` possible starts. The first step has at most four neighbors; afterward the immediately previous cell is unavailable, leaving at most three continuing directions. This gives the conventional $O(mn \cdot 3^L)$ upper bound for word length `L`, with inventory and rare-end pruning improving practical work but not the worst case. Recursion depth and temporary marks use $O(L)$ path space.

## Alternatives and edge cases
- **Allow cell reuse:** incorrectly accepts paths such as searching `ABA` in one adjacent A-B pair.
- **Store a separate visited set:** is correct but adds $O(L)$ hash state and overhead beyond the recursion path.
- **Search all paths without inventory pruning:** preserves worst-case correctness but performs avoidable exponential work on missing-character inputs.
- Diagonal movement is forbidden. A one-character word succeeds exactly when that character occurs somewhere on the board.
- The sentinel used for marking must not be a legal board character, or visited cells could accidentally match the word.
