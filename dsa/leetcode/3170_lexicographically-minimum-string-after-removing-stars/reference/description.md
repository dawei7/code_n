## Description

You are given a string `s`. It may contain any number of `'*'` characters. Your task is to remove all `'*'` characters.

While there is a `'*'`, do the following operation:

<ul>
	<li>Delete the leftmost `'*'` and the **smallest** non-`'*'` character to its *left*. If there are several smallest characters, you can delete any of them.</li>
</ul>

Return the <span data-keyword="lexicographically-smaller-string">lexicographically smallest</span> resulting string after removing all `'*'` characters.
