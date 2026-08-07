## Description

Given a string `s`, return the **maximum** length of a substring such that it contains *at most two occurrences* of each character.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "bcbbbcba"

**Output:** 4

**Explanation:**

The following substring has a length of 4 and contains at most two occurrences of each character: `"bcbb<u>bcba</u>"`.</div>
#### Example 2

<div class="example-block">
**Input:** s = "aaaa"

**Output:** 2

**Explanation:**

The following substring has a length of 2 and contains at most two occurrences of each character: `"<u>aa</u>aa"`.</div>
### Constraints

- $2 \le \text{s.length} \le 100$

- `s` consists only of lowercase English letters.