## Description

You are given two integer arrays `nums` and `target`, each of length `n`, where `nums[i]` is the current value at index `i` and `target[i]` is the desired value at index `i`.

You may perform the following operation any number of times (including zero):

<ul>
	<li>Choose an integer value `x`</li>
	<li>Find all **maximal contiguous segments** where `nums[i] == x` (a segment is **maximal** if it cannot be extended to the left or right while keeping all values equal to `x`)</li>
	<li>For each such segment `[l, r]`, update **simultaneously**:
	<ul>
		<li>`nums[l] = target[l], nums[l + 1] = target[l + 1], ..., nums[r] = target[r]`</li>
	</ul>
	</li>
</ul>

Return the **minimum** number of operations required to make `nums` equal to `target`.
