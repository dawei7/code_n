## Description

You have an array of floating point numbers `averages` which is initially empty. You are given an array `nums` of `n` integers where `n` is even.

You repeat the following procedure `n / 2` times:

<ul>
	<li>Remove the **smallest** element, `minElement`, and the **largest** element `maxElement`, from `nums`.</li>
	<li>Add `(minElement + maxElement) / 2` to `averages`.</li>
</ul>

Return the **minimum** element in `averages`.
