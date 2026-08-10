## General

**Why the linked list is first copied into an array**

For a node at position `i`, the answer is the value of the first later node whose value is strictly larger. The word first makes distance matter: a very large value far to the right must not replace a smaller qualifying value that appears sooner.

A singly linked list supports movement from a node to its successor, but it does not support moving backward. The optimal solution wants to reason from right to left, where information about all later nodes is already available. Its first loop therefore copies every `head.val` into `nums` and advances with `head = head.next`. This costs one forward traversal and gives an array that can be indexed in reverse.

The answer array is then created as `[0] * n`. Zero is the required answer for a node that has no later strictly greater value. Pre-filling the defaults means the algorithm only has to overwrite entries for which it actually finds a next greater node.

**What the monotonic stack represents**

The stack `stk` stores values from nodes strictly to the right of the current index. It does not store every such value. It keeps only values that remain useful candidates for some node farther left.

During the right-to-left traversal, closer nodes are encountered later and are placed nearer the top. Before answering index `i`, the code removes every top value satisfying `stk[-1] <= nums[i]`. Such a value cannot be the next greater value for `nums[i]` because it is not strictly larger.

The removal is also safe for future nodes farther left. Suppose a stack value `x` is at or below the current value `c = nums[i]`. For any future node on the left, the current node `c` is closer than `x`. If that future node is smaller than `x`, then it is also smaller than `c`, so `c` is a qualifying greater value reached sooner. If the future node is at least `x`, then `x` is not greater and cannot qualify anyway. In every possible comparison, `x` will never again be the correct next greater value. It is dominated by the closer value `c` and may be discarded permanently.

After all dominated values are removed, either the stack is empty or its top is strictly greater than `nums[i]`. If it is nonempty, `stk[-1]` is the first greater value to the right, so the code assigns it to `ans[i]`. If it is empty, no useful greater candidate exists and the prefilled zero remains correct.

Finally, `nums[i]` is pushed. It may be the next greater value for some earlier node. Because the loop popped every value less than or equal to it, stack values are strictly decreasing from bottom to top after the push. Equivalently, values increase when read from the top downward. Equal values never coexist because equality does not satisfy the problem's strict-greater requirement and the closer equal value dominates the farther one.

**Why the top is the nearest qualifying node, not merely some greater node**

Monotonicity alone explains why the top is greater, but the dominance rule explains why it is the next greater value. Values are examined in reverse positional order. A newly pushed value is closer to every not-yet-processed node than all older stack entries. It stays above those older entries unless a still-closer value later dominates it.

When index `i` is processed, every actual node between `i` and the surviving stack top has already been considered. A value not retained on the stack was removed only when a closer value at least as large appeared. That closer value then became the better candidate for all positions farther left. Repeating this argument through any chain of removals shows that discarded nodes cannot hide a nearer qualifying answer. Therefore, once values at most `nums[i]` are removed, the top is exactly the closest surviving value that is strictly greater.

The stack can store values rather than pairs of values and indices because the traversal assigns `ans[i]` immediately. The algorithm never needs to return to an unresolved earlier index. Position is already known through `i`, and only the next greater node's value is required.

**A complete trace**

For `nums = [2, 7, 4, 3, 5]`, begin at the final value five. The stack is empty, so `ans[4]` stays zero. Push five, giving `[5]`.

At value three, the top five is greater. Nothing is popped, `ans[3]` becomes five, and three is pushed. The stack from bottom to top is `[5, 3]`.

At value four, three is at most four and is popped. This is safe because the current four is closer to every earlier node and dominates three. Five remains and is greater than four, so `ans[2]` becomes five. Push four, producing `[5, 4]`.

At value seven, four and five are both at most seven, so both are removed. No greater value remains to the right, and `ans[1]` stays zero. Push seven.

At value two, seven is greater, so `ans[0]` becomes seven. The final result is `[7, 0, 5, 5, 0]`.

This trace also shows why choosing the numerically smallest greater value would be wrong. For the initial two, both seven and later values such as four or five are greater, but seven occurs first and must be returned.

**Why popping equal values is necessary**

