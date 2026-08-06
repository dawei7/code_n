## Description

You are given a string `s` and an integer `t`, representing the number of **transformations** to perform. In one **transformation**, every character in `s` is replaced according to the following rules:

<ul>
	<li>If the character is `'z'`, replace it with the string `"ab"`.</li>
	<li>Otherwise, replace it with the **next** character in the alphabet. For example, `'a'` is replaced with `'b'`, `'b'` is replaced with `'c'`, and so on.</li>
</ul>

Return the **length** of the resulting string after **exactly** `t` transformations.

Since the answer may be very large, return it **modulo**<!-- notionvc: eb142f2b-b818-4064-8be5-e5a36b07557a --> `10^9 + 7`.
