## General

**Flatten first, then move a pointer**

The checked-in iterator performs all tree traversal during construction. It stores the binary search tree’s inorder sequence in `self.nums` and then represents the iterator’s current position with integer `self.i`.

This separates the problem into two simple stages:

- recursively traverse the tree once in inorder;
- answer every iterator operation with an array boundary check or a one-step index move.

The approach favors extremely simple $O(1)$ operations after initialization. It does not implement the follow-up that asks to avoid precalculating all values; that alternative requires a lazy traversal stack.

**Why inorder is the required sequence**

For any binary search tree node, every value in its left subtree comes before the node in sorted traversal order, and every value in its right subtree comes after it. Inorder traversal visits:

1. the left subtree;
2. the current node;
3. the right subtree.

The nested `dfs` function follows exactly that order. If `root is None`, it returns immediately because an empty subtree contributes no value. Otherwise, it recursively visits `root.left`, appends `root.val` to `self.nums`, and recursively visits `root.right`.

By induction on each subtree, the appended values are the complete inorder traversal. For a BST, that is the iterator order expected by the interface. The methods do not need to inspect tree links again because `self.nums` is now a random-access representation of the full traversal.

**The initial pointer position**

After traversal, the constructor assigns `self.i = -1`. Index negative one is used conceptually as a sentinel position before the first element. It represents the required non-existent value smaller than every BST element.

The code does not read `self.nums[-1]` at initialization. Although Python would interpret that as the last list element, the index is only a pointer state until a valid movement operation changes it. The first valid call to `next()` increments `self.i` from negative one to zero and returns the smallest inorder value.

This pointer model makes moving backward and forward reversible. If `prev()` changes the index from three to two, a following `next()` changes it back to three and returns the same value that was previously left.

**Checking and moving to the next value**

`hasNext()` returns:

`self.i < len(self.nums) - 1`.

The final valid array index is `len(self.nums) - 1`. A next value exists exactly when the current index is smaller than that final index. At initialization, negative one is smaller for every non-empty tree, so `hasNext()` is true.

`next()` increments `self.i` and returns `self.nums[self.i]`. The problem guarantees calls are valid, so the method does not need an exception branch for moving beyond the list. Its order—increment first, then read—matches the contract that `next` moves right and returns the new current value.

**Checking and moving to the previous value**

`hasPrev()` returns `self.i > 0`. If the current pointer is at index zero, it is already on the smallest traversal value, so no previous value exists. If it is at any later index, decrementing by one remains within the list.

`prev()` decrements `self.i` and returns the value at the new index. Again, the interface guarantees the call is valid.

It is worth noticing why `hasPrev()` does not use `self.i >= 0`. At index zero, the iterator does have a current value, but there is no value to its left. The predicate must describe the availability of a movement, not merely whether the pointer is currently on an element.

**Tracing the sample state**

For a BST whose inorder values are `[3, 7, 9, 15, 20]`, construction stores that list and sets `i = -1`.

- The first `next()` makes `i = 0` and returns three.
- The second makes `i = 1` and returns seven.
- `prev()` returns the pointer to zero and returns three.
- Another `next()` returns to index one and returns seven again.

No tree nodes are revisited during this movement. The iterator simply navigates the already flattened order, so any valid sequence of forward and backward calls behaves consistently.

**Why the class satisfies the interface**

The constructor establishes that `nums` contains every tree value exactly once in inorder and that `i` starts immediately before it. The movement methods change `i` by exactly one in the requested direction. Their return value is the element at the new pointer location. The availability methods test whether that new location would lie within the list.

Therefore, after any valid operation sequence, `i` precisely identifies the current inorder position. `next` yields the element immediately to the right, `prev` yields the one immediately to the left, and the two predicates report whether those movements exist.

**Implementation consequence of eager traversal**

The tree reference is not stored after construction. Once `dfs(root)` returns, all future behavior depends only on `self.nums` and `self.i`. Later external changes to the tree would not be reflected in this iterator, which is consistent with the usual assumption that the traversed BST remains unchanged.

The recursive implementation is concise, but Python recursion depth is a practical concern for a highly skewed tree. A tree with up to $10^5$ nodes can exceed Python’s default recursion limit even though the algorithm’s mathematical complexity is valid. An iterative inorder traversal would preserve eager flattening while avoiding that runtime limitation.

## Complexity detail

Let $N$ be the number of tree nodes and $Q$ the total number of iterator method calls.

The constructor’s depth-first traversal visits every node once and performs constant work per node, taking $O(N)$ time. Each `hasNext`, `next`, `hasPrev`, and `prev` call performs a constant number of comparisons, arithmetic operations, or array accesses, so every call is $O(1)$. Across construction and $Q$ operations, total time is $O(N+Q)$.

`self.nums` stores $N$ values, taking $O(N)$ persistent space. Recursive traversal also uses $O(H)$ call-stack space, where $H$ is tree height and may be $N$ for a skewed tree. Since $H\le N$, total auxiliary space remains $O(N)$.

The constructor is not $O(1)$ and the solution precalculates the entire traversal. It matches the main interface but not the optional no-precalculation follow-up.

## Alternatives and edge cases

- **Lazy iterative inorder traversal:** Store a stack, the next unexplored node, and values revealed so far. Construction can be $O(1)$, `next` is amortized $O(1)$, and `prev` reuses cached values. This addresses the follow-up but is more stateful than the checked-in eager solution.
- **Eager iterative traversal:** Build the same `nums` array with an explicit stack. It retains $O(N)$ constructor time and $O(1)$ operations while avoiding Python recursion-limit failures.
- **Search predecessor or successor from the root on every call:** This can use less retained traversal storage but costs $O(H)$ per movement and needs careful handling when moving repeatedly in both directions.
- **Morris traversal:** It can traverse with constant extra traversal space by temporarily threading the tree, but eager storage is still needed for arbitrary backward movement, and temporary tree mutation complicates the implementation.
- **Single-node tree:** Construction stores one value. Initially `hasNext()` is true; after one `next()`, both `hasNext()` and `hasPrev()` are false.
- **Pointer before the first element:** `i = -1` is a sentinel state only. The first valid operation is `next()`; `prev()` is not valid there under the contract.
- **Pointer at the smallest value:** `hasPrev()` correctly returns false because `i == 0`.
- **Pointer at the largest value:** `hasNext()` returns false because `i == len(nums) - 1`.
- **Alternating movement:** A `prev()` followed by `next()` returns to the same index and value, because both operations adjust one shared pointer.
- **Duplicate BST values:** The iterator mechanics would preserve inorder occurrences even if duplicates existed. The ordering convention for duplicates depends on the BST definition, but the traversal itself remains deterministic.
- **Skewed tree:** Mathematical space is still $O(N)$, but recursive `dfs` may exceed Python’s default recursion depth. An iterative eager traversal is safer for the maximum constraint.
- **Valid-call guarantee:** `next()` and `prev()` do not perform their own boundary checks. Calling them when unavailable could read an unintended negative index or raise `IndexError`, but the platform promises not to do so.
- **Tree mutation after construction:** The flattened list is a snapshot. Changes to node values or structure after initialization are not reflected.
- **Follow-up requirement:** The exact source precalculates all values and therefore intentionally represents the editorial’s first approach, not its lazy follow-up approach.
