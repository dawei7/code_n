## Description

You are given an integer `num`.

A number `num` is called a **Complete Prime Number** if every **prefix** and every **suffix** of `num` is **prime**.

Return `true` if `num` is a Complete Prime Number, otherwise return `false`.

**Note**:

- A **prefix** of a number is formed by the **first** `k` digits of the number.

- A **suffix** of a number is formed by the **last** `k` digits of the number.

- Single-digit numbers are considered Complete Prime Numbers only if they are **prime**.
### Function Contract

**Inputs**

- `num`: The positive integer whose decimal prefixes and suffixes must be examined.

For every length $k$ from 1 through the number of decimal digits, take both the first $k$ digits and the last $k$ digits as integers. The complete number itself is therefore included in both families. A prime is an integer greater than 1 with no positive divisors other than 1 and itself.

**Return value**

Return `true` if every required prefix and suffix is prime. Return `false` as soon as any one of them is nonprime.

### Examples

#### Example 1

<div class="example-block">
**Input:** num = 23

**Output:** true

**Explanation:**

- **​​​​​​​**Prefixes of $num = 23$ are 2 and 23, both are prime.

- Suffixes of $num = 23$ are 3 and 23, both are prime.

- All prefixes and suffixes are prime, so 23 is a Complete Prime Number and the answer is `true`.

</div>
#### Example 2

<div class="example-block">
**Input:** num = 39

**Output:** false

**Explanation:**

- Prefixes of $num = 39$ are 3 and 39. 3 is prime, but 39 is not prime.

- Suffixes of $num = 39$ are 9 and 39. Both 9 and 39 are not prime.

- At least one prefix or suffix is not prime, so 39 is not a Complete Prime Number and the answer is `false`.

</div>
#### Example 3

<div class="example-block">
**Input:** num = 7

**Output:** true

**Explanation:**

- 7 is prime, so all its prefixes and suffixes are prime and the answer is `true`.

</div>
### Constraints

- $1 \le num \le 10^{9}$