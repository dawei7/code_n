## General
**Translate “doing homework” into one interval predicate**

Student $i$ is active at the query precisely when the query is no earlier than
the start and no later than the finish. The required predicate is therefore
`startTime[i] <= queryTime <= endTime[i]`. Both comparisons are non-strict;
using `<` on either side would incorrectly exclude a student at an endpoint.

**Count each aligned interval once**

Traverse `startTime` and `endTime` together so each pair refers to the same
student. Evaluate the predicate in constant time and add its Boolean result to
the count. There is no interaction between students, no need to merge
overlapping intervals, and no need to simulate every moment between a start
and finish. Overlaps simply cause multiple independent increments.

**Why the final count is exact**

For each index, the inclusive comparison is true exactly when `queryTime`
belongs to that student's closed interval. The scan adds one for every true
predicate and zero for every false one. Since the equal-length arrays provide
one aligned pair per student and every pair is visited once, the accumulated
sum contains every qualifying student exactly once and no nonqualifying
student.

## Complexity detail
Let $n$ be the number of students. The scan performs two comparisons and a
constant-time count update for each aligned pair, taking $O(n)$ time. It keeps
only the running count and loop values, so its auxiliary space is $O(1)$.
The magnitudes and lengths of the time intervals do not affect the work.

## Alternatives and edge cases
- **Sort starts and finishes:** Count starts at or before the query and subtract
  finishes strictly before it using binary search. This can answer many query
  times efficiently after preprocessing, but for one query it adds
  $O(n\log n)$ sorting work and extra storage.
- **Simulate every time unit:** Walk from each start through its finish looking
  for the query. This is correct but can take work proportional to total
  interval duration instead of $n$.
- **Difference array over the time domain:** Mark interval starts and the point
  after each finish, then prefix-sum to the query. The bounded time domain makes
  this possible, but it allocates domain-sized storage for a single query.
- **Query equals a start:** Count the student because the left endpoint is
  inclusive.
- **Query equals a finish:** Count the student because the right endpoint is
  inclusive.
- **Start equals finish:** The student is active at that one time only.
- **Overlapping intervals:** Count every containing interval separately; do not
  merge them into one active period.
- **Query outside all intervals:** Return zero.
