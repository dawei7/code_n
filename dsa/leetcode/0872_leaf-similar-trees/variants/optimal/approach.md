## General

Two trees are leaf-similar only when their leaf values appear in the same left-to-right order. Having the same set of leaf values is not enough, and even having the same multiset is not enough. The sequence matters: `[6,7,4]` and `[6,4,7]` describe different leaf orders.

The solution constructs the leaf sequence of each tree with depth-first search and compares the resulting lists. Internal structure is irrelevant except for the order in which it places leaves, so the traversal records no internal node values.

**Recognizing a leaf.** A leaf has neither a left nor a right child. The implementation tests `root.left == root.right`. In an ordinary binary tree from this problem, both child references are `None` exactly at a leaf, so they compare equal. At an internal node, at least one child is a real node; the two child references are not equal in the proper tree structure.

The more explicit condition `root.left is None and root.right is None` would communicate the definition more directly, but the equality check is a compact equivalent under the platform's binary-tree contract. It would be unsafe for a general graph-like object in which both child fields could reference the exact same non-null node, but such shared-child structures are not valid input trees here.

When a leaf is found, its value is appended to `nums` and the function returns immediately. Returning is important because a leaf has no descendants to visit, and it prevents the later child checks from doing unnecessary work.

**Why the traversal produces left-to-right order.** For an internal node, the function recursively processes `root.left` first if it exists, then `root.right` if it exists. Every leaf inside the left subtree appears geometrically before every leaf inside the right subtree. The recursive call itself follows the same rule at every lower node. Therefore, a left-first depth-first traversal appends all leaves in precisely the required left-to-right order.

This can be proven by induction on a subtree. A leaf produces the one-element sequence containing its value, which is correct. For an internal node, assume the recursive traversal correctly produces the left-to-right leaf sequence of each child subtree. The function completes the entire left call before starting the right call, so the combined list is the left subtree's sequence followed by the right subtree's sequence. That concatenation is exactly the parent subtree's left-to-right leaf sequence.

**The list is passed by reference.** The helper returns `None` because it does not need to return a new list from every recursive call. Instead, `nums` refers to one shared list for the current tree, and each discovered leaf appends to it. The calls for `root1` share `l1`, while the calls for `root2` share `l2`. The two trees never share an output list.

After both traversals finish, `l1 == l2` performs element-by-element sequence comparison. It is true only if the lists have equal lengths and every value at every position matches. Thus it rejects all relevant differences:

- a value differs at the same leaf position;
- one tree has extra leaves;
- the same values appear in a different order.

The internal values, depths, and shapes can differ freely. For example, one tree may have a leaf value reached after two edges and the other after five; if the full left-to-right leaf sequences match, the result is still true.

**Why every relevant node is handled.** The helper is initially called on each root. The constraints guarantee that each tree has at least one node, so the exact implementation does not need a null-root guard before reading `root.left`. At an internal node it recursively visits each existing child once. Every node has a unique parent in a tree, so no node is revisited. Every leaf is eventually reached and appended exactly once.

The approach separates extraction from comparison, which makes the reasoning especially transparent for beginners: first reduce each complex tree to the one sequence the definition cares about, then use ordinary list equality to answer the problem.

## Complexity detail

Let $n_1$ and $n_2$ be the node counts, $h_1$ and $h_2$ the tree heights, and $\ell_1$ and $\ell_2$ the numbers of leaves.

- **Time complexity:** $O(n_1+n_2)$. Each node is visited once. Comparing the leaf lists costs at most $O(\ell_1+\ell_2)$, which is already bounded by the node traversal.
- **Space used by recursion:** $O(h_1+h_2)$ across the two sequential traversals in a combined bound; at any instant, only one traversal is active, so the peak stack is $O(\max(h_1,h_2))$.
- **Space used by the exact implementation overall:** $O(h_1+h_2+\ell_1+\ell_2)$ when all retained structures are counted, which is $O(n_1+n_2)$ in the worst case because it explicitly stores both leaf lists.

The branch manifest's $O(h_1+h_2)$ bound describes the traversal-stack component. The exact code also materializes `l1` and `l2`, so a complete accounting must include their leaf storage. A generator-based comparison could achieve stack-only auxiliary storage while preserving the same traversal idea.

## Alternatives and edge cases

- **Lazy leaf generators:** Yield one leaf at a time from each tree and compare the streams. This can avoid storing both full sequences, reducing auxiliary storage to the traversal stacks, but synchronized exhaustion must be checked carefully.
- **Iterative depth-first search:** Stacks can replace recursion. Push the right child before the left so the left side is processed first. This avoids recursion-depth limits but still uses height-proportional traversal storage.
- **Breadth-first traversal:** Ordinary level-order traversal does not produce leaves in left-to-right boundary order when leaves occur at different depths, so it cannot simply append leaves as encountered.
- **Compare leaf sets:** Sets discard order and duplicates, both of which are meaningful. They can incorrectly label different sequences as equal.
- **Compare only leaf counts:** Equal counts say nothing about values or ordering and are insufficient.
- **Single-node trees:** The root has two null children and is itself the only leaf. Two such trees are leaf-similar exactly when their root values match.
- **Different shapes:** Shape does not matter if the leaf sequences agree. The solution never compares internal structure.
- **Different internal values:** Internal node values are not appended and do not influence the result.
- **Repeated leaf values:** Lists retain every occurrence and its position, so duplicates are handled correctly.
- **One sequence is a prefix of the other:** List equality returns false because the lengths differ, even if all shared positions match.
- **Deep skewed trees:** The recursion stack can grow to the number of nodes. The stated maximum of 200 nodes keeps that manageable in the platform environment.
- **Non-null roots:** The helper dereferences its argument immediately. This is correct because the contract guarantees at least one node in each tree; a reusable library version could add a null guard.
- **Child equality shortcut:** `root.left == root.right` relies on a proper tree in which the only equal child references are both `None`. The explicit two-null test is preferable if inputs might contain shared node objects.
