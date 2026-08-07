## Description

Given an integer `n`, an **alternating permutation** is a permutation of the first `n` positive integers such that no **two** adjacent elements are **both** odd or **both** even.

Return *all such ***alternating permutations** sorted in lexicographical order.
### Function Contract

- Refer to method signature.

### Examples
#### Example 1

<div class="example-block">
**Input:** n = 4

**Output:** [[1,2,3,4],[1,4,3,2],[2,1,4,3],[2,3,4,1],[3,2,1,4],[3,4,1,2],[4,1,2,3],[4,3,2,1]]

</div>
#### Example 2

<div class="example-block">
**Input:** n = 2

**Output:** [[1,2],[2,1]]

</div>
#### Example 3

<div class="example-block">
**Input:** n = 3

**Output:** [[1,2,3],[3,2,1]]

</div>
### Constraints

- $1 \le n \le 10$