## General

**Cousins require two independent facts**

Two target nodes are cousins only when:

1. their depths are equal;
2. their parent nodes are different.

Checking only depth would incorrectly classify siblings as cousins. Checking only parents would incorrectly accept nodes on different levels. The algorithm performs a breadth-first traversal and records both pieces of information for each target.

Breadth-first search is a natural fit because it processes the tree level by level. The current level counter is the depth shared by every node removed during one outer-loop iteration.

**Carry each node together with its parent**

The queue begins as

`deque([(root, None)])`.

The root is at depth zero and has no parent, represented by `None`. Whenever the traversal enqueues a child, it stores the current node beside that child:

`q.append((node.left, node))` or `q.append((node.right, node))`.

When the child is later removed from the queue, its parent information is immediately available. There is no need for a separate map from node values to parents.

The queue stores parent node objects, not merely parent values. Since every tree node is a distinct object and values are unique, object identity correctly determines whether two targets share the same immediate parent.

**Freeze one BFS level with `len(q)`**

At the beginning of an outer `while q` iteration, the queue contains exactly the nodes at the current depth. The loop

`for _ in range(len(q))`

evaluates `len(q)` once when the `range` is created. Children appended during that loop are not included in the current iteration; they wait in the queue for the next depth.

This detail preserves level boundaries without inserting sentinel markers. After all nodes from the frozen count are processed, `depth += 1` advances to the next level.

**Record each target when encountered**

If `node.val == x`, the code stores the current `parent` and `depth` in `p1` and `d1`. The `elif node.val == y` branch stores `p2` and `d2`.

The contract guarantees unique node values and `x != y`, so one node can match at most one branch. It also guarantees that both target values exist, so all four recorded variables will have their intended values by the end of traversal.

The traversal continues after finding a target. The exact implementation favors a simple complete BFS over early-exit logic, and with at most one hundred nodes the extra work is small.

**Trace siblings versus cousins**

Suppose `x` and `y` are the left and right children of the same node at depth one. BFS records the same parent object for both and equal depths. The return condition fails because `p1 != p2` is false. They are siblings, not cousins.

Now suppose the targets lie at depth two under different depth-one nodes. They are processed in the same BFS level, so `d1 == d2`. Their parent objects differ, so `p1 != p2`. Both conditions hold and the method returns `True`.

If one target is found at depth one and the other at depth two, their parents may differ, but `d1 == d2` is false. They are not cousins.

**Why parent comparison must use the immediate parent**

Two nodes can share a grandparent and still be cousins, while siblings share the same direct parent. Storing the immediate parent at enqueue time distinguishes precisely those cases.

Comparing only whether targets appear in different left/right subtrees of the root would be insufficient because cousins can occur deeper within the same major subtree under different parents.

**The queue and depth invariant**

At the start of each outer iteration, every queued pair contains a node at the current `depth` and that node's correct immediate parent. This is true initially for the root.

When processing this level, every existing child is enqueued with the current node as its parent. All such children lie exactly one level deeper. Because the current loop consumes only its frozen initial queue length, the queue after the loop contains precisely those next-depth pairs. Incrementing `depth` re-establishes the invariant.

Therefore, whenever either target is encountered, both its recorded parent and depth are correct.

**Why the final Boolean is exact**

If the method returns true, `d1 == d2` proves the target nodes occupy the same depth, and `p1 != p2` proves their immediate parents differ. These are exactly the definition's two conditions, so they are cousins.

Conversely, if the target nodes are cousins, the invariant ensures BFS records their common depth and their distinct parents. Both comparisons are then true. If they are not cousins, at least one defining condition fails, and the corresponding comparison makes the return value false.

**Root-related behavior**

If one target is the root, its parent is `None` and its depth is zero. The other target is different and therefore lies below the root at positive depth. Even though the parent objects differ, the depth check rejects the pair. The constraints prevent both different targets from occupying depth zero.

The initial values `p1 = p2 = None` and `d1 = d2 = None` are safe because both targets are guaranteed to exist. Without that guarantee, two missing targets could make both equality comparisons behave misleadingly; a more general API would need an explicit found check.

## Complexity detail

Let `N` be the number of nodes and `W` the maximum number of nodes on one tree level.

Every node is enqueued once, dequeued once, and processed with constant work. Total time is `O(N)`.

The queue holds at most `O(W)` node-parent pairs, which is `O(N)` in the worst case for a wide tree. The stored target data and depth counter use `O(1)` additional space. Thus auxiliary space is `O(N)` in the worst case.

The traversal is iterative, so tree height does not create recursive call-stack usage.

## Alternatives and edge cases

- **Depth-first search:** Traverse recursively while carrying parent and depth, then compare the two recorded results. It has the same `O(N)` time but uses call-stack space proportional to tree height.
- **Stop after the first relevant level:** Once one target appears in a BFS level, search only the rest of that level and return false if the other is absent. This can avoid deeper traversal but adds control-flow complexity.
- **Sibling check while enqueueing:** Detect whether one parent directly owns both target children. This handles the parent condition, but depth equality still requires level-aware traversal.
- **Store parent values:** Unique node values make this possible, but storing node references works directly and does not rely on numeric encoding.
- **Sibling targets:** They have equal depth but the same parent, so the result is false.
- **Different-depth targets:** The depth comparison rejects them regardless of their parent identities.
- **Targets in opposite root subtrees:** They are cousins only if their depths match; merely being on opposite sides is not enough.
- **One target is the root:** Its depth zero cannot match any different node's depth.
- **Nodes with one child:** The existing child is enqueued normally, and absent children contribute nothing.
- **Unique-value guarantee:** It ensures each target is found exactly once and makes the `if`/`elif` structure unambiguous.
- **Nonempty tree guarantee:** The initial queue contains a real root, so the code safely reads `node.val`.
