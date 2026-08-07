## Description

You are given an array of strings `words` and a string `target`.

A string `x` is called **valid** if `x` is a <span data-keyword="string-prefix">prefix</span> of **any** string in `words`.

Return the **minimum** number of **valid** strings that can be *concatenated* to form `target`. If it is **not** possible to form `target`, return `-1`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">words = ["abc","aaaaa","bcdef"], target = "aabcdabc"</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The target string can be formed by concatenating:

	- Prefix of length 2 of `words[1]`, i.e. `"aa"`.

	- Prefix of length 3 of `words[2]`, i.e. `"bcd"`.

	- Prefix of length 3 of `words[0]`, i.e. `"abc"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">words = ["abababab","ab"], target = "ababaababa"</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The target string can be formed by concatenating:

	- Prefix of length 5 of `words[0]`, i.e. `"ababa"`.

	- Prefix of length 5 of `words[0]`, i.e. `"ababa"`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">words = ["abcdef"], target = "xyz"</span>

**Output:** <span class="example-io">-1</span>

</div>

**Constraints:**

	- `1 <= words.length <= 100`

	- `1 <= words[i].length <= 5 * 10^4`

	- The input is generated such that `sum(words[i].length) <= 10^5`.

	- `words[i]` consists only of lowercase English letters.

	- `1 <= target.length <= 5 * 10^4`

	- `target` consists only of lowercase English letters.
