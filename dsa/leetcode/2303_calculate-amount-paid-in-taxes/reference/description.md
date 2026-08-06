## Description

You are given a **0-indexed** 2D integer array `brackets` where `brackets[i] = [upper_i, percent_i]` means that the `i^th` tax bracket has an upper bound of `upper_i` and is taxed at a rate of `percent_i`. The brackets are **sorted** by upper bound (i.e. `upper_i-1 < upper_i` for `0 < i < brackets.length`).

Tax is calculated as follows:

<ul>
	<li>The first `upper_0` dollars earned are taxed at a rate of `percent_0`.</li>
	<li>The next `upper_1 - upper_0` dollars earned are taxed at a rate of `percent_1`.</li>
	<li>The next `upper_2 - upper_1` dollars earned are taxed at a rate of `percent_2`.</li>
	<li>And so on.</li>
</ul>

You are given an integer `income` representing the amount of money you earned. Return *the amount of money that you have to pay in taxes.* Answers within `10^-5` of the actual answer will be accepted.
