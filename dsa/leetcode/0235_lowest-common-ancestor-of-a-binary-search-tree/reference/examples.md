## Examples

**Example 1**

```text
          [6] LCA
         /   \
      p=2     8=q
      / \     / \
     0   4   7   9
        / \
       3   5
```

- Input: `root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8`
- Output: `6`
- Explanation: Node `6` is the lowest node whose subtree contains both nodes `2` and `8`.

**Example 2**

```text
           6
          / \
   p,LCA=[2] 8
         / \  / \
        0  q=4 7 9
          / \
         3   5
```

- Input: `root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4`
- Output: `2`
- Explanation: Node `2` is the LCA because it is an ancestor of `4`, and a node is allowed to be a descendant of itself.

**Example 3**

- Input: `root = [2,1], p = 2, q = 1`
- Output: `2`
