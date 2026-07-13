# Maximum Enemy Forts That Can Be Captured

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2511 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-enemy-forts-that-can-be-captured](https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/).

### Goal
Given an array representing a line of forts, where `1` represents your army, `-1` represents an enemy army, and `0` represents an empty space, determine the maximum number of consecutive empty spaces you can capture. A capture is valid only if you move your army from a fort to an empty space and end at an enemy fort (or vice versa), effectively sandwiching the empty spaces between your army and an enemy army.

### Function Contract
**Inputs**

- `forts`: A list of integers where each element is `1`, `-1`, or `0`.

**Return value**

- An integer representing the maximum number of `0`s that can be captured. If no capture is possible, return `0`.

### Examples
**Example 1**

- Input: `forts = [1, 0, 0, -1, 0, 0, 0, 0, 1]`
- Output: `4`

**Example 2**

- Input: `forts = [0, 0, 1, -1]`
- Output: `0`

**Example 3**

- Input: `forts = [1, 0, 0, 0, 1]`
- Output: `0`

---

## Solution
### Approach
The problem is solved using a **Single-Pass Linear Scan** (or Two Pointers). We maintain the index of the last seen "non-empty" fort (either `1` or `-1`). Whenever we encounter a different type of non-empty fort, we calculate the distance between the current index and the last seen index, subtract 1 to account for the empty spaces between them, and update the global maximum.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the `forts` array, as we traverse the list exactly once.
- **Space Complexity**: `O(1)`, as we only use a few integer variables to track indices and the maximum count.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(forts: list[int]) -> int:
    max_captured = 0
    last_idx = -1

    for i, fort in enumerate(forts):
        if fort != 0:
            # If we find a fort and it's different from the last one seen,
            # we have a potential capture sequence.
            if last_idx != -1 and forts[last_idx] != fort:
                # The number of zeros between last_idx and i is (i - last_idx - 1)
                max_captured = max(max_captured, i - last_idx - 1)

            # Update the last seen non-empty fort index
            last_idx = i

    return max_captured
```
</details>
