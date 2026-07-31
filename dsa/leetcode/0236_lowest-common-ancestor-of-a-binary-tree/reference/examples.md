## Examples

**Example 1**

```text
             [3] LCA
            /       \
         p=5         1=q
        /   \       / \
       6     2     0   8
            / \
           7   4
```

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1`
- Output: `3`
- Explanation: Node `3` is the LCA of nodes `5` and `1`.

**Example 2**

```text
              3
            /   \
     p,LCA=[5]   1
          /   \  / \
         6     2 0 8
              / \
             7  q=4
```

- Input: `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4`
- Output: `5`
- Explanation: Node `5` is the LCA because it is an ancestor of `4`, and a node is allowed to be its own descendant.

**Example 3**

- Input: `root = [1,2], p = 1, q = 2`
- Output: `1`
