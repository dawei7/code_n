## Examples

**Example 1**

- Input: `root = [2, 1, 3]`
- Output: `true`

```text
  2
 / \
1   3
```

**Example 2**

- Input: `root = [5, 1, 4, null, null, 3, 6]`
- Output: `false`
- Explanation: Node `4` is the right child of root `5`, but `4 < 5`, violating the required ordering.

```text
    5
   / \
  1   4  ← invalid on the right of 5
     / \
    3   6
```
