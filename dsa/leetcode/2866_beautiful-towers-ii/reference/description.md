## Description

You are given a **0-indexed** array `maxHeights` of `n` integers.

You are tasked with building `n` towers in the coordinate line. The `i^th` tower is built at coordinate `i` and has a height of `heights[i]`.

A configuration of towers is **beautiful** if the following conditions hold:

<ol>
	<li>`1 <= heights[i] <= maxHeights[i]`</li>
	<li>`heights` is a **mountain** array.</li>
</ol>

Array `heights` is a **mountain** if there exists an index `i` such that:

<ul>
	<li>For all `0 < j <= i`, `heights[j - 1] <= heights[j]`</li>
	<li>For all `i <= k < n - 1`, `heights[k + 1] <= heights[k]`</li>
</ul>

Return *the **maximum possible sum of heights** of a beautiful configuration of towers*.
