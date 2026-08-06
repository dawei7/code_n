## Description

A string `s` is called **happy** if it satisfies the following conditions:

<ul>
	<li>`s` only contains the letters `'a'`, `'b'`, and `'c'`.</li>
	<li>`s` does not contain any of `"aaa"`, `"bbb"`, or `"ccc"` as a substring.</li>
	<li>`s` contains **at most** `a` occurrences of the letter `'a'`.</li>
	<li>`s` contains **at most** `b` occurrences of the letter `'b'`.</li>
	<li>`s` contains **at most** `c` occurrences of the letter `'c'`.</li>
</ul>

Given three integers `a`, `b`, and `c`, return *the **longest possible happy **string*. If there are multiple longest happy strings, return *any of them*. If there is no such string, return *the empty string *`""`.

A **substring** is a contiguous sequence of characters within a string.
