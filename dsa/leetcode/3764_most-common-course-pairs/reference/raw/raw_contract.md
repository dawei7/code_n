## Function Contract

**Inputs**

- `course_completions`: The course-completion table described above.

Qualification is evaluated per user across that user's complete history. Both boundaries are inclusive: exactly 5 completions and an average rating exactly equal to 4 qualify.

Consecutive pairs never cross between users. Within a qualifying user's history, the first course of a pair must be followed immediately by the second course in chronological order; skipping an intervening completion does not create another pair.

**Return value**

Return an ordered table with columns:

- `first_course`
- `second_course`
- `transition_count`

`transition_count` is the number of qualifying-user histories in which the named adjacency occurs, counting every occurrence. Rows are ordered by `transition_count` descending, then `first_course` ascending, then `second_course` ascending.
