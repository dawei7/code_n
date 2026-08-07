## Description

Given an integer array `nums`, reorder it such that $\text{nums}[0] \le \text{nums}[1] \ge \text{nums}[2] \le \text{nums}[3]...$.

You may assume the input array always has a valid answer.
### Function Contract

**Inputs**

- `nums`: The mutable array of integers to rearrange.

**Return value**

Return `None`. The function mutates `nums` in place so adjacent comparisons alternate between $\le$ and $\ge$, beginning with $\text{nums}[0] \le \text{nums}[1]$.

### Examples

#### Example 1

- **Input:** `nums = [3,5,2,1,6,4]`
- **Output:** `[3,5,1,6,2,4]`
- **Explanation:** [1,6,2,5,3,4] is also accepted.
#### Example 2

- **Input:** `nums = [6,6,5,6,3,8]`
- **Output:** `[6,6,5,6,3,8]`
### Constraints

- $1 \le \text{nums.length} \le 5 * 10^{4}$

- $0 \le \text{nums}[i] \le 10^{4}$

- It is guaranteed that there will be an answer for the given input `nums`.

**Follow up:** Could you solve the problem in `O(n)` time complexity?