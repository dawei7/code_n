## Examples

**Example 1**

- Input: `root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], targetSum = 22`
- Output: `true`
- Explanation: The highlighted root-to-leaf route reaches the requested sum: `5 + 4 + 11 + 2 = 22`.

```text
             [5]
            /   \
          [4]    8
          /     / \
        [11]   13  4
        /  \       \
       7   [2]      1
```

**Example 2**

- Input: `root = [1, 2, 3], targetSum = 5`
- Output: `false`
- Explanation: The tree has two root-to-leaf paths. Their sums are `1 + 2 = 3` and `1 + 3 = 4`, so neither reaches `5`.

```text
    1
   / \
  2   3
```

**Example 3**

- Input: `root = [], targetSum = 0`
- Output: `false`
- Explanation: An empty tree contains no root-to-leaf path.
