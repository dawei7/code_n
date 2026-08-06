## Description

You are given an integer array `nums`. You want to maximize the number of points you get by performing the following operation any number of times:

<ul>
	<li>Pick any `nums[i]` and delete it to earn `nums[i]` points. Afterwards, you must delete **every** element equal to `nums[i] - 1` and **every** element equal to `nums[i] + 1`.</li>
</ul>

Return *the **maximum number of points** you can earn by applying the above operation some number of times*.
