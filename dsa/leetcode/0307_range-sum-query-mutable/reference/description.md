## Description

Given an integer array `nums`, handle multiple queries of the following types:

<ol>
	<li>**Update** the value of an element in `nums`.</li>
	<li>Calculate the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** where `left <= right`.</li>
</ol>

Implement the `NumArray` class:

<ul>
	<li>`NumArray(int[] nums)` Initializes the object with the integer array `nums`.</li>
	<li>`void update(int index, int val)` **Updates** the value of `nums[index]` to be `val`.</li>
	<li>`int sumRange(int left, int right)` Returns the **sum** of the elements of `nums` between indices `left` and `right` **inclusive** (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).</li>
</ul>
