## Description

You are given a string `s` consisting of lowercase English letters.

You can perform the following operation any number of times (including zero):

	- Remove **any** pair of **adjacent** characters in the string that are **consecutive** in the alphabet, in either order (e.g., `'a'` and `'b'`, or `'b'` and `'a'`).

	- Shift the remaining characters to the left to fill the gap.

Return the **<span data-keyword="lexicographically-smaller-string">lexicographically smallest</span>** string that can be obtained after performing the operations optimally.

**Note:** Consider the alphabet as circular, thus `'a'` and `'z'` are consecutive.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abc"</span>

**Output:** <span class="example-io">"a"</span>

**Explanation:**

	- Remove `"bc"` from the string, leaving `"a"` as the remaining string.

	- No further operations are possible. Thus, the lexicographically smallest string after all possible removals is `"a"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "bcda"</span>

**Output:** <span class="example-io">""</span>

**Explanation:**

	- **​​​​​​​**Remove `"cd"` from the string, leaving `"ba"` as the remaining string.

	- Remove `"ba"` from the string, leaving `""` as the remaining string.

	- No further operations are possible. Thus, the lexicographically smallest string after all possible removals is `""`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "zdce"</span>

**Output:** <span class="example-io">"zdce"</span>

**Explanation:**

	- Remove `"dc"` from the string, leaving `"ze"` as the remaining string.

	- No further operations are possible on `"ze"`.

	- However, since `"zdce"` is lexicographically smaller than `"ze"`, the smallest string after all possible removals is `"zdce"`.

</div>

**Constraints:**

	- `1 <= s.length <= 250`

	- `s` consists only of lowercase English letters.
