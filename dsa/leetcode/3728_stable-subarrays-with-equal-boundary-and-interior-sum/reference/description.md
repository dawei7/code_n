## Description

You are given an integer array `capacity`.

A <span data-keyword="subarray-nonempty">subarray</span> `capacity[l..r]` is considered **stable** if:

<ul>
	<li>Its length is **at least** 3.</li>
	<li>The **first** and **last** elements are each equal to the **sum** of all elements **strictly between** them (i.e., `capacity[l] = capacity[r] = capacity[l + 1] + capacity[l + 2] + ... + capacity[r - 1]`).</li>
</ul>

Return an integer denoting the number of **stable subarrays**.
