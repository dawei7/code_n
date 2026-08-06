## Description

You are given three positive integers: `n`, `index`, and `maxSum`. You want to construct an array `nums` (**0-indexed**)** **that satisfies the following conditions:

<ul>
	<li>`nums.length == n`</li>
	<li>`nums[i]` is a **positive** integer where `0 <= i < n`.</li>
	<li>`abs(nums[i] - nums[i+1]) <= 1` where `0 <= i < n-1`.</li>
	<li>The sum of all the elements of `nums` does not exceed `maxSum`.</li>
	<li>`nums[index]` is **maximized**.</li>
</ul>

Return `nums[index]`* of the constructed array*.

Note that `abs(x)` equals `x` if `x >= 0`, and `-x` otherwise.
