## Description

Given a string `s` consisting of words and spaces, return *the length of the **last** word in the string.*

A **word** is a maximal substring consisting of non-space characters only.
### Function Contract

**Inputs**

- `s`: A string of English-letter words separated or surrounded by spaces.

**Return value**

Return the character count of the final maximal non-space substring.

### Examples
#### Example 1

- **Input:** `s = "Hello World"`
- **Output:** `5`
- **Explanation:** The last word is "World" with length 5.
#### Example 2

- **Input:** `s = "   fly me   to   the moon  "`
- **Output:** `4`
- **Explanation:** The last word is "moon" with length 4.
#### Example 3

- **Input:** `s = "luffy is still joyboy"`
- **Output:** `6`
- **Explanation:** The last word is "joyboy" with length 6.
### Constraints

- $1 \le \text{s.length} \le 10^{4}$

- `s` consists of only English letters and spaces `' '`.

- There will be at least one word in `s`.