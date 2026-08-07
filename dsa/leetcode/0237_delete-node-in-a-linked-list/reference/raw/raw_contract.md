## Function Contract

**Inputs**

- `node`: The non-tail `ListNode` to delete. Its `next` pointer is guaranteed to reference another node.

JSON cases encode the suffix beginning at `node` as an array of values. The runner reconstructs the linked nodes before calling `solve(node)`.

**Return value**

Return nothing and mutate the linked list in place. The runner serializes the suffix after mutation so the removed value and one-node reduction can be judged.
