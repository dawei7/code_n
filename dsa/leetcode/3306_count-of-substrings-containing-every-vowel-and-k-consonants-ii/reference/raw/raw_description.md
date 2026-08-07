## Description

You are given a string `word` and a **non-negative** integer `k`.

Return the total number of <span data-keyword="substring-nonempty">substrings</span> of `word` that contain every vowel (`'a'`, `'e'`, `'i'`, `'o'`, and `'u'`) **at least** once and **exactly** `k` consonants.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">word = "aeioqq", k = 1</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

There is no substring with every vowel.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">word = "aeiou", k = 0</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The only substring with every vowel and zero consonants is `word[0..4]`, which is `"aeiou"`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">word = "</span>ieaouqqieaouqq<span class="example-io">", k = 1</span>

**Output:** 3

**Explanation:**

The substrings with every vowel and one consonant are:

	- `word[0..5]`, which is `"ieaouq"`.

	- `word[6..11]`, which is `"qieaou"`.

	- `word[7..12]`, which is `"ieaouq"`.

</div>

**Constraints:**

	- `5 <= word.length <= 2 * 10^5`

	- `word` consists only of lowercase English letters.

	- `0 <= k <= word.length - 5`
