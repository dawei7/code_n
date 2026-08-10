## General

**Merge by tree position, not by value.** Two nodes overlap when they occupy the same path from their respective roots. For example, the left child of `root1` is compared with the left child of `root2`, regardless of the values stored there. The recursive function naturally represents this positional rule because every call receives the two nodes associated with one path.

There are only three structural situations at a position:

1. the first node is absent;
2. the second node is absent;
3. both nodes exist.

The exact solution handles those situations in that order.

**When one node is absent, the other subtree already is the merged result.** If `root1 is None`, nothing from the first tree overlaps this position, so the method returns `root2`. Similarly, if `root2 is None`, it returns `root1`. This is more powerful than merely choosing one node value: it reuses the entire existing subtree below that node. Every descendant in that subtree is also unmatched because the other tree has no node at the current position and therefore cannot have a descendant below that missing node.

This base case also handles both nodes being absent. The first condition returns `root2`, which is `None`, exactly as required.

**When both nodes exist, create the required sum node.** Neither original node alone has the correct value, so the solution allocates

`TreeNode(root1.val + root2.val)`.

It then merges the two left children and assigns the returned root to `node.left`. The same operation on the right children supplies `node.right`. Finally, it returns the newly assembled node to the parent call.

The order is easy to visualize as a top-down decision followed by bottom-up construction:

- decide the merged value at the current position;
- ask recursion for the complete merged left subtree;
- ask recursion for the complete merged right subtree;
- attach those two answers and return the current merged root.

For the sample roots with values `1` and `2`, the first returned node has value `3`. Their left children, `3` and `1`, produce `4`; their right children, `2` and `3`, produce `5`. At the path left-left, only the first tree has `5`, so that existing subtree is returned. At left-right, only the second tree has `4`, so that subtree is returned. The same rule preserves the second tree's `7` at right-right.

**Why the recursion is correct.** Consider the result for one pair of input nodes.

- If the first node is absent, the problem's rule says to use the non-null second node, and the method returns precisely that subtree.
- If the second is absent, the symmetric rule is satisfied.
- If both exist, the required current value is their sum, which the new node stores. The recursive calls solve the identical merge problem for the left position and the right position. Once those correct subtree results are attached, every position below the current node also follows the merge rule.

These cases exhaust all possibilities. Starting at the two roots therefore yields a tree whose value and structure are correct at every reachable position.

**The returned tree is new only where nodes overlap.** The exact source does not mutate either overlapping input node: it allocates a fresh node whenever both inputs exist. However, when one input is `None`, it returns the other input subtree directly rather than cloning it. The result is therefore a hybrid:

- overlapping positions are represented by newly allocated nodes;
- non-overlapping branches are shared by reference with an original tree.

This is safe for merely returning and reading the answer. It matters if a caller later mutates the returned tree, because changing a reused branch also changes the corresponding original input tree. Likewise, later mutations of an input's reused branch are visible through the result. Calling the result a completely deep-copied third tree would be inaccurate.

**Why recursion matches the constraints.** Each call solves one smaller positional subproblem, and child pointers give direct access to the only two next positions. No map from paths to nodes is necessary. With at most 2,000 nodes across both trees, the amount of structural work is modest, although a completely skewed tree can still make Python's recursion depth a practical concern.

## Complexity detail

Let $K$ be the number of positions at which both input trees contain a node, and let $H$ be the maximum number of overlapping positions along one root-to-leaf path. The method allocates and processes one new node for every overlapping position. At a position where one side is missing, it returns immediately and does not traverse the surviving subtree. Thus the exact traversal time is $O(K)$, with constant-time boundary calls around those overlapping nodes.

The manifest states $O(N)$ time and $O(N)$ space, where $N$ can be understood as a broad upper bound on the relevant input or result size. Since $K$ cannot exceed the total number of input nodes, $O(N)$ is valid but less precise.

The active recursion stack has at most $H$ frames, so auxiliary call-stack space is $O(H)$. A balanced overlapping region has logarithmic height, while a skewed overlap can have $H=O(N)$. The method also creates $K$ output nodes, requiring $O(K)$ result storage. If output storage is counted, total additional space is $O(K+H)=O(N)$, matching the manifest. Reused non-overlapping subtrees consume no new node storage.

## Alternatives and edge cases

- **Mutate the first tree:** Add overlapping values into `root1` and attach branches from `root2` where `root1` is absent. This reduces new allocations but deliberately changes the caller's first input.
- **Deep-copy every retained subtree:** Allocate a brand-new node at every position in the union of both trees. This guarantees that the result shares no nodes, but it must traverse and copy non-overlapping branches that the exact solution returns in constant time.
- **Iterative stack of node pairs:** An explicit stack avoids Python recursion limits. It is especially useful for highly skewed trees, but attachment logic is more verbose because each produced child must be connected to its parent.
- **Both roots are `None`:** The first base case returns `None`, which is the correct empty merged tree.
- **Only one root exists:** The entire existing tree is returned by reference without traversal or copying.
- **One-sided branch below an overlap:** The parent is a new node, while the unmatched child subtree is directly shared with its source tree.
- **Negative values:** Addition works unchanged. A merged value may be negative, zero, or positive within the arithmetic range.
- **Skewed trees:** Correctness is unchanged, but recursion depth can become linear and may exceed the language's default stack limit before reaching the stated 2,000-node maximum.
- **Later mutation:** Because non-overlapping subtrees are shared, mutate the returned tree only if aliasing with the inputs is acceptable.
- **Different shapes:** No alignment or rotation is performed. Only identical left/right paths overlap, exactly as required by the root-based merge definition.
