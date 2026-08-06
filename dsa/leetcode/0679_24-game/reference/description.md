## Description

You are given an integer array `cards` of length `4`. You have four cards, each containing a number in the range `[1, 9]`. You should arrange the numbers on these cards in a mathematical expression using the operators `['+', '-', '*', '/']` and the parentheses `'('` and `')'` to get the value 24.

You are restricted with the following rules:

<ul>
	<li>The division operator `'/'` represents real division, not integer division.

	<ul>
		<li>For example, `4 / (1 - 2 / 3) = 4 / (1 / 3) = 12`.</li>
	</ul>
	</li>
	<li>Every operation done is between two numbers. In particular, we cannot use `'-'` as a unary operator.
	<ul>
		<li>For example, if `cards = [1, 1, 1, 1]`, the expression `"-1 - 1 - 1 - 1"` is **not allowed**.</li>
	</ul>
	</li>
	<li>You cannot concatenate numbers together
	<ul>
		<li>For example, if `cards = [1, 2, 1, 2]`, the expression `"12 + 12"` is not valid.</li>
	</ul>
	</li>
</ul>

Return `true` if you can get such expression that evaluates to `24`, and `false` otherwise.
