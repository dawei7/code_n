## Description

A **valid encoding** of an array of `words` is any reference string `s` and array of indices `indices` such that:

<ul>
	<li>`words.length == indices.length`</li>
	<li>The reference string `s` ends with the `'#'` character.</li>
	<li>For each index `indices[i]`, the **substring** of `s` starting from `indices[i]` and up to (but not including) the next `'#'` character is equal to `words[i]`.</li>
</ul>

Given an array of `words`, return *the **length of the shortest reference string** *`s`* possible of any **valid encoding** of *`words`*.*
