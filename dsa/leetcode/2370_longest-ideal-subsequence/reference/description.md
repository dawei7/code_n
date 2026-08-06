## Description

You are given a string `s` consisting of lowercase letters and an integer `k`. We call a string `t` **ideal** if the following conditions are satisfied:

<ul>
	<li>`t` is a **subsequence** of the string `s`.</li>
	<li>The absolute difference in the alphabet order of every two **adjacent** letters in `t` is less than or equal to `k`.</li>
</ul>

Return *the length of the **longest** ideal string*.

A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

**Note** that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of `'a'` and `'z'` is `25`, not `1`.
