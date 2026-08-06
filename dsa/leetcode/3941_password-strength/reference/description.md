## Description

You are given a string `password`.

The **strength** of the password is calculated based on the following rules:

<ul>
	<li>1 point for each distinct lowercase letter (`'a'` to `'z'`).</li>
	<li>2 points for each distinct uppercase letter (`'A'` to `'Z'`).</li>
	<li>3 points for each distinct digit (`'0'` to `'9'`).</li>
	<li>5 points for each distinct special character from the set `"!@#$"`.</li>
</ul>

Each character contributes **at most** once, even if it appears multiple times.

Return an integer denoting the strength of the password.
