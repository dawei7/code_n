## Description

You are given two positive integer arrays `nums` and `target`, of the same length.

In one operation, you can choose any two **distinct** indices `i` and `j` where `0 <= i, j < nums.length` and:

<ul>
	<li>set `nums[i] = nums[i] + 2` and</li>
	<li>set `nums[j] = nums[j] - 2`.</li>
</ul>

Two arrays are considered to be **similar** if the frequency of each element is the same.

Return *the minimum number of operations required to make *`nums`* similar to *`target`. The test cases are generated such that `nums` can always be similar to `target`.
