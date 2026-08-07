## Description

Given a set of **distinct** positive integers `nums`, return the largest subset `answer` such that every pair $(\text{answer}[i], \text{answer}[j])$ of elements in this subset satisfies:

- $\text{answer}[i] \% \text{answer}[j] = 0$, or

- $\text{answer}[j] \% \text{answer}[i] = 0$

If there are multiple solutions, return any of them.
### Function Contract

**Inputs**

- `nums`: The array of distinct positive integers.

**Return value**

Return any maximum-size subset in which every pair is divisible in at least one direction.

### Examples

#### Example 1

- **Input:** `nums = [1,2,3]`
- **Output:** `[1,2]`
- **Explanation:** [1,3] is also accepted.
#### Example 2

- **Input:** `nums = [1,2,4,8]`
- **Output:** `[1,2,4,8]`
### Constraints

- $1 \le \text{nums.length} \le 1000$

- $1 \le \text{nums}[i] \le 2 * 10^{9}$

- All the integers in `nums` are **unique**.