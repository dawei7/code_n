## Description

You are given a binary string `s`.

You can perform the following operation on the string **any** number of times:

- Choose **any** index `i` from the string where $i + 1 < \text{s.length}$ such that $s[i] = '1'$ and $s[i + 1] = '0'$.

- Move the character $s[i]$ to the **right** until it reaches the end of the string or another `'1'`. For example, for `s = "010010"`, if we choose $i = 1$, the resulting string will be `s = "0**<u>001</u>**10"`.

Return the **maximum** number of operations that you can perform.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "1001101"

**Output:** 4

**Explanation:**

We can perform the following operations:

- Choose index $i = 0$. The resulting string is `s = "<u>**001**</u>1101"`.

- Choose index $i = 4$. The resulting string is `s = "0011<u>**01**</u>1"`.

- Choose index $i = 3$. The resulting string is `s = "001**<u>01</u>**11"`.

- Choose index $i = 2$. The resulting string is `s = "00**<u>01</u>**111"`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "00111"

**Output:** 0

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- $s[i]$ is either `'0'` or `'1'`.