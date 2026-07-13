# Alternating Groups I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3206 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [alternating-groups-i](https://leetcode.com/problems/alternating-groups-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/alternating-groups-i/).

### Goal
Given a circular array of binary values (0s and 1s), identify the number of "alternating groups" of size 3. An alternating group is defined as a triplet of consecutive elements where the middle element differs from both its left and right neighbors (i.e., the pattern is either `0, 1, 0` or `1, 0, 1`).

### Function Contract
**Inputs**

- `colors`: A list of integers where each element is either 0 or 1.

**Return value**

- An integer representing the total count of triplets `(colors[i-1], colors[i], colors[i+1])` that satisfy the alternating condition, accounting for the circular nature of the array.

### Examples
**Example 1**

- Input: `colors = [1, 1, 1]`
- Output: `0`

**Example 2**

- Input: `colors = [0, 1, 0, 0, 1]`
- Output: `3`

**Example 3**

- Input: `colors = [1, 0, 1, 0, 1]`
- Output: `5`

---

## Solution
### Approach
The problem utilizes a **Sliding Window** approach with a fixed window size of 3. Because the array is circular, the indices are handled using modulo arithmetic (`i % n`) to ensure that the last elements wrap around to the beginning of the array.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the array exactly once.
- **Space Complexity**: `O(1)`, as we only use a constant amount of extra space for counters and index tracking.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(colors: list[int]) -> int:
    n = len(colors)
    if n < 3:
        return 0

    count = 0
    # Iterate through each index, treating it as the center of a triplet.
    # Due to circularity, the neighbors of index i are (i-1)%n and (i+1)%n.
    for i in range(n):
        left = colors[(i - 1) % n]
        mid = colors[i]
        right = colors[(i + 1) % n]

        # Check if the middle element is different from both neighbors
        if mid != left and mid != right:
            count += 1

    return count
```
</details>
