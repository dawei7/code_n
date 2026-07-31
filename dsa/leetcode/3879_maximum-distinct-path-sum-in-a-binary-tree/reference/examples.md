## Examples

**Example 1**

```text
    2
   / \
  2   1
```

- Input: `root = [2,2,1]`
- Output: `3`
- Explanation:

  - The left child-to-root path `2 -> 2` repeats value `2`, so it is invalid.
  - The best valid path connects the root value `2` to the right child value `1`, giving `2 + 1 = 3`.

**Example 2**

```text
      1
     / \
   -2   5
       / \
      3   5
```

- Input: `root = [1,-2,5,null,null,3,5]`
- Output: `9`
- Explanation:

  - The path `3 -> 5 -> 5` is invalid because value `5` occurs twice.
  - The maximum valid path is `1 -> 5 -> 3`, whose sum is `1 + 5 + 3 = 9`.

**Example 3**

```text
    4
   / \
  6   6
       \
        9
```

- Input: `root = [4,6,6,null,null,null,9]`
- Output: `19`
- Explanation:

  - The path `6 -> 4 -> 6 -> 9` beginning at the left child repeats value `6` and is invalid.
  - The maximum valid path uses the root, right child, and grandchild: `4 -> 6 -> 9`, with sum `4 + 6 + 9 = 19`.
