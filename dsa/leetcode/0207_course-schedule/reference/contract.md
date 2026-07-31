## Function Contract

**Inputs**

- `num_courses`: The number of courses, labeled from `0` through `num_courses - 1`.
- `prerequisites`: Pairs `[course, prerequisite]` describing the required order.

**Return value**

Return `true` if some ordering completes every course, or `false` if the dependencies make that impossible.
