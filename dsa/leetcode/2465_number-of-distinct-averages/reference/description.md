## Description

You are given a **0-indexed** integer array `nums` of **even** length.

As long as `nums` is **not** empty, you must repetitively:

<ul>
	<li>Find the minimum number in `nums` and remove it.</li>
	<li>Find the maximum number in `nums` and remove it.</li>
	<li>Calculate the average of the two removed numbers.</li>
</ul>

The **average** of two numbers `a` and `b` is `(a + b) / 2`.

<ul>
	<li>For example, the average of `2` and `3` is `(2 + 3) / 2 = 2.5`.</li>
</ul>

Return* the number of **distinct** averages calculated using the above process*.

**Note** that when there is a tie for a minimum or maximum number, any can be removed.
