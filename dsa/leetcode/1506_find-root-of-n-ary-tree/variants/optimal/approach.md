## General
**Turn parent cancellation into a root signature**

In a valid tree, every non-root node occurs twice across the supplied information: once as an element of `tree`, and once as a child of its unique parent. The root occurs only in `tree`, because no parent refers to it.

Bitwise XOR cancels equal values because $x \mathbin{\mathrm{XOR}} x = 0$, while zero is neutral. XOR every node value into one accumulator, then XOR every referenced child value into the same accumulator. Each non-root value cancels with its second occurrence. The sole value left is the root's value.

The app-local representation stores child values directly, so it performs this cancellation without reconstructing node objects. The platform-native implementation makes a second linear pass to return the actual node whose `val` equals the remaining value.

**Why order and shape do not affect the result**

XOR is associative and commutative. Therefore neither the random order of the node array nor the order of siblings changes the accumulator. Branching factors and tree depth are also irrelevant: the proof depends only on the one-parent property.

For each non-root node $v$, the accumulator contains exactly two copies of its unique value, and those copies cancel. The root value appears exactly once, so the final accumulator identifies precisely the required node. The guarantee that values are unique makes the native lookup unambiguous.

## Complexity detail
Across all nodes, the child lists contain exactly $N-1$ references. Scanning the $N$ nodes, all $N-1$ edges, and then at most $N$ nodes to recover the native object takes $O(N)$ time.

The accumulator and loop variables occupy constant auxiliary space, independent of $N$. The input node array and child lists already belong to the caller and are not counted as extra storage, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Child-value hash set:** insert every child value, then return the node whose value is absent. This is straightforward and remains $O(N)$ time, but consumes $O(N)$ extra space.
- **Sum cancellation:** subtract every child value from the sum of all node values. It expresses the same invariant, but fixed-width languages may overflow unless they use a sufficiently wide type; XOR avoids that concern.
- **Repeated parent search:** for each candidate, scan every child list to see whether it has a parent. It uses constant space but can require $O(N^2)$ time.
- **Traversal from each candidate:** trying to infer the root by repeatedly exploring descendants does unnecessary work because the input already exposes every incoming edge.
- **Single node:** no child value is present, so its value remains in the accumulator and that node is returned.
- **Root appears last:** array position is irrelevant; the algorithm does not assume the first node is the root.
- **Wide or deep trees:** only the total number of nodes and edges matters; the algorithm uses neither recursion nor a traversal stack.
- **Nonconsecutive values:** cancellation relies on equality, not on values forming a range.
- **Random node order:** commutativity makes all permutations equivalent.
