## Description

You are given an integer array `nums` and a **positive** integer `k`.
A <span data-keyword="subsequence-array">subsequence</span> `sub` of `nums` with length `x` is called **valid** if it satisfies:

<ul>
	<li>`(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.`</li>
</ul>
Return the length of the **longest** **valid** subsequence of `nums`.
