## Description

Given a string `s` and an integer `k`, partition `s` into `k` **<span data-keyword="substring-nonempty">substrings</span>** such that the letter changes needed to make each substring a **semi-palindrome** are minimized.

Return the ***minimum** number of letter changes* required*.*

A **semi-palindrome** is a special type of string that can be divided into **<span data-keyword="palindrome">palindromes</span>** based on a repeating pattern. To check if a string is a semi-palindrome:​

<ol>
	<li>Choose a positive divisor `d` of the string's length. `d` can range from `1` up to, but not including, the string's length. For a string of length `1`, it does not have a valid divisor as per this definition, since the only divisor is its length, which is not allowed.</li>
	<li>For a given divisor `d`, divide the string into groups where each group contains characters from the string that follow a repeating pattern of length `d`. Specifically, the first group consists of characters at positions `1`, `1 + d`, `1 + 2d`, and so on; the second group includes characters at positions `2`, `2 + d`, `2 + 2d`, etc.</li>
	<li>The string is considered a semi-palindrome if each of these groups forms a palindrome.</li>
</ol>

Consider the string `"abcabc"`:

<ul>
	<li>The length of `"abcabc"` is `6`. Valid divisors are `1`, `2`, and `3`.</li>
	<li>For `d = 1`: The entire string `"abcabc"` forms one group. Not a palindrome.</li>
	<li>For `d = 2`:
	<ul>
		<li>Group 1 (positions `1, 3, 5`): `"acb"`</li>
		<li>Group 2 (positions `2, 4, 6`): `"bac"`</li>
		<li>Neither group forms a palindrome.</li>
	</ul>
	</li>
	<li>For `d = 3`:
	<ul>
		<li>Group 1 (positions `1, 4`): `"aa"`</li>
		<li>Group 2 (positions `2, 5`): `"bb"`</li>
		<li>Group 3 (positions `3, 6`): `"cc"`</li>
		<li>All groups form palindromes. Therefore, `"abcabc"` is a semi-palindrome.</li>
	</ul>
	</li>
</ul>
