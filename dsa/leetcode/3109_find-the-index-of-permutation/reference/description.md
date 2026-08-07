## Description

Given an array `perm` of length `n` which is a permutation of `[1, 2, ..., n]`, return the index of `perm` in the lexicographically sorted array of all of the permutations of `[1, 2, ..., n]`.

Since the answer may be very large, return it **modulo** $10^{9} + 7$.
### Function Contract

- Refer to method signature.

### Examples

#### Example 1

<div class="example-block">
**Input:** perm = [1,2]

**Output:** 0

**Explanation:**

There are only two permutations in the following order:

`[1,2]`, `[2,1]`

And `[1,2]` is at index 0.

</div>
#### Example 2

<div class="example-block">
**Input:** perm = [3,1,2]

**Output:** 4

**Explanation:**

There are only six permutations in the following order:

`[1,2,3]`, `[1,3,2]`, `[2,1,3]`, `[2,3,1]`, `[3,1,2]`, `[3,2,1]`

And `[3,1,2]` is at index 4.

</div>
### Constraints

- $1 \le n = \text{perm.length} \le 10^{5}$

- `perm` is a permutation of `[1, 2, ..., n]`.