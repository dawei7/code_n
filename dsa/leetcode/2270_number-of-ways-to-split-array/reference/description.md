## Description

You are given a **0-indexed** integer array `nums` of length `n`.

`nums` contains a **valid split** at index `i` if the following are true:

<ul>
	<li>The sum of the first `i + 1` elements is **greater than or equal to** the sum of the last `n - i - 1` elements.</li>
	<li>There is **at least one** element to the right of `i`. That is, `0 <= i < n - 1`.</li>
</ul>

Return *the number of **valid splits** in* `nums`.
