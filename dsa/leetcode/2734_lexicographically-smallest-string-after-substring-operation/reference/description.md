## Description

Given a string `s` consisting of lowercase English letters. Perform the following operation:

- Select any non-empty substring then replace every letter of the substring with the preceding letter of the English alphabet. For example, 'b' is converted to 'a', and 'a' is converted to 'z'.

Return the **lexicographically smallest** string **after performing the operation**.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "cbabc"

**Output:** "baabc"

**Explanation:**

Perform the operation on the substring starting at index 0, and ending at index 1 inclusive.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "aa"

**Output:** "az"

**Explanation:**

Perform the operation on the last letter.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "acbbc"

**Output:** "abaab"

**Explanation:**

Perform the operation on the substring starting at index 1, and ending at index 4 inclusive.

</div>
#### Example 4

<div class="example-block">
**Input:** s = "leetcode"

**Output:** "kddsbncd"

**Explanation:**

Perform the operation on the entire string.

</div>
### Constraints

- $1 \le \text{s.length} \le 3 * 10^{5}$

- `s` consists of lowercase English letters