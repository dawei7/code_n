## General

**Location alone is not enough state**

Reaching the same cell with different keys creates different possibilities. A lock may be blocked on the first visit but passable after its key is collected.

Therefore, a BFS state contains:

- row `i`;
- column `j`;
- bitmask `state` of collected keys.

The visited set must include all three components. Marking only coordinates would incorrectly discard useful revisits after obtaining new keys.

**Map keys to bits**

The grid contains the first `k` lowercase letters, so:

- key `a` uses bit 0;
- key `b` uses bit 1;
- and so on.

For lowercase character `c`, its bit is:

`1 << (ord(c) - ord('a'))`.

Collecting it applies bitwise OR, which sets the bit without losing earlier keys.

The all-keys target mask is:

`(1 << k) - 1`.

Because keys are exactly the first `k` letters, this mask has precisely all required bits set.

**Find the start and key count**

A generator search locates the unique `@` coordinate.

The key count sums `v.islower()` across all cells. Booleans add as one or zero, and only lowercase key cells satisfy the test under the grid alphabet.

The initial state is the start coordinate with mask zero, placed in both queue and visited set.

**Breadth-first search measures moves**

Every legal step to an adjacent cell costs one move. BFS processes states in nondecreasing move count, so the first state containing all keys has minimum distance.

Variable `ans` is the current BFS level. `for _ in range(len(q))` processes exactly the states already queued for that level before newly discovered next-level states.

After one complete layer, `ans` increases by one.

**Generate four neighbors**

`dirs=(-1,0,1,0,-1)` with `pairwise` produces up, right, down, and left.

For each neighbor, the code first checks grid bounds. It then reads the cell and decides whether movement is legal.

**Walls and locks**

A wall `#` is always skipped.

For an uppercase lock `c`, the corresponding bit index is `ord(c)-ord('A')`. Movement is blocked when:

`state & (1 << lock_index) == 0`.

If the bit is present, the lock cell is traversable like an empty cell. Opening every lock is not the goal; locks matter only as movement restrictions.

**Picking up a key**

`nxt` begins as the current mask. On a lowercase cell:

`nxt |= key_bit`.

If the key was already held, the mask remains unchanged. If it is new, the new state can make previously inaccessible routes useful.

The resulting tuple `(x,y,nxt)` is enqueued only if it has not been visited before.

**Why the goal is checked when dequeuing**

At the start of each state expansion, the code compares its mask with the full mask. Since BFS dequeues by level, the first complete mask is reached using the smallest number of moves.

It is unnecessary to return immediately during neighbor creation; either timing gives the same next-level distance when handled consistently.

**Why revisits are bounded**

There are at most six keys, hence at most `2^6=64` masks per cell. A coordinate may be revisited with different masks, but each exact coordinate-mask state is processed once.

This small key dimension makes BFS practical even though paths may loop.

**Why the result is correct**

Every enqueued transition corresponds to one legal cardinal move: it stays in bounds, avoids walls, respects locks, and updates keys. Conversely, every legal move from a reachable state is considered.

Thus, BFS explores the complete legal state graph. Its unweighted level order guarantees the first all-key state is shortest. If the queue empties, no legal state can reach the full mask, so returning `-1` is correct.

## Complexity detail

Let the grid have `m n` cells and `c` keys.

There are at most `mn2^c` distinct states. Each checks four neighbors, a constant factor. Time is `O(mn2^c)`.

The queue and visited set may store `O(mn2^c)` states, giving the same space bound.

The grid itself is not copied, and `c<=6` bounds the exponential factor by 64.

## Alternatives and edge cases

- **BFS by coordinate only:** Incorrect because returning with more keys can unlock new movement.

- **Permute key orders:** Trying all `c!` orders and pathfinding between keys repeats work and complicates lock constraints.

- **Compress points of interest and use Dijkstra:** Useful for some variants, but direct state BFS is clear with only 64 masks.

- **Key behind its own lock:** It is unreachable unless another route enters; BFS eventually returns `-1` if no route exists.

- **Key collected twice:** OR leaves the mask unchanged, and duplicate coordinate-mask states are skipped.

- **Lock with key already held:** The cell is traversable.

- **Goal before opening every lock:** Correct; only all keys are required.

- **Start adjacent to a key:** It is reached at level one.

- **Walls enclosing a key:** Queue exhausts without a full mask.

- **Revisit start with keys:** It is a distinct state and may lead through a newly passable lock.

- **First `k` letters guarantee:** Full-mask construction relies on key bits having no gaps.

- **Input immutability:** The string rows are read only.
