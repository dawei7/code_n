## Description

You are given the head of an immutable linked list and must print the value of every node in reverse order, from the tail back to the head. The list is opaque: its nodes cannot be inspected through ordinary fields and none of their contents or links may be changed.

An `ImmutableListNode` exposes only two operations:

- `ImmutableListNode.printValue()` prints the value stored in the current node.
- `ImmutableListNode.getNext()` returns the following node.

The serialized list in an input fixture exists only so the judge can construct these nodes internally. Solve the task exclusively through the supplied node interfaces, without modifying the list or trying to access an `ImmutableListNode` directly.
