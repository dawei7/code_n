## General
**Represent a tower with one node.** Each node stores a value and an array of forward pointers, one for every level occupied by that node. A sentinel head owns the maximum number of levels. Level 0 contains every node in sorted order; a node promoted to height $h$ also participates in levels 1 through $h-1$.

**Navigate from sparse levels to dense ones.** Start at the head's highest level. Move right while the next value is strictly smaller than the target, then drop one level and continue. When level 0 is reached, the next node is the first value greater than or equal to the target. `search` succeeds exactly when that node's value equals the target.

**Record the insertion path.** During the same top-down traversal, save the last node smaller than `num` at every level. Choose the new node's height by repeated independent coin-flip-style bits, capped at a fixed level count large enough for the operation limit. For every occupied level, splice the new node between the recorded predecessor and its former successor. Using strict comparison places a duplicate before existing equal nodes without changing sorted order.

**Erase one physical occurrence.** Record predecessors exactly as for insertion and inspect their shared successor at level 0. If it is not `num`, nothing can be erased. Otherwise, unlink that one node at every level on which the predecessor points to it. Other equal nodes are distinct occurrences and remain linked.

The geometric height rule gives about half as many nodes at each successive level. Thus the expected number of horizontal moves plus downward moves is logarithmic, while every inserted value contributes only a constant expected number of pointers.

## Complexity detail
For $n$ stored occurrences, geometric promotion makes `search`, `add`, and `erase` take $O(\log n)$ expected time. A rare unfavorable choice of heights can produce $O(n)$ time, so the guarantee is expected rather than worst-case. The sum of all tower heights is $O(n)$ in expectation; the fixed sentinel and predecessor array use $O(1)$ additional space relative to the stated maximum level.

## Alternatives and edge cases
- **Balanced binary search tree:** It provides logarithmic operations but is substantially more complex to implement from scratch and must explicitly store duplicate counts or nodes.
- **Sorted dynamic array:** Binary search is fast, but insertion and deletion may shift $O(n)$ elements.
- **Single sorted linked list:** Updates can splice in constant time after locating a predecessor, but finding that position takes $O(n)$ time.
- **Hash map of counts:** It gives expected constant-time membership and updates, but it does not implement the requested layered ordered structure.
- **Duplicate values:** Each `add` creates one occurrence, and one successful `erase` removes exactly one.
- **Missing value:** Both `search` and `erase` return `false` without changing links.
- **Empty structure:** The sentinel's forward pointers are all empty, so lookup and deletion terminate immediately.
- **Boundary values:** Zero and $2\times10^4$ are ordinary keys and need no special sentinels in the value domain.
- **Maximum height:** Promotion stops at the allocated level cap, preventing pointer-array overflow.
