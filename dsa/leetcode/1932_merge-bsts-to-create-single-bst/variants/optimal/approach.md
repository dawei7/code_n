## General

**Identify the only possible final root**

Every merge attaches the root of one small BST at a leaf of another BST with the same value. A root that gets attached therefore appears as a child value somewhere in the input. The root of the final combined tree is the one input root that is never consumed this way, so its value must not appear among any input leaf values.

The solution builds `roots`, a dictionary from every distinct root value to its root node. It also collects the values of every left and right child in `leaf_values`. Because each supplied tree has no grandchildren, those children are leaves in their original trees.

It then selects roots whose values do not occur in `leaf_values`. Exactly one candidate is required. If there are none, every tree appears to need a parent, which would create a cycle or leave no final root. If there are several, those roots cannot be joined beneath one another, so more than one component would remain. Either case returns `None`.

The unique candidate becomes `root`. Its value is removed from `roots` because this tree is already the base of the construction. Every remaining dictionary entry represents a tree that still must be grafted exactly once.

**Traverse, graft, and validate at the same time**

The stack begins with the candidate root and the open bounds negative infinity and positive infinity. Each stack item contains a node and the strict value range allowed at that position.

For a node in a valid BST, every node reached through a left edge must be below its ancestor's value, and every node reached through a right edge must be above it. The test `lower < node.val < upper` checks all ancestor restrictions at once. A left child inherits the same lower bound and receives the current value as its upper bound. A right child receives the current value as its lower bound and inherits the same upper bound.

This global range validation is stronger than checking only parent and child. In the invalid merge where a value is smaller than its parent but still too large for an older ancestor, the propagated bound catches the violation.

Before pushing children, the code checks whether the current node is a leaf and whether its value names an unused root in `roots`. If so, a legal merge is available. It removes that root entry and copies the graft root's left and right child references into the current leaf:

`node.left = graft.left` and `node.right = graft.right`.

The leaf and graft root have the same value, so keeping the existing leaf object and attaching the graft's children is structurally equivalent to replacing the leaf with the graft root. Avoiding a second equal-valued root node also preserves the intended merged tree shape.

The newly attached children are then pushed with bounds derived from the shared root value. Thus their original local BST ordering is checked against every ancestor in the larger tree. A small input tree can be a valid BST by itself yet violate the final tree's wider bounds; this traversal detects exactly that problem.

**Why every tree must be consumed**

Removing a dictionary entry when it is grafted guarantees that an input root can be used at most once. When traversal ends, `not roots` is required. If entries remain, those trees were never reached through a matching leaf of the chosen component, so fewer than $n-1$ merges occurred. Returning the partly built tree would be wrong even if that component is internally a valid BST.

Conversely, if the stack completes without a bound violation and the dictionary is empty, all noncandidate trees were attached once, all nodes belong to the one candidate-rooted structure, and strict global BST ordering holds. The method can safely return the candidate root.

**Why the greedy graft is forced**

At a leaf with value $v$, the only input tree that can legally replace it is the tree whose root value is $v$. Root values are unique, so there is no choice among competing grafts. Likewise, a non-leaf cannot be a merge location. The algorithm is not making a risky local optimization; it is executing every merge that the rules force while checking whether the forced construction remains valid.

The source mutates node links during this process. If a later violation makes it return `None`, some earlier grafts may already have changed the supplied trees. That side effect is part of the exact implementation.

## Complexity detail

Let $K$ be the number of input trees and $T$ the total number of input node occurrences. Here $T\le3K$ before overlapping roots are merged.

Building `roots` and `leaf_values` takes $O(K)$ time. Selecting candidates takes $O(K)$. During traversal, each reachable node position in the merged structure is popped once, every dictionary lookup or removal is expected $O(1)$, and each edge is followed once. Total expected time is $O(T)$.

The root dictionary and leaf-value set each hold $O(K)$ entries. The explicit depth-first stack holds $O(H)$ nodes for a tree of height $H$ in the usual binary-tree DFS bound. Thus auxiliary space is $O(K+H)$, matching the manifest. The traversal is iterative, so it avoids Python recursion-depth failure on a tall merged BST.

## Alternatives and edge cases

- **Merge first, validate later:** This can work, but combining grafting with bound validation avoids a second full traversal and rejects violations as soon as they are reached.
- **Only compare each child to its parent:** That is insufficient for BST validity. A descendant can satisfy its parent relation while violating an ancestor bound.
- **Inorder traversal validation:** After constructing a single tree, strict increasing inorder values can validate the BST. It requires the same linear traversal but does not catch problems during grafting.
- **Several root candidates:** They represent disconnected components that cannot all be consumed, so the method correctly returns `None`.
- **No root candidate:** A final rooted tree cannot exist; matching relationships may form a cycle.
- **One input tree:** Its root is the unique candidate, the remaining-root dictionary becomes empty, and the range traversal returns it because input trees are already valid BSTs.
- **Matching value at a non-leaf:** Merges are allowed only at leaves. The code deliberately grafts only when both children are `None`.
- **Tree valid locally but invalid globally:** Propagated lower and upper bounds catch a graft whose descendants cross an ancestor's boundary.
- **Unused tree after traversal:** A nonempty `roots` dictionary proves that not all $n-1$ required merges happened.
- **Duplicate root values:** The contract excludes them; the dictionary relies on that guarantee.
- **Strict inequality:** Equal values elsewhere violate the BST definition, and the open-bound check rejects them.
- **Mutation on failure:** Earlier leaf nodes may have acquired children before a later error is discovered. The exact function does not roll those changes back.
