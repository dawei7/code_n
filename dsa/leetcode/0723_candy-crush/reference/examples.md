## Examples

**Example 1**

The source visual shows the initial board, the state after the first complete round, and the final stable board. Coordinates below are 1-based.

**Initial board**

```text
110   5 112 113  114
210 211   5 213  214
310 311   3 313  314
410 411 412   5  414
  5   1 512   3    3
610   4   1 613  614
710   1   2 713  714
810   1   2   1    1
  1   1   2   2    2
  4   1   4   4 1014
```

The first simultaneous crush removes the four `1` candies in column 2 from rows 7 through 10, the three `2` candies in column 3 from rows 7 through 9, and the three `2` candies in row 9 from columns 3 through 5. The intersecting cell at row 9, column 3 is removed once.

**After the first crush and gravity step**

```text
110   0   0   0    0
210   0   0 113  114
310   0   0 213  214
410   0 112 313  314
  5   5   5   5  414
610 211   3   3    3
710 311 412 613  614
810 411 512 713  714
  1   1   1   1    1
  4   4   4   4 1014
```

The next simultaneous crush removes the first four candies in row 5, the last three in row 6, all five in row 9, and the first four in row 10. Gravity then produces the stable state.

**Stable board**

```text
  0   0   0   0    0
  0   0   0   0    0
  0   0   0   0    0
110   0   0   0  114
210   0   0   0  214
310   0   0 113  314
410   0   0 213  414
610 211 112 313  614
710 311 412 613  714
810 411 512 713 1014
```

- Input: `board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]`
- Output: `[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]`

**Example 2**

- Input: `board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]`
- Output: `[[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]`
