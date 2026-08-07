## Description

You are given two integer arrays `nums` and `threshold`, both of length `n`.

Starting at $step = 1$, you perform the following repeatedly:

- Choose an **unused** index `i` such that $\text{threshold}[i] \le step$.

		<li>If no such index exists, the process ends.

	</li>
- Add $\text{nums}[i]$ to your running total.

- Mark index `i` as used and increment `step` by 1.

Return the **maximum** **total sum** you can obtain by choosing indices optimally.
### Function Contract

**Inputs**

- `nums`: The positive contribution earned when the corresponding index is chosen.
- `threshold`: The earliest step at which each corresponding index becomes eligible.

The arrays have the same length $n$. Each index can be chosen at most once, and the process cannot stop voluntarily while an unused eligible index exists.

**Return value**

Return the greatest running total achievable when the required process terminates.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,10,4,2,1,6], threshold = [5,1,5,5,2,2]

**Output:** 17

**Explanation:**

- At $step = 1$, choose $i = 1$ since $\text{threshold}[1] \le step$. The total sum becomes 10. Mark index 1.

- At $step = 2$, choose $i = 4$ since $\text{threshold}[4] \le step$. The total sum becomes 11. Mark index 4.

- At $step = 3$, choose $i = 5$ since $\text{threshold}[5] \le step$. The total sum becomes 17. Mark index 5.

- At $step = 4$, we cannot choose indices 0, 2, or 3 because their thresholds are `> 4`, so we end the process.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,1,5,2,3], threshold = [3,3,2,3,3]

**Output:** 0

**Explanation:**

At $step = 1$ there is no index `i` with $\text{threshold}[i] \le 1$, so the process ends immediately. Thus, the total sum is 0.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [2,6,10,13], threshold = [2,1,1,1]

**Output:** 31

**Explanation:**

- At $step = 1$, choose $i = 3$ since $\text{threshold}[3] \le step$. The total sum becomes 13. Mark index 3.

- At $step = 2$, choose $i = 2$ since $\text{threshold}[2] \le step$. The total sum becomes 23. Mark index 2.

- At $step = 3$, choose $i = 1$ since $\text{threshold}[1] \le step$. The total sum becomes 29. Mark index 1.

- At $step = 4$, choose $i = 0$ since $\text{threshold}[0] \le step$. The total sum becomes 31. Mark index 0.

- After $step = 4$ all indices have been chosen, so the process ends.

</div>
### Constraints

- $n = \text{nums.length} = \text{threshold.length}$

- $1 \le n \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $1 \le \text{threshold}[i] \le n$