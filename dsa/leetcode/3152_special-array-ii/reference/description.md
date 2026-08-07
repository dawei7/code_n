## Description

An array is considered **special** if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer `nums` and a 2D integer matrix `queries`, where for $\text{queries}[i] = [\text{from}_{i}, \text{to}_{i}]$ your task is to check that subarray $nums[\text{from}_{i}..\text{to}_{i}]$ is **special** or not.

Return an array of booleans `answer` such that $\text{answer}[i]$ is `true` if $nums[\text{from}_{i}..\text{to}_{i}]$ is special.<!-- notionvc: e5d6f4e2-d20a-4fbd-9c7f-22fbe52ef730 -->
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [3,4,1,2,6], queries = [[0,4]]

**Output:** [false]

**Explanation:**

The subarray is `[3,4,1,2,6]`. 2 and 6 are both even.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,3,1,6], queries = [[0,2],[2,3]]

**Output:** [false,true]

**Explanation:**

- The subarray is `[4,3,1]`. 3 and 1 are both odd. So the answer to this query is `false`.

- The subarray is `[1,6]`. There is only one pair: `(1,6)` and it contains numbers with different parity. So the answer to this query is `true`.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$

- $1 \le \text{queries.length} \le 10^{5}$

- $\text{queries}[i].length = 2$

- $0 \le \text{queries}[i][0] \le \text{queries}[i][1] \le \text{nums.length} - 1$