# Cat and Mouse II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1728 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Graph Theory, Topological Sort, Memoization, Matrix, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/cat-and-mouse-ii/) |

## Problem Description

### Goal

Cat and Mouse play on a rectangular grid containing floor cells `.`, impassable walls `#`, one mouse `M`, one cat `C`, and one food cell `F`. Mouse moves first, and the players then alternate turns. On a turn, the current player may stay in place or jump from zero up to that player's maximum distance in one of the four cardinal directions. A jump cannot leave the grid or cross a wall, although Mouse is allowed to jump over Cat.

Cat wins immediately by occupying Mouse's cell or reaching the food first. Mouse wins immediately by reaching the food first. If Mouse cannot reach the food within 1000 turns, Cat wins. Given `catJump` and `mouseJump`, return whether Mouse can force a win when both players choose their moves optimally.

### Function Contract

**Inputs**

- `grid`: an array of `rows` equal-length strings, where $1 \le \texttt{rows},\texttt{cols} \le 8$. Every character is `.`, `#`, `M`, `C`, or `F`, and exactly one each of `M`, `C`, and `F` appears.
- `catJump`: Cat's maximum jump length, where $1 \le \texttt{catJump} \le 8$.
- `mouseJump`: Mouse's maximum jump length, where $1 \le \texttt{mouseJump} \le 8$.

Let $V$ be the number of non-wall cells and let $D$ be the maximum number of legal destinations, including staying, available from any cell to either player.

**Return value**

- Return `True` if Mouse has a strategy that guarantees reaching the food within 1000 turns; otherwise return `False`.

### Examples

**Example 1**

- Input: `grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2`
- Output: `True`
- Explanation: Mouse can force a route to the food before Cat can catch it or reach the food.

**Example 2**

- Input: `grid = ["M.C...F"], catJump = 1, mouseJump = 4`
- Output: `True`
- Explanation: Mouse can jump beyond Cat and land on the food on its first turn.

**Example 3**

- Input: `grid = ["M.C...F"], catJump = 1, mouseJump = 3`
- Output: `False`
- Explanation: Mouse cannot reach the food immediately, and Cat can prevent a forced win.

### Required Complexity

- **Time:** $O(V^2D)$
- **Space:** $O(V^2+VD)$

<details>
<summary>Approach</summary>

#### General

**Build every legal destination**

Index the non-wall cells. For each player and each starting cell, list the starting cell itself and every landing cell reachable in a cardinal direction within that player's jump limit. Stop extending a direction at the grid boundary or the first wall. Passing over Cat does not alter Mouse's move list; landing on Cat is legal but leads to a Cat-winning state.

**Represent the finite game graph**

A state consists of Mouse's cell, Cat's cell, and whose turn comes next, giving at most $2V^2$ states. A state is immediately Cat-winning when Cat is on the food or both players share a cell. Otherwise it is immediately Mouse-winning when Mouse is on the food. Each nonterminal state's outgoing degree is the number of legal moves for the player whose turn it is.

**Propagate forced outcomes backward**

Start a queue with every terminal state and examine its predecessors. If the player moving in a predecessor can choose a child already known to be winning for that player, the predecessor is winning for the same player. If a processed child favors the opponent, remove that option from the predecessor's unresolved degree. Once every option favors the opponent, the predecessor is forced to lose.

Movement is reversible along the same unobstructed row or column segment, so the precomputed destination lists also enumerate predecessor positions. Every game edge is processed only when its child outcome becomes known. States left unresolved belong to cycles from which Mouse cannot force a terminal win; Cat can keep such play alive until the turn limit.

**Track whether the forced win meets the deadline**

Alongside each outcome, store the number of turns under optimal timing. A player that can win chooses the shortest winning child. A player that is forced to lose delays through the longest child. Processing states in increasing attractor distance yields those values: a winning predecessor is assigned from its first winning child, while a losing predecessor is assigned only after all children have been processed.

The initial state is a Mouse win only when its propagated winner is Mouse and its optimal distance is at most 1000. Thus a theoretically forced result beyond the stated deadline is still awarded to Cat.

#### Complexity detail

There are $2V^2$ game states. Each state has at most $D$ outgoing moves, and retrograde propagation examines each corresponding edge once, taking $O(V^2D)$ time. The move lists use $O(VD)$ space; winners, distances, unresolved degrees, delay values, and the queue use $O(V^2)$ space.

#### Alternatives and edge cases

- **Turn-indexed minimax:** Memoizing `(mouse, cat, turn_count)` follows the rules directly, but can create up to $O(1000V^2)$ states and risks deep recursion.
- **Bottom-up 1000-turn dynamic programming:** Rolling two game layers avoids recursion and is exact, but repeats the full state graph for every turn instead of resolving each state once.
- **Staying in place:** Zero-length jumps are legal for both players and must be included in each state's degree.
- **Walls:** A jump stops at the first wall; it cannot land beyond that wall even when the jump limit is large.
- **Passing the opponent:** Mouse may jump over Cat, but landing on Cat's cell gives Cat an immediate win.
- **Food precedence:** Reaching food ends the game immediately, so later moves cannot undo that terminal result.
- **Unresolved cycles:** Repetition never helps Mouse satisfy the deadline; Cat wins by extending such play through 1000 turns.

</details>
