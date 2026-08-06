## Description

A password is said to be **strong** if it satisfies all the following criteria:

<ul>
	<li>It has at least `8` characters.</li>
	<li>It contains at least **one lowercase** letter.</li>
	<li>It contains at least **one uppercase** letter.</li>
	<li>It contains at least **one digit**.</li>
	<li>It contains at least **one special character**. The special characters are the characters in the following string: `"!@#$%^&*()-+"`.</li>
	<li>It does **not** contain `2` of the same character in adjacent positions (i.e., `"aab"` violates this condition, but `"aba"` does not).</li>
</ul>

Given a string `password`, return `true`* if it is a **strong** password*. Otherwise, return `false`.
