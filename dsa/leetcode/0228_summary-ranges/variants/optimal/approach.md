## General
**Extend a run until the first gap**

Keep the position of the first value in the current range. Advance `i` while adjacent values differ by exactly one. The first non-consecutive value closes the current maximal range and begins the next.

At the start of each outer iteration, every value before `i` has been emitted exactly once, and `i` is the first value of the next not-yet-emitted range.

**A first gap proves the range is maximal**

If its first and last values match, emit the single number. Otherwise emit the two endpoints joined by `->`. Intermediate values need no separate storage.

In `[0,1,2,4,5,7]`, the first scan stops after `2`, producing `0->2`. The next stops after `5`, producing `4->5`, and the final singleton produces `7`.

The inner scan extends a range exactly while consecutive membership holds and stops at the first value that cannot belong to it. Thus every emitted interval is maximal. The outer scan resumes at that first excluded value, so the ranges are ordered, disjoint, and cover the entire input.

## Complexity detail
Each element advances `i` once, giving $O(n)$ time. Apart from the required output strings, only positions and endpoint values are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **A set followed by repeated searches:** loses the given order and uses extra space.
- **Expanding every integer inside a range:** does unnecessary work and can be unsafe near integer limits.
- **Empty input:** no range is started, so the result is empty.
- **Integer boundaries:** negative values and boundary-sized integers are formatted normally, and adjacency is checked only between input values.
