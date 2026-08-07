## Description

You are given an array of strings `words`. For each index `i` in the range `[0, words.length - 1]`, perform the following steps:

- Remove the element at index `i` from the `words` array.

- Compute the **length** of the **longest common prefix** among all **adjacent** pairs in the modified array.

Return an array `answer`, where $\text{answer}[i]$ is the length of the longest common prefix between the adjacent pairs after removing the element at index `i`. If **no** adjacent pairs remain or if **none** share a common prefix, then $\text{answer}[i]$ should be 0.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** words = ["jump","run","run","jump","run"]

**Output:** [3,0,0,3,3]

**Explanation:**

- Removing index 0:

		<li>`words` becomes `["run", "run", "jump", "run"]`

- Longest adjacent pair is `["run", "run"]` having a common prefix `"run"` (length 3)

	</li>
- Removing index 1:

		<li>`words` becomes `["jump", "run", "jump", "run"]`

- No adjacent pairs share a common prefix (length 0)

	</li>
- Removing index 2:

		<li>`words` becomes `["jump", "run", "jump", "run"]`

- No adjacent pairs share a common prefix (length 0)

	</li>
- Removing index 3:

		<li>`words` becomes `["jump", "run", "run", "run"]`

- Longest adjacent pair is `["run", "run"]` having a common prefix `"run"` (length 3)

	</li>
- Removing index 4:

		<li>words becomes `["jump", "run", "run", "jump"]`

- Longest adjacent pair is `["run", "run"]` having a common prefix `"run"` (length 3)

	</li>

</div>
#### Example 2

<div class="example-block">
**Input:** words = ["dog","racer","car"]

**Output:** [0,0,0]

**Explanation:**

- Removing any index results in an answer of 0.

</div>
### Constraints

- $1 \le \text{words.length} \le 10^{5}$

- $1 \le \text{words}[i].length \le 10^{4}$

- $\text{words}[i]$ consists of lowercase English letters.

- The sum of $\text{words}[i].length$ is smaller than or equal $10^{5}$.