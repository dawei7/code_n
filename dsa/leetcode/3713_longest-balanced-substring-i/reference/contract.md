## Function Contract

**Inputs**

- `s`: A lowercase English string.

A substring must occupy one contiguous interval of `s`. Only characters present in that interval are compared; absent alphabet letters do not need to have the same frequency.

**Return value**

Return the maximum length among all balanced substrings. Any non-empty one-character substring is balanced, so the result is always at least `1`.
