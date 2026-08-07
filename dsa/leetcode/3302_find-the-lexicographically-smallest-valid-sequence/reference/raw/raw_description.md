## Description

You are given two strings `word1` and `word2`.

A string `x` is called **almost equal** to `y` if you can change **at most** one character in `x` to make it *identical* to `y`.

A sequence of indices `seq` is called **valid** if:

	- The indices are sorted in **ascending** order.

	- *Concatenating* the characters at these indices in `word1` in **the same** order results in a string that is **almost equal** to `word2`.

Return an array of size `word2.length` representing the <span data-keyword="lexicographically-smaller-array">lexicographically smallest</span> **valid** sequence of indices. If no such sequence of indices exists, return an **empty** array.

**Note** that the answer must represent the *lexicographically smallest array*, **not** the corresponding string formed by those indices.<!-- notionvc: 2ff8e782-bd6f-4813-a421-ec25f7e84c1e -->

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">word1 = "vbcca", word2 = "abc"</span>

**Output:** <span class="example-io">[0,1,2]</span>

**Explanation:**

The lexicographically smallest valid sequence of indices is `[0, 1, 2]`:

	- Change `word1[0]` to `'a'`.

	- `word1[1]` is already `'b'`.

	- `word1[2]` is already `'c'`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">word1 = "bacdc", word2 = "abc"</span>

**Output:** <span class="example-io">[1,2,4]</span>

**Explanation:**

The lexicographically smallest valid sequence of indices is `[1, 2, 4]`:

	- `word1[1]` is already `'a'`.

	- Change `word1[2]` to `'b'`.

	- `word1[4]` is already `'c'`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">word1 = "aaaaaa", word2 = "aaabc"</span>

**Output:** <span class="example-io">[]</span>

**Explanation:**

There is no valid sequence of indices.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">word1 = "abc", word2 = "ab"</span>

**Output:** <span class="example-io">[0,1]</span>

</div>

**Constraints:**

	- `1 <= word2.length < word1.length <= 3 * 10^5`

	- `word1` and `word2` consist only of lowercase English letters.
