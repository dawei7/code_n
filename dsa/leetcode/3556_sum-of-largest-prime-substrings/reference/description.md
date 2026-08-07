## Description

Given a string `s`, find the sum of the **3 largest unique prime numbers** that can be formed using any of its** substrings**.

Return the **sum** of the three largest unique prime numbers that can be formed. If fewer than three exist, return the sum of **all** available primes. If no prime numbers can be formed, return 0.

**Note:** Each prime number should be counted only **once**, even if it appears in **multiple** substrings. Additionally, when converting a substring to an integer, any leading zeros are ignored.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "12234"

**Output:** 1469

**Explanation:**

- The unique prime numbers formed from the substrings of `"12234"` are 2, 3, 23, 223, and 1223.

- The 3 largest primes are 1223, 223, and 23. Their sum is 1469.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "111"

**Output:** 11

**Explanation:**

- The unique prime number formed from the substrings of `"111"` is 11.

- Since there is only one prime number, the sum is 11.

</div>
### Constraints

- $1 \le \text{s.length} \le 10$

- `s` consists of only digits.