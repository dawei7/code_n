## Description

You are given an integer `n`.

Return `true` if its binary representation contains **exactly one adjacent pair** of set bits, and `false` otherwise.
### Function Contract

**Inputs**

- `n`: The integer whose binary representation is examined.

The representation of zero is `0`; positive values use their usual binary representation without leading zeroes.

**Return value**

Return `true` if exactly one neighboring pair of binary digits is `11`; otherwise, return `false`.

### Examples
#### Example 1

<div class="example-block">
**Input:** n = 6

**Output:** true

**Explanation:**

- Binary representation of 6 is `110`.

- There is exactly one adjacent pair of set bits (`"11"`). Thus, the answer is `true`​​​​​​​.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 5

**Output:** false

**Explanation:**

- Binary representation of 5 is `101`.

- There is no adjacent pair of set bits. Thus, the answer is `false`​​​​​​​.

</div>
### Constraints

- $0 \le n \le 10^{5}$