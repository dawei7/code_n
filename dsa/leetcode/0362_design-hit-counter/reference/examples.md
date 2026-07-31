## Examples

**Example 1**

- Input: `operations = ["HitCounter","hit","hit","hit","getHits","hit","getHits","getHits"], arguments = [[],[1],[2],[3],[4],[300],[300],[301]]`
- Output: `[null,null,null,null,3,null,4,3]`
- Explanation:
  1. Construct an empty `HitCounter`.
  2. Record hits at times `1`, `2`, and `3`.
  3. At time `4`, all three hits lie in the five-minute window, so `getHits(4)` returns `3`.
  4. Record another hit at time `300`.
  5. At time `300`, the four recorded hits are still counted, so `getHits(300)` returns `4`.
  6. At time `301`, the hit at time `1` is exactly `300` seconds old and expires; `getHits(301)` returns `3`.
