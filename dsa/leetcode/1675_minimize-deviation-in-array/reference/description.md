## Description

You are given an array `nums` of `n` positive integers.

You can perform two types of operations on any element of the array any number of times:

<ul>
	<li>If the element is **even**, **divide** it by `2`.

	<ul>
		<li>For example, if the array is `[1,2,3,4]`, then you can do this operation on the last element, and the array will be `[1,2,3,<u>2</u>].`</li>
	</ul>
	</li>
	<li>If the element is **odd**, **multiply** it by `2`.
	<ul>
		<li>For example, if the array is `[1,2,3,4]`, then you can do this operation on the first element, and the array will be `[<u>2</u>,2,3,4].`</li>
	</ul>
	</li>
</ul>

The **deviation** of the array is the **maximum difference** between any two elements in the array.

Return *the **minimum deviation** the array can have after performing some number of operations.*
