## General

**Treat every board arrangement as a graph state**

The board always contains the six symbols zero through five exactly once. One legal move swaps zero with a side-adjacent tile. Therefore:

- A board arrangement is a graph vertex.
- A legal swap creates an undirected graph edge.
- Every edge costs one move.

The requested minimum is an unweighted shortest-path distance from the initial arrangement to `"123450"`, so breadth-first search is the natural algorithm.

**Encode a board as a six-character string**

The helper `gets` reads rows in row-major order and writes each tile into reusable list `t`, then joins it. For example, `[[1,2,3],[4,0,5]]` becomes `"123405"`.

Strings are immutable and hashable, so they work safely as visited-set keys and queue elements. A nested mutable list would require conversion or copying for the same purpose.

**Restore a queued string into the working board**

The implementation keeps one mutable `board` object for neighbor generation. Before expanding queued state `x`, `setb(x)` writes its six digits back into that board.

This avoids storing a separate matrix for every queued state. The queue remains authoritative through strings; the board is only temporary working memory for the state currently being expanded.

**Generate legal neighbors**

Helper `f` locates zero by scanning the two rows and three columns. It tries four direction offsets: left, right, down, and up.

For every in-bounds neighbor, it swaps zero with that tile, serializes the resulting board, and immediately swaps back. Restoring after each trial is essential: every neighbor must differ from the original current state by exactly one legal move, not accumulate several trial swaps.

Corner zero positions have two neighbors, noncorner edge positions have three, and no invalid coordinate is emitted.

**Handle an already solved board**

If the starting encoding equals `"123450"`, the distance is zero. The method returns before beginning BFS.

**Explore one distance layer at a time**

The queue begins with the start, and `vis` already contains it. At the beginning of each outer iteration, `ans` increases by one. The loop processes exactly the queue length measured at that moment, so all expanded states have the same distance.

Their newly enqueued neighbors belong to the following layer and remain in the deque until the next outer iteration.

If a generated neighbor is the target, it is exactly `ans` moves from the start, and BFS guarantees no shorter undiscovered path exists.

This fixed-size layer processing is what gives `ans` its precise meaning. Without first recording the current queue length, newly discovered states could be expanded immediately in the same outer iteration. Then one iteration could contain paths of several different lengths, and the counter would no longer be a trustworthy move count.

**Why marking on enqueue matters**

A puzzle state can be reached through several move sequences. Adding a state to `vis` at the moment it is enqueued prevents duplicate queue entries from different parents in the same or later layers.

The first discovery is always shortest in BFS, so later discoveries cannot improve its distance.

**Trace the one-move example**

Initial `[[1,2,3],[4,0,5]]` encodes as `"123405"`. Zero is at row one, column one. Swapping it right produces `"123450"`, so target detection returns layer number one.

**Why exhaustion proves impossibility**

The state graph is finite: there are at most `6! = 720` arrangements. If the queue empties, every arrangement reachable from the start has been visited. A target not encountered lies in a different reachability component, so no sequence of legal moves can solve the puzzle.


Serialization is a one-to-one representation of board arrangements. Neighbor generation emits exactly the boards reachable by one legal zero swap, so BFS explores exactly the puzzle’s state graph.

BFS layers correspond to move counts. The first target discovery therefore has minimum distance, the initial equality returns the correct zero case, and exhaustive failure correctly returns `-1`.

## Complexity detail

Let `V` be the number of reachable board states and `E` the legal state transitions among them. BFS visits each state once and examines its outgoing transitions, giving `O(V + E)` time.

For this fixed puzzle, `V <= 720` and each state has at most three neighbors. Encoding, restoring, and locating zero inspect six cells, a fixed constant.

The visited set and queue hold `O(V)` strings. The working board and serialization buffer have constant size.

## Alternatives and edge cases

- **Precompute zero-index adjacency:** String positions can be swapped directly using a fixed neighbor table, avoiding repeated matrix restoration and zero scans.

- **Bidirectional BFS:** Searching from both start and target can reduce the explored frontier.

- **Depth-first search:** It may find a solution but does not guarantee the fewest moves.

- **A-star search:** A heuristic can help larger puzzles, but BFS is sufficient for only 720 possible states.

- **Already solved:** Return zero before queue processing.

- **Unsolvable parity class:** BFS exhausts the reachable component and returns `-1`.

- **Swap restoration:** Omitting it would generate states more than one move away and corrupt graph edges.

- **Shared mutable board:** It is safe because every dequeued string is restored before its neighbors are generated.
