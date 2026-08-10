## General

**This is a shortest path with alternating move durations.** The tourist's first move takes one second, second move two, third one, and so on. Opening-time waits still depend on the destination room. A state might appear to need both room and next-duration parity, but grid geometry makes that parity recoverable from coordinates.

**Why coordinate parity determines move number parity.** Every move changes either row or column by one, so it flips parity of $i+j$. Starting at $(0,0)$ with even parity, any walk reaching $(i,j)$ uses a number of moves congruent to $i+j$ modulo two. Detours add moves in pairs on a bipartite grid and do not change this parity.

Therefore, from a current room with even $i+j$, an even number of moves has been completed and the next move is an odd-numbered move taking one second. From odd parity, the next move takes two seconds. The duration is

`(i + j) % 2 + 1`.

No separate parity dimension is needed.

**Earliest-arrival relaxation.** If current room $(i,j)$ is reached at time $d$, movement toward neighbor $(x,y)$ cannot begin before its opening threshold `moveTime[x][y]`. Waiting is allowed, so departure occurs at `max(d, moveTime[x][y])`. Adding the parity-derived duration gives

$$
t=\max(d,\texttt{moveTime}[x][y])+(i+j)\bmod2+1.
$$

This is exactly the source formula.

**Dijkstra remains valid.** For a fixed edge and coordinate parity, candidate arrival is a nondecreasing function of current arrival. Reaching a room later never permits an earlier traversal result. This FIFO property supports Dijkstra's rule of finalizing the smallest heap time first.

`dist` records earliest known arrivals, and the heap stores candidate triples. An improved neighbor receives an updated distance and new heap entry. Entries whose popped time exceeds current `dist` are stale and skipped.

**Early target extraction.** The first target tuple popped has globally minimum time, so it can be returned. Although target checking precedes stale checking, a larger stale target key cannot appear before its smaller replacement in a min-heap. If the smaller one had already appeared, the method would already have returned. The ordering is therefore sound.

**Four-neighbor generation.** Consecutive pairs of `(-1,0,1,0,-1)` encode the four axial directions. Bounds checking keeps only actual grid cells. Waiting plus connected geometry guarantees eventual reachability, justifying the unconditional loop.
Coordinate parity gives the exact next move duration for every possible path to a room. Assume the smallest non-stale heap state has correct earliest arrival. Any unprocessed alternative predecessor has no smaller arrival, and the monotone wait-plus-duration transition cannot yield a better route to the popped room. Relaxations then consider every legal next move with its exact earliest timing. Induction establishes all finalized distances, including the returned target.

**Why time parity is irrelevant.** Waiting can change whether the clock time is even or odd, but alternation is based on move count, not seconds elapsed. Using `d % 2` would be wrong. Coordinate parity encodes number-of-moves parity even after arbitrary waits.

The source assumes heap, infinity, and `pairwise` imports from its execution harness.

## Complexity detail

For $V=nm$ rooms and $O(V)$ grid edges, Dijkstra performs $O(V)$ successful relaxations up to constant factors. Heap operations cost $O(\log V)$, so time is $O(nm\log(nm))$.

The distance matrix and heap each require $O(nm)$ space. No extra layer for move parity is necessary, which is especially important near $750\times750$ rooms.

## Alternatives and edge cases

- **State includes parity explicitly:** It is correct but doubles vertices unnecessarily because room coordinates already determine parity.
- **Breadth-first search:** Alternating durations and waits make arrival costs nonuniform, so BFS ordering is invalid.
- **Time parity for duration:** It is wrong because waiting changes clock parity without consuming a move.
- **First move:** Start coordinate parity is even, so duration is one second.
- **Second move:** Every neighbor of the start has odd coordinate sum, so its next move lasts two seconds.
- **Waiting before a move:** It delays departure but does not advance the one/two alternation.
- **Destination already open:** Movement begins immediately and adds only the current parity duration.
- **Large grid:** Omitting a redundant parity state halves distance storage relative to a generic formulation.
- **Detours:** Any return to the same coordinate adds an even number of moves, preserving coordinate-based parity.
- **Starting threshold:** The tourist begins at $(0,0)$ at time zero regardless of that cell's value.
- **Stale entries:** Lazy deletion through distance comparison avoids decrease-key support.
- **Multiple equal arrivals:** Strict improvement prevents redundant equal-time pushes without losing optimality.
- **Import requirements:** `heappop`, `heappush`, `inf`, and `pairwise` must be available.
- **Unconditional loop:** Connectivity and unrestricted waiting ensure the target is eventually popped.
- **Destination threshold semantics:** The method waits before starting the move, then adds its one- or two-second duration; opening time is not treated as an arrival deadline.
- **Heap tie order:** Coordinate comparison breaks equal-time tuple ties but has no effect on optimality.
