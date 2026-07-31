## Examples

**Example 1**

- Input: `root = [1, 2, 3, 4, 5, 6, 7]`
- Output: `[1, #, 2, 3, #, 4, 5, 6, 7, #]`
- Explanation: Each node is linked to the next node on its level, including across parent boundaries. The serialized result follows those `next` links in level order, and `#` ends each level.

```text
        1 -> NULL
      /   \
     2 --> 3 -> NULL
    / \   / \
   4 -> 5 -> 6 -> 7 -> NULL
```

**Example 2**

- Input: `root = []`
- Output: `[]`
