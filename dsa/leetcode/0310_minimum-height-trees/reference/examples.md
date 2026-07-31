## Examples

**Example 1**

- Input: `n = 4, edges = [[1,0],[1,2],[1,3]]`
- Output: `[1]`
- Explanation: Rooting the star at node `1` gives height `1`, and no other root does, so node `1` is the only MHT root.

```text
    1
  / | \
 0  2  3

root 1 -> height 1
root 0, 2, or 3 -> height 2
```

**Example 2**

- Input: `n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]`
- Output: `[3,4]`

```text
0   1   2
 \  |  /
    3 -- 4 -- 5

roots 3 and 4 tie for minimum height
```
