## General

**Make head deletion look like ordinary middle deletion**

Removing a non-head node is easy when its predecessor is known: assign the
predecessor's `next` pointer to the removed node's successor. Removing the real
head is awkward because there is no predecessor node whose link can be changed.

The solution creates a dummy node before the original head with
`ListNode(-1, head)`. Every original node now has a predecessor, including the
first one. All removals can use the same pointer operation, and the eventual
head is always `dummy.next`.

The dummy value `-1` lies outside the stated node-value range, but correctness
does not actually depend on that. The loop never tests the dummy's value; it
exists only to own a link.

**Let `pre` point to the retained prefix's final node**

Pointer `pre` starts at the dummy. At the start of each loop iteration, all
original nodes before `pre.next` have already been examined, every matching one
has been bypassed, and `pre` is the final node of the kept prefix.

The next node to decide is always `pre.next`. This viewpoint avoids maintaining
a separate current pointer and makes the link that may need changing directly
available.

**Advance when the next node should remain**

If `pre.next.val != val`, the next node belongs in the result. The assignment
`pre = pre.next` extends the retained prefix by one node. Its links are not
changed, so original relative order remains intact.

On the following iteration, the algorithm examines that retained node's
successor.

**Bypass a matching next node**

If `pre.next.val == val`, assignment
`pre.next = pre.next.next` makes the predecessor skip the matching node and
point directly to its successor. The removed node is no longer reachable from
the dummy and therefore no longer belongs to the returned list.

Crucially, `pre` does not advance after a deletion. Its new `pre.next` has not
yet been examined and may also match. Staying at the same predecessor is what
removes consecutive runs such as `[7,7,7,7]` without skipping every second
node.

**Use the link itself as the loop condition**

`while pre.next` continues while an undecided node exists. Once `pre.next` is
null, every original reachable node has been examined and the retained prefix
is the complete result.

The condition is safe for an empty input because dummy exists and
`dummy.next` is immediately null. The loop performs no work and returns null.

**Trace the mixed example**

For `[1,2,6,3,4,5,6]` with target 6, nodes 1 and 2 do not match, so `pre`
advances through them. The next node is 6, so the link from node 2 changes to
node 3 and `pre` stays at node 2.

Nodes 3, 4, and 5 are retained by advancing. The final 6 is bypassed by setting
node 5's next pointer to null. Returning `dummy.next` yields
`[1,2,3,4,5]`.

If the first node matched, the same operation would update `dummy.next`, which
is why no separate head-removal loop is necessary.

**Why every retained node is valid**

The algorithm advances `pre` onto an original node only after checking that its
value differs from `val`. Therefore every node in the retained prefix is valid.
Deletion never reconnects to an earlier node or changes value order; it only
skips one matching successor.

Every original node eventually becomes `pre.next`. It is either retained and
`pre` advances, or removed and the link advances to the following node. Thus no
node is ignored. At termination, all matches have been bypassed and all
nonmatches remain in their original order.

**Mutation and object identity**

The method reuses the existing nonmatching nodes. It does not allocate a copied
result list or alter node values. Only `next` links are changed, plus one
constant-size dummy allocation.

External references to removed nodes may still exist outside the returned list;
the method simply disconnects them from this head. Python garbage collection can
reclaim an unreferenced removed node later.

**Platform node contract**

The file comments out the standard `ListNode` definition and assumes the harness
provides a constructor accepting both value and next pointer. A standalone node
class that accepts only one constructor argument would make
`ListNode(-1, head)` fail. The environment must match the shown platform
template or the dummy must be created and linked in two statements.

## Complexity detail

Let $n$ be the number of original nodes. Each iteration either advances `pre`
over one kept node or permanently bypasses one removed node. No node is handled
more than once, so time is $O(n)$.

The dummy and predecessor are a constant number of references. No recursion or
proportional collection is used, so auxiliary space is $O(1)$. The returned
list reuses input nodes and is not extra working storage.

## Alternatives and edge cases

- **Separate head cleanup:** Repeatedly move `head` past matching prefixes, then delete internal matches; correct but duplicates boundary logic.
- **Two explicit pointers:** Track `prev` and `curr`, keeping `prev` fixed after deletion, as the competitive variant does.
- **Recursive filtering:** Return the filtered suffix and reconnect a nonmatching head; concise but uses $O(n)$ call-stack space.
- **Empty list:** Dummy points to null and null is returned.
- **All nodes match:** `dummy.next` is repeatedly advanced until null.
- **No node matches:** `pre` walks through every node and no link changes.
- **Consecutive matches:** Do not advance `pre` after bypassing one.
- **Target outside node range:** Nothing matches, though the contract permits target zero while node values start at one.
- **Duplicate retained values:** They remain because only equality with the target matters.
- **Constructor shape:** The supplied `ListNode` must accept `(value, next)` for the exact dummy creation call.
