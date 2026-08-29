## General

This problem deliberately removes the tool normally used to delete a node from a singly linked list. If we have the head, we can walk to the node immediately before the target and change that predecessor's `next` pointer so it skips the target. Here, the function receives only `node`. A singly linked node points forward, not backward, so there is no way to discover or modify the predecessor in constant time.

The important shift in viewpoint is that the contract cares about the **observable list of values**, not about preserving the identity of the particular object that currently stores each value. After the operation, the target value must be absent, the list must contain one fewer reachable node, and the values on both sides must retain their order. We can satisfy all of those requirements without physically unlinking the supplied object.

**Turn the supplied node into its successor**

Let the local part of the list be

```text
... -> node(value = x) -> successor(value = y) -> rest
```

The desired visible result is

```text
... -> (value = y) -> rest
```

Because the caller cannot observe which object stores `y` merely by traversing values, we can make the supplied `node` impersonate its successor:

1. Copy `node.next.val` into `node.val`.
2. Set `node.next` to `node.next.next`.

After the first assignment, the supplied object contains `y` instead of `x`. After the second assignment, the original successor object is bypassed. The predecessor, although inaccessible, still points to the supplied object, so the chain before the target remains connected without any change. The suffix after the successor also remains connected because the supplied object now points directly to it.

This may sound like deleting the wrong node: at the object-identity level, the successor object is the one that becomes unreachable. At the problem's value-sequence level, however, the effect is exactly the deletion of `x`. The supplied object changes from `x` to `y`, and the old copy of `y` disappears. Thus the visible sequence loses exactly `x`, with no duplicated `y` left behind.

**Why the non-tail guarantee is essential**

Both assignments require a real successor. If `node` were the tail, `node.next` would be `None`; there would be no later value to copy and no forward link to bypass. More fundamentally, without access to the predecessor, there is no pointer we could change to make a tail object unreachable. The guarantee that the supplied node is not the tail is therefore not a minor convenience. It is what makes the problem solvable through the given interface.

The guarantee that values are unique also makes the requested deletion unambiguous when the result is described in terms of values. The two-assignment technique itself does not need a search and does not compare values, but uniqueness ensures that removing the target value has one clear interpretation.

**A concrete trace**

Consider `4 -> 5 -> 1 -> 9`, with the function receiving the node whose value is `5`.

- Initially, `node.val` is `5`, `node.next.val` is `1`, and `node.next.next` is the node containing `9`.
- The first assignment changes the supplied node's value from `5` to `1`. Temporarily the reachable values are `4 -> 1 -> 1 -> 9`; the duplicate is expected and lasts only until the next assignment.
- The second assignment makes the supplied node point directly to the node containing `9`. The original successor containing the second copy of `1` is no longer part of the chain.
- Traversal from the unchanged head now produces `4 -> 1 -> 9`, exactly the required result.

The order of these assignments matters conceptually. The solution first reads and preserves the successor's value in the current node, then discards the link to that successor. If it bypassed the successor before retrieving what was needed, it could lose convenient access to the value that must shift into the target position.

**Why two local mutations are sufficient**

Everything before `node` is untouched, including the inaccessible incoming pointer. The supplied object remains at the same position in the chain, so the prefix still reaches it normally. Its new value equals the first value that should appear after the deleted position. Its new `next` pointer equals the link that followed that value originally, so every still-needed later node remains in its original order. The target value is overwritten, and exactly one node—the old successor—is bypassed. These facts establish all four postconditions: the target value disappears, reachable length falls by one, prefix order is unchanged, and suffix order is unchanged.

The method mutates the existing structure and returns nothing. In Python, an unreachable node is eventually handled by garbage collection when no other references retain it; explicit memory deallocation is neither needed nor part of this function's contract.

## Complexity detail

The algorithm executes two assignments and follows only a constant number of pointers. It never walks toward the tail, so its running time is $O(1)$ regardless of whether the full list has two nodes or one thousand nodes.

It allocates no list, stack, replacement node, or other structure whose size depends on the input. Only existing references are read and reassigned, so the auxiliary space complexity is $O(1)$.

These bounds are stronger than the less refined strategy of repeatedly copying every later value one position left and then unlinking the tail. That strategy would produce the same visible sequence but would take $O(k)$ time, where $k$ is the number of nodes from the target through the tail. Copying only the immediate successor proves that the rest of the suffix does not need to move at all.

## Alternatives and edge cases

- **Delete through the predecessor:** With access to `head` or directly to the previous node, the conventional operation is `previous.next = node.next`. This preserves the identities of all surviving nodes, but finding the predecessor costs $O(n)$ from the head and is impossible through the restricted input given here.
- **Shift every later value left:** One can copy values successively from each next node and finally unlink the tail. It works for a non-tail target, but it performs unnecessary traversal and takes linear time in the remaining suffix instead of $O(1)$.
- **Copy and bypass only the successor:** The implemented method is the optimized form of value shifting. It recognizes that after the target receives the successor's value, the entire suffix beginning after that successor is already in the right place.
- **Target is immediately before the tail:** The same two statements work. The tail's value is copied into the target object, and the target's `next` becomes `None`, reducing the list by one node.
- **Smallest legal list:** For a two-node list, the target must be the first node. It receives the second node's value and becomes the new tail, which is still exactly the required one-node result.
- **Attempting to delete the tail:** The method cannot work because `node.next` is `None`. There is no successor value available to copy, and no predecessor reference available to sever the incoming link. The problem explicitly excludes this case.
- **External references to node objects:** Code holding a reference to the supplied object will observe that its value changed rather than that the object vanished. Code holding a separate reference to the old successor may still access that detached object. This identity-level behavior is acceptable because the contract judges the linked list reachable from `head` and defines deletion by its resulting value sequence.
- **Returning a value:** The operation is in-place. Returning the node or the list is unnecessary; the caller observes the mutations through the existing linked structure.
