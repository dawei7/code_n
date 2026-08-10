## General

**Blanks move around pieces, but pieces never cross**

An `L` piece may swap only with a blank immediately to its left, and an `R` piece may swap only with a blank immediately to its right. Neither move lets one piece jump over another piece.

Therefore, if all underscores are deleted, the remaining sequence of `L` and `R` characters must be identical in `start` and `target`. The first nonblank piece in the start must correspond to the first nonblank piece in the target, the second to the second, and so on.

The exact solution records these ordered pieces with their positions:

`a = [(piece, index) ... from start]`

and the analogous list `b` for `target`.

**First ensure both strings contain the same number of pieces**

Moves exchange a piece with a blank. They never create or destroy pieces. If `len(a) != len(b)`, one string contains more nonblank pieces than the other and transformation is impossible.

Equal counts are necessary but not sufficient. The corresponding types and movement directions must also be checked.

**Pair pieces by their invariant order**

`zip(a, b)` pairs the first start piece with the first target piece, then the second with the second, and so on. If paired characters `c` and `d` differ, achieving the target would require an `L` and an `R` to exchange relative order or change type. Neither operation is legal, so the method returns `False`.

This catches examples such as a nonblank sequence `RL` in the start and `LR` in the target. Even if individual directions appear favorable, the pieces cannot pass through each other.

**Check the one-way movement of every L**

Suppose a paired `L` starts at index `i` and must end at index `j`. It can move only left, meaning its index may decrease or remain unchanged. Thus validity requires `j <= i`.

The code rejects `c == 'L' and i < j`, exactly the case where the target position lies to the right and would require an illegal rightward move.

**Check the one-way movement of every R**

An `R` may move only right, so its target index must satisfy `j >= i`. The code rejects `c == 'R' and i > j`, the case requiring movement to the left.

Staying in place is allowed for either piece because the transformation may use any number of moves, including zero for a particular piece.

**Why these conditions are also sufficient**

It is clear that piece order, type equality, and direction constraints are necessary. To see sufficiency, consider the blanks as the space that passes between pieces while the pieces retain their order.

Move required `L` pieces toward their target positions from left to right. Each such target is no farther right than its start, and all earlier pieces already occupy their final earlier positions. The identical piece order guarantees no different piece must be crossed.

Likewise, required `R` movements can be realized from right to left. Each target is no farther left than its start, and processing the rightmost pieces first prevents them from blocking later rightward moves.

The matched order ensures that enough blank positions occur between consecutive target pieces to accommodate these shifts. Another formal view is that the conditions characterize exactly the reachable configurations of one-direction tokens on a line: relative token order is invariant, and each token's coordinate changes only in its permitted direction.

Therefore, if every paired piece passes the tests, a sequence of adjacent legal moves exists and the method returns `True`.

**A trace of the correspondence**

For `start = "_L__R__R_"`, removing blanks gives pieces `L, R, R` at indices 1, 4, and 7. The target `"L______RR"` has the same sequence at indices 0, 7, and 8.

The `L` moves from 1 to 0, which is left. Both `R` pieces move from 4 to 7 and from 7 to 8, which is right. All checks pass.

For `start = "_R"` and `target = "R_"`, the sequences match, but the `R` would move from index 1 to index 0. The condition `i > j` rejects it.

## Complexity detail

Let `n` be the common string length. Each list comprehension scans its string once, and the paired loop visits at most `n` pieces. Total time is `O(n)`.

The exact source materializes lists `a` and `b` containing every nonblank piece and index. In the worst case both strings contain no blanks, so auxiliary space is `O(n)`. This differs from the manifest's `O(1)` claim, which corresponds to a two-pointer implementation that skips underscores without storing the pairs.

The strings are immutable and are not changed. Tuples and lists contain references to one-character strings plus integer positions.

## Alternatives and edge cases

- **Two pointers skipping blanks:** Walk through both strings, compare the next pieces and their indices immediately. This preserves `O(n)` time while achieving true `O(1)` auxiliary space.
- **Breadth-first search over configurations:** It explores an enormous state graph and is unnecessary because reachability has a simple invariant characterization.
- **Compare only strings with underscores removed:** Matching piece order is necessary, but direction constraints are also required; `"_R"` cannot become `"R_"`.
- **Check only each character count:** Equal numbers of L and R do not preserve their relative order. Pieces cannot cross.
- **Allow pieces to jump over one another:** The rules permit only adjacent piece-blank swaps, so jumps would solve a different problem.
- **No pieces:** Both strings consist only of blanks, both lists are empty, and the transformation is already complete.
- **Different piece counts:** Immediate false because moves conserve pieces.
- **Same counts but different order:** Paired characters differ, proving a crossing would be necessary.
- **L stays in place:** `i == j` satisfies the left-only constraint.
- **R stays in place:** `i == j` satisfies the right-only constraint.
- **L target to the left:** It may traverse the intervening blanks without crossing matched earlier pieces.
- **R target to the right:** It may traverse blanks toward that position.
- **Adjacent opposing pieces:** Their order cannot reverse because neither can move through the other.
- **Input preservation:** The method builds separate pair lists and never modifies either string.
- **Exact-source space:** Storing nonblank tuples is linear even though the underlying reachability test can be streamed.
