## Description

You are given a **0-indexed** integer array `nums`. Rearrange the values of `nums` according to the following rules:

<ol>
	<li>Sort the values at **odd indices** of `nums` in **non-increasing** order.

	<ul>
		<li>For example, if `nums = [4,**<u>1</u>**,2,<u>**3**</u>]` before this step, it becomes `[4,<u>**3**</u>,2,**<u>1</u>**]` after. The values at odd indices `1` and `3` are sorted in non-increasing order.</li>
	</ul>
	</li>
	<li>Sort the values at **even indices** of `nums` in **non-decreasing** order.
	<ul>
		<li>For example, if `nums = [<u>**4**</u>,1,<u>**2**</u>,3]` before this step, it becomes `[<u>**2**</u>,1,<u>**4**</u>,3]` after. The values at even indices `0` and `2` are sorted in non-decreasing order.</li>
	</ul>
	</li>
</ol>

Return *the array formed after rearranging the values of* `nums`.
