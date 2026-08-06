## Description

You are given an array of **positive** integers `nums`.

An array `arr` is called **product equivalent** if `prod(arr) == lcm(arr) * gcd(arr)`, where:

<ul>
	<li>`prod(arr)` is the product of all elements of `arr`.</li>
	<li>`gcd(arr)` is the <span data-keyword="gcd-function">GCD</span> of all elements of `arr`.</li>
	<li>`lcm(arr)` is the <span data-keyword="lcm-function">LCM</span> of all elements of `arr`.</li>
</ul>

Return the length of the **longest** **product equivalent** <span data-keyword="subarray-nonempty">subarray</span> of `nums`.
