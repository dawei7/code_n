## Description

You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`. You are also given an array `relations` where `relations[i] = [prevCourse_i, nextCourse_i]`, representing a prerequisite relationship between course `prevCourse_i` and course `nextCourse_i`: course `prevCourse_i` has to be taken before course `nextCourse_i`. Also, you are given the integer `k`.

In one semester, you can take **at most** `k` courses as long as you have taken all the prerequisites in the **previous** semesters for the courses you are taking.

Return *the **minimum** number of semesters needed to take all courses*. The testcases will be generated such that it is possible to take every course.
