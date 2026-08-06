## Examples

**Example 1**

- Input: `grid = [[0, 1], [1, 0]]`
- Output: `[[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]`
- Explanation: The source input-grid image contains the following cells. In the source tree image, `0` represents
  `False` and `1` represents `True`; the root is internal, and its four one-cell leaves follow quadrant order.

| Row | Column 0 | Column 1 |
|---:|---:|---:|
| 0 | 0 | 1 |
| 1 | 1 | 0 |

The corresponding tree relationships are:

| Node | Region | `[isLeaf, val]` | Children |
|---:|---|---|---|
| 0 | whole grid | `[0, 1]` | nodes 1, 2, 3, 4 |
| 1 | top-left | `[1, 0]` | none |
| 2 | top-right | `[1, 1]` | none |
| 3 | bottom-left | `[1, 1]` | none |
| 4 | bottom-right | `[1, 0]` | none |

**Example 2**

- Input: `grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]`
- Output: `[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]`
- Explanation: The complete grid is mixed, so it splits into four quadrants. The top-left, bottom-left, and
  bottom-right quadrants are uniform leaves. The top-right quadrant is mixed and splits once more into four uniform
  leaves. The source matrix image contains these eight rows:

| Row | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 4 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 5 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 6 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 7 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |

The source tree image is fully represented by this relationship table:

| Node | Region | `[isLeaf, val]` | Children in quadrant order |
|---:|---|---|---|
| 0 | whole grid | `[0, 1]` | nodes 1, 2, 3, 4 |
| 1 | top-left | `[1, 1]` | none |
| 2 | top-right | `[0, 1]` | nodes 5, 6, 7, 8 |
| 3 | bottom-left | `[1, 1]` | none |
| 4 | bottom-right | `[1, 0]` | none |
| 5 | top-right / top-left | `[1, 0]` | none |
| 6 | top-right / top-right | `[1, 0]` | none |
| 7 | top-right / bottom-left | `[1, 1]` | none |
| 8 | top-right / bottom-right | `[1, 1]` | none |
