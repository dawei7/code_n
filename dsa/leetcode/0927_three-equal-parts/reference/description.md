## Description

You are given an array `arr` which consists of only zeros and ones, divide the array into **three non-empty parts** such that all of these parts represent the same binary value.

If it is possible, return any `[i, j]` with `i + 1 < j`, such that:

<ul>
	<li>`arr[0], arr[1], ..., arr[i]` is the first part,</li>
	<li>`arr[i + 1], arr[i + 2], ..., arr[j - 1]` is the second part, and</li>
	<li>`arr[j], arr[j + 1], ..., arr[arr.length - 1]` is the third part.</li>
	<li>All three parts have equal binary values.</li>
</ul>

If it is not possible, return `[-1, -1]`.

Note that the entire part is used when considering what binary value it represents. For example, `[1,1,0]` represents `6` in decimal, not `3`. Also, leading zeros **are allowed**, so `[0,1,1]` and `[1,1]` represent the same value.
