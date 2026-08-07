### 1. Description

Given a** **string `s`, find any substring of length `2` which is also present in the reverse of `s`.

Return `true`* if such a substring exists, and *`false`* otherwise.*

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **s = "leetcode"

**Output: **true

**Explanation:** Substring `"ee"` is of length `2` which is also present in $reverse(s) = "edocteel"$.

</div>
#### Example 2

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **s = "abcba"

**Output: **true

**Explanation:** All of the substrings of length `2` `"ab"`, `"bc"`, `"cb"`, `"ba"` are also present in $reverse(s) = "abcba"$.

</div>
#### Example 3

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **s = "abcd"

**Output: **false

**Explanation:** There is no substring of length `2` in `s`, which is also present in the reverse of `s`.

</div>

### 4. Constraints

- $1 \le \text{s.length} \le 100$

- `s` consists only of lowercase English letters.