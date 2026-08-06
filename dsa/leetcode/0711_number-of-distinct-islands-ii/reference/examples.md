## Examples

In the source diagrams below, `1` is land and `0` is water.

**Example 1**

```text
1 1 0 0 0
1 0 0 0 0
0 0 0 0 1
0 0 0 1 1
```

- Input: `grid = [[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]]`
- Output: `1`
- Explanation: Rotating the first island clockwise by 180 degrees makes its occupied-cell pattern match the second island, so they count as the same shape.

**Example 2**

```text
1 1 0 0 0
1 1 0 0 0
0 0 0 1 1
0 0 0 1 1
```

- Input: `grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]`
- Output: `1`
