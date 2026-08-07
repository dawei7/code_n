## Description

You are given a string array `words`, consisting of **distinct** 4-letter strings, each containing lowercase English letters.

A **word square** consists of 4 **distinct** words: `top`, `left`, `right` and `bottom`, arranged as follows:

	- `top` forms the **top row**.

	- `bottom` forms the **bottom row**.

	- `left` forms the **left column** (top to bottom).

	- `right` forms the **right column** (top to bottom).

It must satisfy:

	- `top[0] == left[0]`, `top[3] == right[0]`

	- `bottom[0] == left[3]`, `bottom[3] == right[3]`

Return all valid **distinct** word squares, sorted in **ascending lexicographic** order by the 4-tuple `(top, left, right, bottom)​​​​​​​`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">words = ["able","area","echo","also"]</span>

**Output:** <span class="example-io">[["able","area","echo","also"],["area","able","also","echo"]]</span>

**Explanation:**

There are exactly two valid 4-word squares that satisfy all corner constraints:

	- `"able"` (top), `"area"` (left), `"echo"` (right), `"also"` (bottom)

		<li>`top[0] == left[0] == 'a'`

		- `top[3] == right[0] == 'e'`

		- `bottom[0] == left[3] == 'a'`

		- `bottom[3] == right[3] == 'o'`

	</li>
	- `"area"` (top), `"able"` (left), `"also"` (right), `"echo"` (bottom)

		<li>All corner constraints are satisfied.

	</li>

Thus, the answer is `[["able","area","echo","also"],["area","able","also","echo"]]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">words = ["code","cafe","eden","edge"]</span>

**Output:** <span class="example-io">[]</span>

**Explanation:**

No combination of four words satisfies all four corner constraints. Thus, the answer is empty array `[]`.

</div>

**Constraints:**

	- `4 <= words.length <= 15`

	- `words[i].length == 4`

	- `words[i]` consists of only lowercase English letters.

	- All `words[i]` are **distinct**.
