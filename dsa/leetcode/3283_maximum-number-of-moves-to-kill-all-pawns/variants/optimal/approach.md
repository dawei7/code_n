## General

Each turn selects any remaining pawn, and the knight reaches it by a shortest path. The only lasting effects of a turn are the captured pawn, the knight's new position, and whose turn comes next. This suggests two stages: precompute all relevant knight distances, then solve the alternating game with bitmask minimax.

The source appends the knight's initial coordinate to `positions` after recording `n`, the pawn count. Pawns retain indices zero through `n-1`; index `n` represents the starting location.

For each pawn and the starting location, BFS runs over all fifty-by-fifty cells. Knight moves are unweighted, so layer number `step` is the shortest number of moves. The eight `dx,dy` combinations enumerate every legal knight displacement, and bounds checks keep traversal on the board.

Other pawns are not obstacles and are not captured incidentally, so distance between two relevant positions depends only on board geometry. Independent BFS tables are therefore valid for every future game state.

Memoized `dfs(last,state,k)` represents optimal remaining move total when the knight is at relevant position `last`, `state` marks uncaptured pawns, and `k` identifies the player: one for maximizing Alice, zero for minimizing Bob.

When `state == 0`, no moves remain and the value is zero. Otherwise, every set bit `i` is a legal selected pawn. Capturing it costs `dist[last][x][y]`, moves the knight to index `i`, clears that bit, and toggles the player with `k ^ 1`.

Alice initializes `res=0` and takes the maximum candidate. Bob initializes it to infinity and takes the minimum. Both optimize the same eventual total in opposite directions, exactly matching perfect play.

The initial call uses `last=n`, all pawn bits set, and Alice's maximizing flag.

For example three, Alice may target the farther pawn even while passing through the nearer pawn. The precomputed distance allows that route without modifying state for the passed pawn; only the selected bit is cleared.

**Why this state is complete.** The route used for a shortest capture has no additional consequence: unselected pawns remain, and the knight ends at the selected pawn. Past order matters only through current location and remaining set. Memoization safely merges histories with identical state.

The game tree has exponentially many pawn subsets, but caching evaluates each location-subset-turn combination once. Turn is actually determined by how many pawns have been removed, yet storing it explicitly is simple and correct.

The source mutates the supplied `positions` list by appending the knight start and does not remove it before returning. This side effect is part of the exact implementation.

## Complexity detail

Let $p$ be the pawn count and $B=2500$ board cells. BFS from $p+1$ relevant sources costs $O(pB)$ time and stores $O(pB)$ distances.

Minimax has $O(p2^p)$ meaningful location/subset states and tries up to $p$ captures, giving $O(p^2 2^p)$ time. The cache uses $O(p2^p)$ space.

Total space is $O(pB+p2^p)$, not merely $O(B+p2^p)$ if every source distance grid is counted. Recursion depth is at most fifteen.

## Alternatives and edge cases

- **Compute knight distance during every game transition:** This repeats board searches exponentially. Precomputation separates geometry from game choices.
- **Manhattan distance:** Knight movement does not follow Manhattan distance; BFS is required on the bounded board.
- **Greedy farthest pawn for Alice:** Bob's future minimizing choices can make a locally longest capture globally worse. Full minimax is necessary.
- **Greedy nearest pawn for Bob:** The same look-ahead issue applies symmetrically.
- **Passing another pawn:** It remains in `state` because only the selected pawn is captured.
- **One pawn:** Alice has the sole choice, and the result is its shortest knight distance.
- **Pawn near a board edge:** BFS bounds correctly account for restricted moves.
- **Repeated game state:** `@cache` returns its already optimized value.
- **All positions unique:** Bits identify pawns unambiguously.
- **Input mutation:** Appending the start means callers observe one extra coordinate afterward.
- **Cache clearing:** `dfs.cache_clear()` releases memoized states before returning, though local-function lifetime would also eventually free them.
- **Reachability:** A knight can reach every square on this board size, so distance entries for relevant pawns become nonnegative.
- **Why shortest capture distance is mandatory:** Players choose the target pawn but not an intentionally longer route. Once a target is selected, the rules require the fewest knight moves, so `dist` is the fixed turn cost.
- **Turn parity:** Starting with Alice and toggling after every captured pawn means the player could be inferred from remaining-bit count. Passing `k` explicitly makes the maximizing/minimizing branch visible.
- **Distance source indexing:** `dist[last][x][y]` uses the current pawn or appended start as a BFS source and the selected pawn's coordinates as destination. Knight distances are symmetric, but the stored orientation remains consistent.
- **BFS layer counter:** `step` increments before expanding the current layer, so newly discovered neighbors receive distance one from the source, then two, and so forth.
- **Infinity in Bob's branch:** At least one pawn bit is set whenever that branch runs, so some candidate always replaces infinity before return.
