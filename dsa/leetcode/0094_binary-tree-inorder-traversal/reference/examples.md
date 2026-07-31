## Examples

**Example 1**

- Input: `root = [1, null, 2, 3]`
- Output: `[1, 3, 2]`
- Explanation: The independent tree diagram makes the inorder sequence `1 → 3 → 2` visible.

```text
1
 \
  2
 /
3
```

**Example 2**

- Input: `root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]`
- Output: `[4, 2, 6, 5, 7, 1, 3, 9, 8]`
- Explanation: Traversing the independently rendered tree left subtree, node, then right subtree produces the stated output.

```text
        1
      /   \
     2     3
    / \     \
   4   5     8
      / \   /
     6   7 9
```

**Example 3**

- Input: `root = []`
- Output: `[]`

**Example 4**

- Input: `root = [1]`
- Output: `[1]`
