## Description

Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `s`. Specifically:

- Each letter in `pattern` maps to **exactly** one unique word in `s`.

- Each unique word in `s` maps to **exactly** one letter in `pattern`.

- No two letters map to the same word, and no two words map to the same letter.
### Function Contract

**Inputs**

- `pattern`: A nonempty string of lowercase English letters.
- `s`: Nonempty lowercase English words separated by single spaces.

**Return value**

Return `true` exactly when the pattern letters and words form the required position-by-position bijection.

### Examples
#### Example 1

<div class="example-block">
**Input:** pattern = "abba", s = "dog cat cat dog"

**Output:** true

**Explanation:**

The bijection can be established as:

- `'a'` maps to `"dog"`.

- `'b'` maps to `"cat"`.

</div>
#### Example 2

<div class="example-block">
**Input:** pattern = "abba", s = "dog cat cat fish"

**Output:** false

</div>
#### Example 3

<div class="example-block">
**Input:** pattern = "aaaa", s = "dog cat cat dog"

**Output:** false

</div>
### Constraints

- $1 \le \text{pattern.length} \le 300$

- `pattern` contains only lower-case English letters.

- $1 \le \text{s.length} \le 3000$

- `s` contains only lowercase English letters and spaces `' '`.

- `s` **does not contain** any leading or trailing spaces.

- All the words in `s` are separated by a **single space**.