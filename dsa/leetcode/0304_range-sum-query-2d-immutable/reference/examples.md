## Examples

**Example 1**

- Input: `["NumMatrix","sumRegion","sumRegion","sumRegion"], [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]`
- Output: `[null,8,11,12]`
- Explanation: Construct `NumMatrix` from the displayed $5 \times 5$ matrix. The inclusive rectangle from `(2,1)` to `(4,3)` sums to `8`; the rectangle from `(1,1)` to `(2,2)` sums to `11`; and the rectangle from `(1,2)` to `(2,4)` sums to `12`.

The source illustration highlights these three overlapping rectangles. Here they are identified by coordinates against the same matrix:

```text
       c0 c1 c2 c3 c4
r0      3  0  1  4  2
r1      5  6  3  2  1
r2      1  2  0  1  5
r3      4  1  0  1  7
r4      1  0  3  0  5

R: rows 2..4, columns 1..3 -> 8
G: rows 1..2, columns 1..2 -> 11
B: rows 1..2, columns 2..4 -> 12
```
