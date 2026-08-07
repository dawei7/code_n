## Description

You are given a string `s`. It may contain any number of `'*'` characters. Your task is to remove all `'*'` characters.

While there is a `'*'`, do the following operation:

- Delete the leftmost `'*'` and the **smallest** non-`'*'` character to its *left*. If there are several smallest characters, you can delete any of them.

Return the lexicographically smallest resulting string after removing all `'*'` characters.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "aaba*"

**Output:** "aab"

**Explanation:**

We should delete one of the `'a'` characters with `'*'`. If we choose $s[3]$, `s` becomes the lexicographically smallest.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "abc"

**Output:** "abc"

**Explanation:**

There is no `'*'` in the string.<!-- notionvc: ff07e34f-b1d6-41fb-9f83-5d0ba3c1ecde -->

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists only of lowercase English letters and `'*'`.

- The input is generated such that it is possible to delete all `'*'` characters.