## Description

In the town of Digitville, there was a list of numbers called `nums` containing integers from `0` to `n - 1`. Each number was supposed to appear **exactly once** in the list, however, **two** mischievous numbers sneaked in an *additional time*, making the list longer than usual.<!-- notionvc: c37cfb04-95eb-4273-85d5-3c52d0525b95 -->

As the town detective, your task is to find these two sneaky numbers. Return an array of size **two** containing the two numbers (in *any order*), so peace can return to Digitville.<!-- notionvc: 345db5be-c788-4828-9836-eefed31c982f -->

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0,1,1,0]</span>

**Output:** <span class="example-io">[0,1]</span>

**Explanation:**

The numbers 0 and 1 each appear twice in the array.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0,3,2,1,3,2]</span>

**Output:** <span class="example-io">[2,3]</span>

**Explanation: **

The numbers 2 and 3 each appear twice in the array.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7,1,5,4,3,4,6,0,9,5,8,2]</span>

**Output:** <span class="example-io">[4,5]</span>

**Explanation: **

The numbers 4 and 5 each appear twice in the array.

</div>

**Constraints:**

	- `2 <= n <= 100`

	- `nums.length == n + 2`

	- `0 <= nums[i] < n`

	- The input is generated such that `nums` contains **exactly** two repeated elements.
