# Find the Maximum Sum of Node Values

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3068 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy, Bit Manipulation, Tree, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-maximum-sum-of-node-values](https://leetcode.com/problems/find-the-maximum-sum-of-node-values/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-maximum-sum-of-node-values/).

### Goal
Given an array of node values and an integer `k`, you can perform an operation any number of times: select any two connected nodes and XOR their values with `k`. The objective is to maximize the total sum of all node values after performing any number of these operations.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the initial values of the nodes.
- `k`: An integer used for the XOR operation.
- `edges`: A list of pairs representing the connections between nodes (note: since the operation can be applied to any connected pair, the graph structure allows us to propagate the XOR operation to any two nodes, effectively allowing us to XOR any pair of nodes).

**Return value**

- An integer representing the maximum possible sum of all node values.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1], k = 3, edges = [[0, 1], [0, 2]]`
- Output: `6`

**Example 2**

- Input: `nums = [2, 3], k = 7, edges = [[0, 1]]`
- Output: `9`

**Example 3**

- Input: `nums = [7, 7, 7, 7, 7, 7], k = 3, edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]`
- Output: `42`

---

## Solution
### Approach
The problem can be reduced to a greedy strategy. XORing two nodes with `k` twice is equivalent to doing nothing. XORing any two nodes with `k` is always possible if they are connected. By transitivity, we can XOR any pair of nodes with `k`. The core insight is that we want to maximize the sum by choosing an even number of nodes to XOR with `k`. For each node, we decide whether to keep `nums[i]` or change it to `nums[i] ^ k`. We track the net gain `(nums[i] ^ k) - nums[i]` and ensure we only apply the XOR to an even number of nodes to maintain the parity constraint.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of nodes, as we iterate through the array once to calculate gains and parity.
- **Space Complexity**: `O(1)`, as we only store a few variables regardless of the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(nums: List[int], k: int, edges: List[List[int]]) -> int:
    """
    The problem allows us to XOR any two connected nodes with k.
    Because we can perform this operation any number of times, we can effectively
    XOR any pair of nodes with k. XORing a pair of nodes with k twice is
    equivalent to doing nothing. Thus, we can choose to XOR any even number
    of nodes with k.

    For each node, we calculate the potential gain: (nums[i] ^ k) - nums[i].
    If the gain is positive, we prefer to XOR. We count how many nodes we
    have XORed. If the count is even, we are done. If it is odd, we must
    either revert the XOR for the node with the smallest positive gain or
    apply the XOR to the node with the largest negative gain.
    """
    total_sum = 0
    count = 0
    min_abs_diff = float('inf')

    for x in nums:
        xor_val = x ^ k
        total_sum += max(x, xor_val)

        # If we chose the XORed value, increment count
        if xor_val > x:
            count += 1

        # Track the minimum absolute difference to adjust parity if needed
        min_abs_diff = min(min_abs_diff, abs(x - xor_val))

    # If we XORed an odd number of nodes, we must adjust to make it even
    if count % 2 == 1:
        total_sum -= min_abs_diff

    return total_sum
```
</details>
