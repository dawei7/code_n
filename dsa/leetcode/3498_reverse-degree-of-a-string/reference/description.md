## Description

Given a string `s`, calculate its **reverse degree**.

The **reverse degree** is calculated as follows:

<ol>
	<li>For each character, multiply its position in the *reversed* alphabet (`'a'` = 26, `'b'` = 25, ..., `'z'` = 1) with its position in the string **(1-indexed)**.</li>
	<li>Sum these products for all characters in the string.</li>
</ol>

Return the **reverse degree** of `s`.
