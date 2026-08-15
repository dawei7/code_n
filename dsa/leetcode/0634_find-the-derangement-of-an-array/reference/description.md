### 1. Description

In combinatorial mathematics, a **derangement** is a permutation of the elements of a set, such that no element appears in its original position.

You are given an integer `n`. There is originally an array consisting of `n` integers from `1` to `n` in ascending order, return *the number of **derangements** it can generate*. Since the answer may be huge, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

**Inputs**

- `n`: The number of distinct integers and original positions in the ascending array `[1, 2, ..., n]`.

**Return value**

Return the number of permutations in which every integer occupies a position different from its original one, reduced modulo $10^9 + 7$.

### 3. Examples

#### Example 1

- **Input:** $n = 3$
- **Output:** `2`
- **Explanation:** The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].

#### Example 2

- **Input:** $n = 2$
- **Output:** `1`

### 4. Constraints

- $1 \le n \le 10^{6}$
