## Function Contract

**Inputs**

- `s`: A nonempty lowercase English string to parse from left to right.

The valid words are `zero`, `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight`, and `nine`. A partial word is not a match, and a failed position advances by exactly one character rather than discarding a longer fragment.

**Return value**

Return the string formed by the corresponding digits of all matched number words, in discovery order, or `""` if there are no matches.
