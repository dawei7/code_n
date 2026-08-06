## Function Contract

**Inputs**

- `head`: the first node of a nonempty singly linked list;
- `m`: the number of nodes to keep at the start of each cycle;
- `n`: the number of following nodes to remove.

The app-local contract uses the package's explicit `ListNode` equivalent, whose
`val` and `next` fields represent the source-native node model. Let $L$ be the
number of nodes in the input list.

**Return value**

Return `head` after modifying the list in place so each cycle keeps up to `m`
available nodes and then removes up to `n` available nodes. Retained nodes keep
their original relative order and identity.
