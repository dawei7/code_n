### 1. Description

Given two integers, `n` and `k`, an **alternating permutation** is a permutation of the first `n` positive integers such that no **two** adjacent elements are both odd or both even.

Return the **k-th** **alternating permutation** sorted in *lexicographical order*. If there are fewer than `k` valid **alternating permutations**, return an empty list.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 4, k = 6

**Output:** [3,4,1,2]

**Explanation:**

The lexicographically-sorted alternating permutations of `[1, 2, 3, 4]` are:

- `[1, 2, 3, 4]`

- `[1, 4, 3, 2]`

- `[2, 1, 4, 3]`

- `[2, 3, 4, 1]`

- `[3, 2, 1, 4]`

- `[3, 4, 1, 2]` ← 6th permutation

- `[4, 1, 2, 3]`

- `[4, 3, 2, 1]`

Since $k = 6$, we return `[3, 4, 1, 2]`.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 3, k = 2

**Output:** [3,2,1]

**Explanation:**

The lexicographically-sorted alternating permutations of `[1, 2, 3]` are:

- `[1, 2, 3]`

- `[3, 2, 1]` ← 2nd permutation

Since $k = 2$, we return `[3, 2, 1]`.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 2, k = 3

**Output:** []

**Explanation:**

The lexicographically-sorted alternating permutations of `[1, 2]` are:

- `[1, 2]`

- `[2, 1]`

There are only 2 alternating permutations, but $k = 3$, which is out of range. Thus, we return an empty list `[]`.

</div>

### 4. Constraints

- $1 \le n \le 100$

- $1 \le k \le 10^{15}$