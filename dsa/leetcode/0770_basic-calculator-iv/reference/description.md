## Description

Given an expression such as `expression = "e + 8 - a + 5"` and an evaluation map such as `{"e": 1}` (given in terms of `evalvars = ["e"]` and `evalints = [1]`), return a list of tokens representing the simplified expression, such as `["-1*a","14"]`

<ul>
	<li>An expression alternates chunks and symbols, with a space separating each chunk and symbol.</li>
	<li>A chunk is either an expression in parentheses, a variable, or a non-negative integer.</li>
	<li>A variable is a string of lowercase letters (not including digits.) Note that variables can be multiple letters, and note that variables never have a leading coefficient or unary operator like `"2x"` or `"-x"`.</li>
</ul>

Expressions are evaluated in the usual order: brackets first, then multiplication, then addition and subtraction.

<ul>
	<li>For example, `expression = "1 + 2 * 3"` has an answer of `["7"]`.</li>
</ul>

The format of the output is as follows:

<ul>
	<li>For each term of free variables with a non-zero coefficient, we write the free variables within a term in sorted order lexicographically.
	<ul>
		<li>For example, we would never write a term like `"b*a*c"`, only `"a*b*c"`.</li>
	</ul>
	</li>
	<li>Terms have degrees equal to the number of free variables being multiplied, counting multiplicity. We write the largest degree terms of our answer first, breaking ties by lexicographic order ignoring the leading coefficient of the term.
	<ul>
		<li>For example, `"a*a*b*c"` has degree `4`.</li>
	</ul>
	</li>
	<li>The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables (if they exist.) A leading coefficient of 1 is still printed.</li>
	<li>An example of a well-formatted answer is `["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"]`.</li>
	<li>Terms (including constant terms) with coefficient `0` are not included.
	<ul>
		<li>For example, an expression of `"0"` has an output of `[]`.</li>
	</ul>
	</li>
</ul>

**Note:** You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2^31, 2^31 - 1]`.
