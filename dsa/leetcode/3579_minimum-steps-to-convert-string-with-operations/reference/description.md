## Description

You are given two strings, `word1` and `word2`, of equal length. You need to transform `word1` into `word2`.

For this, divide `word1` into one or more **contiguous <span data-keyword="substring-nonempty">substrings</span>**. For each substring `substr` you can perform the following operations:

<ol>
	<li>
	**Replace:** Replace the character at any one index of `substr` with another lowercase English letter.

	</li>
	<li>
	**Swap:** Swap any two characters in `substr`.

	</li>
	<li>
	**Reverse Substring:** Reverse `substr`.

	</li>
</ol>

Each of these counts as **one** operation and each character of each substring can be used in each type of operation at most once (i.e. no single index may be involved in more than one replace, one swap, or one reverse).

Return the **minimum number of operations** required to transform `word1` into `word2`.
