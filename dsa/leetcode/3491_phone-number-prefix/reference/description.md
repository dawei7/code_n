## Description

You are given a string array `numbers` that represents phone numbers. Return `true` if no phone number is a prefix of any other phone number; otherwise, return `false`.
### Function Contract

- Refer to method signature.

### Examples

#### Example 1

<div class="example-block">
**Input:** numbers = ["1","2","4","3"]

**Output:** true

**Explanation:**

No number is a prefix of another number, so the output is `true`.

</div>
#### Example 2

<div class="example-block">
**Input:** numbers = ["001","007","15","00153"]

**Output:** false

**Explanation:**

The string `"001"` is a prefix of the string `"00153"`. Thus, the output is `false`.

</div>
### Constraints

- $2 \le \text{numbers.length} \le 50$

- $1 \le \text{numbers}[i].length \le 50$

- All numbers contain only digits `'0'` to `'9'`.