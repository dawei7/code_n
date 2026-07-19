## General
**Extend a run until the first gap**

Keep the first value of the current range. Advance one index while adjacent values differ by exactly one. The first non-consecutive value closes the current maximal range and begins the next.

At the start of each outer iteration, every value before the current index has been emitted exactly once, and the current index is the first value of the next not-yet-emitted range.

**A first gap proves the range is maximal**

If its first and last values match, emit the single number. Otherwise emit the two endpoints joined by `->`. Intermediate values need no separate storage.

In `[0,1,2,4,5,7]`, the first scan stops after `2`, producing `0->2`. The next stops after `5`, producing `4->5`, and the final singleton produces `7`.

The inner scan extends a range exactly while consecutive membership holds and stops at the first value that cannot belong to it. Thus every emitted interval is maximal. The outer scan resumes at that first excluded value, so the ranges are ordered, disjoint, and cover the entire input.

## Complexity detail
Each element advances an index once, giving $O(n)$ time. Apart from the required output strings, only indices and endpoint values are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **A set followed by repeated searches:** loses the given order and uses extra space.
- **Expanding every integer inside a range:** does unnecessary work and can be unsafe near integer limits.
- Empty input returns no ranges; negative values and boundary-sized integers are formatted normally.
