## Function Contract

**Inputs**

- `p`: A node object in a parent-linked binary tree.
- `q`: A different node object in the same parent-linked binary tree.

```python
class Node:

    def __init__(
        self,
        val: int = 0,
        left: Node | None = None,
        right: Node | None = None,
        parent: Node | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
```

**Return value**

Return the `Node` object that is the lowest common ancestor of `p` and `q`.
