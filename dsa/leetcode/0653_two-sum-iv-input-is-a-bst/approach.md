## General

**Turn pair search into complement lookup**

For a current node value `v`, a pair sums to `k` exactly when some other node has value `k - v`. Instead of comparing `v` with every node seen before, the algorithm stores visited values in a hash set. Membership lookup then answers the complement question directly.

The traversal order is not important for this reasoning. The exact solution uses depth-first search, visiting a node before recursively visiting its left and right subtrees.

**Meaning of the visited set**

At the moment `dfs(root)` examines a non-null node, `vis` contains the values of all nodes that have already been processed earlier in the traversal. It does not yet contain the current node's value.

The order of operations is:

1. Compute the needed complement `k - root.val`.
2. Check whether that complement is in `vis`.
3. If it is, return `True`.
4. Otherwise, add the current value to `vis`.
5. Search the left and right subtrees.

Checking before inserting is essential because the problem requires two nodes. If `k` equals twice the current value, inserting first would allow one node to match itself. With the actual order, that pair is found only if an earlier distinct node with the same value was already visited.

**Why the BST ordering is not required by this implementation**

The input is guaranteed to be a binary search tree, but the hash-set method treats it as an ordinary binary tree. It does not compare values to decide which branch to enter. Both subtrees may contain a useful complement depending on which current value is being considered, so it traverses them as needed.

Ignoring the ordering is not incorrect. The set provides constant-time expected complement lookup, and visiting every node is still linear. A different solution could exploit inorder sorting and two pointers, but the exact source chooses the simpler traversal-plus-memory tradeoff.

**How recursion stops early**

After processing the current node, the return expression is:

`dfs(root.left) or dfs(root.right)`.

Python's `or` operator short-circuits. If the left subtree finds a valid pair and returns `True`, the right subtree is not visited because the final answer is already known. If the left side returns `False`, the right side is searched.

Similarly, the complement check returns immediately when it succeeds. The method may therefore inspect much less than the whole tree, although worst-case analysis must assume that no pair exists or that the pair is found last.

**A walkthrough**

Take the tree containing values `5, 3, 6, 2, 4, 7` and target nine. The exact preorder traversal begins at five:

- Five needs four; `vis` is empty, so insert five.
- Three needs six; six has not been visited, so insert three.
- Two needs seven; insert two.
- Four needs five; five is already in `vis`.

At that moment, the nodes with values four and five form the target. The recursion returns `True` through every active call, and no further node must be processed.

For a target with no valid pair, every node is eventually added and both subtrees of every reachable node are exhausted before `False` returns.

**Why every valid pair is found**

Consider any two distinct nodes with values `a` and `b` such that `a + b = k`. The depth-first traversal visits one of them first. That first node cannot find the other yet, so it is added to `vis`. When the second node is later processed, its needed complement is the first node's value, already present in `vis`. The check succeeds.

Conversely, the function returns `True` only when `k - root.val` was inserted by a previously processed node. That earlier node is distinct from the current node, and their values sum algebraically to `k`. Thus every reported pair is valid.

If traversal ends without a successful lookup, then for every node, no earlier node held its complement. Any two nodes have an earlier and later member in traversal order, so no valid pair can have been missed. Returning `False` is therefore correct.

**Why values rather than node identities are stored**

Only the numeric sum matters. A node reference would still require extracting or indexing its value for complement lookup. Storing values gives direct membership tests.

If a tree representation permitted duplicate values, a set would not count how many copies exist, but the check-before-add order still handles a two-equal-value pair correctly: the second occurrence sees the value inserted by the first. The valid-BST contract commonly implies distinct keys, so duplicates are not needed for the stated problem.

## Complexity detail

Let `N` be the number of nodes and `H` the tree height.

Each visited node performs one expected constant-time set lookup and one insertion, then is traversed at most once. In the worst case all `N` nodes are visited, so expected time is `O(N)`. Early success can reduce actual work.

The set can contain up to `N` values, giving `O(N)` storage. Recursive depth is `O(H)`, which is `O(N)` for a completely skewed tree. The combined auxiliary-space bound is therefore `O(N)`.

Hash-set operations are expected constant time; pathological collision behavior can weaken that assumption. Python's integer hashing is appropriate for the bounded integer keys here.

The maximum node count is ten thousand. A severely skewed tree can exceed Python's default recursion depth even though the asymptotic bound is valid. An iterative traversal would avoid that practical limitation.

## Alternatives and edge cases

- **Inorder list plus two pointers:** Inorder traversal of a BST produces sorted values. Two pointers can then find a target sum in `O(N)` time and `O(N)` list space. It uses the BST property explicitly but still stores all values.

- **Two BST iterators:** One ascending and one descending iterator can imitate two pointers with `O(H)` space, but carefully ensuring the iterators refer to distinct nodes makes the implementation more complex.

- **Search the BST for each node's complement:** Searching from the root for every node takes `O(NH)` time, which becomes `O(N^2)` in a skewed tree.

- **Compare every pair:** Quadratic pair enumeration ignores both hashing and BST structure and is unnecessary.

- **Target equals twice one value:** One node cannot pair with itself. Checking before insertion prevents that false positive.

- **Negative values and target:** Subtraction and hash lookup work unchanged; no positivity assumption is used.

- **Single-node tree:** The only value is checked against an empty set, then traversal ends. The correct result is `False` because two nodes are required.

- **Pair lies within one subtree:** Recursive search carries the shared `vis` set across the whole traversal, so nodes within the same subtree can match.

- **Pair crosses the root's subtrees:** Values visited in the left subtree remain in `vis` when the right subtree is searched, so cross-subtree pairs are found.

- **No valid pair:** Every node is processed once and the function returns `False` after complete traversal.

- **Early pair:** Short-circuiting prevents unnecessary exploration once correctness is established.

- **Deeply skewed tree:** Replace recursion with an explicit stack if runtime recursion limits must be respected for the largest legal input.

- **Input is not actually a BST:** The exact hash-set traversal would still be correct for any binary tree, even though that lies outside the stated contract.
