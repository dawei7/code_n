## Description

You are given a 2D integer array of student data `students`, where `students[i] = [student_id, bench_id]` represents that student `student_id` is sitting on the bench `bench_id`.

Return the **maximum** number of *unique* students sitting on any single bench. If no students are present, return 0.

**Note**: A student can appear multiple times on the same bench in the input, but they should be counted only once per bench.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">students = [[1,2],[2,2],[3,3],[1,3],[2,3]]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- Bench 2 has two unique students: `[1, 2]`.

	- Bench 3 has three unique students: `[1, 2, 3]`.

	- The maximum number of unique students on a single bench is 3.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">students = [[1,1],[2,1],[3,1],[4,2],[5,2]]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- Bench 1 has three unique students: `[1, 2, 3]`.

	- Bench 2 has two unique students: `[4, 5]`.

	- The maximum number of unique students on a single bench is 3.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">students = [[1,1],[1,1]]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- The maximum number of unique students on a single bench is 1.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">students = []</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- Since no students are present, the output is 0.

</div>

**Constraints:**

	- `0 <= students.length <= 100`

	- `students[i] = [student_id, bench_id]`

	- `1 <= student_id <= 100`

	- `1 <= bench_id <= 100`
