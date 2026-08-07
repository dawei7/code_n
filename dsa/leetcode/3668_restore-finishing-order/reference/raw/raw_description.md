## Description

You are given an integer array `order` of length `n` and an integer array `friends`.

	- `order` contains every integer from 1 to `n` **exactly once**, representing the IDs of the participants of a race in their **finishing** order.

	- `friends` contains the IDs of your friends in the race **sorted** in strictly increasing order. Each ID in friends is guaranteed to appear in the `order` array.

Return an array containing your friends' IDs in their **finishing** order.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">order = [3,1,2,5,4], friends = [1,3,4]</span>

**Output:** <span class="example-io">[3,1,4]</span>

**Explanation:**

The finishing order is `[<u>**3**</u>, <u>**1**</u>, 2, 5, <u>**4**</u>]`. Therefore, the finishing order of your friends is `[3, 1, 4]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">order = [1,4,5,3,2], friends = [2,5]</span>

**Output:** <span class="example-io">[5,2]</span>

**Explanation:**

The finishing order is `[1, 4, <u>**5**</u>, 3, <u>**2**</u>]`. Therefore, the finishing order of your friends is `[5, 2]`.

</div>

**Constraints:**

	- `1 <= n == order.length <= 100`

	- `order` contains every integer from 1 to `n` exactly once

	- `1 <= friends.length <= min(8, n)`

	- `1 <= friends[i] <= n`

	- `friends` is strictly increasing
