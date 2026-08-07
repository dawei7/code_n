## Description

You are given a binary array `nums`.

We call a subarray **alternating** if **no** two **adjacent** elements in the subarray have the **same** value.

Return *the number of alternating subarrays in *`nums`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [0,1,1,1]

**Output:** 5

**Explanation:**

The following subarrays are alternating: `[0]`, `[1]`, `[1]`, `[1]`, and `[0,1]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,0,1,0]

**Output:** 10

**Explanation:**

Every subarray of the array is alternating. There are 10 possible subarrays that we can choose.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $\text{nums}[i]$ is either `0` or `1`.