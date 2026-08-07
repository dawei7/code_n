## Description

You are given an integer array `nums`.

From any index `i`, you can jump to another index `j` under the following rules:

- Jump to index `j` where `j > i` is allowed only if $\text{nums}[j] < \text{nums}[i]$.

- Jump to index `j` where `j < i` is allowed only if $\text{nums}[j] > \text{nums}[i]$.

For each index `i`, find the **maximum** **value** in `nums` that can be reached by following **any** sequence of valid jumps starting at `i`.

Return an array `ans` where $\text{ans}[i]$ is the **maximum** **value** reachable starting from index `i`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,1,3]

**Output:** [2,2,3]

**Explanation:**

- For $i = 0$: No jump increases the value.

- For $i = 1$: Jump to $j = 0$ as $\text{nums}[j] = 2$ is greater than $\text{nums}[i]$.

- For $i = 2$: Since $\text{nums}[2] = 3$ is the maximum value in `nums`, no jump increases the value.

Thus, $ans = [2, 2, 3]$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,3,1]

**Output:** [3,3,3]

**Explanation:**

- For $i = 0$: Jump forward to $j = 2$ as $\text{nums}[j] = 1$ is less than $\text{nums}[i] = 2$, then from $i = 2$ jump to $j = 1$ as $\text{nums}[j] = 3$ is greater than $\text{nums}[2]$.

- For $i = 1$: Since $\text{nums}[1] = 3$ is the maximum value in `nums`, no jump increases the value.

- For $i = 2$: Jump to $j = 1$ as $\text{nums}[j] = 3$ is greater than $\text{nums}[2] = 1$.

Thus, $ans = [3, 3, 3]$.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}​​​​​​​$