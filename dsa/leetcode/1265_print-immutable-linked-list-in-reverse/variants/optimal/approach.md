## General
**Save interfaces rather than values**

Traverse forward from `head` by repeatedly calling `getNext()`. Append each node interface to a stack. This is permitted even though the nodes are immutable: the algorithm stores references to nodes but never reads a field or changes a link.

**Reverse the only available traversal direction**

After the forward scan reaches `null`, pop the saved interfaces. Last-in, first-out order produces the tail first and the head last. Call `printValue()` exactly once on each popped node. Thus every node is printed once, and for any two adjacent original nodes, the later node was pushed later and is consequently printed earlier. The complete emitted order is therefore the reverse of the list.

It is important not to collect or return ordinary integer values: the interface does not expose a value getter, and printing through each original node is part of the contract.

## Complexity detail
The forward traversal visits all $n$ nodes, and the pop phase processes those same $n$ interfaces, for $O(n)$ time. The stack holds $n$ node references in the worst case, so it uses $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Recursion:** Recurse on `getNext()` and call `printValue()` while unwinding; it has the same asymptotic bounds, but a long list can exceed the language's call-stack limit.
- **Constant-space repeated scans:** Find the last unprinted position by walking from `head` each time; it respects immutability and uses $O(1)$ extra space, but takes $O(n^2)$ time.
- **Block checkpoints:** Saving selected node interfaces reduces storage, but reconstructing reverse order within each block requires repeated forward scans and worsens the time bound.
- **Single node:** The stack contains only `head`, whose `printValue()` is called once.
- **Duplicate or negative values:** Node identity and position determine output order; values need not be distinct or positive.
- **Immutable interface:** Accessing fields such as `val` or `next`, assigning links, or printing by another mechanism violates the source-native contract.
