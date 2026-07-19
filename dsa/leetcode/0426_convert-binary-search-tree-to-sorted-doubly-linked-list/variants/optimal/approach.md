## General
**Use inorder traversal as the sorted order**

An inorder traversal of a binary search tree visits nodes from smallest to largest. Keep `previous`, the most recently visited node, and `first`, the smallest node encountered. When visiting a node, connect `previous.right` to it and its `left` back to `previous`; the first visit initializes `first` instead.

**Preserve the unvisited right subtree**

The traversal processes the original left subtree before rewiring the current node's left link. Its original right link is not replaced until a later node connects back as the successor, so recursively visiting the right subtree immediately after linking the current node remains safe.

**Close both ends after traversal**

After inorder traversal, `first` is the minimum and `previous` is the maximum. Set `first.left = previous` and `previous.right = first`. These two assignments turn the already sorted bidirectional chain into the required cycle.

**Why every link is correct**

Each adjacent pair in inorder order is linked exactly when the later node is visited, in both directions. No node is skipped or created. The final two assignments provide the only missing predecessor and successor links, so every node has exactly its sorted predecessor on the left and sorted successor on the right, including wraparound.

## Complexity detail
Every node is visited and linked once, giving $O(n)$ time. Recursive calls follow one root-to-leaf path at a time, so auxiliary space is $O(h)$, where `h` is the tree height.

## Alternatives and edge cases
- **Iterative inorder traversal:** uses an explicit $O(h)$ stack and links nodes in the same order.
- **Collect all nodes first:** simplifies linking but uses $O(n)$ auxiliary space; repeatedly searching that list for each node can further degrade to $O(n^2)$ time.
- **Empty tree:** return `None` without attempting endpoint links.
- **Single node:** both `left` and `right` must point back to that node.
- **Skewed tree:** recursion uses $O(n)$ stack space in the worst case.
