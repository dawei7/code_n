## Description

You are given an integer array `digitSum` of length `n`.

An array `arr` of length `n` is considered **valid** if:

<ul>
	<li>`0 <= arr[i] <= 5000`</li>
	<li>it is **non-decreasing**.</li>
	<li>the **sum of the digits** of `arr[i]` **equals** `digitSum[i]`.</li>
</ul>

Return an integer denoting the number of **distinct valid arrays**. Since the answer may be large, return it modulo `10^9 + 7`.

An array is said to be **non-decreasing** if each element is greater than or equal to the previous element, if it exists.
