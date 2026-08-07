## Description

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.
### Function Contract

**Inputs**

- `haystack`: The lowercase string to search.
- `needle`: The non-empty lowercase string to locate.

**Return value**

Return the zero-based index of the first match, or `-1` if no match exists.

### Examples

#### Example 1

- **Input:** $haystack = "sadbutsad", needle = "sad"$
- **Output:** `0`
- **Explanation:** "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
#### Example 2

- **Input:** $haystack = "leetcode", needle = "leeto"$
- **Output:** `-1`
- **Explanation:** "leeto" did not occur in "leetcode", so we return -1.
### Constraints

- $1 \le \text{haystack.length}, \text{needle.length} \le 10^{4}$

- `haystack` and `needle` consist of only lowercase English characters.