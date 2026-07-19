## General
**Encode each board as one state**

Flatten the six cells into a string such as `"123405"`. The blank's string index determines its legal swap destinations through a fixed adjacency table for the `2 x 3` geometry. Swapping characters produces every neighboring state.

**Search states in increasing move count**

Run breadth-first search from the input state. Store `(state, distance)` pairs in a queue and a set of states already discovered. The first time the target is removed from the queue, its distance is the answer. If the queue empties, the start lies in the unreachable parity component, so return `-1`.

Each graph edge is one legal move. Breadth-first search visits states in nondecreasing path length, so when it first reaches any state it has found a shortest path to that state. In particular, the first target distance is minimum. Exhausting the connected component without finding the target proves no legal sequence exists.

## Complexity detail
Let `V` be the number of board permutations reached and `E` the legal swaps between them. BFS takes $O(V + E)$ time and $O(V)$ space for the queue and visited set. For this fixed puzzle, `V` is at most $6! = 720$ and every state has at most three edges.

## Alternatives and edge cases
- **Bidirectional BFS:** Expanding from both the start and target can reduce the explored frontier while retaining $O(V + E)$ worst-case time.
- **Precomputed distance table:** Because the state space is fixed, one reverse BFS can answer many boards by lookup.
- **Visited list instead of a set:** The search stays correct, but repeated linear membership checks can take $O(V^2)$ time.
- **Depth-first search with pruning:** It can find a solution but does not naturally guarantee minimum moves and may revisit many paths.
- **Already solved board:** Return zero before generating neighbors.
- **Unreachable parity:** BFS explores only the start's 360-state component and returns `-1`.
- **Blank at a corner or edge:** The adjacency table supplies exactly two or three legal swaps as appropriate.
