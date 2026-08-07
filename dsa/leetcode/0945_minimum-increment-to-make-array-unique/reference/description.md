### 1. Description

You are given an integer array `nums`. In one move, you can pick an index `i` where $0 \le i < \text{nums.length}$ and increment $\text{nums}[i]$ by `1`.

Return *the minimum number of moves to make every value in *`nums`* **unique***.

The test cases are generated so that the answer fits in a 32-bit integer.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,2,2]`
- **Output:** `1`
- **Explanation:** After 1 move, the array could be [1, 2, 3].
#### Example 2

- **Input:** `nums = [3,2,1,2,1,7]`
- **Output:** `6`
- **Explanation:** After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown that it is impossible for the array to have all unique values with 5 or less moves.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 10^{5}$