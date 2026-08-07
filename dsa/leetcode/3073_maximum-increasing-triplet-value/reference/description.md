## Description

Given an array `nums`, return *the **maximum value** of a triplet* `(i, j, k)` *such that* `i < j < k` *and* $\text{nums}[i] < \text{nums}[j] < \text{nums}[k]$.

The **value** of a triplet `(i, j, k)` is $\text{nums}[i] - \text{nums}[j] + \text{nums}[k]$.

<div id="gtx-trans" style="position: absolute; left: 274px; top: 102px;">
<div class="gtx-trans-icon"> </div>
</div>

**Example 1: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: ** nums = [5,6,9]

**Output: ** 8

**Explanation: ** We only have one choice for an increasing triplet and that is choosing all three elements. The value of this triplet would be $5 - 6 + 9 = 8$.

</div>

**Example 2: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input:**  nums = [1,5,3,6]

**Output:**  4

**Explanation: ** There are only two increasing triplets:

`(0, 1, 3)`: The value of this triplet is $\text{nums}[0] - \text{nums}[1] + \text{nums}[3] = 1 - 5 + 6 = 2$.

`(0, 2, 3)`: The value of this triplet is $\text{nums}[0] - \text{nums}[2] + \text{nums}[3] = 1 - 3 + 6 = 4$.

Thus the answer would be `4`.

</div>
### Function Contract

- Refer to method signature.

### Constraints

- $3 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- The input is generated such that at least one triplet meets the given condition.