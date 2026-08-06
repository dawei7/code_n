## Description

A parentheses string is a **non-empty** string consisting only of `'('` and `')'`. It is **valid** if **any** of the following conditions is **true**:

<ul>
	<li>It is `()`.</li>
	<li>It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid parentheses strings.</li>
	<li>It can be written as `(A)`, where `A` is a valid parentheses string.</li>
</ul>

You are given an `m x n` matrix of parentheses `grid`. A **valid parentheses string path** in the grid is a path satisfying **all** of the following conditions:

<ul>
	<li>The path starts from the upper left cell `(0, 0)`.</li>
	<li>The path ends at the bottom-right cell `(m - 1, n - 1)`.</li>
	<li>The path only ever moves **down** or **right**.</li>
	<li>The resulting parentheses string formed by the path is **valid**.</li>
</ul>

Return `true` *if there exists a **valid parentheses string path** in the grid.* Otherwise, return `false`.
