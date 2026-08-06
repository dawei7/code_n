## Function Contract

**Inputs**

- `schedule`: a list containing one busy-time schedule per employee. Each employee schedule is a nonempty, sorted list of pairwise non-overlapping `Interval` objects.

In LeetCode's native interface, an interval is an object with integer fields `start` and `end`. The notation `[x, y]` is used only to display an interval compactly: for example, the first interval is read through `schedule[0][0].start` and `schedule[0][0].end`, not through `schedule[0][0][0]`. The cOde(n) adapter accepts the displayed nested-pair form and converts each pair to the corresponding local `Interval` object.

**Return value**

- A chronologically sorted list of finite, positive-length `Interval` objects during which no employee is busy. The cOde(n) adapter serializes these intervals as `[start, end]` pairs.

An endpoint-only meeting such as `[5, 5]` has zero length and must not be returned.
