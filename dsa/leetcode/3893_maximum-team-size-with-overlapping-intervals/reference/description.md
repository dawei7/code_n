## Description

You are given two integer arrays `startTime` and `endTime` of length `n`.

- $\text{startTime}[i]$ represents the start time of the $$i^{\text{th}}$$ employee.

- $\text{endTime}[i]$ represents the end time of the $$i^{\text{th}}$$ employee.

Two employees `i` and `j` can interact if their time intervals **overlap**. Two intervals are considered overlapping if they share **at least one** common time point.

A team is **valid** if there exists **at least one** employee in the team who can interact with every other member of the team.

Return an integer denoting the **maximum** possible size of such a team.
### Function Contract

**Inputs**

- `startTime`: An array whose element at index $i$ is employee $i$'s start time.
- `endTime`: An equally sized array whose element at index $i$ is employee $i$'s end time.

The two values at the same index form one employee's closed interval. Every start time is strictly smaller than its paired end time.

**Return value**

Return the maximum team size for which some member's interval overlaps every other member's interval.

### Examples

#### Example 1

<div class="example-block">
**Input:** startTime = [1,2,3], endTime = [4,5,6]

**Output:** 3

**Explanation:**

- For $i = 0$ with interval `[1, 4]`.

- It overlaps with $i = 1$ having interval `[2, 5]` and $i = 2$ having interval `[3, 6]`.

- Thus, index 0 can interact with all other indices, so the team size is 3.

</div>
#### Example 2

<div class="example-block">
**Input:** startTime = [2,5,8], endTime = [3,7,9]

**Output:** 1

**Explanation:**

- For $i = 0$, interval `[2, 3]` does not overlap with `[5, 7]` or `[8, 9]`.

- For $i = 1$, interval `[5, 7]` does not overlap with `[2, 3]` or `[8, 9]`.

- For $i = 2$, interval `[8, 9]` does not overlap with `[2, 3]` or `[5, 7]`.

- Thus, no index can interact with others, so the maximum team size is 1.

</div>
#### Example 3

<div class="example-block">
**Input:** startTime = [3,4,6], endTime = [8,5,7]

**Output:** 3

**Explanation:**

- For $i = 0$ with interval `[3, 8]`.

- It overlaps with $i = 1$ having interval `[4, 5]` and $i = 2$ having interval `[6, 7]`.

- Thus, index 0 can interact with all other indices, so the team size is 3.

</div>
### Constraints

- $1 \le n = \text{startTime.length} = \text{endTime.length} \le 10^{5}$

- $0 \le \text{startTime}[i] \le \text{endTime}[i] \le 10^{9}$