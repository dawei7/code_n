## Examples

**Example 1**

- Input: `heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]`
- Output: `4`
- Explanation: Rain forms two small ponds containing `1` and `3` unit cubes, for a total volume of `4`.

The first source 3D illustration is represented by aligned terrain heights and retained water depths:

```text
terrain heights          water depth
1 4 3 1 3 2              0 0 0 0 0 0
3 2 1 3 2 4              0 1 2 0 1 0
2 3 3 2 3 1              0 0 0 0 0 0
```

**Example 2**

- Input: `heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]`
- Output: `10`

The second source illustration shows a height-`3` boundary enclosing all nine interior cells:

```text
terrain heights          water depth to level 3
3 3 3 3 3                0 0 0 0 0
3 2 2 2 3                0 1 1 1 0
3 2 1 2 3                0 1 2 1 0
3 2 2 2 3                0 1 1 1 0
3 3 3 3 3                0 0 0 0 0
```
