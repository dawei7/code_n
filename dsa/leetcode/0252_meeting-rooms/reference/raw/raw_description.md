## Description

You are given an array of meeting times `intervals` where `intervals[i] = [start_i, end_i]`.

A person can attend all meetings if no two meeting intervals overlap. Meetings ending at time `t` and starting at time `t` **do not** overlap.

​​​​​​​Return `true` if a person can attend all meetings. Otherwise, return `false`.

**Example 1:**

```
**Input:** intervals = [[0,30],[5,10],[15,20]]
**Output:** false
```

**Example 2:**

```
**Input:** intervals = [[7,10],[2,4]]
**Output:** true
```

**Constraints:**

	- `0 <= intervals.length <= 10^4`

	- `intervals[i].length == 2`

	- `0 <= start_i < end_i <= 10^6`
