## Description

You are given three integers `l`, `r`, and `k`.

Consider all possible integers consisting of **exactly** `k` digits, where each digit is chosen independently from the integer range `[l, r]` (inclusive). If 0 is included in the range, leading zeros are allowed.

Return an integer representing the **sum of all such numbers.**​​​​​​​ Since the answer may be very large, return it **modulo** $10^{9} + 7$.
### Function Contract

**Inputs**

- `l`: The smallest digit that may be chosen.
- `r`: The largest digit that may be chosen; the interval includes both endpoints.
- `k`: The exact number of independently chosen digit positions in every sequence.

For digits $d_{k-1},d_{k-2},\ldots,d_0$, the represented integer is

$\sum_{p=0}^{k-1} d_p10^p.$

Every one of the $(r-l+1)^k$ digit sequences contributes once, including sequences whose first digit is zero.

**Return value**

Return the sum of all represented integers reduced modulo $1{,}000{,}000{,}007$.

### Examples

#### Example 1

<div class="example-block">
**Input:** l = 1, r = 2, k = 2

**Output:** 66

**Explanation:**

- All numbers formed using $k = 2$ digits in the range `[1, 2]` are `11, 12, 21, 22`.

- The total sum is $11 + 12 + 21 + 22 = 66$.

</div>
#### Example 2

<div class="example-block">
**Input:** l = 0, r = 1, k = 3

**Output:** 444

**Explanation:**

- All numbers formed using $k = 3$ digits in the range `[0, 1]` are `000, 001, 010, 011, 100, 101, 110, 111`​​​​​​​.

- These numbers without leading zeros are `0, 1, 10, 11, 100, 101, 110, 111`.

- The total sum is 444.

</div>
#### Example 3

<div class="example-block">
**Input:** l = 5, r = 5, k = 10

**Output:** 555555520

**Explanation:**​​​​​​​

- 5555555555 is the only valid number consisting of $k = 10$ digits in the range `[5, 5]`.

- The total sum is $5555555555 \% (10^{9} + 7) = 555555520$.

</div>
### Constraints

- $0 \le l \le r \le 9$

- $1 \le k \le 10^{9}$