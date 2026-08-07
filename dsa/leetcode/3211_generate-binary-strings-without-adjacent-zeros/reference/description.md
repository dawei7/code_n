## Description

You are given a positive integer `n`.

A binary string `x` is **valid** if all substrings of `x` of length 2 contain **at least** one `"1"`.

Return all **valid** strings with length `n`**, **in *any* order.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** n = 3

**Output:** ["010","011","101","110","111"]

**Explanation:**

The valid strings of length 3 are: `"010"`, `"011"`, `"101"`, `"110"`, and `"111"`.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 1

**Output:** ["0","1"]

**Explanation:**

The valid strings of length 1 are: `"0"` and `"1"`.

</div>
### Constraints

- $1 \le n \le 18$