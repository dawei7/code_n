## Description

You are given a **0-indexed** integer array `nums` representing the score of students in an exam. The teacher would like to form one **non-empty** group of students with maximal **strength**, where the strength of a group of students of indices $i_{0}$, $i_{1}$, $i_{2}$, ... , $i_{k}$ is defined as $nums[i_{0}] * nums[i_{1}] * nums[i_{2}] * ... * nums[i_{k}​]$.

Return *the maximum strength of a group the teacher can create*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `nums = [3,-1,-5,2,5,-9]`
- **Output:** `1350`
- **Explanation:** One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.
#### Example 2

- **Input:** `nums = [-4,-5,-4]`
- **Output:** `20`
- **Explanation:** Group the students at indices [0, 1] . Then, we’ll have a resulting strength of 20. We cannot achieve greater strength.
### Constraints

- $1 \le \text{nums.length} \le 13$

- $-9 \le \text{nums}[i] \le 9$