## Description

You are given a digit string `s` that consists of digits from 0 to 9.

A string is called **semi-repetitive** if there is **at most** one adjacent pair of the same digit. For example, `"0010"`, `"002020"`, `"0123"`, `"2002"`, and `"54944"` are semi-repetitive while the following are not: `"00101022"` (adjacent same digit pairs are 00 and 22), and `"1101234883"` (adjacent same digit pairs are 11 and 88).

Return the length of the **longest semi-repetitive substring** of `s`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "52233"

**Output:** 4

**Explanation:**

The longest semi-repetitive substring is "5223". Picking the whole string "52233" has two adjacent same digit pairs 22 and 33, but at most one is allowed.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "5494"

**Output:** 4

**Explanation:**

`s` is a semi-repetitive string.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "1111111"

**Output:** 2

**Explanation:**

The longest semi-repetitive substring is "11". Picking the substring "111" has two adjacent same digit pairs, but at most one is allowed.

</div>
### Constraints

- $1 \le \text{s.length} \le 50$

- $'0' \le s[i] \le '9'$