## Examples

**Example 1**

- Input: `root = [1, null, 2, 3]`
- Output: `[3, 2, 1]`
- Explanation: Postorder visits node `3`, then its parent `2`, and finally the original root `1`.

```text
1
 \
  2
 /
3
Traversal: 3 -> 2 -> 1
```

**Example 2**

- Input: `root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]`
- Output: `[4, 6, 7, 5, 2, 9, 8, 3, 1]`
- Explanation: Completing both subtrees before each root gives the marked order.

```text
          1
        /   \
       2     3
      / \     \
     4   5     8
        / \   /
       6   7 9
Traversal: 4 -> 6 -> 7 -> 5 -> 2 -> 9 -> 8 -> 3 -> 1
```

**Example 3**

- Input: `root = []`
- Output: `[]`

**Example 4**

- Input: `root = [1]`
- Output: `[1]`
