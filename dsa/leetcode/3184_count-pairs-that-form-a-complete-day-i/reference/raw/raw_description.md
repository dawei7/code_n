## Description

Given an integer array `hours` representing times in **hours**, return an integer denoting the number of pairs `i`, `j` where `i < j` and `hours[i] + hours[j]` forms a **complete day**.

A **complete day** is defined as a time duration that is an **exact** **multiple** of 24 hours.

For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">hours = [12,12,30,24,24]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The pairs of indices that form a complete day are `(0, 1)` and `(3, 4)`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">hours = [72,48,24,3]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The pairs of indices that form a complete day are `(0, 1)`, `(0, 2)`, and `(1, 2)`.

</div>

**Constraints:**

	- `1 <= hours.length <= 100`

	- `1 <= hours[i] <= 10^9`
