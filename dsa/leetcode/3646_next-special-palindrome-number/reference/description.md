## Description

You are given an integer `n`.

A number is called **special** if:

- It is a **palindrome**.

- Every digit `k` in the number appears **exactly** `k` times.

Return the **smallest** special number **strictly **greater than `n`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** n = 2

**Output:** 22

**Explanation:**

22 is the smallest special number greater than 2, as it is a palindrome and the digit 2 appears exactly 2 times.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 33

**Output:** 212

**Explanation:**

212 is the smallest special number greater than 33, as it is a palindrome and the digits 1 and 2 appear exactly 1 and 2 times respectively.

</div>
### Constraints

- $0 \le n \le 10^{15}$