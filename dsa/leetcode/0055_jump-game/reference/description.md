## Description

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true`* if you can reach the last index, or *`false`* otherwise*.
### Function Contract

**Inputs**

- `nums`: The maximum forward-jump length available at each position.

Let $n = \lvert\texttt{nums}\rvert$.

**Return value**

Return `true` if some sequence of permitted jumps reaches the final index; otherwise return `false`.

### Examples

#### Example 1

- **Input:** `nums = [2,3,1,1,4]`
- **Output:** `true`
- **Explanation:** Jump 1 step from index 0 to 1, then 3 steps to the last index.
#### Example 2

- **Input:** `nums = [3,2,1,0,4]`
- **Output:** `false`
- **Explanation:** You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
### Constraints

- $1 \le \text{nums.length} \le 10^{4}$

- $0 \le \text{nums}[i] \le 10^{5}$