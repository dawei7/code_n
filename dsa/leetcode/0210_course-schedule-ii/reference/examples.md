## Examples

**Example 1**

- Input: `numCourses = 2, prerequisites = [[1,0]]`
- Output: `[0,1]`
- Explanation: Course `0` must precede course `1`, so `[0,1]` is the valid order.

**Example 2**

- Input: `numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]`
- Output: `[0,2,1,3]`
- Explanation: Course `0` must come before both `1` and `2`, and both of those courses must come before `3`. Thus `[0,1,2,3]` and `[0,2,1,3]` are both valid orderings.

**Example 3**

- Input: `numCourses = 1, prerequisites = []`
- Output: `[0]`
