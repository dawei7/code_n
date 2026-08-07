## Description

You are given a string `s` consisting of lowercase English letters.

Return an integer denoting the **maximum** number of substrings you can split `s` into such that each **substring** starts with a **distinct** character (i.e., no two substrings start with the same character).
### Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters to partition into consecutive, nonempty pieces.

The pieces must concatenate back to exactly `s`. Only their starting characters must be distinct; characters elsewhere inside the substrings may repeat freely.

**Return value**

Return the greatest possible number of substrings in a valid complete partition of `s`.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "abab"

**Output:** 2

**Explanation:**

- Split `"abab"` into `"a"` and `"bab"`.

- Each substring starts with a distinct character i.e `'a'` and `'b'`. Thus, the answer is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "abcd"

**Output:** 4

**Explanation:**

- Split `"abcd"` into `"a"`, `"b"`, `"c"`, and `"d"`.

- Each substring starts with a distinct character. Thus, the answer is 4.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "aaaa"

**Output:** 1

**Explanation:**

- All characters in `"aaaa"` are `'a'`.

- Only one substring can start with `'a'`. Thus, the answer is 1.

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of lowercase English letters.