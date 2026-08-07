## Description

You are given a string `s` of length `n` and an integer `k`, where `n` is a **multiple** of `k`. Your task is to hash the string `s` into a new string called `result`, which has a length of `n / k`.

First, divide `s` into `n / k` **<span data-keyword="substring-nonempty">substrings</span>**, each with a length of `k`. Then, initialize `result` as an **empty** string.

For each **substring** in order from the beginning:

	- The **hash value** of a character is the index of that characte<!-- notionvc: 4b67483a-fa95-40b6-870d-2eacd9bc18d8 -->r in the **English alphabet** (e.g., `'a' →<!-- notionvc: d3f8e4c2-23cd-41ad-a14b-101dfe4c5aba --> 0`, `'b' →<!-- notionvc: d3f8e4c2-23cd-41ad-a14b-101dfe4c5aba --> 1`, ..., `'z' →<!-- notionvc: d3f8e4c2-23cd-41ad-a14b-101dfe4c5aba --> 25`).

	- Calculate the *sum* of all the **hash values** of the characters in the substring.

	- Find the remainder of this sum when divided by 26, which is called `hashedChar`.

	- Identify the character in the English lowercase alphabet that corresponds to `hashedChar`.

	- Append that character to the end of `result`.

Return `result`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abcd", k = 2</span>

**Output:** <span class="example-io">"bf"</span>

**Explanation:**

First substring: `"ab"`, `0 + 1 = 1`, `1 % 26 = 1`, `result[0] = 'b'`.

Second substring: `"cd"`, `2 + 3 = 5`, `5 % 26 = 5`, `result[1] = 'f'`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "mxz", k = 3</span>

**Output:** <span class="example-io">"i"</span>

**Explanation:**

The only substring: `"mxz"`, `12 + 23 + 25 = 60`, `60 % 26 = 8`, `result[0] = 'i'`.

</div>

**Constraints:**

	- `1 <= k <= 100`

	- `k <= s.length <= 1000`

	- `s.length` is divisible by `k`.

	- `s` consists only of lowercase English letters.
