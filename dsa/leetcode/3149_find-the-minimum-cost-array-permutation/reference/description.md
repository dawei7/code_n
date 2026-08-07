## Description

You are given an array `nums` which is a permutation of `[0, 1, 2, ..., n - 1]`. The **score** of any permutation of `[0, 1, 2, ..., n - 1]` named `perm` is defined as:

$score(perm) = |\text{perm}[0] - nums[\text{perm}[1]]| + |\text{perm}[1] - nums[\text{perm}[2]]| + ... + |perm[n - 1] - nums[\text{perm}[0]]|$

Return the permutation `perm` which has the **minimum** possible score. If *multiple* permutations exist with this score, return the one that is lexicographically smallest among them.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,0,2]

**Output:** [0,1,2]

**Explanation:**

**

![](images/example0gif.gif)

**

The lexicographically smallest permutation with minimum cost is `[0,1,2]`. The cost of this permutation is $|0 - 0| + |1 - 2| + |2 - 1| = 2$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [0,2,1]

**Output:** [0,2,1]

**Explanation:**

**

![](images/example1gif.gif)

**

The lexicographically smallest permutation with minimum cost is `[0,2,1]`. The cost of this permutation is $|0 - 1| + |2 - 2| + |1 - 0| = 2$.

</div>
### Constraints

- $2 \le n = \text{nums.length} \le 14$

- `nums` is a permutation of `[0, 1, 2, ..., n - 1]`.