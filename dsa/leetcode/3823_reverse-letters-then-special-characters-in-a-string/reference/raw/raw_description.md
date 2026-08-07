## Description

You are given a string `s` consisting of lowercase English letters and special characters.

Your task is to perform these **in order**:

	- **Reverse** the **lowercase letters** and place them back into the positions originally occupied by letters.

	- **Reverse** the **special characters** and place them back into the positions originally occupied by special characters.

Return the resulting string after performing the reversals.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "</span>)ebc#da@f(<span class="example-io">"</span>

**Output:** <span class="example-io">"</span>(fad@cb#e)<span class="example-io">"</span>

**Explanation:**

	- The letters in the string are `['e', 'b', 'c', 'd', 'a', 'f']`:

		<li>Reversing them gives `['f', 'a', 'd', 'c', 'b', 'e']`

		- `s` becomes `")fad#cb@e("`

	</li>
	- ​​​​​​​The special characters in the string are `[')', '#', '@', '(']`:

		<li>Reversing them gives `['(', '@', '#', ')']`

		- `s` becomes `<span class="example-io">"</span>(fad@cb#e)<span class="example-io">"</span>`

	</li>

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "z"</span>

**Output:** <span class="example-io">"z"</span>

**Explanation:**

The string contains only one letter, and reversing it does not change the string. There are no special characters.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "!@#$%^&*()"</span>

**Output:** <span class="example-io">"</span>)(*&^%$#@!<span class="example-io">"</span>

**Explanation:**

The string contains no letters. The string contains all special characters, so reversing the special characters reverses the whole string.

</div>

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` consists only of lowercase English letters and the special characters in `"!@#$%^&*()"`.
