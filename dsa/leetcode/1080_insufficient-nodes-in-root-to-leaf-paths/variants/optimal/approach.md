## General

**Pass the remaining sum requirement down the tree**

A node is sufficient when at least one original root-to-leaf path through it has total sum at least `limit`. It is insufficient only when every such path falls short.

Instead of carrying the full path sum, the recursion carries how much more sum is still required. On entering a node:

```python
limit -= root.val
```

The local `limit` now means the minimum additional sum that must be supplied by descendants.

If the original requirement is ten and the path through the current node has accumulated seven, the remaining requirement is three. If it becomes zero or negative, the path has already reached the threshold, though it must still end at an original leaf to define a root-to-leaf path.

Each recursive call receives its own integer value, so changes in one branch do not affect its sibling.

**Handle a missing subtree**

The first condition is:

```python
if root is None:
    return None
```

A missing child contains no root-to-leaf path and cannot make its parent sufficient. Returning `None` also lets the parent assign the pruned result directly to its child pointer.

Although the problem supplies a nonempty original tree, recursive calls naturally reach missing left or right children.

**Decide an original leaf directly**

After subtracting the leaf value:

```python
if root.left is None and root.right is None:
    return None if limit > 0 else root
```

An original leaf completes one root-to-leaf path. If the remaining requirement is positive, the accumulated path sum is strictly below the original threshold, so the leaf is insufficient and is removed.

If `limit <= 0`, the path sum is at least the threshold. Equality is sufficient because the definition removes only paths whose sum is strictly less than `limit`.

This check happens before recursive pruning, so it recognizes leaves from the original tree structure.

**Prune both subtrees before deciding an internal node**

For a non-leaf:

```python
root.left = self.sufficientSubset(root.left, limit)
root.right = self.sufficientSubset(root.right, limit)
```

Each child call removes all nodes in that subtree that do not belong to any sufficient path through the child. The returned root is either a surviving pruned subtree or `None`.

Assigning the results back mutates the existing tree in place. Surviving node objects are reused; removed connections are replaced with `None`.

**Keep an internal node if either child preserves a sufficient path**

After both recursive calls:

```python
return None if root.left is None and root.right is None else root
```

If at least one child survives, that child contains a leaf reachable by a path meeting the remaining requirement. Extending that path through the current node proves the current node lies on a sufficient root-to-leaf path, so it must remain.

If both children disappear, every original descendant path through this internal node was insufficient. The node is therefore insufficient too and returns `None`.

The code does not retest the remaining numeric limit when an internal node becomes childless after pruning. That is correct: it was not an original leaf, and all of its original root-to-leaf continuations have already been proven insufficient. A newly exposed node cannot create a new qualifying original path merely because its children were deleted.

**Why this models simultaneous deletion**

The problem describes deleting all insufficient nodes simultaneously. A careless repeated process might treat nodes exposed as new leaves differently from their original paths.

This postorder recursion bases decisions on whether any original descendant leaf yields a sufficient path. Children are evaluated first, and an internal node survives exactly when one child contains such a path. This computes the simultaneous definition directly, even though pointer updates happen sequentially during recursion.


For each call, the returned subtree contains exactly those nodes in the input subtree that lie on at least one path from the current node to an original leaf whose values meet the remaining requirement.

At a leaf, the numeric comparison establishes that statement directly.

At an internal node, the recursive assumption makes each returned child exact. If neither child survives, no qualifying path exists and returning `None` is correct. If one survives, joining the current node to that child's qualifying path proves the current node and surviving branch are correct.

Applying this reasoning at the original root proves the returned tree contains exactly the sufficient nodes.

**Negative values and limits**

Node values may be negative. Subtracting a negative value increases the remaining requirement, correctly reflecting that the path sum decreased.

A negative `limit` does not mean every node automatically survives. A sufficiently negative path can still fall below it. The same remaining-requirement arithmetic handles all signs.

## Complexity detail

Let `n` be the number of tree nodes and `h` the tree height.

Every non-null node is visited once and performs constant work besides its recursive calls. Total time is `O(n)`.

The recursion stack holds at most one frame per level, using `O(h)` auxiliary space. A balanced tree has `O(log n)` height, while a skewed tree can have `h = n`. The manifest's worst-case space bound is therefore `O(n)`.

The algorithm reuses tree nodes and allocates no second tree.

## Alternatives and edge cases

- **Carry accumulated sum instead:** Pass the root-to-current sum and compare it with `limit` at leaves. It is equivalent to carrying the remaining requirement.
- **Compute best descendant path sum:** A postorder function can return the maximum current-to-leaf sum and prune when the root prefix plus that maximum is too small. It requires careful original-leaf handling.
- **Single sufficient root:** If the root is an original leaf and its value meets the limit, it is returned.
- **Single insufficient root:** If its value is below the limit, the result is `None`.
- **Only one child:** The node survives exactly when that one subtree contains a sufficient path.
- **One surviving branch:** The other pointer becomes `None` while the node and sufficient branch remain.
- **Both branches pruned:** The internal node is pruned too, regardless of becoming a new leaf.
- **Path sum equals limit:** It survives because only strictly smaller sums are insufficient.
- **Negative node:** Remaining requirement increases after subtracting it.
- **Very negative limit:** Arithmetic remains unchanged; actual path sums still determine survival.
- **Root removal:** Returning `None` is valid when every root-to-leaf path is insufficient.
- **Mutation:** The function rewires child pointers of the provided tree. Callers needing the original tree must clone it beforehand.
- **Deep skewed tree:** Recursive depth can approach 5000 and may require an iterative postorder implementation or a higher recursion limit in environments with shallow stacks.
