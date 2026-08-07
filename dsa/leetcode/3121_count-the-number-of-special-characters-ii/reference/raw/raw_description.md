## Description

You are given a string `word`. A letter `c` is called **special** if it appears **both** in lowercase and uppercase in `word`, and **every** lowercase occurrence of `c` appears before the **first** uppercase occurrence of `c`.

Return the number of* ***special** letters* *in* *`word`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">word = "aaAbcBC"</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The special characters are `'a'`, `'b'`, and `'c'`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">word = "abc"</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

There are no special characters in `word`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">word = "AbBCab"</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

There are no special characters in `word`.

</div>

**Constraints:**

	- `1 <= word.length <= 2 * 10^5`

	- `word` consists of only lowercase and uppercase English letters.
