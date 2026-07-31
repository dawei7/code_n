## Examples

**Example 1**

- Input: `numCourses = 2, prerequisites = [[1,0]]`
- Output: `true`
- Explanation: Course `0` can be completed first and course `1` afterward, so both courses can be finished.

**Example 2**

- Input: `numCourses = 2, prerequisites = [[1,0],[0,1]]`
- Output: `false`
- Explanation: Course `1` requires course `0`, while course `0` also requires course `1`; the circular dependency makes completion impossible.
