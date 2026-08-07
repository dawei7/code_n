## Function Contract

**Input**

- `node`: the selected node in a binary search tree with unique values

**Return value**

- Return the successor `Node` itself, or `None` if `node` is last in inorder order.

Each `Node` contains these fields:

- `val`: its integer key
- `left`: its left child or `None`
- `right`: its right child or `None`
- `parent`: its parent or `None` at the root

The caller supplies `node`, not the tree root. Returning only the successor's value does not satisfy the contract.
