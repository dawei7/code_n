## Function Contract

**Input**

- `s`: a nonempty string containing only lowercase English letters.

Process every character from left to right. Discard a character exactly when it belongs to `{a, e, i, o, u}`; retain every other character without changing the retained characters' order.

**Return value**

- The new string formed by concatenating all retained characters. Its length may be zero when every input character is a vowel.
