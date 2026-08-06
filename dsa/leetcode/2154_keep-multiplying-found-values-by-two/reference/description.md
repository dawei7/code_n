## Description

You are given an array of integers `nums`. You are also given an integer `original` which is the first number that needs to be searched for in `nums`.

You then do the following steps:

<ol>
	<li>If `original` is found in `nums`, **multiply** it by two (i.e., set `original = 2 * original`).</li>
	<li>Otherwise, **stop** the process.</li>
	<li>**Repeat** this process with the new number as long as you keep finding the number.</li>
</ol>

Return *the **final** value of *`original`.
