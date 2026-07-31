## Examples

**Example 1**

- Input: `root = [1, 3, null, null, 2]`
- Output: `[3, 1, null, null, 2]`
- Explanation: Value `3` cannot be a left child of `1` because $3>1$. Swapping values `1` and `3` restores the BST.

```text
  1            3
 /            /
3      -->   1
 \            \
  2            2
```

**Example 2**

- Input: `root = [3, 1, 4, null, null, 2]`
- Output: `[2, 1, 4, null, null, 3]`
- Explanation: Value `2` cannot lie in the right subtree of `3` because $2<3$. Exchanging values `2` and `3` restores the ordering.

```text
    3              2
   / \            / \
  1   4   -->    1   4
     /              /
    2              3
```
