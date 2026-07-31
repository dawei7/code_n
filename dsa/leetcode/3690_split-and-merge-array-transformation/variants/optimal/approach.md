## General

**Model arrangements as an unweighted graph.** Treat each complete array arrangement as a vertex in an unweighted graph. Two arrangements are adjacent when one legal split-and-merge operation transforms one into the other. The requested minimum number of operations is therefore the shortest-path distance from `nums1` to `nums2`.

**Generate every legal neighbor once.** Breadth-first search explores this graph in nondecreasing operation count. For every dequeued tuple, enumerate the half-open removed interval `[left, right)`, concatenate the untouched prefix and suffix, and insert the preserved block at every gap in that remaining tuple. Add an arrangement to the queue only the first time it appears. Duplicate input values may cause different moves to produce the same tuple, so the visited set is necessary for both correctness and bounded work.

**Stop at the first target discovery.** If the start already equals the target, return zero. Otherwise, when a generated tuple first equals the target, its parent was reached with the smallest possible number of moves among all unprocessed paths. The new edge therefore gives a shortest transformation and may be returned immediately. The permutation guarantee ensures the target lies in the same finite state space.

## Complexity detail

At length $n$, there are at most $n!$ distinct arrangements; repeated values only reduce that count. One state has $O(n^2)$ removable intervals and at most $O(n)$ reinsertion gaps per interval. Constructing each tuple costs $O(n)$, giving the conservative time bound $O(n!\,n^4)$. The queue and visited set retain at most $n!$ tuples of length $n$, so space is $O(n!\,n)$.

The legal constraint $n\le6$ caps the state space at 720 distinct permutations. Because the entire size interval from 2 through 6 is less than a fourfold span, the package uses strict bounded-domain evidence instead of a misleading runtime-scaling benchmark.

## Alternatives and edge cases

- **Depth-first search:** It can enumerate reachable arrangements but does not naturally guarantee that the first target path is shortest.
- **Bidirectional breadth-first search:** Expanding from both endpoints can reduce explored states, but ordinary BFS is already bounded by only 720 arrangements here.
- **Repeated values:** Multiple index-level moves can collapse to one tuple; tuple-based deduplication correctly treats them as the same state.
- **Moving the whole array or reinserting at its old gap:** These are legal no-ops and are harmless because the current state is already visited.
- **Already equal arrays:** The minimum is zero and should be returned before generating neighbors.
