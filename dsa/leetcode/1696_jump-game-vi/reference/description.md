## Description

You are given a **0-indexed** integer array `nums` and an integer `k`.

You are initially standing at index `0`. In one move, you can jump at most `k` steps forward without going outside the boundaries of the array. That is, you can jump from index `i` to any index in the range `[i + 1, min(n - 1, i + k)]` **inclusive**.

You want to reach the last index of the array (index $n - 1$). Your **score** is the **sum** of all $\text{nums}[j]$ for each index `j` you visited in the array.

Return *the **maximum score** you can get*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `nums = [<u>1</u>,<u>-1</u>,-2,<u>4</u>,-7,<u>3</u>], k = 2`
- **Output:** `7`
- **Explanation:** You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
#### Example 2

- **Input:** `nums = [<u>10</u>,-5,-2,<u>4</u>,0,<u>3</u>], k = 3`
- **Output:** `17`
- **Explanation:** You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
#### Example 3

- **Input:** `nums = [1,-5,-20,4,-1,3,-6,-3], k = 2`
- **Output:** `0`
### Constraints

- $1 \le \text{nums.length}, k \le 10^{5}$

- $-10^{4} \le \text{nums}[i] \le 10^{4}$