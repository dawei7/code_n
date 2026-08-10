## General

**Look outward from the king, not inward from every queen**

A chess queen attacks along its row, column, and two diagonals. From the king’s square, these lines form exactly eight rays: up, down, left, right, and four diagonals. On any one ray, only the nearest queen can attack the king directly. If another queen lies farther along the same ray, the nearer queen blocks it.

This observation changes the problem from “analyze every queen’s line” into “scan the first occupied square in each of eight directions.” It automatically handles blocking and produces at most one answer per direction.

**Constant-time occupancy checks**

The comprehension `s = {(i, j) for i, j in queens}` converts the input coordinates into a set of tuples. A list membership test would scan queens one by one, but a hash set supports expected \(O(1)\) membership. The input uses lists, which are mutable and cannot be hashed; converting each coordinate to tuple `(i, j)` creates the hashable representation used during searches.

The board size is fixed by `n = 8`. The output list `ans` starts empty.

**How the eight directions are generated**

The nested loops choose `a` and `b` independently from \(-1,0,1\). These values describe a row change and column change:

- one coordinate zero and the other nonzero gives a horizontal or vertical direction;
- both coordinates nonzero gives a diagonal direction;
- both zero would mean no movement.

The condition `if a or b` skips only `(0, 0)`, leaving exactly eight direction pairs. In Python, zero is false and \(-1\) and 1 are true, so the condition means “at least one change is nonzero.”

For each direction, `x, y = king` begins at the king’s coordinate. The loop condition checks the next square, `x + a, y + b`, before moving. This ensures the scan never steps outside indices zero through seven.

**Stop at the first queen on each ray**

Inside the loop, `x, y = x + a, y + b` advances exactly one square. If `(x, y) in s`, the queen is appended as `[x, y]` and `break` ends this direction’s scan.

The break is essential. A queen found on the ray attacks the king because every square between them was checked and found empty of queens. Any queen farther away on that same ray cannot attack directly because the found queen occupies an intervening square. Continuing would incorrectly report blocked queens.

If the scan reaches the board edge without finding a queen, that direction contributes nothing.

**Why no other queen can attack**

A queen can attack the king only if they share a row, column, or diagonal. The difference between their coordinates must therefore be a positive multiple of one of the eight direction vectors considered by the loops. Such a queen lies on exactly one scanned ray.

If it is the first queen on that ray, the algorithm appends it. If it is not first, another queen lies between it and the king and blocks the attack. Hence every appended queen really can attack, and every queen that can attack is appended.

**Walking through the first example**

With the king at `[0, 0]`, directions pointing above or left immediately fail the boundary condition. Scanning right along row zero encounters `[0, 1]` first, so that queen is reported. Scanning down column zero encounters `[1, 0]` before `[4, 0]`; the first queen is reported and the farther one is correctly blocked. Scanning down-right visits `[1, 1]` and `[2, 2]` before finding `[3, 3]`, so that queen is reported. The queen at `[2, 4]` shares none of the king’s queen-move lines and is never encountered.

**Output ordering**

The loops visit directions in the order determined by `a = -1, 0, 1` and, within each, `b = -1, 0, 1`. This gives a deterministic result for a fixed input, but it may not match the order shown in examples. The contract explicitly permits any order, so no sorting is needed.

**Why scanning from the king is simpler**

An alternative could examine each queen, verify row, column, or diagonal alignment, and then determine whether another queen lies between it and the king. That requires extra blocking logic. Ray scanning incorporates both alignment and visibility in one process: squares are visited in increasing distance from the king, so the first occupied one is necessarily the visible attacker.

The fixed \(8\)-by-\(8\) board also makes each ray extremely short, at most seven squares. Building the occupancy set dominates the asymptotic cost relative to the number of input queens.

## Complexity detail

Let \(q\) be `len(queens)`. Constructing the set takes expected \(O(q)\) time and \(O(q)\) space. The eight rays inspect at most seven squares each on an \(8\)-by-\(8\) board, a fixed maximum of 56 membership checks, so that portion is \(O(1)\). Total expected time is \(O(q)\), matching the manifest.

The set uses \(O(q)\) auxiliary space. The answer contains at most eight coordinates, one per direction, so it is \(O(1)\) on this fixed board, or output space if counted separately. For a generalized \(B\)-by-\(B\) board, scanning would take \(O(B)\) time across a constant number of rays, yielding \(O(q+B)\).

## Alternatives and edge cases

- **Examine every queen:** Test whether each queen is aligned with the king and retain the nearest queen for each normalized direction. This also takes \(O(q)\) expected time and can avoid scanning empty squares, but direction normalization and distance comparison are more involved.
- **Boolean board:** Fill an \(8\)-by-\(8\) occupancy matrix and scan the same rays. Because the board is fixed, it uses constant space, though the set directly represents only occupied cells.
- **Continue after finding a queen:** This is incorrect because any farther queen on the same ray is blocked. The `break` expresses direct visibility.
- **King on an edge or corner:** Several directions have no in-bounds next square. The while condition rejects them safely without special cases.
- **Adjacent queen:** The first step finds it immediately, and with no intervening square it attacks directly.
- **Multiple queens on one ray:** Only the nearest is returned; all farther queens are blocked.
- **Queens on different rays:** Up to eight queens can attack simultaneously, one from each direction.
- **No attacking queen:** Every ray reaches an edge without a set hit, and the method returns an empty list.
- **Unique positions:** The statement guarantees no duplicate queens and no queen on the king. The set would silently deduplicate repeated coordinates, but such input is outside the contract.
- **Coordinate interpretation:** The method treats the first coordinate as the row and the second as the column. Swapping this convention consistently would preserve geometry, but mixing conventions would scan incorrect squares.
- **Any answer order:** Sorting is unnecessary and would add work solely for presentation. Tests must compare according to the contract’s order-insensitive requirement.
