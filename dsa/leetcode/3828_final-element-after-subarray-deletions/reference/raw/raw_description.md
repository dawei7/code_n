## Description

You are given an integer array `nums`.

Two players, Alice and Bob, play a game in turns, with Alice playing first.

	- In each turn, the current player chooses any **<span data-keyword="subarray-nonempty">subarray</span>** `nums[l..r]` such that `r - l + 1 < m`, where `m` is the **current length** of the array.

	- The selected **subarray is removed**, and the remaining elements are **concatenated** to form the new array.

	- The game continues until **only one** element remains.

Alice aims to **maximize** the final element, while Bob aims to **minimize** it. Assuming both play optimally, return the value of the final remaining element.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,5,2]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

One valid optimal strategy:

	- Alice removes `[1]`, array becomes `[5, 2]`.

	- Bob removes `[5]`, array becomes `[2]`​​​​​​​. Thus, the answer is 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,7]</span>

**Output:** <span class="example-io">7</span>

**Explanation:**

Alice removes `[3]`, leaving the array `[7]`. Since Bob cannot play a turn now, the answer is 7.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`
