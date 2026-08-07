## Description

You are given an integer array `nums`.

A tuple `(i, j, k)` of 3 **distinct** indices is **good** if $\text{nums}[i] = \text{nums}[j] = \text{nums}[k]$.

The **distance** of a **good** tuple is $abs(i - j) + abs(j - k) + abs(k - i)$, where `abs(x)` denotes the **absolute value** of `x`.

Return an integer denoting the **minimum** possible **distance** of a **good** tuple. If no **good** tuples exist, return `-1`.
### Function Contract

**Inputs**

- `nums`: An integer array whose indices and equal values define the candidate tuples.

All three selected indices must be different. Their order in the tuple does not change the sum of the three pairwise absolute distances.

**Return value**

Return the minimum good-tuple distance, or `-1` when no value occurs at least three times.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,1,1,3]

**Output:** 6

**Explanation:**

The minimum distance is achieved by the good tuple `(0, 2, 3)`.

`(0, 2, 3)` is a good tuple because $\text{nums}[0] = \text{nums}[2] = \text{nums}[3] = 1$. Its distance is $abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,1,2,3,2,1,2]

**Output:** 8

**Explanation:**

The minimum distance is achieved by the good tuple `(2, 4, 6)`.

`(2, 4, 6)` is a good tuple because $\text{nums}[2] = \text{nums}[4] = \text{nums}[6] = 2$. Its distance is $abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8$.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1]

**Output:** -1

**Explanation:**

There are no good tuples. Therefore, the answer is -1.

</div>
### Constraints

- $1 \le n = \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le n$