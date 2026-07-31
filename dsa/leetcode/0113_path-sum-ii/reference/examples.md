## Examples

**Example 1**

- Input: `root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], targetSum = 22`
- Output: `[[5, 4, 11, 2], [5, 8, 4, 5]]`
- Explanation: Exactly two root-to-leaf paths reach the target: `5 + 4 + 11 + 2 = 22` and `5 + 8 + 4 + 5 = 22`.

```text
             [5]
            /   \
          [4]   [8]
          /     / \
        [11]   13 [4]
        /  \      / \
       7   [2]  [5]  1
```

**Example 2**

- Input: `root = [1, 2, 3], targetSum = 5`
- Output: `[]`

```text
    1
   / \
  2   3
```

**Example 3**

- Input: `root = [1, 2], targetSum = 0`
- Output: `[]`
