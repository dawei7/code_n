## Description

You are given a string `word`. A letter `c` is called **special** if it appears **both** in lowercase and uppercase in `word`, and **every** lowercase occurrence of `c` appears before the **first** uppercase occurrence of `c`.

Return the number of* ***special** letters* *in* *`word`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** word = "aaAbcBC"

**Output:** 3

**Explanation:**

The special characters are `'a'`, `'b'`, and `'c'`.

</div>
#### Example 2

<div class="example-block">
**Input:** word = "abc"

**Output:** 0

**Explanation:**

There are no special characters in `word`.

</div>
#### Example 3

<div class="example-block">
**Input:** word = "AbBCab"

**Output:** 0

**Explanation:**

There are no special characters in `word`.

</div>
### Constraints

- $1 \le \text{word.length} \le 2 * 10^{5}$

- `word` consists of only lowercase and uppercase English letters.