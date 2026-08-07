## Description

A magician has various spells.

You are given an array `power`, where each element represents the damage of a spell. Multiple spells can have the same damage value.

It is a known fact that if a magician decides to cast a spell with a damage of `power[i]`, they **cannot** cast any spell with a damage of `power[i] - 2`, `power[i] - 1`, `power[i] + 1`, or `power[i] + 2`.

Each spell can be cast **only once**.

Return the **maximum** possible *total damage* that a magician can cast.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">power = [1,1,3,4]</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">power = [7,1,6,6]</span>

**Output:** <span class="example-io">13</span>

**Explanation:**

The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.

</div>

**Constraints:**

	- `1 <= power.length <= 10^5`

	- `1 <= power[i] <= 10^9`
