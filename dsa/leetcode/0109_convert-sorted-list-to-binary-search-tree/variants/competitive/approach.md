## General

The intended competitive algorithm constructs the tree while consuming the sorted linked list exactly once. It uses an important connection: a binary search tree's inorder traversal visits values in ascending order, and the input list already supplies values in that same order.

Instead of repeatedly searching the linked list for middle nodes, the algorithm first learns only the list's length. Numeric interval boundaries determine the balanced tree's shape. A shared pointer then supplies values precisely when an inorder traversal would visit each root.

The protected source contains a Python-version defect in its midpoint expression. The algorithmic explanation below describes the construction the code is clearly intended to implement, then identifies why the exact file does not realize it under Python 3.

**First pass: count rather than copy**

`sortedListToBST` walks `current` from `head` to `None` and increments `length`. This costs one visit per list node but stores no array of values. After the pass, it resets the construction cursor with `self.head = head`.

The helper is called as `sortedListToBSTRecu(0, length)`. Its boundaries form a half-open interval `[start, end)`, so the number of tree positions to construct is `end - start`. When `start == end`, that number is zero and the helper returns `None`.

These indices describe positions in the future inorder traversal. They are not used to index the linked list. Their purpose is to split a known number of positions into balanced left and right subtree sizes.

**Why the left subtree must be built before the root**

For a nonempty interval, an integer midpoint divides its inorder positions. The helper recursively constructs `[start, mid)` first. That call consumes exactly the values meant for the current root's left subtree.

When the left call returns, `self.head` points at the first unconsumed list node. Because the list is ascending and all earlier values were assigned to the left subtree, this node's value is exactly the inorder value for the current root. The code creates `TreeNode(self.head.val)`, attaches the completed left subtree, and advances `self.head` once.

Only then does it construct `[mid + 1, end)`. Those later list values are larger and become the right subtree. The execution order is therefore left subtree, root, right subtree—the definition of inorder traversal.

This order is not an implementation detail that can be rearranged freely. If the source created and consumed the root before the left recursive call, the smallest available value would be placed too high and the generated values would follow preorder rather than inorder positions.

**The moving-pointer invariant**

At the start of a helper call for `[start, end)`, `self.head` points to the first unconsumed value assigned to that interval in inorder order.

The left call consumes exactly `mid - start` values. The current pointer then identifies the root value and advances once. The right call consumes the remaining `end - (mid + 1)` values. Altogether, the call consumes

$$
(\texttt{mid}-\texttt{start})+1+
(\texttt{end}-\texttt{mid}-1)
=\texttt{end}-\texttt{start}
$$

values, exactly matching the interval size. It leaves the cursor at the first value belonging after this entire subtree.

Starting from the complete interval and applying this reasoning recursively shows that every list node is consumed once, in order, and assigned to exactly one tree node. Since earlier consumed values go left and later values go right, the tree satisfies strict binary-search-tree ordering.

**Why the numeric shape is balanced**

With an integer midpoint, the left and right half-open intervals differ in size by at most one. Both recursively use the same split. Their constructed heights therefore differ by at most one at every root, giving a height-balanced tree.

The source does not need random access to find a physical middle list node. The midpoint controls how many nodes the left construction consumes; once it has consumed that many, the shared pointer has arrived at the logical middle automatically.

For `[-10, -3, 0, 5, 9]`, the length is five and the initial integer midpoint is two. The left call consumes `-10` and `-3`, then the root consumes zero, and the right call consumes `5` and `9`. The precise lower-level shape depends on the midpoint convention, but inorder traversal is the original list and the split sizes maintain balance.

**The exact Python 3 defect**

The line `mid = start + (end - start) / 2` uses `/`. In Python 2 with integer operands, `/` performed the intended integer division. In Python 3, `/` always produces a floating-point value. For example, `[0, 5)` gets `mid = 2.5`, not integer index two.

The recursive boundaries then become floats such as `[0, 2.5)` and `[0, 1.25)`. The `start == end` base case no longer corresponds to reducing an integer interval by whole positions. Recursion can continue through fractional ranges instead of making one call per intended node, and it can reach Python's recursion limit rather than construct the answer.

The minimal semantic repair is integer division: `mid = start + (end - start) // 2`. With that correction, the interval sizes, cursor invariant, and complexity claims all hold. Because the campaign preserves protected solutions, this document records the defect rather than modifying the source.

The file defines `head` as a class attribute and then assigns `self.head`, which creates or replaces an instance attribute for the active call. A new public invocation resets it. Nevertheless, this mutable cursor means calls on the same `Solution` instance are not reentrant or safe to interleave.

## Complexity detail

For the intended integer-midpoint implementation, the initial length pass visits all $n$ list nodes once. The recursive construction creates $n$ tree nodes and advances `self.head` exactly $n$ times. Each call performs constant work besides its children, so total time is $O(n)$.

Balanced numeric splitting makes the deepest active recursion path $O(\log n)$. Apart from that stack and a constant number of references and integers, no auxiliary structure grows with the input. The intended auxiliary-space complexity is therefore $O(\log n)$.

The returned tree has $n$ nodes and uses $O(n)$ output space, conventionally excluded from the auxiliary bound. Unlike the Optimal branch's exact source, this method does not allocate an $n$-element value array.

Those bounds do not truthfully describe execution of the protected file under Python 3. Floating midpoint boundaries invalidate the one-call-per-position recurrence and may cause a `RecursionError`. Complexity is only meaningfully stated for the intended Python-2 semantics or after replacing `/` with `//`.

## Alternatives and edge cases

- **Integer-division repair:** Replace `/ 2` with `// 2`. This is necessary for the intended algorithm under Python 3 and preserves $O(n)$ time and $O(\log n)$ auxiliary space.
- **Copy values to an array:** Convert the list to indexed storage and use midpoint recursion. It is straightforward and linear-time but requires $O(n)$ auxiliary memory.
- **Slow/fast pointer at every subtree:** Find and split around each physical middle node. It can avoid the array but costs $O(n\log n)$ time because each recursive level rescans nodes.
- **Destructive midpoint splitting:** Severing `next` links isolates sublists but changes the caller's data and does not remove repeated middle searches.
- **Upper-middle interval choice:** A consistent upper-middle split produces a different valid balanced tree. The cursor consumption counts must be adjusted consistently with that shape.
- **Empty list:** The length is zero, so `[0, 0)` returns `None` without dereferencing `self.head`.
- **One list node:** With correct integer division, the left interval is empty, the sole value becomes the root, and the right interval is empty.
- **Even number of nodes:** Either middle can serve as the root. A deterministic integer convention keeps child sizes within one.
- **Strict ascending values:** Every newly consumed root is greater than all values consumed for its left subtree and smaller than every value reserved for its right subtree.
- **Shared cursor ordering:** The cursor must advance exactly once after the left call and before the right call. Moving either operation breaks the inorder mapping.
- **Repeated public calls:** `sortedListToBST` resets `self.head`, so sequential calls can work after the division fix; nested or concurrent calls on one instance can corrupt shared state.
- **Recursion depth:** The intended balanced construction is logarithmic. The floating-point defect destroys that guarantee and may recurse far more deeply.
- **Locally defined node classes:** The file supplies conventional `TreeNode` and `ListNode` classes. Returned tree nodes expose the expected `val`, `left`, and `right` fields.
- **Manifest interpretation:** The manifest's bounds match the repaired inorder-simulation algorithm, not the exact Python 3 behavior of the unmodified `/` expression.
