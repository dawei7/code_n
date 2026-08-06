## Description

You are given a 2D array `queries`, where `queries[i]` is of the form `[l, r]`. Each `queries[i]` defines an array of integers `nums` consisting of elements ranging from `l` to `r`, both **inclusive**.

In one operation, you can:

<ul>
	<li>Select two integers `a` and `b` from the array.</li>
	<li>Replace them with `floor(a / 4)` and `floor(b / 4)`.</li>
</ul>

Your task is to determine the **minimum** number of operations required to reduce all elements of the array to zero for each query. Return the sum of the results for all queries.
