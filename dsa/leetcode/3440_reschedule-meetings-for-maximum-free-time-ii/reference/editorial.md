### Approach 1: Greedy

#### Intuition

Assume the current meeting to be shifted is $i$. There are two optimal ways to translate the meeting:

1. If meeting $i$ can be moved to an available time slot, and this slot is not adjacent to the two available time slots on either side of meeting $i$, then shifting it can create a new available time slot, with a duration equal to the sum of the durations of meeting $i$ and the two adjacent available slots on either side.

2. Otherwise, moving meeting $i$ simply merges the two adjacent free time periods on both sides.

As we can see that maximum free time that can be obtained after rearranging the meetings is the maximum value of the new available time periods resulting from shifting a meeting.

We use $q[i]$ to record whether meeting $i$ satisfies the condition for the first case. We first traverse the meetings from left to right, maintaining the maximum duration $t_1$ of any non-adjacent free time slot to the left of the current meeting $i$. If $t_1 \ge \textit{endTime}[i] - \textit{startTime}[i]$, then there is a free time slot on the left of meeting $i$ that satisfies case 1, so we record $q[i] = \text{true}$. Similarly, we traverse from right to left to check whether the right side also satisfies the condition.

Then, for each meeting $i$, we define $\textit{left}_i$ as the end time of the previous meeting and $\textit{right}_i$ as the start time of the next meeting. Based on the value of $q[i]$, we determine which case applies:

- Case 1: The new available time slot has a duration of $\textit{right}_i - \textit{left}_i$

- Case 2: The new available time slot has a duration of $\textit{right}_i - \textit{left}_i - (\textit{endTime}[i] - \textit{startTime}[i])$

Finally, return the maximum of all computed durations.

#### Implementation

```python
class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: list[int], endTime: list[int]
    ) -> int:
        n = len(startTime)
        q = [False] * n
        t1 = 0
        t2 = 0
        for i in range(n):
            if endTime[i] - startTime[i] <= t1:
                q[i] = True
            t1 = max(t1, startTime[i] - (0 if i == 0 else endTime[i - 1]))

            if endTime[n - i - 1] - startTime[n - i - 1] <= t2:
                q[n - i - 1] = True
            t2 = max(
                t2,
                (eventTime if i == 0 else startTime[n - i])
- endTime[n - i - 1],
            )

        res = 0
        for i in range(n):
            left = 0 if i == 0 else endTime[i - 1]
            right = eventTime if i == n - 1 else startTime[i + 1]
            if q[i]:
                res = max(res, right - left)
            else:
                res = max(res, right - left - (endTime[i] - startTime[i]))
        return res
```

#### Complexity analysis

Let $n$ be the number of all meetings.

- Time complexity: $O(n)$.

  We need to go through all the meetings.

- Space complexity: $O(n)$.

  A array is needed to record all the meeting situations.

### Approach 2: Greedy + Optimization

#### Intuition

In Approach 1, we used an array $q[i]$ to determine whether meeting $i$ satisfied the condition for an optimal shift. However, if we calculate the result for both cases directly while enumerating meeting $i$, we can eliminate the need for the `q` array altogether. The specific process is as follows:

- We iterate over each meeting and first calculate the duration of the new free time slot if we were to merge the adjacent free slots on both sides of the meeting. This corresponds to Case 2 in the previous approach.

- Then, we perform a left-to-right traversal, maintaining a variable $t_1$ to store the maximum duration of any non-adjacent free slot to the left of the current meeting. If the duration of the current meeting is less than or equal to $t_1$, it means the meeting can be shifted into that earlier free slot. We then compute the new available time obtained after this shift (Case 1).

- Similarly, we perform a right-to-left traversal, using $t_2$ to track the maximum duration of non-adjacent free slots on the right. If the current meeting's duration is less than or equal to $t_2$, then it can be shifted into that slot, and we calculate the resulting new available time (Case 1 from the right side).

In the end, we return the maximum duration among all the computed available time slots.

#### Implementation

```python
class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: list[int], endTime: list[int]
    ) -> int:
        n = len(startTime)
        q = [False] * n
        t1 = 0
        t2 = 0
        for i in range(n):
            if endTime[i] - startTime[i] <= t1:
                q[i] = True
            t1 = max(t1, startTime[i] - (0 if i == 0 else endTime[i - 1]))

            if endTime[n - i - 1] - startTime[n - i - 1] <= t2:
                q[n - i - 1] = True
            t2 = max(
                t2,
                (eventTime if i == 0 else startTime[n - i])
- endTime[n - i - 1],
            )

        res = 0
        for i in range(n):
            left = 0 if i == 0 else endTime[i - 1]
            right = eventTime if i == n - 1 else startTime[i + 1]
            if q[i]:
                res = max(res, right - left)
            else:
                res = max(res, right - left - (endTime[i] - startTime[i]))
        return res
```

#### Complexity analysis

Let $n$ be the number of all meetings.

- Time complexity: $O(n)$.

  We need to go through all the meetings.

- Space complexity: $O(1)$.