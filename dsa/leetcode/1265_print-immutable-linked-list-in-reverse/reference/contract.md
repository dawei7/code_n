## Function Contract

**Input**

- `head`: the first `ImmutableListNode` in a nonempty immutable linked list.

Starting from `head`, `getNext()` advances through the list toward the tail. Node values are not returned by that method and are not available through a public value field.

**Output**

Return `None`. Produce the answer as a side effect by calling `printValue()` on every original node exactly once, in tail-to-head order.

The linked list must remain unchanged, and the implementation may operate only through `getNext()` and `printValue()`.
