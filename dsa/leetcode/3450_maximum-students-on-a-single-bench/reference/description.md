## Description

You are given a 2D integer array of student data `students`, where $\text{students}[i] = [\text{student}_{id}, \text{bench}_{id}]$ represents that student $\text{student}_{id}$ is sitting on the bench $\text{bench}_{id}$.

Return the **maximum** number of *unique* students sitting on any single bench. If no students are present, return 0.

**Note**: A student can appear multiple times on the same bench in the input, but they should be counted only once per bench.
### Function Contract

- Refer to method signature.

### Examples

#### Example 1

<div class="example-block">
**Input:** students = [[1,2],[2,2],[3,3],[1,3],[2,3]]

**Output:** 3

**Explanation:**

- Bench 2 has two unique students: `[1, 2]`.

- Bench 3 has three unique students: `[1, 2, 3]`.

- The maximum number of unique students on a single bench is 3.

</div>
#### Example 2

<div class="example-block">
**Input:** students = [[1,1],[2,1],[3,1],[4,2],[5,2]]

**Output:** 3

**Explanation:**

- Bench 1 has three unique students: `[1, 2, 3]`.

- Bench 2 has two unique students: `[4, 5]`.

- The maximum number of unique students on a single bench is 3.

</div>
#### Example 3

<div class="example-block">
**Input:** students = [[1,1],[1,1]]

**Output:** 1

**Explanation:**

- The maximum number of unique students on a single bench is 1.

</div>
#### Example 4

<div class="example-block">
**Input:** students = []

**Output:** 0

**Explanation:**

- Since no students are present, the output is 0.

</div>
### Constraints

- $0 \le \text{students.length} \le 100$

- $\text{students}[i] = [\text{student}_{id}, \text{bench}_{id}]$

- $1 \le \text{student}_{id} \le 100$

- $1 \le \text{bench}_{id} \le 100$