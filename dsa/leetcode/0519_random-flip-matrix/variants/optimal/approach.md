## General
**Flatten the matrix into a virtual array**

Number cells from `0` through `rows * cols - 1`. A flat index converts back to `(floor(index / cols), index % cols)`. Track `remaining`, the length of the still-available prefix of a conceptual array containing every unused index.

**Perform a sparse Fisher-Yates removal**

For a flip, draw a ticket uniformly from `[0, remaining)`. A hash map records only virtual positions whose values differ from their indices. Read the selected flat index from `remap.get(ticket, ticket)`, decrement `remaining`, and replace the ticket's virtual value with the value from the new last active position.

**Store only displaced positions**

There is no physical array of all cells. Each flip creates at most one active remapping and removes an obsolete last-position entry. Reset clears the map and restores `remaining` to the full cell count, which logically reconstructs the identity array in constant time.

**Why every unflipped cell is equally likely**

The virtual active prefix contains every unflipped flat index exactly once: initially it is the identity sequence, and each flip swaps the chosen value with the last active value before shrinking the prefix. A uniform ticket therefore selects each remaining cell with probability `1 / remaining`. Removal prevents repeats until reset, while reset reestablishes the initial invariant.

## Complexity detail
For `q` adapter operations, expected hash-map work is $O(q)$ time; each native flip and reset is expected $O(1)$. At most one remapping is retained per flip since the latest reset, so space is $O(f)$ for `f` currently flipped cells rather than $O(rows \cdot cols)$.

## Alternatives and edge cases
- **Explicit list of available cells:** supports uniform selection but removing a middle element takes $O(rows \cdot cols)$ time unless it also uses a swap-with-last technique, and allocating the list costs full-matrix space.
- **Rejection sampling with a flipped set:** uses simple state but can require many retries when few zero cells remain.
- **Materialized binary matrix plus random probes:** consumes $O(rows \cdot cols)$ space and inherits rejection behavior.
- **One cell:** every flip after a reset must return `[0,0]`.
- **All cells flipped:** the contract does not call `flip` again until reset.
- **Reset:** must make previously returned coordinates eligible again.
- **Large sparse matrix:** construction must avoid allocating one entry per cell.
