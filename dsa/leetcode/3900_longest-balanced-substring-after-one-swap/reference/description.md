## Description

You are given a binary string `s` consisting only of characters `'0'` and `'1'`.

A string is **balanced** if it contains an **equal** number of `'0'`s and `'1'`s.

You can perform **at most one** swap between any two characters in `s`. Then, you select a **balanced** substring from `s`.

Return an integer representing the **maximum** length of the **balanced** substring you can select.
### Function Contract

**Inputs**

- `s`: A non-empty string containing only `'0'` and `'1'`.

One operation may exchange the characters at any two indices in the complete string. The substring is selected after this optional operation and must occupy consecutive indices.

**Return value**

Return the maximum length of a substring containing equal numbers of zeros and ones after at most one swap. Return `0` when no non-empty balanced substring can be produced.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "100001"

**Output:** 4

**Explanation:**

- Swap `"10<u>**0**</u>00<u>**1**</u>"`. The string becomes `"101000"`.

- Select the substring `"<u>**1010**</u>00"`, which is balanced because it has two `'0'`s and two `'1'`s.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "111"

**Output:** 0

**Explanation:**

- Choose not to perform any swaps.

- Select the empty substring, which is balanced because it has zero `'0'`s and zero `'1'`s.

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists only of the characters `'0'` and `'1'`.