## Description

You are given a collection of numbered `balls` and instructed to sort them into boxes for a nearly balanced distribution. There are two rules you must follow:

	- Balls with the same box must have the same value. But, if you have more than one ball with the same number, you can put them in different boxes.

	- The biggest box can only have one more ball than the smallest box.

​Return the *fewest number of boxes* to sort these balls following these rules.

**Example 1: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> balls = [3,2,3,2,3] </span>

**Output: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 2 </span>

**Explanation:**

We can sort `balls` into boxes as follows:

	- `[3,3,3]`

	- `[2,2]`

The size difference between the two boxes doesn't exceed one.

</div>

**Example 2: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> balls = [10,10,10,3,1,1] </span>

**Output: ** <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 4 </span>

**Explanation:**

We can sort `balls` into boxes as follows:

	- `[10]`

	- `[10,10]`

	- `[3]`

	- `[1,1]`

You can't use fewer than four boxes while still following the rules. For example, putting all three balls numbered 10 in one box would break the rule about the maximum size difference between boxes.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`
