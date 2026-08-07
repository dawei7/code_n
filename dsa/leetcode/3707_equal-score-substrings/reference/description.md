## Description

You are given a string `s` consisting of lowercase English letters.

The **score** of a string is the sum of the positions of its characters in the alphabet, where $'a' = 1$, $'b' = 2$, ..., $'z' = 26$.

Determine whether there exists an index `i` such that the string can be split into two **non-empty** **<strong>substrings**</strong> `s[0..i]` and $s[(i + 1)..(n - 1)]$ that have **equal** scores.

Return `true` if such a split exists, otherwise return `false`.
### Function Contract

**Inputs**

- `s`: A lowercase English string of length $n$.

Each candidate split index satisfies $0\le i<n-1$, ensuring that both the prefix and suffix contain at least one character. A letter `c` contributes `ord(c) - ord("a") + 1` to its substring's score.

**Return value**

Return `true` if the score of `s[0..i]` equals the score of `s[(i + 1)..(n - 1)]` for at least one legal `i`; return `false` if no legal split balances the scores.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "adcb"

**Output:** true

**Explanation:**

Split at index $i = 1$:

- Left substring = $s[0..1] = "ad"$ with $score = 1 + 4 = 5$

- Right substring = $s[2..3] = "cb"$ with $score = 3 + 2 = 5$

Both substrings have equal scores, so the output is `true`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "bace"

**Output:** false

**Explanation:​​​​​​**

**​​​​​​​**No split produces equal scores, so the output is `false`.

</div>
### Constraints

- $2 \le \text{s.length} \le 100$

- `s` consists of lowercase English letters.