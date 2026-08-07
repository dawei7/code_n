## Description

You are given a string `word`. A letter is called **special** if it appears **both** in lowercase and uppercase in `word`.

Return the number of* ***special** letters in* *`word`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">word = "aaAbcBC"</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The special characters in `word` are `'a'`, `'b'`, and `'c'`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">word = "abc"</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

No character in `word` appears in uppercase.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">word = "abBCab"</span>

**Output:** 1

**Explanation:**

The only special character in `word` is `'b'`.

</div>

**Constraints:**

	- `1 <= word.length <= 50`

	- `word` consists of only lowercase and uppercase English letters.
