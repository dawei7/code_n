## Description

*(This problem is an **interactive problem**.)*

You may recall that an array `arr` is a **mountain array** if and only if:

<ul>
	<li>`arr.length >= 3`</li>
	<li>There exists some `i` with `0 < i < arr.length - 1` such that:
	<ul>
		<li>`arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`</li>
		<li>`arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`</li>
	</ul>
	</li>
</ul>

Given a mountain array `mountainArr`, return the **minimum** `index` such that `mountainArr.get(index) == target`. If such an `index` does not exist, return `-1`.

**You cannot access the mountain array directly.** You may only access the array using a `MountainArray` interface:

<ul>
	<li>`MountainArray.get(k)` returns the element of the array at index `k` (0-indexed).</li>
	<li>`MountainArray.length()` returns the length of the array.</li>
</ul>

Submissions making more than `100` calls to `MountainArray.get` will be judged *Wrong Answer*. Also, any solutions that attempt to circumvent the judge will result in disqualification.
