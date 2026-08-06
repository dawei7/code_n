## Description

You are given two strings `stamp` and `target`. Initially, there is a string `s` of length `target.length` with all `s[i] == '?'`.

In one turn, you can place `stamp` over `s` and replace every letter in the `s` with the corresponding letter from `stamp`.

<ul>
	<li>For example, if `stamp = "abc"` and `target = "abcba"`, then `s` is `"?????"` initially. In one turn you can:

	<ul>
		<li>place `stamp` at index `0` of `s` to obtain `"abc??"`,</li>
		<li>place `stamp` at index `1` of `s` to obtain `"?abc?"`, or</li>
		<li>place `stamp` at index `2` of `s` to obtain `"??abc"`.</li>
	</ul>
	Note that `stamp` must be fully contained in the boundaries of `s` in order to stamp (i.e., you cannot place `stamp` at index `3` of `s`).</li>
</ul>

We want to convert `s` to `target` using **at most** `10 * target.length` turns.

Return *an array of the index of the left-most letter being stamped at each turn*. If we cannot obtain `target` from `s` within `10 * target.length` turns, return an empty array.
