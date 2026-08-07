## Description

You are given an integer array `nums`.

The **alternating sum** of `nums` is the value obtained by **adding** elements at even indices and **subtracting** elements at odd indices. That is, $\text{nums}[0] - \text{nums}[1] + \text{nums}[2] - \text{nums}[3]...$

Return an integer denoting the alternating sum of `nums`.
### Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.

Indices are zero-based. Values at indices $0,2,4,\ldots$ have positive signs, while values at indices $1,3,5,\ldots$ have negative signs.

**Return value**

Return the signed sum of all elements under that alternating sign pattern.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,3,5,7]

**Output:** -4

**Explanation:**

- Elements at even indices are $\text{nums}[0] = 1$ and $\text{nums}[2] = 5$ because 0 and 2 are even numbers.

- Elements at odd indices are $\text{nums}[1] = 3$ and $\text{nums}[3] = 7$ because 1 and 3 are odd numbers.

- The alternating sum is $\text{nums}[0] - \text{nums}[1] + \text{nums}[2] - \text{nums}[3] = 1 - 3 + 5 - 7 = -4$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [100]

**Output:** 100

**Explanation:**

- The only element at even indices is $\text{nums}[0] = 100$ because 0 is an even number.

- There are no elements on odd indices.

- The alternating sum is $\text{nums}[0] = 100$.

</div>
### Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 100$