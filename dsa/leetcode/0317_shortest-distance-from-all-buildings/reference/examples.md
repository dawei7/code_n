## Examples

**Example 1**

- Input: `grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]`
- Output: `7`
- Explanation: Buildings occupy `(0,0)`, `(0,4)`, and `(2,2)`, while `(0,2)` is an obstacle. Building a house at `(1,2)` gives shortest distances `3`, `3`, and `1`, whose minimum total is `7`.

```text
1 0 2 0 1
0 0 H 0 0    H = chosen empty land at (1,2)
0 0 1 0 0
```

**Example 2**

- Input: `grid = [[1,0]]`
- Output: `1`

**Example 3**

- Input: `grid = [[1]]`
- Output: `-1`
