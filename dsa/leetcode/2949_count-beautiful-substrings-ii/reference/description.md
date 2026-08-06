## Description

You are given a string `s` and a positive integer `k`.

Let `vowels` and `consonants` be the number of vowels and consonants in a string.

A string is **beautiful** if:

<ul>
	<li>`vowels == consonants`.</li>
	<li>`(vowels * consonants) % k == 0`, in other terms the multiplication of `vowels` and `consonants` is divisible by `k`.</li>
</ul>

Return *the number of **non-empty beautiful substrings** in the given string* `s`.

A **substring** is a contiguous sequence of characters in a string.

**Vowel letters** in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

**Consonant letters** in English are every letter except vowels.
