## Description

You are given two strings `word1` and `word2`.

A string `x` is called **valid** if `x` can be rearranged to have `word2` as a <span data-keyword="string-prefix">prefix</span>.

Return the total number of **valid** <span data-keyword="substring-nonempty">substrings</span> of `word1`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">word1 = "bcca", word2 = "abc"</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The only valid substring is `"bcca"` which can be rearranged to `"abcc"` having `"abc"` as a prefix.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">word1 = "abcabc", word2 = "abc"</span>

**Output:** <span class="example-io">10</span>

**Explanation:**

All the substrings except substrings of size 1 and size 2 are valid.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">word1 = "abcabc", word2 = "aaabc"</span>

**Output:** <span class="example-io">0</span>

</div>

**Constraints:**

	- `1 <= word1.length <= 10^5`

	- `1 <= word2.length <= 10^4`

	- `word1` and `word2` consist only of lowercase English letters.
