## Description

You are given two integers, `m` and `k`, and an integer array `nums`.

A sequence of integers `seq` is called **magical** if:

- `seq` has a size of `m`.

- $0 \le \text{seq}[i] < \text{nums.length}$

- The **binary representation** of $2^\text{seq}[0] + 2^\text{seq}[1] + ... + 2^seq[m - 1]$ has `k` **set bits**.

The **array product** of this sequence is defined as $prod(seq) = (nums[\text{seq}[0]] * nums[\text{seq}[1]] * ... * nums[seq[m - 1]])$.

Return the **sum** of the **array products** for all valid **magical** sequences.

Since the answer may be large, return it **modulo** $10^{9} + 7$.

A **set bit** refers to a bit in the binary representation of a number that has a value of 1.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** m = 5, k = 5, nums = [1,10,100,10000,1000000]

**Output:** 991600007

**Explanation:**

All permutations of `[0, 1, 2, 3, 4]` are magical sequences, each with an array product of $10^{13}$.

</div>
#### Example 2

<div class="example-block">
**Input:** m = 2, k = 2, nums = [5,4,3,2,1]

**Output:** 170

**Explanation:**

The magical sequences are `[0, 1]`, `[0, 2]`, `[0, 3]`, `[0, 4]`, `[1, 0]`, `[1, 2]`, `[1, 3]`, `[1, 4]`, `[2, 0]`, `[2, 1]`, `[2, 3]`, `[2, 4]`, `[3, 0]`, `[3, 1]`, `[3, 2]`, `[3, 4]`, `[4, 0]`, `[4, 1]`, `[4, 2]`, and `[4, 3]`.

</div>
#### Example 3

<div class="example-block">
**Input:** m = 1, k = 1, nums = [28]

**Output:** 28

**Explanation:**

The only magical sequence is `[0]`.

</div>
### Constraints

- $1 \le k \le m \le 30$

- $1 \le \text{nums.length} \le 50$

- $1 \le \text{nums}[i] \le 10^{8}$