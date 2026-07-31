## Function Contract

**Inputs**

- `root`: The BST root, encoded in app cases as a level-order array.
- `operations`: A sequence beginning with `BSTIterator`, followed by `next` and `hasNext` calls.

**Return value**

Return one result per operation: `null` for construction, the next integer for `next`, and a boolean for `hasNext`.
