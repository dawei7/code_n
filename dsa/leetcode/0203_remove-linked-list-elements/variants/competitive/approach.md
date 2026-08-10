## General

**Introduce a predecessor before the real list**

The competitive method allocates `dummy` and points `dummy.next` at the original
head. This sentinel gives the real first node a predecessor, so deleting a
matching head uses exactly the same link update as deleting a matching internal
node.

The dummy stores negative infinity, a value outside the node and target ranges.
Its value is never compared, so any placeholder would work. The important field
is its `next` link.

**Track both predecessor and current node**

`prev` starts at the dummy and `curr` starts at the original head. Before each
iteration, `curr` is the next original node to inspect, while `prev` is the last
node retained in the reachable result prefix.

These pointers can differ by more than one original position after deletions,
because removed nodes are no longer between `prev` and the next retained
candidate.

**Bypass when the current value matches**

When `curr.val == val`, assignment `prev.next = curr.next` removes `curr` from
the list reachable through dummy. `prev` deliberately stays unchanged because
the next candidate is now its direct successor and might also match.

Afterward, the common update `curr = curr.next` moves to the removed node's
former successor. Access remains valid during the assignment because local
variable `curr` still references the removed node even though the list link no
longer does.

**Advance both roles when keeping a node**

When the value differs, the node belongs in the result. `prev = curr` extends
the retained prefix. The common `curr = curr.next` then moves to the following
node.

Thus every loop iteration advances `curr` exactly once, while `prev` advances
only across nodes that remain. That asymmetry is the central rule for safely
handling consecutive matches.

**Trace a matching prefix and suffix**

For `[6,6,1,2,6]` with target 6, the first removal changes `dummy.next` to the
second 6. `prev` stays dummy. The second removal changes `dummy.next` to node 1.

Nodes 1 and 2 are retained, advancing `prev` through them. At the final 6,
node 2's next pointer is changed to null. Returning `dummy.next` produces
`[1,2]` without any special prefix or suffix branch.

For an all-matching list, dummy's link advances repeatedly until it is null, so
the returned head is null.

**Why the pointer invariant proves exact filtering**

At the start of an iteration, every node before `curr` has been classified.
The chain from `dummy.next` through `prev` contains exactly the classified
nonmatching nodes in original order.

If current matches, bypassing it leaves that retained chain unchanged and
removes exactly one invalid node. If it does not match, moving `prev` onto it
adds exactly one valid node at the end of the chain. Moving `curr` advances the
unclassified boundary in either case. The invariant is preserved until
`curr` becomes null, at which point all nodes have been classified.

Therefore every target-valued node is disconnected, every other node remains,
and retained order is unchanged.

**Return through the dummy rather than the old head**

The original `head` reference may point to a removed node. `dummy.next` always
tracks the first surviving node as prefix deletions occur. Returning old `head`
would be wrong whenever the list starts with the target; returning `dummy.next`
handles every case.

**Top-level node definition is harness-like support**

The file defines `ListNode` above `Solution`. It is a simple helper whose
constructor accepts only a value and initializes `next` to null. The algorithm
therefore constructs `dummy` with one argument and assigns its link on the next
line.

In the LeetCode environment, the platform normally supplies a compatible node
type. The logic needs only `val` and `next`; it does not depend on object
comparison or the particular negative-infinity sentinel value.

**Mutation does not allocate replacement nodes**

Only one dummy node is new. Every retained node is an original object, and the
method modifies links rather than values. This preserves identity for callers
holding references to retained nodes.

Removed nodes may still be referenced elsewhere; they are excluded from the
returned chain but not forcibly destroyed.

## Complexity detail

The `curr` pointer advances to the next original node once per loop iteration,
so all $n$ nodes are examined exactly once. Link updates and comparisons are
constant time, giving $O(n)$ total time.

The algorithm stores one dummy node and two pointers, independent of list
length. Auxiliary space is $O(1)$. It uses no recursion and no collection of
removed values.

## Alternatives and edge cases

- **Successor-only pointer:** Inspect `pre.next` and either advance or bypass, as the optimal variant does.
- **Repeated head removal:** Clean matching heads first and then process internal nodes; works but adds separate logic.
- **Recursive solution:** Filter the suffix and decide whether to keep the current head; uses proportional stack space.
- **Empty input:** `curr` is null immediately and `dummy.next` returns null.
- **All matching:** Dummy's link eventually becomes null.
- **No matching values:** Both pointers advance through the unchanged list.
- **Consecutive matches:** Keep `prev` stationary after each deletion.
- **Matching original head:** Dummy link becomes the next candidate.
- **Matching tail:** Predecessor link is set to null.
- **Sentinel value:** Negative infinity is convenient but semantically irrelevant because dummy is never tested.
