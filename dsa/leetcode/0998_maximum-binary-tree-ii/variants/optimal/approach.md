## General
**Only the right spine can change:** Inorder traversal of a maximum tree recovers its source list. Because `val` is appended at the list's end, it lies to the right of every existing element. Therefore its position in the reconstructed tree can affect only ancestors reached by following right-child links from the root.

**Find the first smaller right-spine node:** If `val` exceeds the root, create a new root and attach the entire old tree as its left child. Otherwise, walk down the right spine while the next node's value remains greater than `val`. Create the new node at the first break: its left child becomes the smaller right subtree that used to occupy that link, and the preceding node's right child becomes the new node.

All nodes above the insertion point remain greater than `val`, so their maximum-tree relationships stay valid. Every node moved under the new node is smaller than `val`, and its inorder positions still precede the appended value. The resulting tree therefore has exactly the inorder sequence `a` followed by `val` and preserves the maximum-tree construction.

## Complexity detail
The algorithm examines at most the $H$ nodes on the right spine, giving $O(H)$ time. It creates one node and uses a constant number of pointers, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Recover the full list and rebuild:** Inorder traversal followed by maximum-tree reconstruction is correct but touches every node and can take $O(N^2)$ time with repeated maximum searches.
- **Recursive right-spine insertion:** This expresses the same recurrence in $O(H)$ time but uses $O(H)$ call-stack space.
- **New global maximum:** When `val > root.val`, the returned node is a new root whose left child is the old root.
- **New smallest suffix value:** The insertion reaches the end of the right spine and attaches a leaf.
- **Middle insertion:** A smaller right subtree becomes the new node's left subtree rather than being discarded.
