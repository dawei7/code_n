## Description

You are given an integer `num`. You will apply the following steps to `num` **two** separate times:

<ul>
	<li>Pick a digit `x (0 <= x <= 9)`.</li>
	<li>Pick another digit `y (0 <= y <= 9)`. Note `y` can be equal to `x`.</li>
	<li>Replace all the occurrences of `x` in the decimal representation of `num` by `y`.</li>
</ul>

Let `a` and `b` be the two results from applying the operation to `num` *independently*.

Return *the max difference* between `a` and `b`.

Note that neither `a` nor `b` may have any leading zeros, and **must not** be 0.
