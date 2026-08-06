## Description

You are given an integer array `nums`, and you can perform the following operation **any** number of times on `nums`:

<ul>
	<li>Swap the positions of two elements `nums[i]` and `nums[j]` if `gcd(nums[i], nums[j]) > 1` where `gcd(nums[i], nums[j])` is the **greatest common divisor** of `nums[i]` and `nums[j]`.</li>
</ul>

Return `true` *if it is possible to sort *`nums`* in **non-decreasing** order using the above swap method, or *`false`* otherwise.*
