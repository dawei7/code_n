## Description

You are given an array `nums` which is a <span data-keyword="permutation">permutation</span> of `[0, 1, 2, ..., n - 1]`. The **score** of any permutation of `[0, 1, 2, ..., n - 1]` named `perm` is defined as:

`score(perm) = |perm[0] - nums[perm[1]]| + |perm[1] - nums[perm[2]]| + ... + |perm[n - 1] - nums[perm[0]]|`

Return the permutation `perm` which has the **minimum** possible score. If *multiple* permutations exist with this score, return the one that is <span data-keyword="lexicographically-smaller-array">lexicographically smallest</span> among them.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,0,2]</span>

**Output:** <span class="example-io">[0,1,2]</span>

**Explanation:**

**

![](images/example0gif.gif)

**

The lexicographically smallest permutation with minimum cost is `[0,1,2]`. The cost of this permutation is `|0 - 0| + |1 - 2| + |2 - 1| = 2`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0,2,1]</span>

**Output:** <span class="example-io">[0,2,1]</span>

**Explanation:**

**

![](images/example1gif.gif)

**

The lexicographically smallest permutation with minimum cost is `[0,2,1]`. The cost of this permutation is `|0 - 1| + |2 - 2| + |1 - 0| = 2`.

</div>

**Constraints:**

	- `2 <= n == nums.length <= 14`

	- `nums` is a permutation of `[0, 1, 2, ..., n - 1]`.
