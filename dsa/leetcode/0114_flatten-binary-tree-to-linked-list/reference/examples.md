## Examples

**Example 1**

- Input: `root = [1, 2, 5, 3, 4, null, 6]`
- Output: `[1, null, 2, null, 3, null, 4, null, 5, null, 6]`

```text
Before:                 After:
      1                 1
     / \                 \
    2   5                 2
   / \   \                 \
  3   4   6                 3
                             \
                              4
                               \
                                5
                                 \
                                  6
```

**Example 2**

- Input: `root = []`
- Output: `[]`

**Example 3**

- Input: `root = [0]`
- Output: `[0]`
