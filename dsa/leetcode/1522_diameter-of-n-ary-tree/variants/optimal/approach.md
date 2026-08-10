## General

**A diameter can be assembled at its highest node**

The longest path between two tree nodes has a unique highest node where the two endpoint branches meet. At that node, the path uses the two longest downward branches. One branch may have length zero when one endpoint is the meeting node itself.

The stored recursive function computes the longest downward branch for every node and updates a shared maximum from the best two child branches.

**Meaning of the dfs return value**

For a non-null node, `dfs(root)` returns one plus the maximum child return. A leaf has no children, so `m1` remains zero and it returns one.

Thus the returned number is the count of nodes on the longest downward path beginning at the current node. When a parent receives child value `t`, that same number is also the number of edges from the parent down through that child to the deepest endpoint:

- A leaf child returns one, representing the one edge from parent to child.
- A deeper child returns two or more, matching the parent's edge distance down that branch.

This dual interpretation makes `m1 + m2` an edge count for a path passing through the current node.

The null guard returns zero. The formal input root is non-null, but this makes the helper defined for an absent child-like value.

**Tracking the two largest branches**

`m1` is the largest child return seen so far and `m2` is the second largest.

If new `t` exceeds `m1`, the old largest moves to second place and `t` becomes largest. Otherwise, if it exceeds `m2`, only second place changes. Values no larger than both are irrelevant to the best path bridged by this node.

This selection uses constant local state and avoids sorting all child heights.

**Updating the global diameter**

After every child subtree has been processed, `m1 + m2` is the longest path whose highest meeting point is the current node and whose sides descend through two different children.

If the node has only one child, `m2` remains zero, so the candidate is the longest path from the current node into that child subtree. If it is a leaf, both are zero and its candidate diameter is zero.

`ans = max(ans, m1 + m2)` compares this local candidate with candidates from all descendants. The outer method initializes `ans = 0`, invokes DFS, and returns the maximum edge length.

**Why this finds paths not passing through the root**

Every simple path has a lowest common ancestor relative to the root. That ancestor is the highest meeting node for the two path endpoints. When DFS processes it, the two relevant downward distances are among its child branches, and the top-two selection produces a candidate at least as long.

Conversely, every candidate `m1 + m2` corresponds to a real simple path joining endpoints down those branches, or joining the current node to one descendant when the second branch is zero. Therefore, the maximum candidate is exactly the diameter.

**Why postorder is necessary**

The parent cannot know a child's height until that child's descendants have been processed. Recursive calls happen before the local diameter update, giving a postorder computation from leaves upward.

Node values never matter; only the tree shape and children relationships affect path lengths.

## Complexity detail

Let $N$ be the number of nodes and $H$ the tree height. Every node is visited once, and every parent-child edge is examined once. Maintaining two maxima is constant work per child, so time is $O(N)$.

The recursion stack uses $O(H)$ space, which becomes $O(N)$ in a chain. Local scalar state is constant per active frame, so worst-case auxiliary space is $O(N)$, matching the manifest.

The stated depth can reach one thousand, close to Python's common recursion limit. A deepest valid tree may raise `RecursionError` depending on the environment. An iterative postorder traversal avoids that practical limit.

## Alternatives and edge cases

- **Sort all child heights:** Take the largest two after sorting. It is correct but adds per-node sorting and temporary storage.
- **Two breadth-first searches:** For an undirected tree representation, farthest-from-arbitrary then farthest-again finds the diameter, but the given nodes expose only child links unless parent edges are built.
- **Iterative postorder:** Store nodes and visitation state explicitly to avoid recursion-depth problems.
- **Single node:** Both branch lengths are zero, so diameter is zero.
- **One long chain:** Every node has one branch, and the diameter is the root-to-leaf edge count.
- **Star tree:** The root's two largest child branches are both one, giving diameter two.
- **One child at a meeting node:** The zero second branch correctly permits the node itself as an endpoint.
- **Diameter below root:** The descendant's local update records it before returning upward.
- **Edge count versus node count:** Child return one represents one parent-to-leaf edge, so `m1 + m2` is already in edges.
- **Non-null contract:** The helper's null case is defensive; a formal tree has at least one node.
