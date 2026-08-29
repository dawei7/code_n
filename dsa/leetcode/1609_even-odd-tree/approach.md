## General

**Check one complete level at a time**

The rules change with level parity and compare nodes from left to right, so breadth-first search is a natural fit. The queue `q` begins with the root and, at the start of each outer iteration, contains exactly one complete level in left-to-right order.

`even` is initialized to one, a truthy value representing level zero. After each level, `even ^= 1` toggles one to zero or zero to one.

**Choose a safe previous-value sentinel**

For an even-indexed level, values must be odd and strictly increasing. The source initializes `prev = 0`. Node values are at least one, so the first valid odd value is automatically greater than zero.

For an odd-indexed level, values must be even and strictly decreasing. The source initializes `prev = inf`, so the first finite value is automatically smaller.

These sentinels allow the first node to pass through the same ordering comparisons as every later node without a separate “first item” flag.

**Freeze the level size**

`for _ in range(len(q))` evaluates the queue length at the beginning of the level. Children appended during the loop belong to the next level and do not increase the number of current iterations.

The loop pops current nodes from the left. Appending each left child before its right child preserves left-to-right order for the next level.

**Rules on even-indexed levels**

When `even` is truthy, the invalid condition is:

`root.val % 2 == 0 or prev >= root.val`.

The first part rejects an even value because even-indexed levels require odd values. The second rejects any value not strictly greater than the previous one. Equality is invalid because the order must be strict.

If neither part is true, the current value is odd and greater than `prev`. The source assigns `prev = root.val` so the next node is compared with its immediate left neighbor.

**Rules on odd-indexed levels**

When `even` is false, the invalid condition is:

`root.val % 2 == 1 or prev <= root.val`.

An odd value violates the required even parity. A value greater than or equal to the previous one violates strict decrease.

Passing means the value is even and smaller than its left neighbor, after which it becomes the new `prev`.

**Why adjacent comparisons prove the whole order**

For a sequence to be strictly increasing, it is sufficient and necessary that every value after the first be greater than the immediately previous value. Transitivity then makes each value greater than all earlier values. The same argument holds for strict decrease.

Thus one `prev` scalar per level is sufficient; the method does not need to retain the entire level’s values.

**Why early failure is correct**

If any node has the wrong parity, that level violates the definition regardless of all other nodes. If any adjacent pair violates the required strict direction, the sequence is invalid. The source immediately returns `False` in either case.

If BFS finishes, every node passed its parity rule and every level passed all adjacent order comparisons. Returning `True` is then justified.

**A level trace**

For even level values `[3,7,9]`, `prev` starts at zero. Three is odd and above zero; seven is odd and above three; nine is odd and above seven. The level passes.

For odd level values `[12,8,6,2]`, `prev` starts at infinity. Every value is even, and each is below the previous. The level passes.

For `[3,3,7]` on an even level, the second three triggers `prev >= root.val` because three is not strictly greater than three. The source returns false.

**Queue invariant**

Initially, `q` contains exactly level zero. Assume it contains one level in order. The frozen-size loop removes all and only those nodes, and appends their children in left-then-right order. The resulting queue is exactly the next level in left-to-right order. Induction maintains the invariant through the tree.

Combining this invariant with the level-specific checks proves the returned Boolean matches the Even-Odd definition.

## Complexity detail

Let $N$ be the number of nodes and $W$ the tree’s maximum width.

Every node is enqueued once, dequeued once, and checked with constant work, so time complexity is $O(N)$.

The queue stores nodes from at most the current and developing next level, bounded by $O(W)$ up to a constant factor. Scalar state is constant. Auxiliary space is $O(W)$, which can be $O(N)$ for a wide tree.

Unlike recursive DFS, this implementation does not use call-stack depth and safely handles a highly skewed tree.

## Alternatives and edge cases

- **Depth-first search with one previous value per depth:** Preorder visiting left before right preserves level order across the traversal and can validate with $O(H)$ stored values plus recursion.
- **Store full level arrays:** This is unnecessary; adjacent comparisons need only one `prev` value.
- **Sort level values before checking:** Sorting would destroy the original left-to-right order that must be validated.
- **Single-node tree:** The root must be odd; ordering is vacuously valid.
- **Wrong root parity:** Level zero requires odd, so an even root immediately fails.
- **Equal adjacent values:** Strict order rejects equality on either level parity.
- **Correct parity but wrong direction:** The ordering comparison still rejects the tree.
- **Correct direction but wrong parity:** The modulo test independently rejects it.
- **Missing children:** BFS includes only real nodes; their left-to-right order is preserved without placeholders.
- **Positive-value constraint:** It makes zero and infinity safe sentinels. If negatives were allowed, explicit first-node handling would be safer.
- **Very wide tree:** Queue storage reaches $O(W)$ as stated.
- **Skewed tree:** Width is one, so queue storage stays constant.
- **Toggle with XOR:** `even ^= 1` alternates integer one and zero, which Python uses as true and false.
- **Early return:** Once one violation appears, remaining nodes cannot restore validity.
