## Description

You are given a **sorted** array `nums` of `n` non-negative integers and an integer `maximumBit`. You want to perform the following query `n` **times**:

<ol>
	<li>Find a non-negative integer `k < 2^maximumBit` such that `nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k` is **maximized**. `k` is the answer to the `i^th` query.</li>
	<li>Remove the **last **element from the current array `nums`.</li>
</ol>

Return *an array* `answer`*, where *`answer[i]`* is the answer to the *`i^th`* query*.
