## General

A binary search tree gives every node a strict ordering rule:

- every value in its left subtree is smaller than the node's value;
- every value in its right subtree is larger.

The value to insert is guaranteed not to be present already. The solution follows the one root-to-leaf path on which that value is allowed to appear, creates a node when it reaches an empty child position, and reconnects the returned subtree while recursion unwinds.

**Why only one branch can contain the insertion position**

At a current node `root`, compare `val` with `root.val`.

If `val < root.val`, placing `val` anywhere in the right subtree would violate the BST rule because every right-subtree value must be greater than `root.val`. The only possible region is the left subtree.

If `val > root.val`, the symmetric reasoning leaves only the right subtree.

The code writes the first comparison as `root.val > val`. Equality needs no branch because the source guarantees `val` is new.

This branch choice is repeated at every visited node, narrowing the legal region until it becomes an empty subtree.

**The recursive contract**

`insertIntoBST(root, val)` returns the root of a valid BST that contains:

- every node that was in the input subtree rooted at `root`; and
- exactly one new node whose value is `val`.

This contract explains why every call returns a node reference and why the caller assigns that return value back into a child field.

**The empty-subtree base case**

When `root is None`, the legal search path has reached an unused child link. The method returns `TreeNode(val)`.

The new node begins with no children. A one-node tree is a valid BST, so the recursive contract holds for the base case. This is the only place a node is allocated, ensuring insertion happens exactly once.

If the original tree itself is empty, the initial call immediately takes this base case and the new node becomes the returned root.

**Reconnecting the changed subtree**

Suppose `val < root.val`. The recursive call inserts into the left subtree and returns the root of that updated subtree. The assignment

`root.left = self.insertIntoBST(root.left, val)`

stores that returned root in the current node's left link.

This assignment is essential. When `root.left` was originally `None`, the recursive call returns a newly allocated node; without assignment, that node would not become reachable from the tree.

When the subtree was nonempty, the recursive call normally returns its same root object after modifying a deeper link. Assigning it again is still correct and makes the recursive contract uniform.

The right-side assignment has the identical role when `val > root.val`.

**Why each call returns `root`**

After its chosen child subtree has been updated, the current node remains the root of this entire subtree. The insertion does not rotate nodes or replace an existing non-null root.

Returning `root` passes the updated subtree back to the caller. Eventually, the original top-level root is returned unchanged as an object reference unless the original tree was empty.

The return statements form a chain:

- the empty position returns the new node;
- its parent stores that node and returns itself;
- each ancestor stores its returned child and returns itself;
- the caller receives the root of the complete updated tree.

**A trace**

Insert `5` into a BST rooted at `4` whose right child is `7`.

- At `4`, `5 > 4`, so recurse right.
- At `7`, `5 < 7`, so recurse left.
- The left child of `7` is empty, so create and return node `5`.
- The `7` call assigns that node to `7.left` and returns `7`.
- The `4` call assigns the returned `7` subtree to `4.right` and returns `4`.

The new value is greater than every ancestor where the path went right and smaller than every ancestor where it went left, so it fits all accumulated bounds.

**Why inserting at the first empty position is valid**

The comparisons along the path impose a lower and upper bound on every legal value in the current subtree. At the reached empty child, `val` satisfies all those bounds because each branch was selected from its comparison.

Creating a leaf introduces no descendants that could violate ordering. All subtrees not on the path remain untouched, and every path ancestor keeps the new value on its correct side.

Therefore, the whole tree remains a BST.

**Why the algorithm is complete and correct**

At each non-null node, exactly one child subtree can legally contain `val`. The algorithm chooses that child, so it never discards a valid insertion location. A finite tree's chosen path eventually reaches `None`, where a new node is created.

The base case creates exactly the required value. On return, each ancestor reconnects a valid updated child on the side justified by the comparison. By induction from the new leaf to the original root, every returned subtree is a valid BST containing all original nodes plus the new one.

The contract permits multiple valid output trees, but the standard leaf insertion used here is one accepted choice and does not require restructuring.

## Complexity detail

Let `h` be the number of nodes on the followed root-to-empty path, proportional to the tree height.

The algorithm visits one node per level and performs constant work there. Its running time is

$$
O(h).
$$

For a balanced BST, `h = O(\log n)`. For a completely skewed BST, `h = O(n)`.

The exact implementation is recursive. It keeps one call frame for every visited level until the new node is returned, so auxiliary stack space is

$$
O(h).
$$

Only the one required output node is newly allocated. An iterative implementation could achieve `O(1)` auxiliary space, but that constant-space claim does not describe this literal recursive source.

## Alternatives and edge cases

- **Iterative descent:** Walk with a current pointer until the required child is null, attach the new node there, and return the original root. It has the same `O(h)` time and `O(1)` auxiliary space.

- **Tree rebuilding:** Constructing a new copy is unnecessary because the contract permits in-place link changes and only one path is affected.

- **Empty tree:** The base case creates the only node and returns it as the new root.

- **Insert smaller than every node:** The path repeatedly goes left and adds the value beneath the current minimum.

- **Insert larger than every node:** The path repeatedly goes right and adds the value beneath the current maximum.

- **Unique-value guarantee:** No equality branch is required. If duplicates were allowed, the implementation would need a stated placement policy.

- **Original root identity:** A nonempty tree returns the same top-level object, though one descendant link changes.

- **Skewed tree:** Time and recursion depth become linear, and a very deep tree can exceed Python's recursion limit.

- **Negative values:** Only comparisons matter, so negative and positive values behave identically.

- **Child assignment:** Calling recursion without assigning its return would lose a new node created at an empty child.

- **Exactly one allocation:** Every non-null call chooses one branch; only the first null call creates a node, so duplicates cannot be inserted accidentally.
