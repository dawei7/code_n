## Description

You are given a string `s` consisting of lowercase English letters.

You **must** repeatedly perform the following operation while the string `s` has **at least** two **consecutive **characters:

	- Remove the **leftmost** pair of **adjacent** characters in the string that are **consecutive** in the alphabet, in either order (e.g., `'a'` and `'b'`, or `'b'` and `'a'`).

	- Shift the remaining characters to the left to fill the gap.

Return the resulting string after no more operations can be performed.

**Note:** Consider the alphabet as circular, thus `'a'` and `'z'` are consecutive.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abc"</span>

**Output:** <span class="example-io">"c"</span>

**Explanation:**

	- Remove `"ab"` from the string, leaving `"c"` as the remaining string.

	- No further operations are possible. Thus, the resulting string after all possible removals is `"c"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "adcb"</span>

**Output:** <span class="example-io">""</span>

**Explanation:**

	- Remove `"dc"` from the string, leaving `"ab"` as the remaining string.

	- Remove `"ab"` from the string, leaving `""` as the remaining string.

	- No further operations are possible. Thus, the resulting string after all possible removals is `""`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "zadb"</span>

**Output:** <span class="example-io">"db"</span>

**Explanation:**

	- Remove `"za"` from the string, leaving `"db"` as the remaining string.

	- No further operations are possible. Thus, the resulting string after all possible removals is `"db"`.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists only of lowercase English letters.
