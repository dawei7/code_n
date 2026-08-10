## General

**Model the game by positions and whose turn it is**

A complete game state is `(mouse_position, cat_position, turn)`. Turn zero means Mouse moves next; turn one means Cat moves next.

The board contains at most 64 cells, so although play can last many turns, the number of distinct position-turn states is finite: at most $2V^2$, where $V$ is the number of flattened grid positions.

The source classifies each state as:

- zero: outcome not yet proven,
- one: Mouse can force a win,
- two: Cat can force a win.

Rather than exploring forward recursively and struggling with cycles, it starts from known terminal outcomes and propagates their consequences backward.

**Flatten cells and precompute legal moves**

Cell `(i,j)` becomes vertex `i*n+j`. While scanning non-wall cells, the source records Cat, Mouse, and food positions.

For each of the four directions, it tries jump lengths from zero through the player's maximum. A jump stops as soon as it leaves the grid or encounters a wall; this correctly prevents jumping over walls.

The legal destinations are stored in `g_mouse[v]` and `g_cat[v]`. Jump length zero represents staying still.

Because zero is considered separately for all four directions, the exact adjacency lists contain four duplicate stay destinations. These duplicates do not add a new strategic choice. The later degree counts and predecessor enumeration both retain the same multiplicity, so their eliminations remain consistent; they only add a constant amount of redundant processing.

**Why the same move lists can find predecessors**

A legal straight jump between two open cells is reversible: if a player can move from `u` to `v` without crossing a wall and within its jump limit, the reverse direction from `v` to `u` is also legal.

Therefore, when retrograde processing asks which previous player positions could move into a current position, it can iterate that current position's ordinary move list.

**Initialize terminal states**

`ans[m][c][t]` stores the outcome. The queue begins with states whose winner is already determined:

- `ans[food][i][1] = 1`: Mouse has just reached food, so with Cat nominally next, Mouse has won.
- `ans[i][food][0] = 2`: Cat has reached food, so Cat has won.
- `ans[i][i][0] = ans[i][i][1] = 2`: occupying the same cell is a Cat win regardless of turn.

When both players occupy food, the same-position assignments occur last and make Cat the outcome, matching the capture/food terminal conditions.

The queue may receive duplicate or overlapping terminal states, but processing reads the final stored outcome and propagation remains idempotent for already classified predecessors.

**Record how many moves remain unrefuted**

`degree[m][c][0]` is the number of Mouse destinations from `m`, and `degree[m][c][1]` is the number of Cat destinations from `c`.

During backward propagation, a move is removed from consideration when its child state is proven to be a win for the opponent. If all moves are removed, the player to move is forced to lose.

This is the standard retrograde-game meaning of degree, not graph degree between state tuples.

**Generate unresolved predecessor states**

For current state `(m,c,t)`, the preceding turn is `pt = t ^ 1`.

If `pt == 1`, Cat moved most recently. Mouse remained at `m`, while Cat could previously have occupied any `pc` able to move to `c`. The helper emits unresolved `(m,pc,1)` states.

If `pt == 0`, Mouse moved most recently. Cat remained at `c`, and predecessor Mouse positions `pm` yield `(pm,c,0)`.

Already classified predecessors are skipped so their outcomes are not reconsidered through unrelated child states.

**A player needs one winning move**

Suppose the popped child has outcome `t`, where one represents Mouse and two Cat. The expression `pt == t - 1` checks whether the player moving in the predecessor is the winner of that child:

- Mouse turn zero matches Mouse outcome `1 - 1 = 0`.
- Cat turn one matches Cat outcome `2 - 1 = 1`.

If they match, the moving player can choose this child and force their own win. The predecessor is immediately assigned outcome `t` and queued.

**A player loses only when every move loses**

If the child winner is the opponent, that move is undesirable. The source decrements the predecessor's degree.

When the degree reaches zero, every legal move has been proven to lead to the opponent's win. The predecessor is therefore also assigned the current opponent outcome `t` and queued.

Together, these rules encode optimal play: select any winning move if one exists; otherwise lose only after all alternatives are known losing.

**Why unresolved states mean Mouse cannot force a win**

Retrograde propagation classifies every state from which one player can force a terminal victory. States left at zero belong to cycles or indefinite-play regions where neither forced terminal result was established.

The game rule awards Cat the win if Mouse does not reach food within the turn limit. Repeating a finite state permits indefinite avoidance, so an unresolved cycle is not a Mouse forced win. `canMouseWin` returns true only when the initial state equals outcome one; zero therefore correctly returns false.

**Why the starting result is correct**

The initial state uses Mouse's start, Cat's start, and turn zero because Mouse moves first. Retrograde induction proves every queued classification from already correct terminal states using optimal-choice rules.

Thus outcome one exactly means Mouse has a strategy forcing food before Cat's capture, food arrival, or indefinite delay. Any other outcome makes the returned Boolean false.

## Complexity detail

Let $V$ be the number of flattened board positions and $D$ the maximum number of destinations considered per position, proportional to the jump bounds and four directions.

Move construction costs $O(VD)$. There are $O(V^2)$ position pairs and two turns. Each resolved state scans up to $O(D)$ predecessor moves, giving $O(V^2D)$ time.

`ans` and `degree` use $O(V^2)$ space. The two move graphs use $O(VD)$, and the queue can hold $O(V^2)$ states. Total space is $O(V^2+VD)$, matching the manifest.

Duplicate stay edges multiply only a fixed four-direction constant and do not change these bounds.

## Alternatives and edge cases

- **Memoized forward minimax with a turn counter:** It can encode the 1000-turn limit directly but creates a much larger time dimension and delicate cycle handling.
- **Value iteration:** Repeatedly classify states until convergence. Retrograde degree processing reaches the same fixed point more directly.
- **No stay move:** That would change the game; jump length zero must be legal for both players.
- **Duplicate stay destinations:** They are strategy-equivalent but counted consistently in degrees and predecessor lists.
- **Wall blocking:** Directional generation stops at the first wall, so no longer jump may cross it.
- **Board boundary:** Generation also stops when coordinates leave the grid.
- **Mouse reaches food:** Outcome one is terminal before Cat's next move.
- **Cat reaches food:** Outcome two is terminal.
- **Same position:** Cat wins, including overlap at food.
- **Disconnected regions:** Unreachable terminal states may leave cycles unresolved, which returns false for Mouse.
- **Multiple legal winning moves:** Finding the first is enough to classify the predecessor.
- **All moves losing:** Degree reaches zero only after every listed option has been refuted.
- **Turn encoding:** Zero is Mouse and one is Cat; the arithmetic `t-1` relies on outcomes one and two.
