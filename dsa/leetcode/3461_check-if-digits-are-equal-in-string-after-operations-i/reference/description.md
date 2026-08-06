## Description

You are given a string `s` consisting of digits. Perform the following operation repeatedly until the string has **exactly** two digits:

<ul>
	<li>For each pair of consecutive digits in `s`, starting from the first digit, calculate a new digit as the sum of the two digits **modulo** 10.</li>
	<li>Replace `s` with the sequence of newly calculated digits, *maintaining the order* in which they are computed.</li>
</ul>

Return `true` if the final two digits in `s` are the **same**; otherwise, return `false`.
