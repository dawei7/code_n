## General

**The in-place difficulty is simultaneous state change**

Every cell's next state must be computed from the same original generation. If the algorithm changed a live cell directly from 1 to 0 and then processed its neighbor, that neighbor would incorrectly see the new dead state rather than the original live state. A full copy solves this, but the follow-up asks for constant extra space.

The exact source temporarily encodes both old and new state in the board cell itself. During the first pass, original-state information remains recoverable even after a cell has been assigned its next state. A second pass converts temporary markers back to ordinary zeros and ones.

**Understand the four stored states**

The source uses this transition encoding:

| Original state | Next state | Value during first pass |
|---:|---:|---:|
| dead 0 | dead 0 | `0` |
| dead 0 | live 1 | `-1` |
| live 1 | live 1 | `1` |
| live 1 | dead 0 | `2` |

The sign separates original state:

- positive temporary values, `1` and `2`, were originally live;
- nonpositive values, `0` and `-1`, were originally dead.

The exact numeric marker also remembers the next state. Marker `2` means a live cell must become dead, while marker `-1` means a dead cell must become live. Unchanged cells keep their ordinary value.

This encoding is the reverse of another common convention that uses `-1` for live-to-dead and `2` for dead-to-live. What matters is consistency. The protected source counts `> 0` as originally live, so its marker meanings are exactly those in the table above.

**Count original live neighbors even after earlier updates**

For each cell `(i, j)`, the source examines row coordinates from `i - 1` through `i + 1` and column coordinates from `j - 1` through `j + 1`. Out-of-bounds coordinates are skipped. This square contains the eight neighbors and the cell itself.

A candidate location contributes one when `board[x][y] > 0`. Original live cells still have value 1 if they survive or 2 if they were processed earlier and will die. Both count as live in the original generation. A newly born cell has marker `-1`, which is not positive, so later cells correctly still regard it as originally dead.

Thus scan order cannot contaminate neighbor counts: temporary transitions preserve exactly the old-state classification needed by every later calculation.

**Why the counter starts at `-board[i][j]`**

The nested neighborhood loops include the current cell itself, although the Game of Life rules count only the eight other positions. Rather than add a separate `(x, y) != (i, j)` condition, the source initializes

```text
live = -board[i][j]
```

At the moment a cell is processed, its own value is still an original `0` or `1`; no other cell changes it. If it is live, `live` starts at -1 and the self-position later satisfies `> 0`, adding one and canceling to zero. If it is dead, `live` starts at zero and the self-position contributes nothing. In both cases, the final count equals the number of live neighbors excluding the cell itself.

This subtraction depends on processing each cell exactly once and changing only the currently processed cell. Earlier cells may have markers, but the current cell cannot have been marked by another iteration.

**Apply the rules using the original state**

After counting, a currently live cell is identified by the original value 1 at its own first visit. If it has fewer than two or more than three live neighbors, it dies and is changed to marker 2. A live cell with two or three neighbors remains 1.

The source's condition uses `if board[i][j]` for the live case. At this point the current unprocessed cell is either 0 or 1, so truthiness is equivalent to original liveness.

A currently dead cell is identified by `board[i][j] == 0`. If it has exactly three live neighbors, it becomes marker `-1`. Otherwise, it remains zero.

The two transition checks do not conflict. A live cell changed to 2 cannot satisfy the later `== 0` birth condition. A dead cell does not enter the first live condition.

**Why unchanged states need no marker**

A surviving live cell remains 1. That value already communicates both facts: it was originally live for first-pass neighbor counting and it should be live in the final board.

A dead cell that remains dead stays zero, likewise representing both old and new state. Markers are needed only when the two generations disagree.

This minimizes writes and makes the cleanup pass simple.

**Normalize temporary markers in a second pass**

After every cell's next state has been computed from original-state signs, old information is no longer needed. The source scans the board again:

- marker 2 becomes 0, completing live-to-dead transitions;
- marker `-1` becomes 1, completing dead-to-live transitions;
- unchanged 0 and 1 cells need no action.

The board then contains only the required binary next generation. The method mutates it in place and returns `None`.

**Why all updates are simultaneous in meaning**

Although the CPU processes cells sequentially, every neighbor test uses the encoded original state: positive means originally live, nonpositive means originally dead. No first-pass decision observes another cell's next-state liveness.

Therefore, the first pass computes exactly the same decisions that a read-only copy of the original board would produce. The second pass reveals those already computed decisions all at once conceptually. “Simultaneous” here means common input generation, not physically parallel execution.

**Trace the marker idea on a birth and a death**

Suppose an originally dead cell has three originally live neighbors. Its value is zero while counted; after the rule, it becomes `-1`. A later adjacent cell checks `> 0`, sees false, and correctly does not count this future birth in the current generation. Cleanup turns it into 1.

Suppose an originally live cell has only one live neighbor. It becomes 2. A later adjacent cell checks `2 > 0`, sees true, and correctly counts that cell as live in the old generation even though it will die. Cleanup turns it into zero.

Those two examples capture why ordinary immediate 0/1 updates would fail and why the signed markers work.

## Complexity detail

Let the board have $m$ rows and $n$ columns. The first pass visits every cell and examines a fixed 3-by-3 neighborhood of nine candidate coordinates. Nine is constant, so this pass takes $O(mn)$ time. The cleanup pass also takes $O(mn)$ time, leaving total time $O(mn)$.

The algorithm stores dimensions, loop indices, a neighbor count, and a few coordinates. It allocates no board-sized structure, so auxiliary space is $O(1)$. The temporary markers occupy existing input cells and do not count as additional storage.

The board itself is modified in place. No recursion or growing collection is used.

## Alternatives and edge cases

- **Copy the board:** Read every old state from a full copy and write new states into the original. It is straightforward and $O(mn)$ time but requires $O(mn)$ additional space.
- **Bit encoding:** Store the old state in one bit and the new state in another, then shift every cell. This is another clean $O(1)$-space technique; the signed-marker source uses comparison and explicit cleanup instead.
- **Different marker convention:** Using `-1` for live-to-dead and `2` for dead-to-live works only if old liveness is tested with `abs(value) == 1`. Mixing that rule with this source's `> 0` test would be incorrect.
- **Corner cell:** Only three neighbor coordinates are in bounds; all others are skipped.
- **Edge non-corner cell:** It has at most five legal neighbors, handled by the same bounds checks.
- **Single-cell dead board:** It has zero live neighbors, remains zero, and needs no marker.
- **Single-cell live board:** Self-count cancellation leaves zero neighbors, so under-population marks it 2 and cleanup makes it dead.
- **All dead cells:** No cell has three live neighbors, so the board remains all zero.
- **Birth beside processed deaths:** Death markers remain positive and count as originally live, so the birth calculation is still based on the old generation.
- **Survival rule:** A live cell with exactly two or three neighbors stays 1; no explicit assignment is necessary.
- **Infinite sparse board:** Store coordinates of live cells in a set and count neighbor occurrences around them, rather than materializing infinitely many dead cells. This changes the representation and uses space proportional to the active region.
- **Huge board stored externally:** Because one row's update depends only on itself and adjacent rows, a streaming design can retain a small rolling window of rows, though writing results requires careful separation from unread original data.
- **Rectangular dimensions:** Separate `m` and `n` bounds support all legal non-square boards.
- **Original binary constraint:** The marker logic assumes first-pass unprocessed cells begin only as 0 or 1. Other initial values would collide with the temporary-state interpretation.
