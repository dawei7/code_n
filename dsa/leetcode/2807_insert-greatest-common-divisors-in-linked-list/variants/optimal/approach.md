## General

**One insertion belongs to every original edge.** A singly linked list of $n$ nodes has $n-1$ adjacencies between consecutive original nodes. For each such pair, the task requires one new node whose value is their greatest common divisor. The new node must be placed between the pair, while the original nodes remain in their original order.

The solution performs this transformation in one forward pass with two references: `pre` points to the left original node of the pair currently being handled, and `cur` points to the right original node. They are initialized as `head` and `head.next`.

**Compute the value before changing links.** During an iteration, `gcd(pre.val, cur.val)` computes the greatest common divisor of the current original pair. Python's standard `gcd` implements the Euclidean algorithm and returns the positive greatest common divisor for the positive values guaranteed by the constraints.

The result is stored in `x`. Computing it before relinking makes the intended pair unambiguous. Even after insertion, `pre` and `cur` still refer to the original node objects, but the ordering keeps the data flow easy to verify.

**Splice one node between the pair.** The expression `ListNode(x, cur)` constructs a new node whose value is `x` and whose next pointer already targets the right original node. Assigning that node to `pre.next` changes the local chain from

`pre -> cur`

to

`pre -> gcd-node -> cur`.

Nothing after `cur` is lost because `cur.next` is untouched. Nothing before `pre` is changed. The new node has exactly the required value and location.

**Advance over the inserted node, not through it.** The update `pre, cur = cur, cur.next` is the crucial detail. Python evaluates the right-hand side references before performing either assignment. The new `pre` becomes the original right node from the pair just processed, and the new `cur` becomes that original node's next neighbor.

The inserted gcd node is deliberately skipped. If the algorithm advanced to `pre.next` instead, it would land on the new node and might compute another gcd involving generated data, producing too many insertions or even an endless chain. The problem asks for gcds between originally adjacent nodes, so each iteration must move from one original edge to the next original edge.

For an original list `18 -> 6 -> 10`, the first iteration inserts six between eighteen and six. The pointer update then makes the original six the left endpoint and the original ten the right endpoint. The second iteration inserts two between them. The result is `18 -> 6 -> 6 -> 2 -> 10`, where the first two sixes are distinct nodes with different roles.

**Loop invariant.** At the start of each iteration, `pre` and `cur` are consecutive nodes in the original list. Every original adjacency before `pre` has already received exactly one correct inserted node, and the suffix beginning at `cur` still has its original internal links.

The splice correctly resolves the current adjacency without damaging the suffix. The pointer update establishes the same invariant for the next original pair. When `cur` becomes `None`, there is no original node to the right of `pre`, so every original adjacency has been processed exactly once.

**Return the same head.** Insertions occur only after existing nodes. The first original node is never replaced, so `head` remains the correct entry point. Returning it exposes the fully mutated list.

**Why no array conversion is needed.** The operation can be performed locally because the gcd for an edge needs only its two endpoint values, and a singly linked splice needs only a reference to the left node and the preserved right node. Converting the list to an array would add memory and later reconstruction work without providing useful information.

**Mutation is intentional.** The exact method changes the supplied list and allocates the required new nodes. A caller holding a reference to any original node observes the inserted structure around it after completion. This is consistent with linked-list transformation problems, but it is worth distinguishing required output-node allocation from algorithmic scratch space.

## Complexity detail

Let $n$ be the number of original nodes and let $V$ be the largest node value. The loop executes once for each original adjacency, so it has $n-1$ iterations. The Euclidean algorithm computes one gcd in $O(\log V)$ time in the usual word-arithmetic model. Total time is therefore $O(n \log V)$.

Given the constraint $V \le 1000$, gcd work has a small fixed upper bound, so it is also reasonable to describe practical traversal time as linear in $n$. The more informative general statement retains the $\log V$ factor.

The pointer variables and gcd value use $O(1)$ auxiliary space. The method allocates exactly $n-1$ new list nodes because those nodes are the required transformed output. If output storage is counted, additional space is $O(n)$. If the complexity convention excludes storage required by the returned structure, auxiliary space is $O(1)$. The manifest reports $O(n)$ space, which corresponds to including the inserted nodes.

The method is iterative, so it does not use an $O(n)$ recursion stack. The original nodes are reused rather than copied.

## Alternatives and edge cases

- **Recursive traversal:** Process a pair, insert its gcd node, and recurse on the next original node. It can be correct if it skips the inserted node carefully, but it adds $O(n)$ call-stack space.
- **Convert to an array and rebuild:** This makes original adjacency obvious but uses $O(n)$ extra storage and discards the benefit of local linked-list splicing.
- **Manual Euclidean algorithm:** Repeated remainder operations can replace Python's `gcd` with the same $O(\log V)$ bound. The library function is clearer and well tested.
- **Single-node list:** `cur` starts as `None`, the loop does nothing, and the original head is returned. There are zero adjacencies and therefore zero insertions.
- **Two-node list:** Exactly one iteration inserts exactly one gcd node.
- **Equal adjacent values:** Their gcd equals that value, so an equal-valued node is inserted; equal values do not mean the insertion should be skipped.
- **One value divides the other:** The gcd is the smaller value, and that value is still inserted as a distinct node.
- **Repeated original values:** Adjacencies are defined by node positions, not distinct values, so every edge is processed separately.
- **Skipping inserted nodes:** Advancing to the original `cur` is necessary. Treating a generated node as the next left endpoint changes the problem.
- **Pointer assignment order:** Python's simultaneous assignment safely reads `cur.next` before rebinding `cur`. Splitting the update into statements should preserve a temporary reference or the same ordering.
- **Input aliases:** Because the list is mutated, any external reference into it observes inserted successors.
- **Positive values:** The contract excludes zero and negatives, so the returned gcd values are positive and require no sign normalization.
