## General

The zero-valued nodes are separators. Every block of nonzero nodes between two separators must become one output node whose value is the block sum.

The exact implementation scans the input once and builds a new linked list behind a dummy node. It does not overwrite and reconnect the consumed input nodes as the manifest summary suggests.

**Skip the leading separator**

The contract guarantees that the first node has value zero, so `cur = head.next` begins at the first node after that separator.

Because there are no two consecutive zeros and the list contains at least the leading and trailing separators, this starting node belongs to the first nonempty block unless the contract were violated.

The leading zero is not copied into the answer. This helps ensure the returned list contains no zero separators.

**Accumulate one block at a time**

Variable `s` stores the sum of the current block and starts at zero. As long as `cur.val` is nonzero, the code adds it to `s`.

Every nonzero node lies between two separators and belongs to exactly one block. The scan reaches it once, so its value is included once in the appropriate sum.

The node constraints allow values up to one thousand, and each group has at least one nonzero node because separators are never consecutive. Therefore every completed group sum is positive.

**Use each zero to close a group**

When `cur.val` is zero, the accumulated block is complete. The code creates `ListNode(s)` and attaches it with `tail.next`. It then advances `tail` to the newly created node and resets `s` to zero for the next group.

The final input node is also zero, so the last block is closed and emitted before the scan ends. No special “flush after the loop” step is needed.

Resetting `s` is essential. Without it, the next output node would contain a cumulative total across several blocks rather than the sum between its own consecutive separators.

**Build through a dummy head**

`dummy = tail = ListNode()` creates one temporary node and gives both names the same reference. `dummy` remains fixed as the anchor before the first output node, while `tail` advances as nodes are appended.

The first completed group is assigned to `dummy.next`. Later groups attach after the current tail. Returning `dummy.next` discards the temporary anchor from the visible result and gives the caller the first sum node.

The dummy pattern avoids a separate branch for “is this the first output node?” Every group uses the same append statements.

**Why the output order is correct**

The pointer `cur` moves only forward. A group is emitted when its closing zero is encountered, before any values from the next group are accumulated.

Consequently, output nodes appear in exactly the same left-to-right order as their source blocks. The algorithm does not sort or reorder sums.

For `[0,3,1,0,4,5,2,0]`, the scan accumulates four before the first encountered separator and appends node four. After resetting, it accumulates eleven and appends node eleven at the final separator. Returning after the dummy yields `[4,11]`.

**Why the constructed list is exactly the requested merge**

Every separator after the leading one ends one block, and the no-consecutive-zero guarantee ensures that block contains at least one nonzero node. The algorithm appends exactly one output node at each such separator.

Its value is the sum of all and only nodes since the previous separator because `s` was reset there and every intervening value was added once. No output node has value zero, since every block contains positive values. Every required block appears once and in order, so the returned list is the desired merged list.

**Distinguish output allocation from working memory**

The original input list is read but never rewired or overwritten. Each block creates a fresh `ListNode`. This may be preferable when preserving the input matters, but it differs from the in-place editorial approach.

If there are $g$ separator-delimited groups, the returned list necessarily contains $g$ nodes. The dummy is one additional temporary node that becomes unreachable after return if no other reference is kept.

## Complexity detail

Let $n$ be the number of input nodes. `cur` advances once per node after the head and never moves backward, so time is $O(n)$.

Let $g$ be the number of nonzero groups. The exact source allocates $g$ returned nodes plus one dummy, so its allocated space is $O(g)$, which is $O(n)$ in the worst case. Excluding the required output nodes, its auxiliary working state is $O(1)$.

The manifest's $O(1)$ space and “overwrites the consumed prefix” summary describe an in-place variant. They do not describe this source's fresh list allocation. The time bound remains $O(n)$ for both designs.

## Alternatives and edge cases

- **In-place two pointers:** Store each group sum into an existing nonzero node and reconnect the retained prefix. This matches the manifest and uses $O(1)$ auxiliary space without allocating output nodes.
- **Recursive block processing:** Sum one block and recurse from its closing zero. It is conceptually compact but consumes call-stack space proportional to the number of groups.
- **Array of sums first:** Collect group totals in a list and then build nodes. This adds an unnecessary intermediate $O(g)$ container.
- **One group:** The trailing zero emits one sum node, and `dummy.next` points directly to it.
- **Single-value group:** That value is copied unchanged as the group sum.
- **Several groups:** Resetting `s` at every separator keeps their sums independent.
- **Leading zero:** It is skipped deliberately and never appears in the output.
- **Trailing zero:** It triggers creation of the final sum node; no post-loop flush is required.
- **No consecutive separators:** This guarantees the code never emits a zero sum for an empty group.
- **Positive block sums:** Nonseparator values are positive under the separator interpretation, so output nodes contain no zero.
- **Input preservation:** The source does not alter `val` or `next` on any original node.
- **Fresh output identity:** Returned nodes are newly allocated and are not nodes from the input list.
- **Dummy exclusion:** Returning `dummy.next` prevents the zero-valued helper node from entering the result.
- **Manifest discrepancy:** The metadata describes in-place overwriting, while the exact solution constructs a separate list and therefore allocates linear output space.
