## General
**Use iterative inorder traversal as the sorted order**

An inorder traversal of a binary search tree visits nodes from smallest to largest. Use an explicit `stack` to descend through left children, then pop the next node to visit. Keep `previous`, the most recently visited node, and `first`, the smallest node encountered. When visiting a node, connect `previous.right` to it and its `left` back to `previous`; the first visit initializes `first` instead.

**Preserve the unvisited right subtree**

The traversal processes the original left subtree before rewiring the current node's left link. Save the current node's original `right` pointer as `right_subtree` before linking it into the list, then continue the traversal from that saved subtree. This makes the separation between unvisited tree edges and completed list edges explicit.

**Close both ends after traversal**

After inorder traversal, `first` is the minimum and `previous` is the maximum. Set `first.left = previous` and `previous.right = first`. These two assignments turn the already sorted bidirectional chain into the required cycle.

**Why every link is correct**

Each adjacent pair in inorder order is linked exactly when the later node is visited, in both directions. No node is skipped or created. The final two assignments provide the only missing predecessor and successor links, so every node has exactly its sorted predecessor on the left and sorted successor on the right, including wraparound.

## Complexity detail
Every node is pushed, popped, and linked once, giving $O(n)$ time. The explicit stack holds at most one root-to-leaf path, so auxiliary space is $O(h)$, where `h` is the tree height. Unlike interpreter recursion, the heap-backed list also supports the legal 2,000-node skew boundary.

## Alternatives and edge cases
- **Recursive inorder traversal:** is shorter, but a legal 2,000-node spine exceeds Python's default recursion limit even though its asymptotic $O(h)$ space bound is the same.
- **Collect all nodes first:** simplifies linking but uses $O(n)$ auxiliary space; repeatedly searching that list for each node can further degrade to $O(n^2)$ time.
- **Empty tree:** return `None` without attempting endpoint links.
- **Single node:** both `left` and `right` must point back to that node.
- **Skewed tree:** the explicit stack grows to $O(n)$ without depending on the interpreter recursion limit.
