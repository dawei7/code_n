## Description

A word is considered **valid** if:

	- It contains a **minimum** of 3 characters.

	- It contains only digits (0-9), and English letters (uppercase and lowercase).

	- It includes **at least** one **vowel**.

	- It includes **at least** one **consonant**.

You are given a string `word`.

Return `true` if `word` is valid, otherwise, return `false`.

**Notes:**

	- `'a'`, `'e'`, `'i'`, `'o'`, `'u'`, and their uppercases are **vowels**.

	- A **consonant** is an English letter that is not a vowel.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">word = "234Adas"</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

This word satisfies the conditions.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">word = "b3"</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

The length of this word is fewer than 3, and does not have a vowel.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">word = "a3$e"</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

This word contains a `'$'` character and does not have a consonant.

</div>

**Constraints:**

	- `1 <= word.length <= 20`

	- `word` consists of English uppercase and lowercase letters, digits, `'@'`, `'#'`, and `'$'`.
