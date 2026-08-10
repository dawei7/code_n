## General

The snake has two simultaneous properties that one data structure does not conveniently provide by itself. Its body is ordered from head to tail, because the next move adds a new head and usually removes the old tail. It is also a set of occupied cells, because detecting a self-collision requires quickly asking whether the new head overlaps the body. The exact solution therefore stores the same live cells in two complementary forms:

- `q` is a deque. Its left end, `q[0]`, is the head, and its right end, `q[-1]`, is the tail.
- `vis` is a set containing every coordinate currently occupied by the snake.

The deque provides constant-time head insertion and tail removal. The set provides expected constant-time collision checks. Keeping them synchronized avoids either shifting an array on every move or scanning the whole snake for membership.

**Initial state and persistent fields.**

The constructor translates the interface's `height` and `width` into `self.m` and `self.n`. Rows are valid from `0` through `self.m - 1`; columns are valid from `0` through `self.n - 1`. The snake starts at `(0, 0)`, so both `q` and `vis` initially contain that one coordinate.

`food` remains in its given appearance order. `idx` points to the next food item that has not yet been eaten, and `score` counts consumed items. These two values advance together, but both are kept explicitly: `idx` locates the next coordinate and `score` is the required return value.

**Computing the proposed head.**

Every call begins from the current head `q[0]`. The variables `x` and `y` start as its row and column. The `match` statement changes exactly one coordinate: up subtracts one from the row, down adds one to the row, left subtracts one from the column, and right adds one to the column.

At this point `(x, y)` is only a proposed new head. The source first checks whether it lies outside the grid. A row below zero or at least `height`, or a column below zero or at least `width`, hits a wall. In that case the method immediately returns `-1` without changing the deque, occupancy set, score, or food index.

**Food changes whether the tail moves.**

The next uneaten food is active only when `idx < len(food)`. The snake eats it only if the proposed head matches both its row and column. Later food coordinates are intentionally ignored until earlier food has been eaten, exactly matching the one-at-a-time appearance rule.

On a food move, the score and food index increase. The old tail remains in place, while a new head will be added, so the snake grows by one cell.

On an ordinary move, the snake's length stays fixed. The source removes `q.pop()`, the old tail coordinate, and removes the same coordinate from `vis`. It then plans to add the proposed head at the front. The body therefore slides forward by one cell.

**Why tail removal occurs before self-collision testing.**

Consider a non-food move whose new head is the cell occupied by the current tail. During the same move, that tail leaves the snake. The contract defines collision using the body after moving, so this move is legal. If membership were checked before removing the tail, the set would contain the target and incorrectly report a collision.

The exact source handles this semantic boundary cleanly: on a non-food move it removes the tail first, then checks whether `(x, y)` remains in `vis`. If it remains, the coordinate belongs to some non-tail body segment and the move is a genuine self-collision. If it does not remain, entering the vacated tail cell is allowed.

On a food move the tail is not removed. However, the problem guarantees that newly appearing food is not placed on a cell occupied by the snake. Thus a valid food coordinate cannot equal the old tail or another body cell at the moment it appears. Keeping the tail in `vis` is therefore both semantically correct and safe.

**Committing a successful move.**

After the optional tail removal, membership of `(x, y)` in `vis` detects self-collision. If occupied, the method returns `-1`. Otherwise it adds the new head with `q.appendleft((x, y))` and inserts the same coordinate into `vis`. The score is then returned.

For a non-food success, one coordinate left both structures and one entered, so the length is unchanged. For a food success, no coordinate left and one entered, so length increases by one. Since the snake begins with length one and grows once per eaten item, its length always equals `score + 1` during valid play.

**A move-by-move trace of the example.**

On the `3`-column by `2`-row board, the snake starts at `(0, 0)`. `R` proposes `(0, 1)`, removes the old tail `(0, 0)`, and adds the new head; score remains zero. `D` similarly moves to `(1, 1)`. `R` reaches the active food at `(1, 2)`, so the tail stays and the snake grows to two cells while score becomes one.

