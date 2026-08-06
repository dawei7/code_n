## Description

Given two strings `s` and `t`, transform string `s` into string `t` using the following operation any number of times:

<ul>
	<li>Choose a **non-empty** substring in `s` and sort it in place so the characters are in **ascending order**.

	<ul>
		<li>For example, applying the operation on the underlined substring in `"1<u>4234</u>"` results in `"1<u>2344</u>"`.</li>
	</ul>
	</li>
</ul>

Return `true` if *it is possible to transform `s` into `t`*. Otherwise, return `false`.

A **substring** is a contiguous sequence of characters within a string.
