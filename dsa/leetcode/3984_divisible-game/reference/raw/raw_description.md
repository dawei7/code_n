## Description

You are given an integer array `nums` of length `n`.

Alice and Bob are playing a game. Alice chooses:

	- An integer `k` such that `k > 1`.

	- Two integers `l` and `r` such that `0 <= l <= r < n`.

Initially, both Alice's and Bob's scores are 0.

For each index `i` in the range `[l, r]` (inclusive):

	- If `nums[i]` is divisible by `k`, Alice's score **increases** by `nums[i]`.

	- Otherwise, Bob's score **increases** by `nums[i]`.

The **score difference** is Alice's score **minus** Bob's score.

Alice wants to **maximize** the score difference. If there are multiple values of `k` that achieve the **maximum** score difference, she chooses the **smallest** such `k`.

Return the **product** of the **maximum** score difference and the chosen value of `k`. Since the result can be large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,4,6,8]</span>

**Output:** <span class="example-io">36</span>

**Explanation:**

	- Alice can choose `k = 2`, `l = 1`, and `r = 3`.

	- All values in `nums[1..3]` are divisible by 2, so Alice's score is `4 + 6 + 8 = 18`, while Bob's score is 0.

	- The score difference is 18, which is the maximum possible. Among all values of `k` that achieve this score difference, the smallest is 2.

	- Therefore, the answer is `18 * 2 = 36`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,1,2]</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

	- Alice can choose `k = 2`, `l = 0`, and `r = 2`.

	- The values `nums[0]` and `nums[2]` are divisible by 2, so Alice's score is `2 + 2 = 4`. The value `nums[1]` is not divisible by 2, so Bob's score is 1.

	- The score difference is `4 - 1 = 3`, which is the maximum possible. Among all values of `k` that achieve this score difference, the smallest is 2.

	- Therefore, the answer is `3 * 2 = 6`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1]</span>

**Output:** <span class="example-io">1000000005</span>

**Explanation:**

	- Alice must choose some `k > 1`. The smallest possible choice is `k = 2`.

	- Since `nums[0]` is not divisible by 2, Alice's score is 0, while Bob's score is 1.

	- The score difference is -1, which is the maximum possible.

	- Therefore, the answer is `-1 * 2 = -2`. Modulo `10^9 + 7`, this equals 1000000005.

</div>

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i] <= 10^6`
