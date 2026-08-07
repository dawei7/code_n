## Function Contract

**Platform interface**

- `BSTIterator(root)` initializes the iterator with the `root` of a binary search tree.
- `hasNext()` returns `true` if there exists a number in the traversal to the right of the pointer, otherwise `false`.
- `next()` moves the pointer to the right and returns the number at the pointer.
- `hasPrev()` returns `true` if there exists a number in the traversal to the left of the pointer, otherwise `false`.
- `prev()` moves the pointer to the left and returns the number at the pointer.

**Return value**

- `BSTIterator`: None (`null`).
- `hasNext` / `hasPrev`: boolean.
- `next` / `prev`: integer.
