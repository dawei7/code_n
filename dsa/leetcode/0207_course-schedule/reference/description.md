### 1. Description

There are a total of `numCourses` courses you have to take, labeled from `0` to $numCourses - 1$. You are given an array `prerequisites` where $\text{prerequisites}[i] = [a_{i}, b_{i}]$ indicates that you **must** take course $b_{i}$ first if you want to take course $a_{i}$.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

### 2. Function Contract

**Inputs**

- `numCourses`: The number of courses, labeled from `0` through $numCourses - 1$.
- `prerequisites`: Pairs `[course, prerequisite]` describing the required order.

**Return value**

Return `true` if some ordering completes every course, or `false` if the dependencies make that impossible.

### 3. Examples

#### Example 1

- **Input:** $numCourses = 2, prerequisites = [[1,0]]$
- **Output:** `true`
- **Explanation:** There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
#### Example 2

- **Input:** $numCourses = 2, prerequisites = [[1,0],[0,1]]$
- **Output:** `false`
- **Explanation:** There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

### 4. Constraints

- $1 \le numCourses \le 2000$

- $0 \le \text{prerequisites.length} \le 5000$

- $\text{prerequisites}[i].length = 2$

- $0 \le a_{i}, b_{i} < numCourses$

- All the pairs prerequisites[i] are **unique**.