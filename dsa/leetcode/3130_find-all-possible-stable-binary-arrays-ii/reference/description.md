## Description

You are given 3 positive integers `num_zeros`, `num_ones`, and `limit`.

A <span data-keyword="binary-array">binary array</span> `arr` is called **stable** if:

<ul>
	<li>The number of occurrences of 0 in `arr` is **exactly **`num_zeros`.</li>
	<li>The number of occurrences of 1 in `arr` is **exactly** `num_ones`.</li>
	<li>Each <span data-keyword="subarray-nonempty">subarray</span> of `arr` with a size greater than `limit` must contain **at least** one occurrence of **both** 0 and 1.</li>
</ul>

Return an integer denoting the *total* number of **stable** binary arrays.

Since the answer may be very large, return it **modulo** `10^9 + 7`.
