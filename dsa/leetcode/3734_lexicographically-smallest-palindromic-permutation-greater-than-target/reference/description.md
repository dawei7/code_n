### 1. Description

You are given two strings `s` and `target`, each of length `n`, consisting of lowercase English letters.

Return the **lexicographically smallest string** that is **both** a **palindromic permutation** of `s` and **strictly** greater than `target`. If no such permutation exists, return an empty string.

### 2. Function Contract

**Inputs**

- `s`: The multiset of lowercase letters that the result must permute exactly.
- `target`: The equal-length string that the result must exceed lexicographically and strictly.

A palindromic permutation uses every character occurrence from `s` and reads identically from left to right and right to left. Equality with `target` is insufficient.

**Return value**

Return the smallest qualifying palindrome in lexicographic order, or `""` when no qualifying palindromic permutation exists.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = "baba", target = "abba"

**Output:** "baab"

**Explanation:**

- The palindromic permutations of `s` (in lexicographical order) are `"abba"` and `"baab"`.

- The lexicographically smallest permutation that is strictly greater than `target` is `"baab"`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "baba", target = "bbaa"

**Output:** ""

**Explanation:**

- The palindromic permutations of `s` (in lexicographical order) are `"abba"` and `"baab"`.

- None of them is lexicographically strictly greater than `target`. Therefore, the answer is `""`.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "abc", target = "abb"

**Output:** ""

**Explanation:**

`s` has no palindromic permutations. Therefore, the answer is `""`.

</div>
#### Example 4

<div class="example-block">
**Input:** s = "aac", target = "abb"

**Output:** "aca"

**Explanation:**

- The only palindromic permutation of `s` is `"aca"`.

- `"aca"` is strictly greater than `target`. Therefore, the answer is `"aca"`.

</div>

### 4. Constraints

- $1 \le n = \text{s.length} = \text{target.length} \le 300$

- `s` and `target` consist of only lowercase English letters.