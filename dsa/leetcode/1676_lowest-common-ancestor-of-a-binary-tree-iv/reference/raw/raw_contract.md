## Function Contract

**Inputs**

- `root`: The root `TreeNode` of a binary tree containing $N$ nodes with unique values.
- `nodes`: A nonempty list of $K$ distinct `TreeNode` references drawn from that same tree.

```python
class TreeNode:

    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right
```

**Return value**

Return the `TreeNode` object that is the lowest common ancestor shared by every supplied target node in `nodes`.
