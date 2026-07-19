## General
**Interpret the permutation as directed cycles**

Each index has exactly one outgoing edge to `nums[index]`, and every index also has exactly one incoming edge because all values are distinct. The graph is therefore a collection of disjoint cycles.

**Start only from globally unseen indices**

Scan every index. If it is already visited, its entire cycle was counted earlier. Otherwise follow successive array values, marking each reached index and counting the cycle length.

**Record the largest completed cycle**

The walk ends when it reaches a marked index. Under the permutation contract, a new walk cannot merge into a different partly visited path; it closes the cycle that began at the current unseen start. Compare its count with the maximum.

**Why cycle length equals nesting-set size**

Starting at any index repeatedly follows the unique outgoing edges around its cycle and visits every cycle member once before returning to the start. Thus every start in the same cycle has the same nesting-set size. The outer scan starts one walk for each disjoint cycle, so taking the largest counted cycle gives the maximum over all starts.

## Complexity detail
Every index is marked during exactly one cycle walk, so the total traversal time is $O(n)$. The Boolean visited array uses $O(n)$ space.

## Alternatives and edge cases
- **Mark in the input array:** can achieve $O(1)$ auxiliary space by overwriting values, but it mutates the caller's permutation.
- **Restart from every index:** is correct but retraverses the same cycle from each member and takes $O(n^2)$ time for one large cycle.
- **Identity permutation:** every index is a one-element cycle.
- **Single element:** points to itself and gives answer one.
- **One full cycle:** every starting index produces all `n` values.
- **Several cycles:** only the longest cycle contributes to the answer.
- **Permutation guarantee:** removes tails and merges that would occur in a general functional graph.
