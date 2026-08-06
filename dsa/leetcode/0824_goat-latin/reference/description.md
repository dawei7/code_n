## Description

You are given a string `sentence` that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

<ul>
	<li>If a word begins with a vowel (`'a'`, `'e'`, `'i'`, `'o'`, or `'u'`), append `"ma"` to the end of the word.

	<ul>
		<li>For example, the word `"apple"` becomes `"applema"`.</li>
	</ul>
	</li>
	<li>If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add `"ma"`.
	<ul>
		<li>For example, the word `"goat"` becomes `"oatgma"`.</li>
	</ul>
	</li>
	<li>Add one letter `'a'` to the end of each word per its word index in the sentence, starting with `1`.
	<ul>
		<li>For example, the first word gets `"a"` added to the end, the second word gets `"aa"` added to the end, and so on.</li>
	</ul>
	</li>
</ul>

Return* the final sentence representing the conversion from sentence to Goat Latin*.
