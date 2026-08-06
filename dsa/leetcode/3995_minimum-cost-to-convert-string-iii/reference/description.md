## Description

You are given two strings, `source` and `target`.

You are also given a 2D string array `rules`, where `rules[i] = [pattern_i, replacement_i]`, and an integer array `costs`, where `costs[i]` is the base cost of applying `rules[i]`. Both arrays have the same length. Additionally, `pattern_i` and `replacement_i` have the same length.

You may apply **any** rule **any** number of times. Each rule application works as follows:

<ul>
	<li>Choose an index `l` such that the range of positions from `l` to `l + pattern_i.length - 1` exists in the current string and **none** of these positions has been used in a previous rule application.</li>
	<li>For each index `j`, the character `pattern_i[j]` must either be **equal** to the current character at position `l + j`, or be `'*'`.</li>
	<li>Replace the characters in this range with `replacement_i`. The replacement is used **exactly** as given and does not contain wildcards.</li>
	<li>The cost of this rule application is `costs[i]` **plus** the number of `'*'` characters in `pattern_i`.</li>
	<li>Once a character position has been used in a rule application, it **cannot** be used in any **later** rule application.</li>
</ul>

Since every `pattern_i` and `replacement_i` have the same length, character positions are preserved after every rule application.

Return the **minimum** total cost required to transform `source` into `target`. If it is impossible, return -1.
