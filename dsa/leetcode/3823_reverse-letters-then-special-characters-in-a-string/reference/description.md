### 1. Description

You are given a string `s` consisting of lowercase English letters and special characters.

Your task is to perform these **in order**:

- **Reverse** the **lowercase letters** and place them back into the positions originally occupied by letters.

- **Reverse** the **special characters** and place them back into the positions originally occupied by special characters.

Return the resulting string after performing the reversals.

### 2. Function Contract

**Inputs**

- `s`: A nonempty string containing only lowercase English letters and special characters from the permitted set.

Let $N = \lvert\texttt{s}\rvert$.

**Return value**

Return a string of length $N$. Every original letter position must still contain a letter, with the left-to-right letter sequence reversed. Every original special-character position must still contain a special character, with that left-to-right sequence reversed.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = ")ebc#da@f("

**Output:** "(fad@cb#e)"

**Explanation:**

- The letters in the string are `['e', 'b', 'c', 'd', 'a', 'f']`:

		<li>Reversing them gives `['f', 'a', 'd', 'c', 'b', 'e']`

- `s` becomes `")fad#cb@e("`

	</li>
- ​​​​​​​The special characters in the string are `[')', '#', '@', '(']`:

		<li>Reversing them gives `['(', '@', '#', ')']`

- `s` becomes `"(fad@cb#e)"`

	</li>

</div>
#### Example 2

<div class="example-block">
**Input:** s = "z"

**Output:** "z"

**Explanation:**

The string contains only one letter, and reversing it does not change the string. There are no special characters.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "!@#$%^&*()"

**Output:** ")(*&^%$#@!"

**Explanation:**

The string contains no letters. The string contains all special characters, so reversing the special characters reverses the whole string.

</div>

### 4. Constraints

- $1 \le \text{s.length} \le 100$

- `s` consists only of lowercase English letters and the special characters in $"!@#$%^&*()"$.