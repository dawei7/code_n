## General
**Give every ship one canonical cell**

The leftmost cell of a horizontal ship and the topmost cell of a vertical ship have no ship cell immediately above or immediately left. Every other cell in either orientation has one of those predecessors.

**Count only canonical starts**

Scan every board position. Ignore empty cells. For an `"X"`, also ignore it when the cell above exists and is `"X"`, or when the cell to the left exists and is `"X"`. Count it only when both predecessor checks are absent or empty.

**Why no start is shared by two ships**

Ships are straight and distinct ships do not touch orthogonally. Therefore an `"X"` cannot be the intersection of horizontal and vertical ships, and no neighboring ship can masquerade as its predecessor. Each ship contributes exactly one accepted start cell.

**Avoid mutation and visited storage**

The local predecessor test derives membership from the valid board structure itself. There is no need to erase cells, flood-fill a component, or remember previously visited coordinates.

## Complexity detail
Every one of the $r \cdot c$ cells receives a constant number of neighbor checks, giving $O(rc)$ time. Counters and indices use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Depth-first or breadth-first component counting:** is linear but uses $O(rc)$ visited storage or modifies the board.
- **Walk back to a canonical head for every ship cell:** is correct but can rescan a long ship and take quadratic time.
- **Count all X cells and divide by a length:** fails because ships can have different lengths.
- An all-empty board contains zero ships.
- A one-cell ship is its own canonical start.
- A ship may occupy an entire row or column.
- Boundary checks must not read above the first row or left of the first column.
