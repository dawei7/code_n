### 1. Description

Given a string `s`, find the **first** non-repeating character in it and return its index. If it **does not** exist, return `-1`.

### 2. Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.

**Return value**

Return the smallest index whose character has total frequency one, or `-1` if every character repeats.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = "leetcode"

**Output:** 0

**Explanation:**

The character `'l'` at index 0 is the first character that does not occur at any other index.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "loveleetcode"

**Output:** 2

</div>
#### Example 3

<div class="example-block">
**Input:** s = "aabb"

**Output:** -1

</div>

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of only lowercase English letters.