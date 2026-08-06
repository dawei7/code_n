## Description

You are given a string `s` consisting of lowercase English letters and digits.

For each character, its **mirror character** is defined by reversing the order of its character set:

<ul>
	<li>For letters, the mirror of a character is the letter at the same position from the end of the alphabet.
	<ul>
		<li>For example, the mirror of `'a'` is `'z'`, and the mirror of `'b'` is `'y'`, and so on.</li>
	</ul>
	</li>
	<li>For digits, the mirror of a character is the digit at the same position from the end of the range `'0'` to `'9'`.
	<ul>
		<li>For example, the mirror of `'0'` is `'9'`, and the mirror of `'1'` is `'8'`, and so on.</li>
	</ul>
	</li>
</ul>

For each **unique** character `c` in the string:

<ul>
	<li>Let `m` be its **mirror** character.</li>
	<li>Let `freq(x)` denote the number of times character `x` appears in the string.</li>
	<li>Compute the **absolute difference** between their **frequencies**, defined as: `|freq(c) - freq(m)|`</li>
</ul>

The mirror pairs `(c, m)` and `(m, c)` are the same and must be counted **only once**.

Return an integer denoting the total sum of these values over all such **distinct mirror pairs**.
