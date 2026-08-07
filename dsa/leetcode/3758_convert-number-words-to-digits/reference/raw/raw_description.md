## Description

You are given a string `s` consisting of lowercase English letters. `s` may contain **valid concatenated** English words representing the digits 0 to 9, without spaces.

Your task is to **extract** each valid number word **in order** and convert it to its corresponding digit, producing a string of digits.

Parse `s` from left to right. At each position:

	- If a valid number word starts at the current position, append its corresponding digit to the result and advance by the length of that word.

	- Otherwise, skip **exactly** one character and continue parsing.

Return the resulting digit string. If no number words are found, return an empty string.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "onefourthree"</span>

**Output:** <span class="example-io">"143"</span>

**Explanation:**

	- Parsing from left to right, extract the valid number words "one", "four", "three".

	- These map to digits 1, 4, 3. Thus, the final result is `"143"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "ninexsix"</span>

**Output:** <span class="example-io">"96"</span>

**Explanation:**

	- The substring `"nine"` is a valid number word and maps to 9.

	- The character `"x"` does not match any valid number word prefix and is skipped.

	- Then, the substring `"six"` is a valid number word and maps to 6, so the final result is `"96"`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "zeero"</span>

**Output:** <span class="example-io">""</span>

**Explanation:**

	- No substring forms a valid number word during left-to-right parsing.

	- All characters are skipped and incomplete fragments are ignored, so the result is an empty string.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">s = "tw"</span>

**Output:** <span class="example-io">""</span>

**Explanation:**

	- No substring forms a valid number word during left-to-right parsing.

	- All characters are skipped and incomplete fragments are ignored, so the result is an empty string.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` contains only lowercase English letters.
