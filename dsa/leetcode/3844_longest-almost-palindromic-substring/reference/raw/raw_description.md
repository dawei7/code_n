## Description

You are given a string `s` consisting of lowercase English letters.

A <span data-keyword="substring-nonempty">substring</span> is **almost-palindromic** if it becomes a <span data-keyword="palindrome-string">palindrome</span> after removing **exactly** one character from it.

Return an integer denoting the length of the **longest** **almost-palindromic** substring in `s`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abca"</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

Choose the substring `"<u>**abca**</u>"`.

	- Remove `"ab<u>**c**</u>a"`.

	- The string becomes `"aba"`, which is a palindrome.

	- Therefore, `"abca"` is almost-palindromic.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "abba"</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

Choose the substring `"<u>**abba**</u>"`.

	- Remove `"a<u>**b**</u>ba"`.

	- The string becomes `"aba"`, which is a palindrome.

	- Therefore, `"abba"` is almost-palindromic.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "zzabba"</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

Choose the substring `"z<u>**zabba**</u>"`.

	- Remove `"<u>**z**</u>abba"`.

	- The string becomes `"abba"`, which is a palindrome.

	- Therefore, `"zabba"` is almost-palindromic.

</div>

**Constraints:**

	- `2 <= s.length <= 2500`

	- `s` consists of only lowercase English letters.
