## Description

Given a string `s` containing only digits, return the lexicographically smallest string that can be obtained after swapping **adjacent** digits in `s` with the same **parity** at most **once**.

Digits have the same parity if both are odd or both are even. For example, 5 and 9, as well as 2 and 4, have the same parity, while 6 and 9 do not.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "45320"

**Output:** "43520"

**Explanation: **

$s[1] = '5'$ and $s[2] = '3'$ both have the same parity, and swapping them results in the lexicographically smallest string.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "001"

**Output:** "001"

**Explanation:**

There is no need to perform a swap because `s` is already the lexicographically smallest.

</div>
### Constraints

- $2 \le \text{s.length} \le 100$

- `s` consists only of digits.