## General
**Store two generations in separate bits**

Use each cell's low bit for its original state and a second bit for its next state. Count live neighbors using the low bit even after some cells have been annotated.

During the first pass, every cell's low bit remains its original generation. A set second bit means the Game of Life rules make that cell live in the next generation.

**Commit only after every next state is known**

After all next-state bits are set, shift every cell right once. Because every decision read only original low bits, the resulting board is exactly a simultaneous update.

The neighbor count is correct by the invariant. Setting the next bit precisely for original-live cells with two or three neighbors and original-dead cells with three implements all four rules. The final shift selects those computed states for every cell at once.

Because the low bit never changes during the first pass, earlier annotations cannot influence later neighbor counts. Every next-state bit is therefore computed from the same original generation, and the final shift exposes those decisions simultaneously.

## Complexity detail
Each of `mn` cells checks eight neighbors in constant time and is normalized once, giving $O(mn)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Copy the board:** is linear time but uses $O(mn)$ extra space.
- **Recompute or copy the full board per cell:** can take $O((mn)^2)$.
- Boundary cells simply ignore out-of-grid neighbors; a lone live cell dies.
