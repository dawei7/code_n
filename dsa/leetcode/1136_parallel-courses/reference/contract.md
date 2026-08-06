## Function Contract

**Inputs**

- `n`: the number of courses, labeled with the consecutive integers from `1` through `n`.
- `relations`: the directed prerequisite relationships. Each unique entry `[prevCourse_i, nextCourse_i]` requires `prevCourse_i` to be completed before `nextCourse_i` may be taken.

Let $r = \lvert\texttt{relations}\rvert$.

There is no limit on how many currently eligible courses can be taken together. A course with several prerequisites becomes eligible only after all of them have been completed in earlier semesters.

**Return value**

- The least number of semesters needed to take every course, or `-1` if no valid completion schedule exists.
