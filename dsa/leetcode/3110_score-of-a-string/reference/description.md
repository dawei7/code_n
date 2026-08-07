## Description

You are given a string `s`. The **score** of a string is defined as the sum of the absolute difference between the **ASCII** values of adjacent characters.

Return the **score** of* *`s`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "hello"

**Output:** 13

**Explanation:**

The **ASCII** values of the characters in `s` are: $'h' = 104$, $'e' = 101$, $'l' = 108$, $'o' = 111$. So, the score of `s` would be $|104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13$.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "zaz"

**Output:** 50

**Explanation:**

The **ASCII** values of the characters in `s` are: $'z' = 122$, $'a' = 97$. So, the score of `s` would be $|122 - 97| + |97 - 122| = 25 + 25 = 50$.

</div>
### Constraints

- $2 \le \text{s.length} \le 100$

- `s` consists only of lowercase English letters.