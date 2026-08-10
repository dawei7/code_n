## General

**Treat every matrix configuration as a graph state**

Each cell is binary, and the matrix has at most nine cells. If $k=m\cdot n$, there are only $2^k$ possible configurations. A flip moves deterministically from one configuration to another, so the problem becomes an unweighted shortest-path search: configurations are vertices, one legal cell flip is an edge, the input matrix is the start, and the all-zero matrix is the target.

Breadth-first search is the correct traversal because every edge costs one flip. It explores all states one flip away, then two flips away, and so on. The first time it reaches zero, the current level is the minimum number of operations.

**Encode the matrix as one integer**

Cell `(i, j)` is assigned bit position `i * n + j`. The expression

`sum(1 << (i * n + j) ... if mat[i][j])`

sets precisely the bits corresponding to one-cells. Because each bit position is distinct, addition behaves like bitwise OR here. The zero matrix is integer zero.

This compact representation makes configurations hashable for `vis` and avoids copying a two-dimensional matrix for every transition.

**Generate one flip transition**

The direction sequence `[0, -1, 0, 1, 0, 0]` produces five coordinate offsets from consecutive pairs: the cell itself, left, up, right, and down. For a chosen center `(i,j)`, the inner loop considers those five positions and skips any outside the matrix.

Variable `nxt` begins as the current state. For each affected bit, the code tests whether it is set. If set, subtracting its power of two clears it; if clear, bitwise OR sets it. Since each affected coordinate appears once, this exactly toggles the cell.

Using XOR with the bit mask would be a shorter equivalent operation, but the explicit branches make both toggle directions visible.

**Breadth-first levels measure flips**

The deque starts with the encoded input and `ans = 0`. At the beginning of each outer iteration, `len(q)` is the number of states at the current distance. Processing exactly that many states prevents newly appended next-level configurations from being mixed into the same distance.

If a popped state is zero, `ans` is returned. Otherwise, the algorithm tries all $k$ possible flip centers. A new configuration is inserted only if absent from `vis`. This prevents cycles such as flipping the same cell twice and ensures every configuration is expanded at most once.

After the current layer finishes, `ans` increases by one. Therefore every state subsequently in the queue requires one additional flip.

**Why the first zero is optimal**

Every legal flip is generated from every visited configuration, so BFS does not omit any operation sequence. Each queue edge corresponds to exactly one flip and has equal cost. Standard BFS ordering guarantees that all paths shorter than `ans` have already been explored when a level-`ans` state is popped.

Thus, if zero is found, no shorter sequence exists. If the queue empties, every configuration reachable from the input has been explored without reaching zero, so returning `-1` is correct.

For an initially zero matrix, the first popped state is zero and the method returns zero without generating transitions.

**Why repeated flips need no special rule**

Flipping a center twice cancels its effect, so a shortest sequence never needs the same center twice. The BFS does not explicitly enforce that observation, but visited-state deduplication automatically discards cycles and all other repeated paths. This state-based reasoning is simpler and safely covers interactions among overlapping flip neighborhoods.

## Complexity detail

There are at most $2^k$ configurations. Each expanded configuration tries $k$ centers, and each center toggles at most five cells, a constant. Worst-case time is $O(k2^k)$.

The visited set and queue may hold $O(2^k)$ encoded states. Each state is one bounded integer, so space is $O(2^k)$. The transition uses constant temporary space.

With $k\le9$, the state space has at most 512 configurations, making exhaustive BFS practical.

## Alternatives and edge cases

- **Enumerate flip subsets:** Because each center need be used at most once, test all $2^k$ subsets and choose the smallest successful one. It has similar exponential behavior but does not discover solutions in increasing flip count automatically.
- **First-row Lights Out enumeration:** Guess flips in the first row and derive later rows. It can reduce enumeration width but requires more specialized row reasoning.
- **Mutate matrix copies:** This is conceptually direct but allocates and hashes much larger objects than a bitmask.
- **Initially zero:** The answer is zero at the first BFS pop.
- **Single cell one:** Flipping that cell reaches zero in one step.
- **Impossible matrix:** Queue exhaustion returns `-1`.
- **Boundary centers:** Only existing neighbors are toggled; bounds checks handle corners and edges.
- **Duplicate paths:** Different flip orders may reach the same state, and `vis` keeps only its shortest discovery.
- **Toggle implementation:** Subtraction is safe only after confirming the bit is set; OR safely sets a clear bit.
- **Bit indexing:** Row-major position `i * n + j` is one-to-one for all cells.
