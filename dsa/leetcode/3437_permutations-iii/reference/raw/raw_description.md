## Description

Given an integer `n`, an **alternating permutation** is a permutation of the first `n` positive integers such that no **two** adjacent elements are **both** odd or **both** even.

Return *all such ***alternating permutations** sorted in lexicographical order.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 4</span>

**Output:** <span class="example-io">[[1,2,3,4],[1,4,3,2],[2,1,4,3],[2,3,4,1],[3,2,1,4],[3,4,1,2],[4,1,2,3],[4,3,2,1]]</span>

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 2</span>

**Output:** <span class="example-io">[[1,2],[2,1]]</span>

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 3</span>

**Output:** <span class="example-io">[[1,2,3],[3,2,1]]</span>

</div>

**Constraints:**

	- `1 <= n <= 10`
