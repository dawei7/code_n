## Description

Given two integers, `num` and `t`. A **number **`x`** **is** achievable** if it can become equal to `num` after applying the following operation **at most** `t` times:

	- Increase or decrease `x` by `1`, and *simultaneously* increase or decrease `num` by `1`.

Return the **maximum **possible value of `x`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">num = 4, t = 1</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

Apply the following operation once to make the maximum achievable number equal to `num`:

	- Decrease the maximum achievable number by 1, and increase `num` by 1.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">num = 3, t = 2</span>

**Output:** <span class="example-io">7</span>

**Explanation:**

Apply the following operation twice to make the maximum achievable number equal to `num`:

	- Decrease the maximum achievable number by 1, and increase `num` by 1.

</div>

**Constraints:**

	- `1 <= num, t <= 50`
