## Description

You are given an integer `n` perform the following steps:

- Convert each digit of `n` into its *lowercase English word* (e.g., 4 → "four", 1 → "one").

- **Concatenate** those words in the **original digit order** to form a string `s`.

Return the number of **distinct** characters in `s` that appear an **odd** number of times.
### Function Contract

- Refer to method signature.

### Examples

#### Example 1

<div class="example-block">
**Input:** n = 41

**Output:** 5

**Explanation:**

41 → `"fourone"`

Characters with odd frequencies: `'f'`, `'u'`, `'r'`, `'n'`, `'e'`. Thus, the answer is 5.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 20

**Output:** 5

**Explanation:**

20 → `"twozero"`

Characters with odd frequencies: `'t'`, `'w'`, `'z'`, `'e'`, `'r'`. Thus, the answer is 5.

</div>
### Constraints

- $1 \le n \le 10^{9}$