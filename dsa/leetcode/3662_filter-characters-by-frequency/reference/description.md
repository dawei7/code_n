## Description

You are given a string `s` consisting of lowercase English letters and an integer `k`.

Your task is to construct a new string that contains only those characters from `s` which appear **fewer** than `k` times in the entire string. The order of characters in the new string must be the **same** as their **order** in `s`.

Return the resulting string. If no characters qualify, return an empty string.

Note: **Every occurrence** of a character that occurs fewer than `k` times is kept.
### Function Contract

- Refer to method signature.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "aadbbcccca", k = 3

**Output:** "dbb"

**Explanation:**

Character frequencies in `s`:

- `'a'` appears 3 times

- `'d'` appears 1 time

- `'b'` appears 2 times

- `'c'` appears 4 times

Only `'d'` and `'b'` appear fewer than 3 times. Preserving their order, the result is `"dbb"`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "xyz", k = 2

**Output:** "xyz"

**Explanation:**

All characters (`'x'`, `'y'`, `'z'`) appear exactly once, which is fewer than 2. Thus the whole string is returned.

</div>
### Constraints

- $1 \le \text{s.length} \le 100$

- `s` consists of lowercase English letters.

- $1 \le k \le \text{s.length}$