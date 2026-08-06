## Description

A parentheses string is valid if and only if:

<ul>
	<li>It is the empty string,</li>
	<li>It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or</li>
	<li>It can be written as `(A)`, where `A` is a valid string.</li>
</ul>

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

<ul>
	<li>For example, if `s = "()))"`, you can insert an opening parenthesis to be `"(**(**)))"` or a closing parenthesis to be `"())**)**)"`.</li>
</ul>

Return *the minimum number of moves required to make *`s`* valid*.
