## Description

You are given an array of **positive** integers `nums`.

An array `arr` is called **product equivalent** if $prod(arr) = lcm(arr) * gcd(arr)$, where:

- `prod(arr)` is the product of all elements of `arr`.

- `gcd(arr)` is the GCD of all elements of `arr`.

- `lcm(arr)` is the LCM of all elements of `arr`.

Return the length of the **longest** **product equivalent** subarray of `nums`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,1,2,1,1,1]

**Output:** 5

**Explanation:**

The longest product equivalent subarray is `[1, 2, 1, 1, 1]`, where $prod([1, 2, 1, 1, 1]) = 2$, $gcd([1, 2, 1, 1, 1]) = 1$, and $lcm([1, 2, 1, 1, 1]) = 2$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,3,4,5,6]

**Output:** 3

**Explanation:**

The longest product equivalent subarray is $[3, 4, 5].$

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2,3,1,4,5,1]

**Output:** 5

</div>
### Constraints

- $2 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 10$