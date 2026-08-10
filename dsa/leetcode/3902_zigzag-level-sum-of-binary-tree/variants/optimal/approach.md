## General

The traversal has two independent responsibilities:

1. discover every actual tree level in ordinary breadth-first order; and
2. inspect the current level in the required zigzag direction until the first node missing the required child.

The source deliberately keeps those responsibilities separate. It builds the next level from every current node before applying the stopping rule to the current level's sum. Therefore, stopping a level's sum does not prune descendants from future output levels.

**The level queue stays in left-to-right order**

The list `q` contains exactly the nodes of the current depth, ordered from left to right. Initially it contains only the root, which is level 1.

To create `nq`, the source loops through `q` from left to right and appends each node's left child before its right child. This is the standard breadth-first rule. If `q` is left-to-right for one level, this child insertion order makes `nq` left-to-right for the next level.

By induction, `q` retains natural left-to-right order at every depth. The source never reverses `q` itself.

**Why the next level is built before the sum scan**

The phrase “stop” applies only to processing nodes for the current level sum. It does not say to stop traversing the tree or discard the violating node's descendants.

The source first gathers all children:

```text
for node in q:
    append node.left if present
    append node.right if present
```

Only after `nq` is complete does it inspect nodes for the current answer entry. Even if the first inspected node immediately violates the child condition and the sum is zero, all existing children from the entire level have already been preserved for the next iteration.

This ordering is essential. Building `nq` only from nodes processed before the break would incorrectly erase legitimate subtrees and might omit deeper levels from `ans`.

**Odd levels: inspect left to right and require a left child**

The Boolean `left` is initially true, corresponding to one-based level 1. For index `i` from 0 through `m-1`, where `m = len(q)`, the source chooses

```text
node = q[i]
child = node.left
```

If the left child is absent, it breaks before adding that node's value. Otherwise, the value contributes to `s` and inspection continues.

Thus an odd level's sum is the value sum of the longest left-to-right prefix in which every inspected node has a left child.

**Even levels: inspect right to left and require a right child**

After each level, `left = not left` toggles the direction. On an even level, iteration counter `i` still grows from 0 upward, but the selected node is

```text
q[m - i - 1]
```

The first selected node is the rightmost, followed by the next node to its left. The required child is `node.right`.

The level sum is therefore the longest right-to-left prefix whose nodes all have right children. As soon as a selected node lacks a right child, the source stops before adding that node and ignores every remaining node farther left for this level's sum.

Indexing the existing list backward avoids allocating a reversed copy.

**A trace of the stopping behavior**

Consider level 2 containing nodes 2 and 8 from left to right. Because level 2 is even, inspection order is 8, then 2.

- If node 8 has a right child, its value is included.
- If node 2 lacks a right child, processing stops before adding 2.

The level sum is therefore 8. This remains true even if node 2 has a left child: the even-level rule specifically requires a right child.

At an odd level, the analogous rule uses left children. If the first left-to-right node has no left child, the source appends zero for that level because `s` has not yet received any value.

**Why every answer entry matches its level**

At the start of an iteration, `q` contains every node at one depth in natural order, and `left` matches that depth's parity. The indexed scan visits nodes in exactly the specified direction.

For each visited node, the source checks the required directional child before adding its value. Hence all values added occur strictly before the first violating node. When a violation occurs, `break` prevents that node and every later node in inspection order from contributing. If no violation occurs, all nodes contribute.

The method appends `s` once for every nonempty `q`, then replaces `q` with the complete next level. Consequently `ans[i]` is exactly the requested sum for level $i+1$, and the loop continues through the deepest actual level.

The deepest level always contains leaves and therefore begins with a node missing the required child for that parity. Its answer entry is zero, and the following `nq` is empty, ending the traversal.

## Complexity detail

Let $N$ be the number of tree nodes and $W$ the maximum number of nodes on any one level.

Every node is visited once while building a next-level list. A node may also be inspected once during its level's sum scan; early breaks can only reduce that work. Total running time is

$$
O(N).
$$

At one iteration, `q` holds the current level and `nq` holds the next level. Their combined size is bounded by a constant multiple of the tree's maximum width, so the breadth-first auxiliary storage is

$$
O(W).
$$

The returned `ans` contains one integer per tree level. If output storage is included, total additional storage is $O(W+H)$ for tree height $H$. Standard auxiliary-space reporting excludes the required output and gives the manifest's $O(W)$ bound.

The source uses ordinary Python lists rather than repeatedly removing from the front, so there is no hidden $O(W)$ shift per node. It iterates by index and replaces the entire level list after each pass.

## Alternatives and edge cases

- **Deque breadth-first traversal:** A queue with stored level sizes also works, but preserving each full level in a list makes reverse inspection straightforward.
- **Reverse a copied level:** Using `reversed(q)` can express even-level order clearly; the source instead maps index `i` to `m-i-1` without another list.
- **Build children after the stopping scan:** This is incorrect if it gathers children only from contributing nodes, because the stopping condition affects the level sum rather than future traversal.
- **Single-node tree:** The root lacks the required left child at odd level 1, so the result is `[0]`.
- **First node violates:** The level contributes zero, but its existing children and other nodes' children were already gathered for the next level.
- **Violation after several nodes:** Earlier inspected values remain in the sum; the violating node and all later nodes in that direction are excluded.
- **Negative node values:** Included values may make a level sum negative. The stopping rule depends only on child existence, not on values.
- **Odd-level requirement:** Only a left child permits inclusion; having a right child alone is insufficient.
- **Even-level requirement:** Only a right child permits inclusion; having a left child alone is insufficient.
- **Direction toggling:** Parity changes for every actual level, even when the preceding level contributed zero.
- **Nonempty-root contract:** The source initializes `q = [root]` and dereferences its nodes, so it relies on the promised nonempty tree.
- **Platform-provided node type:** `TreeNode` is part of the harness contract; users implement only the `Solution` method.
