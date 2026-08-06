## Description

There are `n` courses labeled from `1` through `n`. Each unique pair `relations[i] = [prevCourse_i, nextCourse_i]` states that `prevCourse_i` is a prerequisite of `nextCourse_i` and must be taken first.

Within one semester, you may take any number of courses whose entire prerequisite set has already been completed in an earlier semester. Courses that become eligible during a semester therefore wait until the next semester.

Return the minimum number of semesters required to take every course. If the prerequisite relationships make it impossible to complete all courses, return `-1`.
