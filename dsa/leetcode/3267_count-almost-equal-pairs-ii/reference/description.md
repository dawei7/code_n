## Description

**Attention**: In this version, the number of operations that can be performed, has been increased to **twice**.<!-- notionvc: 278e7cb2-3b05-42fa-8ae9-65f5fd6f7585 -->

You are given an array `nums` consisting of positive integers.

We call two integers `x` and `y` **almost equal** if both integers can become equal after performing the following operation **at most <u>twice</u>**:

<ul>
	<li>Choose **either** `x` or `y` and swap any two digits within the chosen number.</li>
</ul>

Return the number of indices `i` and `j` in `nums` where `i < j` such that `nums[i]` and `nums[j]` are **almost equal**.

**Note** that it is allowed for an integer to have leading zeros after performing an operation.
