## General

A quad-tree leaf represents a uniform square: every cell is either zero or one. An internal node represents four equally sized quadrants. Logical OR can therefore be computed recursively without expanding either tree into a matrix.

The helper `dfs(t1, t2)` returns a quad tree representing the OR of the two regions described by `t1` and `t2`.

**Both regions are uniform.** If both nodes are leaves, every cell in each represented region has its node's Boolean value. Their OR is uniform too, so the method returns one leaf whose value is:

`t1.val or t2.val`.

No children are needed because the result region contains one repeated value.

**One region is a true leaf.** If `t1` is a leaf with value true, every cell in its region is one. One OR anything is one, so the result is exactly that true leaf and no recursion into `t2` is necessary.

The code returns `t1 if t1.val else t2`. Thus when `t1` is false, zero OR the other region equals the other region, and the complete `t2` subtree can be returned unchanged.

The symmetric branch applies the same identity when `t2` is the leaf:

- true dominates and is returned;
- false is the identity, so `t1` is returned.

These short-circuit rules are the tree equivalent of Boolean identities:

$$
1\lor x=1,\qquad 0\lor x=x.
$$

They can skip a large subtree when one input region is uniform.

**Both regions are subdivided.** When neither node is a leaf, corresponding quadrants cover the same coordinates. The method recursively ORs:

- top-left with top-left;
- top-right with top-right;
- bottom-left with bottom-left;
- bottom-right with bottom-right.

The four returned quadrant roots are attached to a new internal result node `res`.

Cross-pairing quadrants would combine different matrix coordinates and be incorrect. The shared valid-grid size guarantee ensures corresponding nodes represent equal-sized regions at this recursive level.

**Compress a uniform result.** Recursive OR may make all four result quadrants identical uniform leaves. A valid canonical quad tree should then represent the whole region with one leaf instead of an unnecessary internal node.

The code checks two facts:

- every child has `isLeaf == True`;
- all four child values are equal.

Only when both hold can the parent region be uniform. It then assigns `res = res.topLeft`, reusing one of those equivalent leaves.

Equal `val` fields on internal children would not be sufficient, because the problem permits arbitrary internal-node values. The `isLeaf` checks are essential.

**Why returning an existing subtree is safe.** In the true/false short-circuit cases and compression, the method may return a node already belonging to one input. It never mutates returned nodes or either input tree, so structural sharing does not change their meaning. The contract asks for a representing tree, not a deep copy.

For two false leaves, the both-leaf branch returns false. For false leaf OR a complex tree, it returns the complex tree because every matrix bit stays unchanged. For true leaf OR any tree, it returns true immediately.

**Why every output cell has the correct value.** The proof follows node structure. Leaf cases apply Boolean OR to uniform regions exactly. Internal cases divide the region into four disjoint quadrants and recursively compute each corresponding OR. Those quadrants cover the entire region, so their parent represents the complete cellwise result. Compression changes representation only when all quadrant cells share one value.

**Why recursion terminates.** Each non-short-circuited internal call descends one tree level into smaller quadrants. Valid quad trees eventually reach leaves, where a base case returns.

The exact platform `Node` constructor is assumed to support the argument forms used by the accepted solution: a value/is-leaf leaf construction and an empty internal construction whose children are assigned afterward.

## Complexity detail

Let $q$ be the number of paired node regions actually visited. Each call performs constant work besides up to four recursive calls, so time is $O(q)$. Short-circuiting can make $q$ much smaller than the total nodes in both inputs; worst case visits corresponding structure throughout.

The recursion stack depth is the quad-tree height $h$, giving $O(h)$ auxiliary stack space, matching the manifest. Newly created output nodes are output storage and can total $O(q)$.

Reused input subtrees reduce allocation but do not change the worst-case traversal bound.

## Alternatives and edge cases

- **Expand to matrices:** OR every cell and rebuild a tree. It wastes space proportional to grid area and ignores compression already present.
- **Always recurse through a true leaf:** This is correct but discards the strongest short-circuit and performs unnecessary work.
- **Compare internal `val` fields:** Their values are semantically irrelevant; uniformity requires leaf status.
- **Both false leaves:** Return one false leaf.
- **Both true leaves:** Return one true leaf.
- **True leaf with internal node:** True dominates the entire region.
- **False leaf with internal node:** The internal subtree is already the result.
- **Four equal result leaves:** Collapse them into one leaf.
- **Four unequal or internal children:** Keep the internal result node.
- **Input sharing:** Safe because no returned subtree is mutated.
- **Maximum grid depth:** Recursion is bounded by the power-of-two grid exponent.
