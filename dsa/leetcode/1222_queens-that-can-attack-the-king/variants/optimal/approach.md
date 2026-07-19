## General
**Index occupied squares.** Convert every queen coordinate to a tuple in a hash set. This makes each board-square occupancy test constant expected time and separates lookup order from the input order.

**Scan outward on the eight attack rays.** From the king, step through each of the horizontal, vertical, and diagonal direction vectors. The first occupied square encountered on a ray contains the only queen on that ray that can attack: record it and stop scanning that direction. If the board edge is reached first, that direction contributes nothing.

**Why only the first queen matters.** Every attacking queen must lie on exactly one of the eight rays from the king. On a fixed ray, the nearest queen has no queen between it and the king, so it attacks. Any farther queen has that nearest queen between it and the king and is blocked. Therefore selecting the first occupied square from each ray returns all and only the direct attackers.

## Complexity detail
Building the occupied set takes $O(q)$ time and space. The eight ray scans examine at most seven squares each on the fixed $8\times8$ board, which is constant additional work, so total time is $O(q)$ and space is $O(q)$.

## Alternatives and edge cases
- **Check every queen and every blocker:** Classifying each queen's line and scanning all other queens for an intervening piece is correct but takes $O(q^2)$ time.
- **Materialize an $8\times8$ board:** A Boolean board also supports constant-time lookup and uses constant board space, but the coordinate set is more direct.
- **Multiple queens on one ray:** Only the nearest one is returned; every farther queen is blocked.
- **Adjacent queen:** A queen one square from the king attacks immediately because no square can lie between them.
- **No aligned queen:** The result is empty even when many queens occupy other squares.
- **Corner king:** Five directions leave the board immediately; the same direction loop needs no special case.
- **Output order:** Direction order is an implementation detail because the contract permits any order.
