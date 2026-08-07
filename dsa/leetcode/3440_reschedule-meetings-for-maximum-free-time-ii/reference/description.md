## Description

You are given an integer `eventTime` denoting the duration of an event. You are also given two integer arrays `startTime` and `endTime`, each of length `n`.

These represent the start and end times of `n` **non-overlapping** meetings that occur during the event between time $t = 0$ and time $t = eventTime$, where the $$i^{\text{th}}$$meeting occurs during the time$[\text{startTime}[i], \text{endTime}[i]].$

You can reschedule **at most **one meeting by moving its start time while maintaining the **same duration**, such that the meetings remain non-overlapping, to **maximize** the **longest** *continuous period of free time* during the event.

Return the **maximum** amount of free time possible after rearranging the meetings.

**Note** that the meetings can **not** be rescheduled to a time outside the event and they should remain non-overlapping.

**Note:** *In this version*, it is **valid** for the relative ordering of the meetings to change after rescheduling one meeting.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** eventTime = 5, startTime = [1,3], endTime = [2,5]

**Output:** 2

**Explanation:**

![](images/example0_rescheduled.png)

Reschedule the meeting at `[1, 2]` to `[2, 3]`, leaving no meetings during the time `[0, 2]`.

</div>
#### Example 2

<div class="example-block">
**Input:** eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]

**Output:** 7

**Explanation:**

![](images/rescheduled_example0.png)

Reschedule the meeting at `[0, 1]` to `[8, 9]`, leaving no meetings during the time `[0, 7]`.

</div>
#### Example 3

<div class="example-block">
**Input:** eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]

**Output:** 6

**Explanation:**

**

![](images/image3.png)

**

Reschedule the meeting at `[3, 4]` to `[8, 9]`, leaving no meetings during the time `[1, 7]`.

</div>
#### Example 4

<div class="example-block">
**Input:** eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]

**Output:** 0

**Explanation:**

There is no time during the event not occupied by meetings.

</div>
### Constraints

- $1 \le eventTime \le 10^{9}$

- $n = \text{startTime.length} = \text{endTime.length}$

- $2 \le n \le 10^{5}$

- $0 \le \text{startTime}[i] < \text{endTime}[i] \le eventTime$

- $\text{endTime}[i] \le startTime[i + 1]$ where `i` lies in the range `[0, n - 2]`.