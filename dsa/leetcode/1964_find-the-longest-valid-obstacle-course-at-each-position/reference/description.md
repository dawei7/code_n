## Description

You want to build some obstacle courses. You are given a **0-indexed** integer array `obstacles` of length `n`, where `obstacles[i]` describes the height of the `i^th` obstacle.

For every index `i` between `0` and `n - 1` (**inclusive**), find the length of the **longest obstacle course** in `obstacles` such that:

<ul>
	<li>You choose any number of obstacles between `0` and `i` **inclusive**.</li>
	<li>You must include the `i^th` obstacle in the course.</li>
	<li>You must put the chosen obstacles in the **same order** as they appear in `obstacles`.</li>
	<li>Every obstacle (except the first) is **taller** than or the **same height** as the obstacle immediately before it.</li>
</ul>

Return *an array* `ans` *of length* `n`, *where* `ans[i]` *is the length of the **longest obstacle course** for index* `i`* as described above*.
