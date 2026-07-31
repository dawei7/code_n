## Examples

**Example 1**

- Input: `occupiedIntervals = [[2,6],[4,8],[10,10],[10,12],[14,16]], freeStart = 7, freeEnd = 11`
- Output: `[[2,6],[12,12],[14,16]]`
- **Explanation:** Merging the occupied input produces `[2,8]`, `[10,12]`, and `[14,16]`. Removing every point from `7` through `11` leaves `[2,6]`, the single point `[12,12]`, and the unchanged interval `[14,16]`.

**Example 2**

- Input: `occupiedIntervals = [[1,5],[2,3]], freeStart = 3, freeEnd = 8`
- Output: `[[1,2]]`
- **Explanation:** The overlapping inputs first combine into `[1,5]`. Excluding all points in `[3,8]` removes the right part of that merged interval, leaving `[1,2]`.
