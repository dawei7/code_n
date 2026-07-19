## General
**Represent the body for both order and membership**

Two views of the body serve different operations. A deque stores cells from tail to head so the oldest cell can leave in constant time. A set stores the same cells for constant-time self-collision checks.

**Resolve each move in game order**

For each direction, compute the candidate head from the current head. A position outside the board loses immediately. Next determine whether the candidate equals the next unconsumed food coordinate.

**Remove a moving tail before checking collision**

If no food is eaten, remove the tail from both the deque and occupied set *before* testing the new head against the body. This ordering is essential: moving into the cell vacated by the tail on the same move is legal. If food is eaten, the tail stays and the food index advances. After the appropriate tail handling, an occupied candidate is a real self-collision; otherwise append it as the new head and return the number of foods consumed.

**Why both body views remain consistent**

The deque and set contain exactly the snake cells after every successful move. A normal move removes one tail and adds one head, preserving length; an eating move adds only the head, increasing length by one. The collision test considers precisely the cells that remain occupied after the simultaneous tail movement, so it rejects every and only illegal body collision.

## Complexity detail
Every move performs constant-time deque and expected constant-time set operations, so `q` moves take $O(q)$ total time. The snake begins with one cell and grows once per consumed food, so the deque and set use $O(f)$ space, more precisely $O(f + 1)$.

## Alternatives and edge cases
- **Body list only:** makes tail removal or collision membership $O(length)$ per move.
- **Full occupancy matrix:** gives constant-time membership but uses $O(width \cdot height)$ space even when the snake is short.
- Check wall coordinates before indexing the board.
- Food is consumed only in the supplied order.
- Moving into the departing tail cell is legal, while moving into any other body segment is not.
- After game over, later moves continue returning `-1` defensively.
