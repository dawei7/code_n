## Description

You are given a **bitonic** array `nums` of length `n`.

Split the array into **two** parts:

<ul>
	<li>**Ascending part**: from index 0 to the peak element (inclusive).</li>
	<li>**Descending part**: from the peak element to index `n - 1` (inclusive).</li>
</ul>

The peak element belongs to both parts.

Return:

<ul>
	<li>0 if the sum of the **ascending** part is greater.</li>
	<li>1 if the sum of the **descending** part is greater.</li>
	<li>-1 if both sums are **equal**.</li>
</ul>

**Notes**:

<ul>
	<li>A **bitonic** array is an array that is **strictly increasing** up to a **single peak** element and then **strictly decreasing**.</li>
	<li>An array is said to be **strictly increasing** if each element is **strictly greater** than its **previous** one (if exists).</li>
	<li>An array is said to be **strictly decreasing** if each element is **strictly smaller** than its **previous** one (if exists).</li>
</ul>
