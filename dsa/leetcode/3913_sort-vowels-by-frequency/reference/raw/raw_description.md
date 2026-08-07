## Description

You are given a string `s` consisting of lowercase English characters.

Rearrange only the **vowels** in the string so that they appear in **non-increasing** order of their frequency.

If multiple vowels have the same **frequency**, order them by the position of their **first occurrence** in `s`.

Return the modified string.

Vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

The **frequency** of a letter is the number of times it occurs in the string.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "leetcode"</span>

**Output:** <span class="example-io">"leetcedo"</span>

**Explanation:**​​​​​​​

	- Vowels in the string are `['e', 'e', 'o', 'e']` with frequencies: `e = 3`, `o = 1`.

	- Sorting in non-increasing order of frequency and placing them back into the vowel positions results in `"leetcedo"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "aeiaaioooa"</span>

**Output:** <span class="example-io">"aaaaoooiie"</span>

**Explanation:**​​​​​​​

	- Vowels in the string are `['a', 'e', 'i', 'a', 'a', 'i', 'o', 'o', 'o', 'a']` with frequencies: `a = 4`, `o = 3`, `i = 2`, `e = 1`.

	- Sorting them in non-increasing order of frequency and placing them back into the vowel positions results in `"aaaaoooiie"`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "baeiou"</span>

**Output:** <span class="example-io">"baeiou"</span>

**Explanation:**

	- Each vowel appears exactly once, so all have the same frequency.

	- Thus, they retain their relative order based on first occurrence, and the string remains unchanged.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of lowercase English letters
