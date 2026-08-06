## Description

You are given a string `source` of size `n`, a string `pattern` that is a <span data-keyword="subsequence-string">subsequence</span> of `source`, and a **sorted** integer array `targetIndices` that contains **distinct** numbers in the range `[0, n - 1]`.

We define an **operation** as removing a character at an index `idx` from `source` such that:

<ul>
	<li>`idx` is an element of `targetIndices`.</li>
	<li>`pattern` remains a <span data-keyword="subsequence-string">subsequence</span> of `source` after removing the character.</li>
</ul>

Performing an operation **does not** change the indices of the other characters in `source`. For example, if you remove `'c'` from `"acb"`, the character at index 2 would still be `'b'`.

Return the **maximum** number of *operations* that can be performed.
