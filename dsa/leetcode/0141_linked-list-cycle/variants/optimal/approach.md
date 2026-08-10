## General

**Detect a repeated node identity**

A cycle exists when repeatedly following `next` reaches the same node object again. Repeated values do not imply a cycle: two different nodes may store the same `val`. The selected solution therefore stores node references in a set, not node values.

The local variable `head` acts as the traversal pointer. At each iteration, the code first asks whether this exact node is already in `s`.

- If it is present, traversal has returned to a previously visited object, so a cycle exists.
- If it is absent, the node is added and traversal advances to `head.next`.

If traversal eventually reaches `None`, the list has a real end and cannot contain a cycle reachable from the supplied head.

**Why checking before insertion matters**

The first encounter with a node should not count as repetition. The code checks membership, then inserts. On a later encounter, the stored identity makes the check true.

In the first example, traversal visits nodes at indices zero, one, two, and three. The tail points back to the node at index one. When that node becomes `head` for the second time, it is already in `s`, and the method returns `True`.

For an acyclic list, every visited node is new until the final node advances to `None`. The loop stops and returns `False`.

For a self-loop, the only node is inserted on the first iteration. Its `next` points to itself, so the second iteration finds the same object in the set and returns true.

**Why repetition is equivalent to a cycle**

If the algorithm reports true, it has reached the same object at two different traversal times. Between those two visits, following one or more `next` pointers led from that node back to itself. Those links form a cycle.

Conversely, if a reachable cycle exists, traversal eventually enters it. The cycle contains finitely many nodes, and every node inside it has a next pointer to another node in the cycle. Continuing forever would visit more positions than there are distinct cycle nodes, so some node must repeat. Since the set retains every earlier reference, the algorithm detects that repetition.

Thus the test has neither false positives nor false negatives under the linked-list contract.

**The `pos` value is not an algorithm input**

Examples describe `pos` only to explain how the test harness creates the tail connection. The function receives only `head`. Trying to inspect a variable named `pos` would violate the function contract.

The method discovers the topology from node references themselves. It does not need to know which index the tail targets, and it does not require node values to encode positions.

**The original list is not modified**

Assigning `head = head.next` changes only the local traversal variable. It does not change any node’s `next` field. The list remains intact after the function returns.

This is different from marking nodes by overwriting `val` or rewiring pointers. Such mutation could damage caller data and could confuse legitimate repeated values with visitation state.

**Hashing assumptions**

Ordinary `ListNode` instances use identity-based equality and hashing, so they can be set members. The set distinguishes objects even when their values match.

If a custom node class defined equality without a compatible hash, instances could be unhashable and this exact implementation would fail. The platform’s standard node identity semantics support the method.

## Complexity detail

Let $n$ be the number of distinct nodes reachable from `head`.

Each distinct node is inserted once. In an acyclic list, the loop visits all $n$ nodes and then `None`. In a cyclic list, it visits at most all $n$ distinct nodes before the next encounter repeats one. Expected set membership and insertion are $O(1)$, so expected time is $O(n)$.

The set may retain all $n$ node references, giving $O(n)$ auxiliary space.

This exact source therefore contradicts the variant manifest’s $O(1)$ space claim. It is linear-time and correct, but it does not satisfy the constant-memory follow-up. The manifest would fit Floyd’s two-pointer algorithm, not this visited-set implementation.

No output-sized storage is relevant because the function returns one Boolean.

## Alternatives and edge cases

- **Floyd’s slow and fast pointers:** Move one pointer one step and another two steps. They meet inside a cycle, while the fast pointer reaches `None` in an acyclic list. This achieves $O(1)$ space.
- **Temporarily mark nodes:** Alter a value or pointer to record visitation. It can use constant space but mutates input and is unsafe when values are unrestricted or restoration is difficult.
- **Bounded traversal by known node count:** If the exact node count were separately provided, more than that many steps would prove a cycle. The native interface does not provide this count.
- **Empty list:** The loop never runs and returns false.
- **One node without a loop:** The node is inserted, then traversal reaches `None`.
- **One node pointing to itself:** The second visit is detected.
- **Repeated values:** They do not matter because the set stores node objects rather than `val`.
- **Cycle begins at head:** Detection occurs after one complete trip around that cycle.
- **Long noncyclic prefix:** Every prefix node is stored before traversal enters and eventually repeats within the cycle.
- **Runtime dependencies:** The source annotation uses `Optional` without importing it. The platform supplies `ListNode`, but standalone Python also needs `from typing import Optional` and a concrete `ListNode` definition.
- **Manifest mismatch:** Calling this visited-set source constant-space would hide its primary tradeoff.
