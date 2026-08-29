## General

Forward game search is difficult because cycles represent draws and both players choose optimally. The solution works backward from states whose outcomes are already certain. This is retrograde analysis.

A state is $(m,c,t)$:

- $m$ is the mouse position;
- $c$ is the cat position;
- $t$ is whose turn comes next, mouse or cat.

The three stored outcomes are mouse win, cat win, and unresolved. Any state still unresolved after all forced outcomes propagate is a draw.

**Terminal states.**

- If $m=0$, the mouse has reached the hole, so the state is a mouse win regardless of whose turn would be next.
- If $m=c$ at a non-hole node, the cat has caught the mouse, so it is a cat win.

Both turn versions of every terminal position are initialized and enqueued.

**Degree means legal moves remaining.** `degree[m][c][t]` begins as the number of moves the player whose turn it is can make:

- mouse degree is `len(graph[m])`;
- cat degree is `len(graph[c])` minus any edge to node 0, because the cat may not enter the hole.

The code subtracts one for cat positions adjacent to the hole. The graph is undirected, so those positions are exactly the nodes listed in `graph[0]`.

During backward propagation, degree is repurposed as the number of outgoing moves not yet proven to lose for the player to move.

**Generate predecessor states.** Suppose current resolved state is $(m,c,t)$. The previous mover was `pt = t ^ 1`.

- If the previous mover was the cat, the previous mouse position was still $m$, and the previous cat position can be any neighbor of current $c$, except hole 0.
- If the previous mover was the mouse, the previous cat position was still $c$, and the previous mouse position can be any neighbor of current $m$.

These reverse edges enumerate exactly the states that could choose one legal move into the current state.

**How one resolved child determines a predecessor.** Consider unresolved predecessor $(pm,pc,pt)$ and the resolved outcome `t` of one possible next state.

If that outcome is a win for the player moving in the predecessor, that player can deliberately choose this move. The predecessor immediately receives the same winning outcome and is enqueued.

If the outcome is a win for the opponent, this move is bad for the player to move. Decrement the predecessor's remaining degree. When degree reaches zero, every legal move has been resolved as an opponent win. The opponent can force victory regardless of the move, so the predecessor is assigned that losing outcome and enqueued.

An unresolved child is not decremented. It may ultimately be a draw and allow the player to avoid losing. This is why states with a draw option are not incorrectly forced into losses.

**Why the queue propagation is correct.** Terminal states have known outcomes. Whenever a state is marked winning, there is a concrete move to a child already proven winning for its mover. Whenever a state is marked losing, every legal child has already been proven winning for the opponent. These are exactly the minimax rules.

By induction over queue removals, every assigned outcome is correct. Conversely, every state from which a player can force a finite win eventually receives evidence through a winning child or exhaustion of all losing choices. States that never resolve have neither a forced winning move nor all moves forced to lose; optimal repetition can preserve a non-losing cycle, so the problem classifies them as draws.

**Why unresolved value can share numeric zero with draw.** During processing, zero means “not resolved yet.” The algorithm never enqueues such a state. At completion, remaining zeros are intentionally interpreted as ties. The dual meaning is safe because only nonzero terminal or propagated states drive the queue.

The requested initial state is mouse at 1, cat at 2, and mouse to move, so the final lookup is `ans[1][2][MOUSE_TURN]`.

## Complexity detail

There are $2n^2$ possible position-and-turn states. Processing one resolved state may inspect up to $O(n)$ predecessor positions through an adjacency list.

- **Time complexity:** $O(n^3)$ in the worst case.
- **Space complexity:** $O(n^2)$ for outcomes, degrees, and the queue, excluding the input graph.

Each state is resolved and enqueued at most once because propagation acts only while its outcome is unresolved.

## Alternatives and edge cases

- **Depth-limited minimax:** Choosing an arbitrary move limit risks confusing long forced wins with draws and needs careful state repetition handling.
- **Naive recursion with a visited set:** A cycle on the current path does not alone determine the minimax outcome of the state; retrograde resolution is more reliable.
- **Value iteration:** Repeatedly update game states until stable. It can work but the degree queue processes only relevant changes.
- **Cat edge to hole:** It must be excluded from both degree and predecessor generation because it is illegal.
- **Mouse already in hole:** Mouse wins even if the next-turn field says cat.
- **Same mouse and cat node:** Cat wins for non-hole collision states.
- **Winning child:** One available winning move is enough because the current player chooses optimally.
- **Losing state:** It is established only after every legal move is proven to let the opponent win.
- **Draw option:** An unresolved/draw child prevents degree from reaching zero and lets the player avoid a forced loss.
- **Repeated graph position:** A state includes whose turn it is; identical positions with different turns are different states.
- **Both players can move:** The contract avoids zero-degree ordinary states, while cat-hole exclusion is handled explicitly.
- **Undirected graph:** Reverse predecessor enumeration can use the same adjacency lists as forward moves.
- **Initial answer zero:** It means optimal play leads to a draw, not that computation failed.
