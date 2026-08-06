## Description

You are given a **0-indexed** integer array `nums` containing **positive** integers.

Your task is to **minimize** the length of `nums` by performing the following operations **any** number of times (including zero):

<ul>
	<li>Select **two** **distinct** indices `i` and `j` from `nums`, such that `nums[i] > 0` and `nums[j] > 0`.</li>
	<li>Insert the result of `nums[i] % nums[j]` at the end of `nums`.</li>
	<li>Delete the elements at indices `i` and `j` from `nums`.</li>
</ul>

Return *an integer denoting the **minimum** **length** of *`nums`* after performing the operation any number of times.*
