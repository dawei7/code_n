## General

**Restate the survival rule**

A node must be removed exactly when some strictly greater value occurs later in the original list. Equivalently, a node survives when its value is at least every value to its right. Such nodes are suffix maxima, with equal values allowed to survive because the rule says “greater,” not “greater than or equal.”

The exact solution first copies all node values into the array `nums`. It then processes those values from left to right with a monotonic stack and finally creates a new linked list from the surviving values.

Although the branch summary describes reversing the list and using running suffix maxima in constant space, the protected implementation does not reverse or reuse nodes. Its actual array-and-stack behavior is what matters here.

**Why a monotonic stack can discard doomed earlier values**

For each current value `v`, the loop repeatedly pops while `stk[-1] < v`. Every popped value belonged to an earlier node, and the current node lies to its right with a strictly greater value. The popped node therefore satisfies the removal rule, so discarding it is unquestionably safe.

After all smaller top values have been removed, either the stack is empty or its top is at least `v`. Appending `v` makes the stack non-increasing from bottom to top. This ordering is important: if `v` is greater than several recent survivors, those smaller values occur consecutively at the top and can all be removed.

Consider values `[5,2,13,3,8]`:

- Reading 5 produces `[5]`.
- Reading 2 produces `[5,2]` because 5 is not smaller than 2.
- Reading 13 pops 2 and 5, then produces `[13]`.
- Reading 3 produces `[13,3]`.
- Reading 8 pops 3, then produces `[13,8]`.

Those final values are the required list.

**Why a value left in the stack really survives**

Whenever an element is popped, the current later value is a direct witness that it must be removed. Now consider an element that remains after the whole scan. If any later input value were strictly greater, then when that later value was processed, the stack's non-increasing structure would eventually expose and pop the smaller element after any even smaller values above it were removed. Because it was never popped, no such greater value exists to its right.

Thus the final stack contains exactly the original nodes that satisfy the survival rule. Values are appended in input order, and popping removes entries without rearranging the rest, so the survivors also remain in their original relative order.

This gives both directions needed for correctness: every removed value has a greater witness to its right, and every retained value has no greater value to its right.

**Strict comparison preserves duplicates**

The condition is `stk[-1] < v` rather than `stk[-1] <= v`. If an earlier node and a later node both have value 7, the later 7 is not greater than the earlier one. Both should remain unless some still larger value occurs afterward.

For `[1,1,1,1]`, no comparison is strict, nothing is popped, and all four values are reconstructed.

**Why reading values first helps**

A singly linked list offers only forward traversal. Storing values in `nums` lets the code apply an ordinary stack algorithm without manipulating links during the decision phase. In fact, this exact stack scans forward rather than using `nums` for reverse traversal; the array simply separates list reading from value processing.

Each input node is visited once while filling `nums`. The original `head` variable advances to `None`, but the nodes themselves are not modified.

**Rebuild the result**

After the stack is complete, a dummy node provides a stable starting point. The variable temporarily named `head` is set to the dummy and advances as each surviving value is copied into a new `ListNode`. Returning `dummy.next` skips the artificial node and yields the first real result node.

The reconstruction means the returned list contains new node objects. It preserves values and order, which is all the problem contract requires, but it is not an in-place filtering of the input list.

The input contains at least one node, and the final node is always a suffix maximum, so `stk` cannot be empty for a valid input. The dummy technique would nevertheless make linking convenient regardless of the number of survivors.

## Complexity detail

Let $n$ be the number of input nodes. Copying values costs $O(n)$. During the stack pass, every value is pushed once and popped at most once, so the total work of all nested `while` iterations is $O(n)$ rather than $O(n^2)$. Rebuilding at most $n$ result nodes costs another $O(n)$. Overall time is $O(n)$.

The `nums` array can hold $n$ values, and `stk` can also hold $n$ values for a non-increasing input. The newly allocated result list contains up to $n$ nodes. Excluding required output but including working arrays, auxiliary space is $O(n)$. The exact implementation does not satisfy the manifest's $O(1)$ auxiliary-space claim.

Stack operations are amortized constant time: a value that causes many pops is charging work to entries that can never be popped again.

## Alternatives and edge cases

- **Reverse twice in place:** Reverse the linked list, retain running maxima while scanning from the original right, and reverse survivors again. This reaches $O(1)$ auxiliary space but mutates pointers and is not the exact code.
- **Recursion from the tail:** Solve the suffix first and compare the current value with the surviving suffix head. It uses $O(n)$ call-stack space and risks recursion-depth failure for $10^5$ nodes in Python.
- **Quadratic lookahead:** Scan every later node for each current node. It is direct but costs $O(n^2)$ time.
- **Strictly decreasing input:** No later value is greater, so every node remains and the stack reaches size $n$.
- **Strictly increasing input:** Every node except the last is popped.
- **Equal values:** Equal later values do not trigger removal because the comparison is strict.
- **Single node:** It has nothing to its right and is returned as a newly allocated one-node list.
- **Multiple pops:** One large value may invalidate many earlier candidates; amortized analysis still keeps total work linear.
- **Object identity:** The solution preserves values and order but returns new nodes rather than original node objects.
- **Manifest mismatch:** The two arrays and rebuilt list must not be described as an in-place constant-space implementation.
