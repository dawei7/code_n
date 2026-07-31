## Examples

**Example 1**

- Input: `root = [1, null, 2, 3]`
- Output: `[1, 2, 3]`
- Explanation: Preorder visits the root `1`, then the right-subtree root `2`, and then `2`'s left child `3`.

```text
1
 \
  2
 /
3
Traversal: 1 -> 2 -> 3
```

**Example 2**

- Input: `root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]`
- Output: `[1, 2, 4, 5, 6, 7, 3, 8, 9]`
- Explanation: Visiting each node before its left and right subtrees produces the marked order.

```text
          1
        /   \
       2     3
      / \     \
     4   5     8
        / \   /
       6   7 9
Traversal: 1 -> 2 -> 4 -> 5 -> 6 -> 7 -> 3 -> 8 -> 9
```

**Example 3**

- Input: `root = []`
- Output: `[]`

**Example 4**

- Input: `root = [1]`
- Output: `[1]`
