# Cat and Mouse

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 913 |
| Difficulty | Hard |
| Topics | Math, Dynamic Programming, Graph Theory, Topological Sort, Memoization, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/cat-and-mouse/) |

## Problem Description
### Goal

Mouse and Cat play a turn-based game on an undirected graph. For each node `a`, `graph[a]` lists exactly the nodes joined to `a` by an edge. Mouse begins at node `1` and moves first, Cat begins at node `2` and moves second, and node `0` is the hole.

On every turn, the active player must traverse one incident edge. Cat may never move to node `0`. Mouse wins as soon as it reaches the hole, while Cat wins as soon as both players occupy the same node. If a position repeats with Mouse and Cat on the same nodes as before and with the same player due to move, the game is a draw.

Assume that both players choose moves optimally. Return `1` when Mouse can force a win, `2` when Cat can force a win, and `0` when neither player can force a win and optimal play leads to a draw.

### Function Contract
**Inputs**

- `graph`: an adjacency list for an undirected graph. Let $n$ be the number of nodes, with $3 \le n \le 50$.
- Every adjacency list is nonempty and contains unique valid neighbors other than its own node. The input guarantees that both players can always make a legal move under the game rules.

**Return value**

An integer outcome: `1` for a Mouse win, `2` for a Cat win, or `0` for a draw under optimal play.

### Examples
**Example 1**

- Input: `graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]`
- Output: `0`
- Explanation: Each player can prevent the other from forcing a win, so optimal play repeats a state.

**Example 2**

- Input: `graph = [[1,3],[0],[3],[0,2]]`
- Output: `1`
- Explanation: Mouse moves directly from node `1` to the hole.

**Example 3**

- Input: `graph = [[2],[2],[0,1]]`
- Output: `2`
- Explanation: Mouse's only move enters Cat's starting node.

### Required Complexity
- **Time:** $O(n^3)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Treat turns as finite game states**

A position is determined by a triple $(m,c,t)$: Mouse is at node $m$, Cat is at node $c$, and $t$ identifies whose turn comes next. There are only $2n^2$ such states. Instead of following play forward and having to detect cycles inside many mutually recursive choices, classify these states backward from outcomes that are already certain.

States with $m=0$ are Mouse wins. States with $m=c$ and $m \ne 0$ are Cat wins. Put every such terminal state into a queue. For every other state, record its number of legal outgoing moves: Mouse may use every neighbor of $m$, whereas Cat's count excludes node `0`.

**Propagate forced outcomes backward**

When a resolved state is removed from the queue, enumerate the parent states that can move into it. A parent is immediately assigned the same winner if the player whose turn it is can select this winning child. Otherwise, that child is losing for the active player, so decrement the parent's remaining unresolved move count.

If that count reaches zero, every legal move from the parent is known to let the opponent force a win. The parent must therefore be a win for that opponent. Enqueue each newly resolved parent so its result can continue propagating backward.

This reasoning handles optimal choice directly: one favorable move is enough to establish a player's win, but an opponent win is established only after every legal move has been proved unfavorable. When the queue becomes empty, every still-unclassified state belongs to a cycle from which neither side can force a terminal win. Those states are draws. The requested result is the classification of $(1,2,\text{Mouse turn})$.

#### Complexity detail

There are $O(n^2)$ position-and-turn states. A resolved state can inspect up to $O(n)$ predecessor moves, so the worst-case time is $O(n^3)$. The outcome table, remaining-degree table, and queue each contain $O(n^2)$ state information, giving $O(n^2)$ auxiliary space.

#### Alternatives and edge cases

- **Depth-limited minimax with memoization:** Expanding states forward can be correct when the move count is included in the memoization key and repetition is capped after all possible states, but it creates $O(n^3)$ memoized states and can require $O(n^4)$ transition work.
- **Repeated full-table relaxation:** Scanning every unresolved state until no value changes is conceptually similar to retrograde analysis, but repeatedly revisits states and can add an extra factor of $n$.
- **Cat and hole:** Cat's legal degree and predecessor generation must both exclude moves into node `0`; treating that edge as legal changes the game.
- **Repeated positions:** A repetition includes both player locations and whose turn it is. Equal locations with different active players are not the same state.
- **Unresolved states:** A state left uncolored after propagation is a draw, not an implementation failure; it represents play that can remain in a cycle under optimal resistance.
- **Immediate terminals:** Mouse reaching node `0` and Cat sharing Mouse's node take precedence over any later move choices.

</details>
