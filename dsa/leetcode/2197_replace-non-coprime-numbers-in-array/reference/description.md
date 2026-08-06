## Description

You are given an array of integers `nums`. Perform the following steps:

<ol>
	<li>Find **any** two **adjacent** numbers in `nums` that are **non-coprime**.</li>
	<li>If no such numbers are found, **stop** the process.</li>
	<li>Otherwise, delete the two numbers and **replace** them with their **LCM (Least Common Multiple)**.</li>
	<li>**Repeat** this process as long as you keep finding two adjacent non-coprime numbers.</li>
</ol>

Return *the **final** modified array.* It can be shown that replacing adjacent non-coprime numbers in **any** arbitrary order will lead to the same result.

The test cases are generated such that the values in the final array are **less than or equal** to `10^8`.

Two values `x` and `y` are **non-coprime** if `GCD(x, y) > 1` where `GCD(x, y)` is the **Greatest Common Divisor** of `x` and `y`.
