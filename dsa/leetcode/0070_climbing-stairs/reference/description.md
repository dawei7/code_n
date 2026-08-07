## Description

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?
### Function Contract

**Inputs**

- `n`: The positive number of steps in the staircase.

**Return value**

Return the number of ordered sequences of one-step and two-step moves whose total is `n`.

### Examples
#### Example 1

- **Input:** $n = 2$
- **Output:** `2`
- **Explanation:** There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
#### Example 2

- **Input:** $n = 3$
- **Output:** `3`
- **Explanation:** There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
### Constraints

- $1 \le n \le 45$