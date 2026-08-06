## Description

Given an array of integers `cost` and an integer `target`, return *the **maximum** integer you can paint under the following rules*:

<ul>
	<li>The cost of painting a digit `(i + 1)` is given by `cost[i]` (**0-indexed**).</li>
	<li>The total cost used must be equal to `target`.</li>
	<li>The integer does not have `0` digits.</li>
</ul>

Since the answer may be very large, return it as a string. If there is no way to paint any integer given the condition, return `"0"`.
