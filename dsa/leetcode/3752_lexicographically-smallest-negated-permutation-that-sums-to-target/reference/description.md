## Description

You are given a positive integer `n` and an integer `target`.

Return the **lexicographically smallest** array of integers of size `n` such that:

- The **sum** of its elements equals `target`.

- The **absolute values** of its elements form a **permutation** of size `n`.

If no such array exists, return an empty array.

A **permutation** of size `n` is a rearrangement of integers `1, 2, ..., n`.
### Function Contract

**Inputs**

- `n`: The array length and the largest required absolute value.
- `target`: The required signed sum of all array elements.

Every magnitude in the inclusive range $1$ through $n$ must occur once. Lexicographic order compares the first unequal positions of two arrays by their ordinary signed integer values.

**Return value**

Return the lexicographically smallest valid signed permutation, or `[]` if no assignment of signs can produce `target`.

### Examples
#### Example 1

<div class="example-block">
**Input:** n = 3, target = 0

**Output:** [-3,1,2]

**Explanation:**

The arrays that sum to 0 and whose absolute values form a permutation of size 3 are:

- `[-3, 1, 2]`

- `[-3, 2, 1]`

- `[-2, -1, 3]`

- `[-2, 3, -1]`

- `[-1, -2, 3]`

- `[-1, 3, -2]`

- `[1, -3, 2]`

- `[1, 2, -3]`

- `[2, -3, 1]`

- `[2, 1, -3]`

- `[3, -2, -1]`

- `[3, -1, -2]`

The lexicographically smallest one is `[-3, 1, 2]`.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 1, target = 10000000000

**Output:** []

**Explanation:**

There are no arrays that sum to 10000000000 and whose absolute values form a permutation of size 1. Therefore, the answer is `[]`.

</div>
### Constraints

- $1 \le n \le 10^{5}$

- $-10^{10} \le target \le 10^{10}$