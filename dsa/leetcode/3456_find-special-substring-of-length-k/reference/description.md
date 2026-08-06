## Description

You are given a string `s` and an integer `k`.

Determine if there exists a <span data-keyword="substring-nonempty">substring</span> of length **exactly** `k` in `s` that satisfies the following conditions:

<ol>
	<li>The substring consists of **only one distinct character** (e.g., `"aaa"` or `"bbb"`).</li>
	<li>If there is a character **immediately before** the substring, it must be different from the character in the substring.</li>
	<li>If there is a character **immediately after** the substring, it must also be different from the character in the substring.</li>
</ol>

Return `true` if such a substring exists. Otherwise, return `false`.
