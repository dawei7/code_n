## Description

You are given a string `s` of length `n` and an integer `k`, where `n` is a **multiple** of `k`. Your task is to hash the string `s` into a new string called `result`, which has a length of `n / k`.

First, divide `s` into `n / k` **<span data-keyword="substring-nonempty">substrings</span>**, each with a length of `k`. Then, initialize `result` as an **empty** string.

For each **substring** in order from the beginning:

<ul>
	<li>The **hash value** of a character is the index of that characte<!-- notionvc: 4b67483a-fa95-40b6-870d-2eacd9bc18d8 -->r in the **English alphabet** (e.g., `'a' →<!-- notionvc: d3f8e4c2-23cd-41ad-a14b-101dfe4c5aba --> 0`, `'b' →<!-- notionvc: d3f8e4c2-23cd-41ad-a14b-101dfe4c5aba --> 1`, ..., `'z' →<!-- notionvc: d3f8e4c2-23cd-41ad-a14b-101dfe4c5aba --> 25`).</li>
	<li>Calculate the *sum* of all the **hash values** of the characters in the substring.</li>
	<li>Find the remainder of this sum when divided by 26, which is called `hashedChar`.</li>
	<li>Identify the character in the English lowercase alphabet that corresponds to `hashedChar`.</li>
	<li>Append that character to the end of `result`.</li>
</ul>

Return `result`.
