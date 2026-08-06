## Description

We have `n` cities labeled from `1` to `n`. Two different cities with labels `x` and `y` are directly connected by a bidirectional road if and only if `x` and `y` share a common divisor **strictly greater** than some `threshold`. More formally, cities with labels `x` and `y` have a road between them if there exists an integer `z` such that all of the following are true:

<ul>
	<li>`x % z == 0`,</li>
	<li>`y % z == 0`, and</li>
	<li>`z > threshold`.</li>
</ul>

Given the two integers, `n` and `threshold`, and an array of `queries`, you must determine for each `queries[i] = [a_i, b_i]` if cities `a_i` and `b_i` are connected directly or indirectly. (i.e. there is some path between them).

Return *an array *`answer`*, where *`answer.length == queries.length`* and *`answer[i]`* is *`true`* if for the *`i^th`* query, there is a path between *`a_i`* and *`b_i`*, or *`answer[i]`* is *`false`* if there is no path.*
