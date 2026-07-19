## General
**Materialize one side as complements can query it.** Traverse the first tree and insert every node value into a hash set. The traversal may be iterative, avoiding recursion-depth concerns for a skewed tree.

**Probe with every node from the other tree.** Traverse the second tree. For a node value `x`, compute `target - x` and test whether that complement is in the first tree's set. If so, the set value comes from `root1` and `x` comes from `root2`, so the required cross-tree pair exists.

**Why exhausting the second tree proves failure.** Every possible pair contains exactly one second-tree node. When that node is visited, the hash lookup tests the only first-tree value that could complete its sum. If all $m$ probes fail, no pair among the $nm$ possibilities can equal `target`.

The binary-search-tree ordering is not needed for this hash formulation, but the method remains linear and handles positive and negative values uniformly.

## Complexity detail
The first traversal visits $n$ nodes and the second visits at most $m$, with expected $O(1)$ hash insertion and lookup, giving $O(n+m)$ expected time. The value set stores $O(n)$ entries, and iterative traversal stacks can hold $O(n+m)$ nodes in the broad stated bound.

## Alternatives and edge cases
- **Two inorder arrays and two pointers:** Sorted traversals followed by opposite-direction pointers also take $O(n+m)$ time and $O(n+m)$ space.
- **Two lazy BST iterators:** An ascending iterator for the first tree and descending iterator for the second achieves $O(n+m)$ time with $O(h_1+h_2)$ space.
- **Compare every cross-tree pair:** This is correct but takes $O(nm)$ time.
- **Binary-search the second tree per first node:** It uses BST order but takes $O(nh_2)$ time, which becomes quadratic for a skewed tree.
- **Single-node trees:** Their two values are a valid pair because the nodes belong to different trees.
- **Equal values across trees:** They may be paired; cross-tree identity, not value distinctness, is required.
- **Negative target:** Complement arithmetic works without a special case.
- **Skewed trees:** Iterative traversal avoids call-stack overflow.
