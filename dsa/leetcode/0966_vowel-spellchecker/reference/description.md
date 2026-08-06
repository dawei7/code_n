## Description

Given a `wordlist`, we want to implement a spellchecker that converts a query word into a correct word.

For a given `query` word, the spell checker handles two categories of spelling mistakes:

<ul>
	<li>Capitalization: If the query matches a word in the wordlist (**case-insensitive**), then the query word is returned with the same case as the case in the wordlist.

	<ul>
		<li>Example: `wordlist = ["yellow"]`, `query = "YellOw"`: `correct = "yellow"`</li>
		<li>Example: `wordlist = ["Yellow"]`, `query = "yellow"`: `correct = "Yellow"`</li>
		<li>Example: `wordlist = ["yellow"]`, `query = "yellow"`: `correct = "yellow"`</li>
	</ul>
	</li>
	<li>Vowel Errors: If after replacing the vowels `('a', 'e', 'i', 'o', 'u')` of the query word with any vowel individually, it matches a word in the wordlist (**case-insensitive**), then the query word is returned with the same case as the match in the wordlist.
	<ul>
		<li>Example: `wordlist = ["YellOw"]`, `query = "yollow"`: `correct = "YellOw"`</li>
		<li>Example: `wordlist = ["YellOw"]`, `query = "yeellow"`: `correct = ""` (no match)</li>
		<li>Example: `wordlist = ["YellOw"]`, `query = "yllw"`: `correct = ""` (no match)</li>
	</ul>
	</li>
</ul>

In addition, the spell checker operates under the following precedence rules:

<ul>
	<li>When the query exactly matches a word in the wordlist (**case-sensitive**), you should return the same word back.</li>
	<li>When the query matches a word up to capitalization, you should return the first such match in the wordlist.</li>
	<li>When the query matches a word up to vowel errors, you should return the first such match in the wordlist.</li>
	<li>If the query has no matches in the wordlist, you should return the empty string.</li>
</ul>

Given some `queries`, return a list of words `answer`, where `answer[i]` is the correct word for `query = queries[i]`.
