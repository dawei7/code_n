## Function Contract

`solve(head: Node | None, insertVal: int) -> Node`

`Node` contains an integer `val` and a `next` reference to another node in the cycle.

**Inputs**

- `head`: any node in a sorted circular singly linked list, or `None` for an empty list.
- `insertVal`: the value to store in the newly allocated node.

**Return value**

Insert exactly one node and preserve the circular, non-descending cyclic order. Return the original linked-list head node when the input is nonempty; otherwise return the newly created self-linked node. Any insertion location satisfying the order contract is valid.
