## Description

You may recall that an array `arr` is a **mountain array** if and only if:

<ul>
	<li>`arr.length >= 3`</li>
	<li>There exists some index `i` (**0-indexed**) with `0 < i < arr.length - 1` such that:
	<ul>
		<li>`arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`</li>
		<li>`arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`</li>
	</ul>
	</li>
</ul>

Given an integer array `nums`​​​, return *the **minimum** number of elements to remove to make *`nums*​​​*`* **a **mountain array**.*
