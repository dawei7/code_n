## Description

You are given a string `s`.

Consider performing the following operation until `s` becomes **empty**:

<ul>
	<li>For **every** alphabet character from `'a'` to `'z'`, remove the **first** occurrence of that character in `s` (if it exists).</li>
</ul>

For example, let initially `s = "aabcbbca"`. We do the following operations:

<ul>
	<li>Remove the underlined characters `s = "<u>**a**</u>a**<u>bc</u>**bbca"`. The resulting string is `s = "abbca"`.</li>
	<li>Remove the underlined characters `s = "<u>**ab**</u>b<u>**c**</u>a"`. The resulting string is `s = "ba"`.</li>
	<li>Remove the underlined characters `s = "<u>**ba**</u>"`. The resulting string is `s = ""`.</li>
</ul>

Return *the value of the string *`s`* right **before** applying the **last** operation*. In the example above, answer is `"ba"`.
