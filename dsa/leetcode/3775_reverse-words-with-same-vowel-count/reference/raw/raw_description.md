## Description

You are given a string `s` consisting of lowercase English words, each separated by a single space.

Determine how many vowels appear in the **first** word. Then, reverse each following word that has the **same vowel count**. Leave all remaining words unchanged.

Return the resulting string.

Vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "cat and mice"</span>

**Output:** <span class="example-io">"cat dna mice"</span>

**Explanation:**​​​​​​​

	- The first word `"cat"` has 1 vowel.

	- `"and"` has 1 vowel, so it is reversed to form `"dna"`.

	- `"mice"` has 2 vowels, so it remains unchanged.

	- Thus, the resulting string is `"cat dna mice"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "book is nice"</span>

**Output:** <span class="example-io">"book is ecin"</span>

**Explanation:**

	- The first word `"book"` has 2 vowels.

	- `"is"` has 1 vowel, so it remains unchanged.

	- `"nice"` has 2 vowels, so it is reversed to form `"ecin"`.

	- Thus, the resulting string is `"book is ecin"`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "banana healthy"</span>

**Output:** <span class="example-io">"banana healthy"</span>

**Explanation:**

	- The first word `"banana"` has 3 vowels.

	- `"healthy"` has 2 vowels, so it remains unchanged.

	- Thus, the resulting string is `"banana healthy"`.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of lowercase English letters and spaces.

	- Words in `s` are separated by a **single** space.

	- `s` does **not** contain leading or trailing spaces.
