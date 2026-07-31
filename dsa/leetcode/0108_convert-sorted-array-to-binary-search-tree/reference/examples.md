## Examples

**Example 1**

- Input: `nums = [-10, -3, 0, 5, 9]`
- Output: `[0, -3, 9, -10, null, 5]`

```text
       0
      / \
    -3   9
    /   /
 -10   5
```

- Explanation: This is one accepted height-balanced binary search tree. The tree `[0, -10, 5, null, -3, null, 9]` is also accepted:

```text
       0
      / \
   -10   5
      \   \
      -3   9
```

**Example 2**

- Input: `nums = [1, 3]`
- Output: `[3, 1]`

- Explanation: Both `[1, null, 3]` and `[3, 1]` represent height-balanced binary search trees:

```text
  1       3
   \     /
    3   1
```
