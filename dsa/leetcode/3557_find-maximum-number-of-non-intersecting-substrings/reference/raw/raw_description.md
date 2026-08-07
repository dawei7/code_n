## Description

You are given a string `word`.

Return the **maximum** number of non-intersecting **<span data-keyword="substring-nonempty">substrings</span>** of word that are at **least** four characters long and start and end with the same letter.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">word = "abcdeafdef"</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The two substrings are `"abcdea"` and `"fdef"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">word = "bcdaaaab"</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The only substring is `"aaaa"`. Note that we cannot **also** choose `"bcdaaaab"` since it intersects with the other substring.

</div>

**Constraints:**

	- `1 <= word.length <= 2 * 10^5`

	- `word` consists only of lowercase English letters.