`U` proposes `(0, 2)` and performs a normal slide. `L` then reaches the second food at `(0, 1)`, keeps the tail, and raises the score to two. The final `U` proposes row `-1`; the boundary check returns `-1` before any state update.

**Why the maintained state is correct.**

Initially the deque contains the snake in head-to-tail order and the set contains exactly the same coordinate. Assume both descriptions are synchronized before a valid move. On a non-food move, removing the deque's rightmost coordinate and the same set member deletes exactly the tail; adding the new coordinate to the deque's left and set adds exactly the head. On a food move, only the new head is added. Therefore both structures again describe the same snake, and deque order remains head to tail.

The collision test is performed against precisely the body that will remain after tail behavior has been decided. Hence every committed move is in bounds and has unique live coordinates. The stored score and next-food index also advance exactly on food matches, so the returned score is correct.

**Game-over state is assumed to terminate future use.**

The source has no `game_over` flag. A wall collision returns before mutation. A self-collision can occur after a non-food tail has already been removed, so that failed call may partially mutate internal state. Under the game rules, no meaningful moves should occur after `-1`; the game is over. A reusable defensive API would need to record terminal state and avoid partial updates, but the checked-in implementation relies on the terminal contract.

## Complexity detail

Let $q$ be the number of calls to `move`, let $f$ be the number of food items, and let $L$ be the current snake length.

Each call performs a fixed number of coordinate operations, at most one deque removal, one deque insertion, one set removal, and one set membership test and insertion. Deque endpoint operations are $O(1)$, and set operations are expected $O(1)$. Therefore each move takes expected $O(1)$ time and all $q$ calls take expected $O(q)$ time, matching the manifest's total-time notation.

The deque and occupancy set each store $L$ coordinates. Since the snake starts with length one and grows only by eating a food item, $L\le f+1$. Thus live snake state uses $O(f)$ space. The object also retains the given food list of $f$ coordinates, so total persistent storage is $O(f)$. This is much smaller than allocating a `height * width` occupancy grid when the food list is short.

The method uses only a constant number of local variables per call. Hash-set complexity is expected because it depends on hashing, while coordinate tuples of bounded integers behave as standard efficient keys.

## Alternatives and edge cases

- **Deque without an occupancy set:** The body order remains efficient, but checking whether the proposed head overlaps a body coordinate requires scanning up to $L$ cells, making one move $O(L)$.

- **Occupancy set without ordered body storage:** Collision checks are fast, but the algorithm no longer knows which coordinate is the tail that must leave on a non-food move. Both representations serve distinct needs.

- **Grid occupancy array:** A Boolean `height * width` matrix gives deterministic constant-time membership but consumes $O(height\cdot width)$ space, potentially enormous compared with the at-most-`f + 1` snake cells.

- **Store linearized cell IDs:** Encode `(row, col)` as `row * width + col` in the set and deque. This can reduce tuple overhead while preserving the same algorithm and asymptotic bounds.

- **Moving into the current tail:** This is legal on a non-food move because the tail leaves first. It is one of the most important ordering details in the implementation.

- **Moving into any other body cell:** Removing the tail does not remove that coordinate, so membership remains true and the method returns `-1`.

- **Eating food:** The tail must remain, or the snake would fail to grow. Score and food index both advance once, and no later food can be eaten out of order.

- **No food remaining:** The index guard prevents out-of-range access. Every later valid move behaves as a non-food slide and returns the final score.

- **One-cell snake reversing direction:** Its old head is also its tail. On a non-food move the old cell is removed before checking the adjacent destination, so normal movement remains valid.

- **One-row or one-column boards:** Boundary checks still work. Legal motion is restricted to the board's single dimension, and the same tail/collision rules apply.

- **Invalid direction strings:** The contract guarantees one of `U`, `D`, `L`, or `R`. With another string, the `match` statement would leave the proposed head unchanged and could produce unintended behavior, so external validation would be needed outside the promised domain.

- **Calls after `-1`:** The game definition says play is over. Because this source does not persist a terminal flag and may partially modify state on self-collision, callers must not expect meaningful recovery after a losing move.
