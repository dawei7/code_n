## Description

You are given a **palindromic** string `s` and an integer `k`.

Return the **k-th** **lexicographically smallest** palindromic permutation of `s`. If there are fewer than `k` distinct palindromic permutations, return an empty string.

**Note:** Different rearrangements that yield the same palindromic string are considered identical and are counted once.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "abba", k = 2

**Output:** "baab"

**Explanation:**

- The two distinct palindromic rearrangements of `"abba"` are `"abba"` and `"baab"`.

- Lexicographically, `"abba"` comes before `"baab"`. Since $k = 2$, the output is `"baab"`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "aa", k = 2

**Output:** ""

**Explanation:**

- There is only one palindromic rearrangement: `"aa"`.

- The output is an empty string since $k = 2$ exceeds the number of possible rearrangements.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "bacab", k = 1

**Output:** "abcba"

**Explanation:**

- The two distinct palindromic rearrangements of `"bacab"` are `"abcba"` and `"bacab"`.

- Lexicographically, `"abcba"` comes before `"bacab"`. Since $k = 1$, the output is `"abcba"`.

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{4}$

- `s` consists of lowercase English letters.

- `s` is guaranteed to be palindromic.

- $1 \le k \le 10^{6}$