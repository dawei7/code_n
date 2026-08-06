## Description

A string is a *valid parentheses string* (denoted VPS) if and only if it consists of `"("` and `")"` characters only, and:

<ul>
	<li>It is the empty string, or</li>
	<li>It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are VPS's, or</li>
	<li>It can be written as `(A)`, where `A` is a VPS.</li>
</ul>

We can similarly define the *nesting depth* `depth(S)` of any VPS `S` as follows:

<ul>
	<li>`depth("") = 0`</li>
	<li>`depth(A + B) = max(depth(A), depth(B))`, where `A` and `B` are VPS's</li>
	<li>`depth("(" + A + ")") = 1 + depth(A)`, where `A` is a VPS.</li>
</ul>

For example, `""`, `"()()"`, and `"()(()())"` are VPS's (with nesting depths 0, 1, and 2), and `")("` and `"(()"` are not VPS's.

Given a VPS <font face="monospace">seq</font>, split it into two disjoint subsequences `A` and `B`, such that `A` and `B` are VPS's (and `A.length + B.length = seq.length`). The subsequences may not necessarily be contiguous.

For example, for the sequence `123456789`, one possible split is:

<ul data-end="822" data-start="776">
	<li data-end="800" data-start="776">
	<p data-end="800" data-start="778"><code data-end="799" data-start="778">A = {1, 3, 5, 7, 9}</code>,

	</li>
	<li data-end="822" data-start="801">
	<p data-end="822" data-start="803"><code data-end="821" data-start="803">B = {2, 4, 6, 8}</code>.

	</li>
</ul>

<p data-end="855" data-start="824">This corresponds to the output `[0, 1, 0, 1, 0, 1, 0, 1, 0]`  where 0 indicates membership in <code data-end="929" data-start="926">A</code> and 1 indicates membership in <code data-end="965" data-start="962">B</code>.

Now choose **any** such `A` and `B` such that `max(depth(A), depth(B))` is the minimum possible value.

Return an `answer` array (of length `seq.length`) that encodes such a choice of `A` and `B`:  `answer[i] = 0` if `seq[i]` is part of `A`, else `answer[i] = 1`.  Note that even though multiple answers may exist, you may return any of them.
