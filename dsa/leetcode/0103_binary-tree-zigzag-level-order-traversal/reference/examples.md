## Examples

**Example 1**

- Input: `root = [3, 9, 20, null, null, 15, 7]`
- Output: `[[3], [20, 9], [15, 7]]`

```text
      3          left to right: [3]
     / \
    9  20        right to left: [20, 9]
      /  \
     15   7      left to right: [15, 7]
```

**Example 2**

- Input: `root = [1]`
- Output: `[[1]]`

**Example 3**

- Input: `root = []`
- Output: `[]`
