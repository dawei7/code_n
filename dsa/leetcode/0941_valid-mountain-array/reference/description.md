## Description

Given an array of integers `arr`, return *`true` if and only if it is a valid mountain array*.

Recall that arr is a mountain array if and only if:

<ul>
	<li>`arr.length >= 3`</li>
	<li>There exists some `i` with `0 < i < arr.length - 1` such that:
	<ul>
		<li>`arr[0] < arr[1] < ... < arr[i - 1] < arr[i] `</li>
		<li>`arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`</li>
	</ul>
	</li>
</ul>
<img src="https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png" width="500" />
