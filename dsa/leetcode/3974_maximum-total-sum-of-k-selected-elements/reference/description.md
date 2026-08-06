## Description

You are given an integer array `nums` and two integers `k` and `mul`.

Select **exactly** `k` elements from `nums`. Process these elements one by one in any order you choose.

For each selected element, **independently** choose one of the following:

<ul>
	<li>**Add** the element's value to the total sum, or</li>
	<li>**Multiply** the element by the **current** value of `mul` and **add** the result to the total sum.</li>
</ul>

After processing each selected element, `mul` **decreases** by 1, regardless of which option was chosen. The current value of `mul` may become 0 or negative.

Return an integer denoting the **maximum** possible total sum.
