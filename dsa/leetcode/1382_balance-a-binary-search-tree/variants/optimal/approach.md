## General

**Separate preserving order from choosing shape**

A binary search tree's inorder traversal visits values in sorted order: recursively visit the left subtree, then the node, then the right subtree. The exact solution first extracts this sorted sequence and then builds an entirely new tree whose shape is balanced.

This separation simplifies the problem. The inorder phase preserves every value and the BST ordering information. The construction phase can then choose middle values as roots without worrying about the original, possibly skewed shape.

**Collecting the sorted values**

The nested `dfs(root)` returns for a null child. For every real node, it visits `root.left`, appends `root.val` to `nums`, and visits `root.right`. Because the input is a BST, every left-subtree value is smaller than the node and every right-subtree value is larger. Applying that fact recursively makes `nums` strictly increasing.

Each original node is appended exactly once, so the list contains precisely the same multiset of values as the input. Under the normal strict-BST definition there are no duplicates, but the construction's ordering reasoning would also preserve nondecreasing order if a consistent duplicate policy existed.

For a right-skewed tree with values 1, 2, 3, and 4, inorder traversal yields `[1, 2, 3, 4]` even though the original height is four nodes. The list deliberately forgets that poor shape.

**What `build(i, j)` means**

The second helper returns a balanced BST containing exactly the sorted values from indices `i` through `j`, inclusive. If `i > j`, the range is empty and the correct subtree is `None`.

For a nonempty range, `mid = (i + j) >> 1` computes the floor of $(i+j)/2$, using a right shift as integer division by two. `nums[mid]` becomes the subtree root. All earlier range values go into
`build(i, mid - 1)`, and all later values go into `build(mid + 1, j)`.

The exact code recursively constructs `left` and `right` first, then returns `TreeNode(nums[mid], left, right)`. Creating the parent before or after its children would produce the same final links; this order simply makes both completed subtrees available to the constructor.

**Why choosing the midpoint preserves the BST property**

Since `nums` is sorted, every value in indices `i` through `mid - 1` is smaller than `nums[mid]`, and every value in `mid + 1` through `j` is greater. By recursively applying the same rule, the returned left and right structures are themselves BSTs. Attaching them under the middle value therefore creates a valid BST for the whole range.

**Why choosing the midpoint guarantees balance**

The number of indices on the two sides of the floor midpoint differs by at most one. Thus the left and right recursive problems contain either equal numbers of values or sizes differing by one.

More importantly, each recursive call repeats the midpoint split. A subtree built from $q$ sorted values has height determined by repeatedly halving $q$. Its two child ranges have nearly equal sizes and consequently heights that differ by at most one. By induction over range size, every constructed node satisfies the balance requirement, not only the root.

For four values, the lower midpoint index one selects value 2. The left range contains value 1, while the right range contains 3 and 4. Their heights differ by one, which is valid. Choosing the upper middle value 3 would also produce a valid answer; the problem allows any balanced result.

**Why constructing new nodes is allowed**

The requirement asks for a balanced BST with the same node values, not the same node identities. The exact method creates new `TreeNode` objects and leaves the original tree unchanged. This is different from rotation-based methods that reuse and rewire existing nodes, but both satisfy the value-and-shape contract.

**Why the complete algorithm is correct**

Inorder traversal records every input value exactly once and in increasing order. For any range, midpoint construction places all smaller range values in the left recursively valid BST and all larger values in the right recursively valid BST, proving the output remains a BST with exactly the same values. Nearly equal range splits recursively guarantee child heights differ by at most one at every node. Therefore `build(0, len(nums) - 1)` returns a balanced BST containing precisely the original values.

## Complexity detail

Let $N$ be the number of nodes and $H$ the original tree height. Inorder DFS visits every original node once, taking $O(N)$ time. Construction creates one new node per list value, also $O(N)$. Total time is $O(N)$.

`nums` uses $O(N)$ space, and the newly returned tree itself contains $N$ nodes. The inorder recursion can reach $O(H)$ frames, which is $O(N)$ for a skewed input. The construction recursion has only $O(\log N)$ depth because it builds balanced ranges. Auxiliary storage is therefore $O(N)$ overall, matching the manifest.

## Alternatives and edge cases

- **Day–Stout–Warren rotations:** Convert the existing tree into a right vine and rotate it into balance in $O(N)$ time with $O(1)$ auxiliary pointer storage. It is space-efficient but much harder to implement and mutates the tree.
- **Reuse node references from inorder traversal:** Store nodes rather than values and reconnect them around midpoints. This avoids allocating new nodes but must carefully overwrite old child pointers.
- **Repeated AVL insertion:** Insert sorted or original values into a self-balancing tree. It works but costs $O(N\log N)$ rather than exploiting the already sorted inorder sequence.
- **Already balanced input:** The method may return a different but still valid balanced tree; preserving the exact original shape is not required.
- **Single node:** The only index becomes the midpoint and both child ranges are empty.
- **Even number of nodes:** The lower midpoint is chosen by floor division; the two child sizes differ by one and remain balanced.
- **Severely skewed input:** Values are recovered correctly, but recursive inorder traversal may exceed Python's recursion limit at up to 10,000 nodes.
- **Iterative inorder traversal:** An explicit stack avoids that recursion-limit risk while producing the same sorted list.
- **Original tree identity:** New nodes are returned, so external references to original nodes do not point into the balanced result.
- **Original tree mutation:** The code only reads original pointers and values; it leaves the input unchanged.
- **Null root outside the contract:** `dfs` leaves `nums` empty and `build(0, -1)` returns `None`.
- **Bit shift midpoint:** `(i + j) >> 1` is floor integer division by two for the nonnegative indices used here.
