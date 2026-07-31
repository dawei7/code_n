## Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.
- `k`: The number of leading characters to reverse, with `1 <= k <= len(s)`.

Only the prefix `s[0:k]` changes order. The suffix beginning at index `k` is copied without modification.

**Return value**

Return `s[0:k]` in reverse order followed by `s[k:]`.
