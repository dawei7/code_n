## Description

You are given an array of `words` where each word consists of lowercase English letters.

`word_A` is a **predecessor** of `word_B` if and only if we can insert **exactly one** letter anywhere in `word_A` **without changing the order of the other characters** to make it equal to `word_B`.

<ul>
	<li>For example, `"abc"` is a **predecessor** of `"ab<u>a</u>c"`, while `"cba"` is not a **predecessor** of `"bcad"`.</li>
</ul>

A **word chain*** *is a sequence of words `[word_1, word_2, ..., word_k]` with `k >= 1`, where `word_1` is a **predecessor** of `word_2`, `word_2` is a **predecessor** of `word_3`, and so on. A single word is trivially a **word chain** with `k == 1`.

Return *the **length** of the **longest possible word chain** with words chosen from the given list of *`words`.
