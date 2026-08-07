## Description

You are given a string `s` and an integer `k`.

Reverse the first `k` characters of `s` and return the resulting string.
### Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.
- `k`: The number of leading characters to reverse, with `1 <= k <= len(s)`.

Only the prefix `s[0:k]` changes order. The suffix beginning at index `k` is copied without modification.

**Return value**

Return `s[0:k]` in reverse order followed by `s[k:]`.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "abcd", k = 2

**Output:** "bacd"

**Explanation:**​​​​​​​

The first $k = 2$ characters `"ab"` are reversed to `"ba"`. The final resulting string is `"bacd"`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "xyz", k = 3

**Output:** "zyx"

**Explanation:**

The first $k = 3$ characters `"xyz"` are reversed to `"zyx"`. The final resulting string is `"zyx"`.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "hey", k = 1

**Output:** "hey"

**Explanation:**

The first $k = 1$ character `"h"` remains unchanged on reversal. The final resulting string is `"hey"`.

</div>
### Constraints

- $1 \le \text{s.length} \le 100$

- `s` consists of lowercase English letters.

- $1 \le k \le \text{s.length}$