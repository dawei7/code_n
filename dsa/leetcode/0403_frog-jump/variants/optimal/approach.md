## General
**A stone position alone is not enough state**

Future options depend on the jump used to arrive, so associate each stone with the set of reachable last-jump lengths. Initialize position zero with jump length zero; applying $0 + 1$ enforces the required first jump.

**Propagate the three legal successors**

Process stones from left to right. For every stored last jump `k`, try $k - 1$, `k`, and $k + 1$, ignoring nonpositive lengths. If the resulting position is a stone, add that new jump length to its set.

**Merge paths that reach the same state**

Many jump sequences can arrive at the same `(position, last_jump)` pair. A set stores that pair once because all future behavior from it is identical. This prevents exponential re-exploration without discarding any distinct future option.

**Why reachability propagation is complete**

Every inserted state extends a previously reachable state by one permitted positive jump, so it represents a valid path. Conversely, take any valid path and consider its states in order: the initial state exists, and propagation tries exactly the next path jump, so induction inserts every state on that path. The final stone is reachable precisely when its set is nonempty.

## Complexity detail
For `n` stones, a stone can be associated with $O(n)$ distinct jump lengths, and each state generates three constant-time transitions. Time and stored state are therefore $O(n^2)$.

## Alternatives and edge cases
- **Memoized depth-first search:** explores the same position-and-jump states recursively and has the same asymptotic bounds.
- **Uncached path search:** may revisit equivalent states along exponentially many jump sequences.
- **Scan all prior edges for every candidate jump:** is correct but can take $O(n^3)$ time.
- If the second stone is not at position one, the first jump cannot land.
- Jump length zero or negative is never permitted.
- A large gap can make all later stones unreachable.
- Different last-jump lengths on the same stone must remain separate states.
