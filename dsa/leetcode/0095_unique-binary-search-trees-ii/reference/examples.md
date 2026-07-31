## Examples

**Example 1**

- Input: `n = 3`
- Output: `[[1, null, 2, null, 3], [1, null, 3, 2], [2, 1, 3], [3, 1, null, null, 2], [3, 2, null, 1]]`

The following independent rendering shows the five distinct structures represented by that output:

```text
1       1       2       3       3
 \       \     / \     /       /
  2       3   1   3   1       2
   \     /             \     /
    3   2               2   1
```

**Example 2**

- Input: `n = 1`
- Output: `[[1]]`
