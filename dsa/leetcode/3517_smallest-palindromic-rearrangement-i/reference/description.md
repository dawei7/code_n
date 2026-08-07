## Description

You are given a **palindromic** string `s`.

Return the **lexicographically smallest** palindromic permutation of `s`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "z"

**Output:** "z"

**Explanation:**

A string of only one character is already the lexicographically smallest palindrome.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "babab"

**Output:** "abbba"

**Explanation:**

Rearranging `"babab"` → `"abbba"` gives the smallest lexicographic palindrome.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "daccad"

**Output:** "acddca"

**Explanation:**

Rearranging `"daccad"` → `"acddca"` gives the smallest lexicographic palindrome.

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of lowercase English letters.

- `s` is guaranteed to be palindromic.