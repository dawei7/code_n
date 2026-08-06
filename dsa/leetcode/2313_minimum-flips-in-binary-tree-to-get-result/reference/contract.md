## Function Contract

**Inputs**

- `root`: The root `TreeNode` of a nonempty binary tree where node values are 0 (false), 1 (true), 2 (OR), 3 (AND), 4 (XOR), or 5 (NOT).

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

- `result`: A boolean value (`True` or `False`) that the root must evaluate to.

**Return value**

Return an integer representing the minimum number of leaf flips required so that the root evaluates to `result`.
