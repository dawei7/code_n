## Examples

**Example 1**

- Input: `root = [3,2,3,null,3,null,1]`
- Output: `7`
- Explanation: Robbing the root and the two shown grandchildren yields the maximum amount, `3 + 3 + 1 = 7`.

```text
       [3]
       / \
      2   3
       \   \
       [3] [1]
```

**Example 2**

- Input: `root = [3,4,5,1,3,null,1]`
- Output: `9`
- Explanation: Robbing the two children of the root yields the maximum amount, `4 + 5 = 9`.

```text
        3
       / \
     [4] [5]
     / \   \
    1   3   1
```
