## Description

The **count-and-say** sequence is a sequence of digit strings defined by the recursive formula:

<ul>
	<li>`countAndSay(1) = "1"`</li>
	<li>`countAndSay(n)` is the run-length encoding of `countAndSay(n - 1)`.</li>
</ul>

<a href="http://en.wikipedia.org/wiki/Run-length_encoding" target="_blank">Run-length encoding</a> (RLE) is a string compression method that works by replacing each maximal group of consecutive identical characters with the concatenation of the length of the group followed by the character itself. For example, to compress the string `"3322251"` we replace `"33"` with `"23"`, replace `"222"` with `"32"`, replace `"5"` with `"15"`, and replace `"1"` with `"11"`. Thus the compressed string becomes `"23321511"`.

Given a positive integer `n`, return *the *`n^th`* element of the **count-and-say** sequence*.
