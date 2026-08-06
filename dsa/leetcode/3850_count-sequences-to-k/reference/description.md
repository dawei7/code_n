## Description

You are given an integer array `nums`, and an integer `k`.

Start with an initial value `val = 1` and process `nums` from left to right. At each index `i`, you must choose **exactly one** of the following actions:

<ul>
	<li>Multiply `val` by `nums[i]`.</li>
	<li>Divide `val` by `nums[i]`.</li>
	<li>Leave `val` unchanged.</li>
</ul>

After processing all elements, `val` is considered **equal** to `k` only if its final rational value **exactly** equals `k`.

Return the count of **distinct** sequences of choices that result in `val == k`.

**Note:** Division is rational (exact), not integer division. For example, `2 / 4 = 1 / 2`.
