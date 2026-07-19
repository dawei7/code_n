## General
**Search strings by number of swaps**

Treat every distinct anagram as a graph vertex. Two vertices are adjacent when one arbitrary-position swap transforms one into the other. Every edge costs one swap, so breadth-first search from `s1` reaches `s2` at the minimum possible $k$. A visited set prevents repeated work when different swap sequences produce the same string.

**Fix the first mismatch in every generated neighbor**

For a dequeued string, find the first index `i` where it differs from `s2`. Earlier positions already match and never need to be disturbed. Generate swaps only with later indices `j` such that `current[j] == s2[i]`; each neighbor immediately fixes position `i`.

Also require `current[j] != s2[j]`. Taking the needed letter from an already correct position would create a new mismatch, while the anagram counts guarantee that some later mismatched occurrence of that letter exists.

This pruning preserves an optimal path. Any complete transformation must eventually move the required letter into the first mismatched position. That correcting swap can be chosen before operations confined to later positions without increasing the swap count. BFS explores every such correction choice, including alternatives caused by duplicate letters, and therefore still discovers a shortest transformation.

## Complexity detail
At most $P$ distinct anagrams can be visited. A state may inspect $O(n)$ swap partners, and constructing each neighbor string costs $O(n)$, giving the conservative $O(n^2P)$ time bound. The visited set and queue can hold $P$ strings of length $n$, using $O(nP)$ space.

## Alternatives and edge cases
- **Unpruned all-swap BFS:** Generating every pair of swapped indices is correct, but explores many states that break an already matched prefix.
- **Bidirectional BFS:** Expanding from both strings can reduce the practical search frontier, though it requires careful frontier and visited-set coordination.
- **Depth-first branch and bound:** Track the best solution and prune by mismatch lower bounds; it can be effective but does not provide BFS's immediate shortest-path guarantee.
- **Identical strings:** The initial state already equals the target, so the answer is `0`.
- **One swap:** Two mismatched positions containing each other's target letters are resolved in one edge.
- **Duplicate letters:** Different index swaps may create the same string, making deduplication essential.
- **Disjoint cycles:** Each permutation cycle can require several swaps, and BFS naturally combines their choices.
- **Arbitrary positions:** The cost counts swaps, not the distance between swapped indices.
- **Small alphabet:** Repetition can make $P$ much smaller than $n!$, which the frequency-aware bound captures.
