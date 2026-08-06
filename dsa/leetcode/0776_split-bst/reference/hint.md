## Hint

Use recursion. When `root.val <= target`, split `root.right`, then reconnect the returned smaller half as `root.right`. The opposite comparison is symmetric on the left child.
