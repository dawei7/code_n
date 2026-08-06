## Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you **must** take course `a_i` first if you want to take course `b_i`.

<ul>
	<li>For example, the pair `[0, 1]` indicates that you have to take course `0` before you can take course `1`.</li>
</ul>

Prerequisites can also be **indirect**. If course `a` is a prerequisite of course `b`, and course `b` is a prerequisite of course `c`, then course `a` is a prerequisite of course `c`.

You are also given an array `queries` where `queries[j] = [u_j, v_j]`. For the `j^th` query, you should answer whether course `u_j` is a prerequisite of course `v_j` or not.

Return *a boolean array *`answer`*, where *`answer[j]`* is the answer to the *`j^th`* query.*
