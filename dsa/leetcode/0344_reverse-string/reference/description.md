## Description

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> with `O(1)` extra memory.
### Function Contract

**Inputs**

- `s`: The mutable array of characters to reverse.

**Return value**

Return nothing; after the call, `s` itself must contain the characters in reverse order.

### Examples
#### Example 1

- **Input:** $s = ["h","e","l","l","o"]$
- **Output:** `["o","l","l","e","h"]`
#### Example 2

- **Input:** $s = ["H","a","n","n","a","h"]$
- **Output:** `["h","a","n","n","a","H"]`
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- $s[i]$ is a <a href="https://en.wikipedia.org/wiki/ASCII#Printable_characters" target="_blank">printable ascii character</a>.