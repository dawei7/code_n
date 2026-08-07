## Description

You are given an array of strings `message` and an array of strings `bannedWords`.

An array of words is considered **spam** if there are **at least** two words in it that **exactly** match any word in `bannedWords`.

Return `true` if the array `message` is spam, and `false` otherwise.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">message = ["hello","world","leetcode"], bannedWords = ["world","hello"]</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

The words `"hello"` and `"world"` from the `message` array both appear in the `bannedWords` array.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"]</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

Only one word from the `message` array (`"programming"`) appears in the `bannedWords` array.

</div>

**Constraints:**

	- `1 <= message.length, bannedWords.length <= 10^5`

	- `1 <= message[i].length, bannedWords[i].length <= 15`

	- `message[i]` and `bannedWords[i]` consist only of lowercase English letters.