The comparison is `<=` rather than `<`. An equal value is not strictly larger, so it cannot answer the current position. Keeping it would also be pointless for earlier positions: the current equal value is closer and has the same ability to be greater than those earlier values. Removing the farther duplicate preserves all possible answers while keeping the stack strictly monotonic.

For a list such as `[2, 2, 3]`, the rightmost three is retained. Processing the middle two yields three. When the first two is processed, the closer equal two is popped, exposing three, so its answer is also three. For `[2, 2]`, the second two is popped while processing the first, and both answers remain zero.

**Why the whole method is correct**

Before processing each index `i`, the stack contains an ordered set of undominated candidate values from positions to the right. Popping removes exactly the candidates that cannot be strictly greater than the current value and that can never help an earlier value because the current node dominates them. If a candidate remains, the top is the closest qualifying one by the reverse traversal and stack order. The assignment is therefore correct for `i`. Pushing the current value restores the candidate structure for index `i - 1`.

The base case is the last node. Nothing lies to its right, the stack is empty, and its answer correctly remains zero. Applying the argument at every earlier index proves all entries. Copying the list preserves its original order exactly, so array index `i` corresponds to the same node position required by the output.

## Complexity detail

Let `N` be the number of nodes. Copying the linked list into `nums` visits each node once and takes `O(N)` time. The reverse `for` loop has `N` iterations.

Although one iteration can pop several values, each array value is pushed exactly once and can be popped at most once. Across the entire method there are at most `N` pushes and `N` pops. This aggregate accounting is why the nested-looking `while` loop is linear rather than quadratic. Total running time is `O(N)`.

The `nums` array stores `N` values because reverse traversal is not available on a singly linked list. The stack can also contain `N` values in the worst case. For example, when the original list is strictly increasing, the right-to-left traversal sees values in decreasing order and no value is popped before the end. These structures use `O(N)` auxiliary space. The required `ans` array contains `N` results and uses another `O(N)` output space. Whether output space is counted or excluded, the overall asymptotic space bound remains `O(N)`, matching the manifest.

## Alternatives and edge cases

- **Scan forward from every node:** For each position, following next pointers until a greater value appears is straightforward but can inspect nearly the whole suffix repeatedly. A decreasing list makes this `O(N^2)`.
- **Forward monotonic stack of indices:** One can traverse the list once, append a default zero, and keep unresolved pairs of index and value. A new larger value resolves and pops smaller entries. That approach is also `O(N)` time and `O(N)` space and avoids the separate `nums` array, but it must store indices because answers are filled later.
- **Array plus forward index stack:** After copying values, a standard next-greater-element algorithm can keep unresolved indices and fill them when a larger value arrives. It has the same asymptotic bounds. The exact solution instead fills each answer immediately during a reverse pass and needs only values in the stack.
- **Reverse the linked list in place:** Reversal would permit a right-to-left logical scan without an array, but it mutates the supplied structure and would need restoration if callers expect the list to remain intact. The result array still needs original positional order, adding bookkeeping.
- **Balanced search tree or heap:** These structures can find some larger value, but the problem asks for the first larger node by position, not the smallest larger value numerically. They do not naturally preserve the required nearest-position rule.
- **Single node:** The copied array has one value. The stack is initially empty, so its answer remains zero, exactly as required.
- **Strictly decreasing values:** Every new current value pops all smaller candidates. No node has a greater value to its right, and the result remains all zeroes.
- **Strictly increasing values:** During reverse traversal no top is at most the current value. Each node receives the value immediately to its right, while the final node receives zero.
- **All values equal:** Equality triggers popping, and no assignment is made. Every answer is zero because equal is not strictly greater.
- **Large values:** Node values may reach `10^9`, but the algorithm only compares and stores them. It performs no arithmetic that could overflow.
- **Repeated greater candidates:** The answer is based on position. The stack's dominance rule retains the closer useful occurrence and discards a farther occurrence when the closer value is at least as large.
- **Consumption of `head`:** The local variable advances to `None` while values are copied, but this does not delete or alter list nodes. Rebinding the local reference leaves the caller's linked list structure unchanged.
