## Description

You are given an integer array `nums` of length `n`.

Construct a new array `ans` of length `2 * n` such that the first `n` elements are the same as `nums`, and the next `n` elements are the elements of `nums` in reverse order.

Formally, for `0 <= i <= n - 1`:

<ul>
	<li>`ans[i] = nums[i]`</li>
	<li>`ans[i + n] = nums[n - i - 1]`</li>
</ul>

Return an integer array `ans`.
