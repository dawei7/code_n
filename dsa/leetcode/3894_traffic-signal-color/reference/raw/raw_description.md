## Description

You are given an integer `timer` representing the remaining time (in seconds) on a traffic signal.

The signal follows these rules:

	- If `timer == 0`, the signal is `"Green"`

	- If `timer == 30`, the signal is `"Orange"`

	- If `30 < timer <= 90`, the signal is `"Red"`

Return the current state of the signal. If none of the above conditions are met, return `"Invalid"`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">timer = 60</span>

**Output:** <span class="example-io">"Red"</span>

**Explanation:**

Since `timer = 60`, and `30 < timer <= 90`, the answer is `"Red"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">timer = 5</span>

**Output:** <span class="example-io">"Invalid"</span>

**Explanation:**

Since `timer = 5`, it does not satisfy any of the given conditions, the answer is `"Invalid"`.

</div>

**Constraints:**

	- `0 <= timer <= 1000`
