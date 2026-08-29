## General

The tree is processed bottom-up. For every node, the source first makes all paths inside each child subtree equal. It then compares the resulting child path scores and raises every deficient child branch to the largest one.

Increasing a child node itself raises every path through that child by the same amount, so one changed node is sufficient for each deficient child subtree.

**Rooting the undirected tree**

The adjacency list stores both directions. An iterative traversal from root zero records:

- `parent`, preventing movement back upward;
- `children[node]`, the rooted child relation;
- `order`, with every parent appearing before its descendants.

Reversing `order` guarantees all children are processed before their parent. This avoids recursion-limit problems on a chain of `10^5` nodes.

**Meaning of best_path**

After node `u` is processed, `best_path[u]` is the common score of every path from `u` to a leaf in its subtree after the minimum-node-count equalization decisions made below `u`.

For a leaf, there is one path consisting only of that leaf, so:

`best_path[u]=cost[u]`.

No change is needed because a single path is already equal to itself.

**Equalizing child branches**

For an internal node, each child `v` already has one common child-to-leaf score `best_path[v]`.

All node-to-leaf paths through child `v` add the same current-node cost, so differences among branches depend only on those child scores.

Because costs may only increase, the final common child contribution cannot be below:

`target=max(best_path[child])`.

Choosing this maximum is sufficient and avoids unnecessary extra amount, although the objective counts changed nodes rather than increment size.

For every child below target, increase that child node’s cost by:

`target-best_path[child]`.

This one increase affects every leaf path in that entire child subtree equally and raises them precisely to target. The source counts one changed node for that child.

Children already at target require no change.

Afterward every path beginning at the current node has common score:

`cost[node]+target`,

which becomes `best_path[node]`.

**Why one changed node per deficient child is optimal**

A deficient child subtree must gain positive total cost on **every** path it contributes. An increase outside that subtree cannot selectively fix it:

- increasing the current node raises all sibling branches equally and preserves their difference;
- increasing another child does not affect this child’s paths.

Therefore at least one node inside each deficient child branch must change.

Increasing the child root itself fixes all of that branch’s paths with exactly one changed node. The lower bound and construction match, so one is minimum.

Different deficient children are disjoint subtrees, so one changed node cannot serve two of them. Their required counts add.

**Why earlier subtree decisions remain valid**

Internal equalization within a child made all of its paths equal. Raising the child root adds the same amount to every one of those paths, preserving equality.

Thus parent-level corrections never invalidate completed descendant work, which is the core optimal-substructure property.

**Example**

If an internal node has child common scores `4,7,7,2`, target is seven. The branches scoring four and two each need one changed node, regardless of their different increment amounts. Raising their child roots by three and five makes all four contributions seven, costing two changed nodes.

## Complexity detail

Adjacency construction and rooting examine `O(n)` tree entries. Bottom-up processing examines every child edge once, so total time is `O(n)`.

Graph, parent, children, order, and best-path arrays all use `O(n)` space. The traversal is iterative, so no recursive stack is added.

## Alternatives and edge cases

- **Recursive postorder:** It expresses the same recurrence but can fail on a maximum-depth Python chain.
- **Increase leaves individually:** This may change many nodes in one deficient subtree; raising its child root fixes every path with one node.
- **Raise the current node:** It adds equally to all branches and cannot remove differences among child scores.
- **Choose a target above the maximum:** It cannot reduce the number of already deficient children and may force maximum branches to change too, so it is never better.
- **Single chain:** Every internal node has one child, so no comparisons differ and answer is zero.
- **Star tree:** Every leaf cost is a child score; all leaves below the maximum each contribute one change.
- **Equal child scores:** No node is counted at that parent.
- **Large increment:** Increment magnitude is unrestricted and does not affect the objective; one node still counts once.
- **Positive costs:** Best paths grow safely; Python integers avoid overflow.
- **Several leaves inside one child:** Their internal equality is already established before the child-root adjustment.
- **Root cost:** Changing it cannot help equalization because it belongs to every root-to-leaf path equally.
- **Tree guarantee:** Parent-only avoidance relies on connected acyclic input.
- **Input preservation:** The source computes conceptual increases but never modifies `cost`.
- **Minimum number versus minimum amount:** The recurrence counts deficient branches, not the numeric sum of increments, exactly matching the requested objective.
