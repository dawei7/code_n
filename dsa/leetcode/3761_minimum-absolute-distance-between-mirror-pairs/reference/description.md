## Description

You are given an integer array `nums`.

A **mirror pair** is a pair of indices `(i, j)` such that:

- $0 \le i < j < \text{nums.length}$, and

- $reverse(\text{nums}[i]) = \text{nums}[j]$, where `reverse(x)` denotes the integer formed by reversing the digits of `x`. Leading zeros are omitted after reversing, for example $reverse(120) = 21$.

Return the **minimum** absolute distance between the indices of any mirror pair. The absolute distance between indices `i` and `j` is $abs(i - j)$.

If no mirror pair exists, return `-1`.
### Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers whose ordered index pairs are examined.

Only the earlier value $\text{nums}[i]$ is reversed. The condition is therefore directional when a value ends in zero: `120` followed by `21` matches, whereas `21` followed by `120` does not.

**Return value**

Return the minimum value of $\lvert i-j\rvert$ over all mirror pairs `(i,j)` with $i<j$, or `-1` if there is no such pair.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [12,21,45,33,54]

**Output:** 1

**Explanation:**

The mirror pairs are:

- (0, 1) since $reverse(\text{nums}[0]) = reverse(12) = 21 = \text{nums}[1]$, giving an absolute distance $abs(0 - 1) = 1$.

- (2, 4) since $reverse(\text{nums}[2]) = reverse(45) = 54 = \text{nums}[4]$, giving an absolute distance $abs(2 - 4) = 2$.

The minimum absolute distance among all pairs is 1.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [120,21]

**Output:** 1

**Explanation:**

There is only one mirror pair (0, 1) since $reverse(\text{nums}[0]) = reverse(120) = 21 = \text{nums}[1]$.

The minimum absolute distance is 1.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [21,120]

**Output:** -1

**Explanation:**

There are no mirror pairs in the array.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$​​​​​​​