## General
**Flatten the boundary into one cycle**

The robot never enters an interior cell: starting on the boundary and turning counterclockwise at each corner makes it follow the perimeter in the order bottom, right, top, left. Its cycle length is

$$
P=2(\texttt{width}+\texttt{height})-4.
$$

Store one perimeter index, initially zero. A `step(num)` call replaces it with `(position + num) % P`, making the operation independent of `num`.

**Decode position and direction by segment**

Use the lengths `width - 1` and `height - 1` to determine which of the four boundary segments contains the index, then convert its offset to `[x,y]`. Direction is the direction of the most recently completed movement along that segment. The index zero needs one extra flag: before any movement the robot faces `East`, but after a positive whole number of cycles it has just moved south into `(0,0)` and faces `South`.

Each successful unit step advances to the next point of the same perimeter cycle, including the counterclockwise corner turn. Modular addition therefore reaches exactly the state produced by literal simulation. The segment formulas invert the flattened index, and the movement flag resolves the only index whose initial and post-cycle directions differ.

## Complexity detail
Construction and every method call take $O(1)$ time, so $Q$ calls take $O(Q)$ total time regardless of the numeric step counts. The class stores a fixed number of integers and one Boolean, requiring $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Move one cell at a time:** This directly follows the statement but takes time proportional to the sum of all requested steps, which can be much larger than $Q$.
- **Precompute every perimeter state:** Indexing a boundary array also gives constant-time calls, but uses $O(\texttt{width}+\texttt{height})$ space.
- Reaching a corner does not turn immediately; the robot retains its incoming direction until the next attempted step is blocked.
- Returning to `(0,0)` after a complete cycle leaves the robot facing `South`, unlike its initial `East` direction.
- Step counts larger than the perimeter must wrap using modulo without losing the post-movement direction.
- Consecutive `step` calls are equivalent to one call with their sum because state persists.
