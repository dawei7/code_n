# Find the Substring With Maximum Cost

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2606 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-substring-with-maximum-cost](https://leetcode.com/problems/find-the-substring-with-maximum-cost/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-substring-with-maximum-cost/).

### Goal
Given a string `s` and a mapping of characters to integer costs, calculate the maximum possible cost of any substring within `s`. The cost of a substring is defined as the sum of the costs of its individual characters. If a character is not explicitly mapped, its cost is its 1-based alphabetical position (e.g., 'a'=1, 'b'=2, ..., 'z'=26). If the maximum cost is negative, the result should be 0 (representing an empty substring).

### Function Contract
**Inputs**

- `s` (str): The input string consisting of lowercase English letters.
- `chars` (str): A string containing unique characters that have custom costs.
- `vals` (List[int]): A list of integers where `vals[i]` is the cost associated with `chars[i]`.

**Return value**

- `int`: The maximum cost achievable by any substring of `s`.

### Examples
**Example 1**

- Input: `s = "adaa", chars = "d", vals = [-1000]`
- Output: `2`
- Explanation: The substring "aa" has a cost of 1 + 1 = 2.

**Example 2**

- Input: `s = "abc", chars = "abc", vals = [-1, -1, -1]`
- Output: `0`
- Explanation: All substrings have negative costs, so the maximum cost is 0 (empty substring).

**Example 3**

- Input: `s = "bcacc", chars = "c", vals = [-1]`
- Output: `2`
- Explanation: The best non-empty substring has total cost 2, and the empty substring is allowed when every running choice is worse.

---

## Solution
### Approach
This problem is a classic application of **Kadane's Algorithm**. By mapping each character in the string to its respective cost, the problem transforms into finding the "Maximum Subarray Sum" in a 1D array. We iterate through the string, maintaining a running sum of the current subarray, and reset the sum to zero if it drops below zero, while tracking the global maximum encountered.

### Complexity Analysis
- **Time Complexity**: `O(n + m)`, where `n` is the length of string `s` and `m` is the length of `chars`. We iterate through `chars` once to build the cost map and through `s` once to compute the maximum cost.
- **Space Complexity**: `O(1)` (or `O(k)` where `k` is the alphabet size), as the cost map stores at most 26 character mappings.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(s: str, chars: str, vals: list[int]) -> int:
    # Initialize cost map with default 1-based alphabetical values
    cost_map = {chr(ord('a') + i): i + 1 for i in range(26)}

    # Override with custom costs
    for char, val in zip(chars, vals):
        cost_map[char] = val

    max_cost = 0
    current_running_sum = 0

    # Apply Kadane's Algorithm
    for char in s:
        current_running_sum += cost_map[char]

        # If the current subarray sum is better than the global max, update it
        if current_running_sum > max_cost:
            max_cost = current_running_sum

        # If the running sum drops below 0, reset it (start a new potential substring)
        if current_running_sum < 0:
            current_running_sum = 0

    return max_cost
```
</details>
