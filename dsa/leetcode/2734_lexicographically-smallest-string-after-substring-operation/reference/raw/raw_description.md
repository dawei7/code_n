## Description

Given a string `s` consisting of lowercase English letters. Perform the following operation:

	- Select any non-empty <span data-keyword="substring-nonempty">substring</span> then replace every letter of the substring with the preceding letter of the English alphabet. For example, 'b' is converted to 'a', and 'a' is converted to 'z'.

Return the <span data-keyword="lexicographically-smaller-string">**lexicographically smallest**</span> string **after performing the operation**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "cbabc"</span>

**Output:** <span class="example-io">"baabc"</span>

**Explanation:**

Perform the operation on the substring starting at index 0, and ending at index 1 inclusive.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "aa"</span>

**Output:** <span class="example-io">"az"</span>

**Explanation:**

Perform the operation on the last letter.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "acbbc"</span>

**Output:** <span class="example-io">"abaab"</span>

**Explanation:**

Perform the operation on the substring starting at index 1, and ending at index 4 inclusive.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">s = "leetcode"</span>

**Output:** <span class="example-io">"kddsbncd"</span>

**Explanation:**

Perform the operation on the entire string.

</div>

**Constraints:**

	- `1 <= s.length <= 3 * 10^5`

	- `s` consists of lowercase English letters
