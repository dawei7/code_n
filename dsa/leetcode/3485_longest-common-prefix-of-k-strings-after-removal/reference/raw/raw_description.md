## Description

You are given an array of strings `words` and an integer `k`.

For each index `i` in the range `[0, words.length - 1]`, find the **length** of the **longest common <span data-keyword="string-prefix">prefix</span>** among any `k` strings (selected at **distinct indices**) from the remaining array after removing the `i^th` element.

Return an array `answer`, where `answer[i]` is the answer for `i^th` element. If removing the `i^th` element leaves the array with fewer than `k` strings, `answer[i]` is 0.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">words = ["jump","run","run","jump","run"], k = 2</span>

**Output:** <span class="example-io">[3,4,4,3,4]</span>

**Explanation:**

	- Removing index 0 (`"jump"`):

		<li>`words` becomes: `["run", "run", "jump", "run"]`. `"run"` occurs 3 times. Choosing any two gives the longest common prefix `"run"` (length 3).

	</li>
	- Removing index 1 (`"run"`):

		<li>`words` becomes: `["jump", "run", "jump", "run"]`. `"jump"` occurs twice. Choosing these two gives the longest common prefix `"jump"` (length 4).

	</li>
	- Removing index 2 (`"run"`):

		<li>`words` becomes: `["jump", "run", "jump", "run"]`. `"jump"` occurs twice. Choosing these two gives the longest common prefix `"jump"` (length 4).

	</li>
	- Removing index 3 (`"jump"`):

		<li>`words` becomes: `["jump", "run", "run", "run"]`. `"run"` occurs 3 times. Choosing any two gives the longest common prefix `"run"` (length 3).

	</li>
	- Removing index 4 ("run"):

		<li>`words` becomes: `["jump", "run", "run", "jump"]`. `"jump"` occurs twice. Choosing these two gives the longest common prefix `"jump"` (length 4).

	</li>

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">words = ["dog","racer","car"], k = 2</span>

**Output:** <span class="example-io">[0,0,0]</span>

**Explanation:**

	- Removing any index results in an answer of 0.

</div>

**Constraints:**

	- `1 <= k <= words.length <= 10^5`

	- `1 <= words[i].length <= 10^4`

	- `words[i]` consists of lowercase English letters.

	- The sum of `words[i].length` is smaller than or equal `10^5`.
