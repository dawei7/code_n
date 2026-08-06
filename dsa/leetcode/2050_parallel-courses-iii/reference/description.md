## Description

You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`. You are also given a 2D integer array `relations` where `relations[j] = [prevCourse_j, nextCourse_j]` denotes that course `prevCourse_j` has to be completed **before** course `nextCourse_j` (prerequisite relationship). Furthermore, you are given a **0-indexed** integer array `time` where `time[i]` denotes how many **months** it takes to complete the `(i+1)^th` course.

You must find the **minimum** number of months needed to complete all the courses following these rules:

<ul>
	<li>You may start taking a course at **any time** if the prerequisites are met.</li>
	<li>**Any number of courses** can be taken at the **same time**.</li>
</ul>

Return *the **minimum** number of months needed to complete all the courses*.

**Note:** The test cases are generated such that it is possible to complete every course (i.e., the graph is a directed acyclic graph).
