## Description

You are given an integer `n`. You roll a fair 6-sided dice `n` times. Determine the total number of **distinct** sequences of rolls possible such that the following conditions are satisfied:

<ol>
	<li>The **greatest common divisor** of any **adjacent** values in the sequence is equal to `1`.</li>
	<li>There is **at least** a gap of `2` rolls between **equal** valued rolls. More formally, if the value of the `i^th` roll is **equal** to the value of the `j^th` roll, then `abs(i - j) > 2`.</li>
</ol>

Return *the** total number** of distinct sequences possible*. Since the answer may be very large, return it **modulo** `10^9 + 7`.

Two sequences are considered distinct if at least one element is different.
