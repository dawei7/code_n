## Description

Given an integer `n`, your task is to count how many strings of length `n` can be formed under the following rules:

<ul>
	<li>Each character is a lower case vowel (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`)</li>
	<li>Each vowel `'a'` may only be followed by an `'e'`.</li>
	<li>Each vowel `'e'` may only be followed by an `'a'` or an `'i'`.</li>
	<li>Each vowel `'i'` **may not** be followed by another `'i'`.</li>
	<li>Each vowel `'o'` may only be followed by an `'i'` or a `'u'`.</li>
	<li>Each vowel `'u'` may only be followed by an `'a'`.</li>
</ul>

Since the answer may be too large, return it modulo `10^9 + 7`.
