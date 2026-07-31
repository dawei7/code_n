## Examples

**Example 1**

- Input: `operations = ["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"], arguments = [[],[1],[],[3],[],[7],[],[2],[],[6],[]]`
- Output: `[null,null,[[1,1]],null,[[1,1],[3,3]],null,[[1,1],[3,3],[7,7]],null,[[1,3],[7,7]],null,[[1,3],[6,7]]]`
- Explanation:
  - Constructing `SummaryRanges` starts with an empty stream.
  - After `addNum(1)`, the observed values are `[1]`; `getIntervals()` returns `[[1,1]]`.
  - After `addNum(3)`, the values are `[1,3]`; `getIntervals()` returns `[[1,1],[3,3]]`.
  - After `addNum(7)`, the values are `[1,3,7]`; `getIntervals()` returns `[[1,1],[3,3],[7,7]]`.
  - After `addNum(2)`, the values are `[1,2,3,7]`; `getIntervals()` returns `[[1,3],[7,7]]`.
  - After `addNum(6)`, the values are `[1,2,3,6,7]`; `getIntervals()` returns `[[1,3],[6,7]]`.
