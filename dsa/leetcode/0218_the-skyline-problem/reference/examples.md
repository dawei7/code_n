## Examples

**Example 1**

```text
Figure A — input rectangles (horizontal span × height)
  [2,9) × 10    [3,7) × 15    [5,12) × 12
  [15,20) × 10  [19,24) × 8

Figure B — visible contour; ● marks an output key point
  ●(2,10) -> ●(3,15) -> ●(7,12) -> ●(12,0)
             ground gap          -> ●(15,10) -> ●(20,8) -> ●(24,0)

Visible horizontal segments
  [2,3):10  [3,7):15  [7,12):12  [12,15):0
  [15,20):10  [20,24):8  [24,...):0
```

- Input: `buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]`
- Output: `[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]`
- Explanation: Figure A lists the input buildings. Figure B traces their combined outer contour, with every marked point corresponding to a key point in the output.

**Example 2**

- Input: `buildings = [[0,2,3],[2,5,3]]`
- Output: `[[0,3],[5,0]]`
