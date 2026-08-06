## Description

You are given an array `nums` of `n` integers and two integers `k` and `x`.

The **x-sum** of an array is calculated by the following procedure:

<ul>
	<li>Count the occurrences of all elements in the array.</li>
	<li>Keep only the occurrences of the top `x` most frequent elements. If two elements have the same number of occurrences, the element with the **bigger** value is considered more frequent.</li>
	<li>Calculate the sum of the resulting array.</li>
</ul>

**Note** that if an array has less than `x` distinct elements, its **x-sum** is the sum of the array.

Return an integer array `answer` of length `n - k + 1` where `answer[i]` is the **x-sum** of the <span data-keyword="subarray-nonempty">subarray</span> `nums[i..i + k - 1]`.
