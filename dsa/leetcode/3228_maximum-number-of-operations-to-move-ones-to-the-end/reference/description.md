## Description

You are given a <span data-keyword="binary-string">binary string</span> `s`.

You can perform the following operation on the string **any** number of times:

<ul>
	<li>Choose **any** index `i` from the string where `i + 1 < s.length` such that `s[i] == '1'` and `s[i + 1] == '0'`.</li>
	<li>Move the character `s[i]` to the **right** until it reaches the end of the string or another `'1'`. For example, for `s = "010010"`, if we choose `i = 1`, the resulting string will be `s = "0**<u>001</u>**10"`.</li>
</ul>

Return the **maximum** number of operations that you can perform.
