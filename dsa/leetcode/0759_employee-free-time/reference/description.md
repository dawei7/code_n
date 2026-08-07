## Description

We are given a list `schedule` of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping `Intervals`, and these intervals are in sorted order.

Return the list of finite intervals representing **common, positive-length free time** for *all* employees, also in sorted order.

(Even though we are representing `Intervals` in the form `[x, y]`, the objects inside are `Intervals`, not lists or arrays. For example, $\text{schedule}[0][0].start = 1$, $\text{schedule}[0][0].end = 2$, and $\text{schedule}[0][0][0]$ is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
### Function Contract

**Inputs**

- `schedule`: a list containing one busy-time schedule per employee. Each employee schedule is a nonempty, sorted list of pairwise non-overlapping `Interval` objects.

In LeetCode's native interface, an interval is an object with integer fields `start` and `end`. The notation `[x, y]` is used only to display an interval compactly: for example, the first interval is read through `schedule[0][0].start` and `schedule[0][0].end`, not through `schedule[0][0][0]`. The cOde(n) adapter accepts the displayed nested-pair form and converts each pair to the corresponding local `Interval` object.

**Return value**

- A chronologically sorted list of finite, positive-length `Interval` objects during which no employee is busy. The cOde(n) adapter serializes these intervals as `[start, end]` pairs.

An endpoint-only meeting such as `[5, 5]` has zero length and must not be returned.

### Examples
#### Example 1

- **Input:** $schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]$
- **Output:** `[[3,4]]`
- **Explanation:** There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
#### Example 2

- **Input:** $schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]$
- **Output:** `[[5,6],[7,9]]`
### Constraints

- $1 \le \text{schedule.length} , \text{schedule}[i].length \le 50$

- $0 \le \text{schedule}[i].start < \text{schedule}[i].end \le 10^{8}$