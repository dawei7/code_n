## Description

You are given a positive integer `days` representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array `meetings` of size `n` where, `meetings[i] = [start_i, end_i]` represents the starting and ending days of meeting `i` (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

**Note: **The meetings may overlap.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">days = 10, meetings = [[5,7],[1,3],[9,10]]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

There is no meeting scheduled on the 4^th and 8^th days.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">days = 5, meetings = [[2,4],[1,3]]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

There is no meeting scheduled on the 5^th day.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">days = 6, meetings = [[1,6]]</span>

**Output:** 0

**Explanation:**

Meetings are scheduled for all working days.

</div>

**Constraints:**

	- `1 <= days <= 10^9`

	- `1 <= meetings.length <= 10^5`

	- `meetings[i].length == 2`

	- `<font face="monospace">1 <= meetings[i][0] <= meetings[i][1] <= days</font>`
