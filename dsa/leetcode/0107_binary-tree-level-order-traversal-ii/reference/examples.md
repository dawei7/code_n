## Examples

**Example 1**

- Input: `root = [3, 9, 20, null, null, 15, 7]`
- Output: `[[15, 7], [9, 20], [3]]`

```text
      3          returned last:  [3]
     / \
    9  20        returned second: [9, 20]
      /  \
     15   7      returned first: [15, 7]
```

**Example 2**

- Input: `root = [1]`
- Output: `[[1]]`

**Example 3**

- Input: `root = []`
- Output: `[]`
