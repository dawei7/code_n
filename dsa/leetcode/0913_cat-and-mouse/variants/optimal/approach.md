## General
**Treat turns as finite game states**

A position is determined by a triple $(m,c,t)$: Mouse is at node $m$, Cat is at node $c$, and $t$ identifies whose turn comes next. There are only $2n^2$ such states. Instead of following play forward and having to detect cycles inside many mutually recursive choices, classify these states backward from outcomes that are already certain.

States with $m=0$ are Mouse wins. States with $m=c$ and $m \ne 0$ are Cat wins. Put every such terminal state into a queue. For every other state, record its number of legal outgoing moves: Mouse may use every neighbor of $m$, whereas Cat's count excludes node `0`.

**Propagate forced outcomes backward**

When a resolved state is removed from the queue, enumerate the parent states that can move into it. A parent is immediately assigned the same winner if the player whose turn it is can select this winning child. Otherwise, that child is losing for the active player, so decrement the parent's remaining unresolved move count.

If that count reaches zero, every legal move from the parent is known to let the opponent force a win. The parent must therefore be a win for that opponent. Enqueue each newly resolved parent so its result can continue propagating backward.

This reasoning handles optimal choice directly: one favorable move is enough to establish a player's win, but an opponent win is established only after every legal move has been proved unfavorable. When the queue becomes empty, every still-unclassified state belongs to a cycle from which neither side can force a terminal win. Those states are draws. The requested result is the classification of $(1,2,\text{Mouse turn})$.

## Complexity detail
There are $O(n^2)$ position-and-turn states. A resolved state can inspect up to $O(n)$ predecessor moves, so the worst-case time is $O(n^3)$. The outcome table, remaining-degree table, and queue each contain $O(n^2)$ state information, giving $O(n^2)$ auxiliary space.

## Alternatives and edge cases
- **Depth-limited minimax with memoization:** Expanding states forward can be correct when the move count is included in the memoization key and repetition is capped after all possible states, but it creates $O(n^3)$ memoized states and can require $O(n^4)$ transition work.
- **Repeated full-table relaxation:** Scanning every unresolved state until no value changes is conceptually similar to retrograde analysis, but repeatedly revisits states and can add an extra factor of $n$.
- **Cat and hole:** Cat's legal degree and predecessor generation must both exclude moves into node `0`; treating that edge as legal changes the game.
- **Repeated positions:** A repetition includes both player locations and whose turn it is. Equal locations with different active players are not the same state.
- **Unresolved states:** A state left uncolored after propagation is a draw, not an implementation failure; it represents play that can remain in a cycle under optimal resistance.
- **Immediate terminals:** Mouse reaching node `0` and Cat sharing Mouse's node take precedence over any later move choices.
