## Description

Given an array of integers `nums`, half of the integers in `nums` are **odd**, and the other half are **even**.

Sort the array so that whenever $\text{nums}[i]$ is odd, `i` is **odd**, and whenever $\text{nums}[i]$ is even, `i` is **even**.

Return *any answer array that satisfies this condition*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `nums = [4,2,5,7]`
- **Output:** `[4,5,2,7]`
- **Explanation:** [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
#### Example 2

- **Input:** `nums = [2,3]`
- **Output:** `[2,3]`
### Constraints

- $2 \le \text{nums.length} \le 2 * 10^{4}$

- `nums.length` is even.

- Half of the integers in `nums` are even.

- $0 \le \text{nums}[i] \le 1000$

**Follow Up:** Could you solve it in-place?