## Description

You are given a <span data-keyword="binary-string">binary string</span> `s`.

You are also given an array of strings `strs`, where each `strs[i]` has the **same** length as `s` and consists of characters `'0'`, `'1'`, and `'?'`. Each `'?'` can be replaced by either `'0'` or `'1'`.

You may perform the following operation any number of times (including zero):

<ul>
	<li>Choose any <span data-keyword="subsequence-string">subsequence</span> `sub` of `s`.</li>
	<li>Sort `sub` in **non-decreasing** order.</li>
	<li>Replace the chosen **subsequence** in `s` with the sorted `sub`, keeping all other characters unchanged.</li>
</ul>

Return a boolean array `ans`, where `ans[i]` is `true` if it's possible to replace all `'?'` in `strs[i]` with `'0'` or `'1'` and transform `s` into the resulting string using the allowed operation above, otherwise return `false`.
