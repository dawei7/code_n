## Description

You are given a string `word`.

Return the **maximum** number of non-intersecting **substrings** of word that are at **least** four characters long and start and end with the same letter.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** word = "abcdeafdef"

**Output:** 2

**Explanation:**

The two substrings are `"abcdea"` and `"fdef"`.

</div>
#### Example 2

<div class="example-block">
**Input:** word = "bcdaaaab"

**Output:** 1

**Explanation:**

The only substring is `"aaaa"`. Note that we cannot **also** choose `"bcdaaaab"` since it intersects with the other substring.

</div>
### Constraints

- $1 \le \text{word.length} \le 2 * 10^{5}$

- `word` consists only of lowercase English letters.