## Examples

**Example 1**

- Input: `root = [1,2,3,null,5,null,4]`
- Output: `[1,3,4]`
- Explanation: Looking from the right reveals `1` at the first level, `3` at the second, and `4` at the third.

```text
        1  <- visible
       / \
      2   3  <- visible
       \   \
        5   4  <- visible
```

**Example 2**

- Input: `root = [1,2,3,4,null,null,null,5]`
- Output: `[1,3,4,5]`
- Explanation: Node `3` blocks `2` at level two. There is no node to the right of `4` at level three or `5` at level four, so both left-subtree nodes remain visible.

```text
        1  <- visible
       / \
      2   3  <- visible
     /
    4  <- visible
   /
  5  <- visible
```

**Example 3**

- Input: `root = [1,null,3]`
- Output: `[1,3]`

**Example 4**

- Input: `root = []`
- Output: `[]`
