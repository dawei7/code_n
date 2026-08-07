## Description

You are given an integer array `nums`.

Return an integer that is the **maximum** distance between the **indices** of two (not necessarily different) prime numbers in `nums`*.*
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [4,2,9,5,3]

**Output:** 3

**Explanation:** $\text{nums}[1]$, $\text{nums}[3]$, and $\text{nums}[4]$ are prime. So the answer is $|4 - 1| = 3$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,8,2,8]

**Output:** 0

**Explanation:** $\text{nums}[2]$ is prime. Because there is just one prime number, the answer is $|2 - 2| = 0$.

</div>
### Constraints

- $1 \le \text{nums.length} \le 3 * 10^{5}$

- $1 \le \text{nums}[i] \le 100$

- The input is generated such that the number of prime numbers in the `nums` is at least one.