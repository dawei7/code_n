## Description

You are given two integer arrays `nums` and `divisors`.

The **divisibility score** of $\text{divisors}[i]$ is the number of indices `j` such that $\text{nums}[j]$ is divisible by $\text{divisors}[i]$.

Return the integer $\text{divisors}[i]$ with the **maximum** divisibility score. If multiple integers have the maximum score, return the smallest one.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [2,9,15,50], divisors = [5,3,7,2]

**Output:** 2

**Explanation:**

The divisibility score of $\text{divisors}[0]$ is 2 since $\text{nums}[2]$ and $\text{nums}[3]$ are divisible by 5.

The divisibility score of $\text{divisors}[1]$ is 2 since $\text{nums}[1]$ and $\text{nums}[2]$ are divisible by 3.

The divisibility score of $\text{divisors}[2]$ is 0 since none of the numbers in `nums` is divisible by 7.

The divisibility score of $\text{divisors}[3]$ is 2 since $\text{nums}[0]$ and $\text{nums}[3]$ are divisible by 2.

As $\text{divisors}[0]$, $\text{divisors}[1]$, and $\text{divisors}[3]$ have the same divisibility score, we return the smaller one which is $\text{divisors}[3]$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,7,9,3,9], divisors = [5,2,3]

**Output:** 3

**Explanation:**

The divisibility score of $\text{divisors}[0]$ is 0 since none of numbers in `nums` is divisible by 5.

The divisibility score of $\text{divisors}[1]$ is 1 since only $\text{nums}[0]$ is divisible by 2.

The divisibility score of $\text{divisors}[2]$ is 3 since $\text{nums}[2]$, $\text{nums}[3]$ and $\text{nums}[4]$ are divisible by 3.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [20,14,21,10], divisors = [10,16,20]

**Output:** 10

**Explanation:**

The divisibility score of $\text{divisors}[0]$ is 2 since $\text{nums}[0]$ and $\text{nums}[3]$ are divisible by 10.

The divisibility score of $\text{divisors}[1]$ is 0 since none of the numbers in `nums` is divisible by 16.

The divisibility score of $\text{divisors}[2]$ is 1 since $\text{nums}[0]$ is divisible by 20.

</div>
### Constraints

- $1 \le \text{nums.length}, \text{divisors.length} \le 1000$

- $1 \le \text{nums}[i], \text{divisors}[i] \le 10^{9}$