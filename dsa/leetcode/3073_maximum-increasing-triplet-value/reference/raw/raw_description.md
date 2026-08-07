## Description

Given an array `nums`, return *the **maximum value** of a triplet* `(i, j, k)` *such that* `i < j < k` *and* `nums[i] < nums[j] < nums[k]`.

The **value** of a triplet `(i, j, k)` is `nums[i] - nums[j] + nums[k]`.

<div id="gtx-trans" style="position: absolute; left: 274px; top: 102px;">
<div class="gtx-trans-icon"> </div>
</div>

**Example 1: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">nums = [5,6,9] </span>

**Output: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">8 </span>

**Explanation: ** We only have one choice for an increasing triplet and that is choosing all three elements. The value of this triplet would be `5 - 6 + 9 = 8`.

</div>

**Example 2: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input:** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> nums = [1,5,3,6] </span>

**Output:** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 4 </span>

**Explanation: ** There are only two increasing triplets:

`(0, 1, 3)`: The value of this triplet is `nums[0] - nums[1] + nums[3] = 1 - 5 + 6 = 2`.

`(0, 2, 3)`: The value of this triplet is `nums[0] - nums[2] + nums[3] = 1 - 3 + 6 = 4`.

Thus the answer would be `4`.

</div>

**Constraints:**

	- `3 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- The input is generated such that at least one triplet meets the given condition.
