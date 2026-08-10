## General

**The root value is the global minimum**

Every internal node stores the smaller of its two children's values. Therefore, an internal node is no larger than either child. Applying that fact repeatedly down every path shows that the root is no larger than every node in the tree.

The smallest value is consequently:

`v = root.val`.

The second minimum is the smallest node value strictly greater than `v`. Equal copies of the minimum do not count as a second distinct value.

**Track the best qualifying value**

The solution initializes `ans = -1` to mean that no value greater than `v` has been found. This sentinel is safe because all legal node values are positive.

During traversal, when `root.val > v`:

- if `ans == -1`, this is the first candidate, so assign it;
- otherwise, keep `min(ans, root.val)`.

Values equal to `v` are ignored because the question asks for the second minimum value in the set of distinct values.

**Traverse the entire tree**

The nested `dfs` recursively visits the left and right children, then evaluates the current node. This is postorder traversal.

The answer logic would work in preorder or inorder as well because it depends only on the multiset of values, not on structural order. Postorder is simply the order implemented by the exact source.

A null pointer does nothing. Every real node is eventually compared with the known minimum.

**A walkthrough**

For the tree represented by `[2, 2, 5, null, null, 5, 7]`, the root establishes `v = 2`.

Nodes equal to two are ignored. The first encountered five sets `ans = 5`. Another five leaves it unchanged. Seven is greater than two but larger than the current candidate five, so the minimum update keeps five.

The returned second minimum is five.

For `[2, 2, 2]`, no node is strictly larger than two. `ans` remains negative one, which is the required failure result.

**Why the special tree property matters**

Without the property, `root.val` would not necessarily be the global minimum. The algorithm would need to track both the smallest and second-smallest values while traversing.

Here, the property gives the first minimum for free. The search only has to find the smallest value above it.

**Why duplicates are handled correctly**

Suppose the minimum value appears many times. None passes the strict `> v` test, so they cannot incorrectly fill `ans`.

Suppose the true second minimum also appears many times. The first occurrence initializes or lowers `ans` to that value, and later equal occurrences leave it unchanged. The result is a value, not a count, so this is correct.

**Why the final result is correct**

The traversal examines every node. Let `C` be the set of all visited values strictly greater than `v`.

After any processed portion of the traversal, `ans` is either negative one when that portion contains no candidate, or the minimum candidate seen so far. The update preserves this statement for each new node.

At the end, if `C` is nonempty, `ans = min(C)`, which is exactly the second distinct minimum because `v` is the global minimum. If `C` is empty, every node equals `v` and no second minimum exists, so returning negative one is correct.

**The exact traversal does not exploit possible pruning**

If a node value is already greater than `v`, the special property implies all its descendants are at least that node value. That node itself is therefore the smallest value in its subtree above `v`, and its descendants cannot provide a smaller candidate.

An optimized traversal could update `ans` at that node and skip its children. The exact source visits them anyway. It remains linear and correct, and the small node bound makes the simpler exhaustive scan acceptable.

## Complexity detail

Let `N` be the number of nodes and `H` the tree height.

Every node is visited once and processed with constant work, so running time is `O(N)`.

The recursive call stack follows at most one root-to-leaf path at a time, using `O(H)` space. The tree stores no extra per-node data and the scalar variables use `O(1)` space.

The special full-or-leaf structure does not force balance. A tree can still have height proportional to `N`, so the worst-case stack bound is `O(N)`, although the source caps `N` at only 25.

## Alternatives and edge cases

- **Prune above-minimum subtrees:** When a node value exceeds `v`, update the candidate and stop descending because all descendants are at least that value. This may inspect fewer nodes while retaining `O(N)` worst-case time.

- **Track two minima generically:** Traverse any binary tree while maintaining smallest and second-smallest distinct values. This does not rely on the special property but uses slightly more update logic.

- **Collect values into a set and sort:** It is simple but uses `O(N)` extra space and `O(N log N)` sorting time.

- **Breadth-first traversal:** A queue can perform the same candidate updates in `O(N)` time but uses width-dependent space.

- **All values equal:** No strict candidate exists, so the answer is negative one.

- **Single-node tree:** The root is the only value and the result is negative one.

- **Second minimum equals a child of the root:** It is found like any other candidate.

- **Second minimum occurs deep in the tree:** Exhaustive traversal reaches it even if all ancestors on that path equal the minimum.

- **Repeated second minimum:** Duplicate occurrences do not change the returned value.

- **Positive-value guarantee:** It makes negative one an unambiguous sentinel. With arbitrary negative values, a separate Boolean or infinity should be used.

- **Nonempty-tree guarantee:** The exact source reads `root.val` before traversal, so a null root would fail outside the contract.

- **Two-or-zero children property:** The scan itself can traverse any shape, but the proof that the root is globally minimum relies on the stated value relationship throughout the special tree.

- **Postorder versus preorder:** Traversal order does not affect the minimum aggregation; only complete coverage matters.
