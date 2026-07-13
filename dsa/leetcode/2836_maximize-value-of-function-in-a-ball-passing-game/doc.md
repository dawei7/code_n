# Maximize Value of Function in a Ball Passing Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2836 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximize-value-of-function-in-a-ball-passing-game](https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/).

### Goal
Given a circular array of receivers where each player `i` passes the ball to player `receiver[i]`, determine the maximum possible sum of indices encountered by a ball starting at any player and being passed exactly `k` times (total of `k+1` players visited).

### Function Contract
**Inputs**

- `receiver`: A list of integers where `receiver[i]` is the index of the player who receives the ball from player `i`.
- `k`: An integer representing the total number of passes to be made.

**Return value**

- An integer representing the maximum total value (sum of indices) accumulated during a sequence of `k` passes.

### Examples
**Example 1**

- Input: `receiver = [2, 0, 1]`, `k = 4`
- Output: `6`
- Explanation: Starting at index 1: 1 -> 0 -> 2 -> 1 -> 0. Sum: 1+0+2+1+0 = 4. Starting at index 2: 2 -> 1 -> 0 -> 2 -> 1. Sum: 2+1+0+2+1 = 6.

**Example 2**

- Input: `receiver = [1, 1, 1, 2, 3]`, `k = 3`
- Output: `10`
- Explanation: Starting at index 4: 4 -> 3 -> 2 -> 1. Sum: 4+3+2+1 = 10.

**Example 3**

- Input: `receiver = [0, 0, 0, 0, 0]`, `k = 1`
- Output: `4`
- Explanation: Starting at index 4: 4 -> 0. Sum: 4+0 = 4.

---

## Solution
### Approach
The problem is solved using **Binary Lifting** (also known as Sparse Table for functional graphs). Since `k` can be very large, we precompute the state after $2^j$ passes for every player. Specifically, we maintain two tables: `jump[j][i]` (the player reached after $2^j$ passes starting from `i`) and `sum_val[j][i]` (the sum of indices visited in those $2^j$ passes). This allows us to compute the result for any `k` in $O(\log k)$ time.

### Complexity Analysis
- **Time Complexity**: $O(n \log k)$, where $n$ is the number of players. We precompute tables of size $n \times \log k$.
- **Space Complexity**: $O(n \log k)$ to store the jump and sum tables.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(receiver: list[int], k: int) -> int:
    n = len(receiver)
    if k == 0:
        return n - 1

    # max_log is the number of bits needed to represent k
    max_log = k.bit_length()

    # jump[j][i] stores the player reached after 2^j passes starting from i
    # sum_val[j][i] stores the sum of indices visited in 2^j passes starting from i
    jump = [[0] * n for _ in range(max_log)]
    sum_val = [[0] * n for _ in range(max_log)]

    for i in range(n):
        jump[0][i] = receiver[i]
        sum_val[0][i] = i

    for j in range(1, max_log):
        for i in range(n):
            mid = jump[j-1][i]
            jump[j][i] = jump[j-1][mid]
            sum_val[j][i] = sum_val[j-1][i] + sum_val[j-1][mid]

    ans = 0
    for i in range(n):
        curr_sum = 0
        curr_pos = i
        temp_k = k

        # Use binary lifting to traverse k steps
        for j in range(max_log):
            if (temp_k >> j) & 1:
                curr_sum += sum_val[j][curr_pos]
                curr_pos = jump[j][curr_pos]

        # Add the final node reached after k passes
        curr_sum += curr_pos
        ans = max(ans, curr_sum)

    return ans
```
</details>
