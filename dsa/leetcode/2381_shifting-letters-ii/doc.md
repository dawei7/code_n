# Shifting Letters II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2381 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [shifting-letters-ii](https://leetcode.com/problems/shifting-letters-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/shifting-letters-ii/).

### Goal
Given a string and a series of range-based shift operations, apply all shifts to the string. A shift operation consists of a start index, an end index, and a direction (forward or backward). A forward shift moves a character to the next letter in the alphabet (wrapping 'z' to 'a'), while a backward shift moves it to the previous letter (wrapping 'a' to 'z'). The goal is to return the final string after all operations are applied.

### Function Contract
**Inputs**

- `s`: A string consisting of lowercase English letters.
- `shifts`: A list of lists, where each inner list contains three integers `[start, end, direction]`. `start` and `end` are inclusive indices, and `direction` is 1 for forward shift and 0 for backward shift.

**Return value**

- A string representing the modified characters after all shifts are applied.

### Examples
**Example 1**

- Input: `s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]`
- Output: `"ace"`

**Example 2**

- Input: `s = "dztz", shifts = [[0,0,0],[1,1,1]]`
- Output: `"catz"`

**Example 3**

- Input: `s = "x", shifts = [[0,0,0]]`
- Output: `"w"`

---

## Solution
### Approach
The problem is solved using the **Difference Array** technique (a variation of Prefix Sum). Since we need to perform range updates efficiently, we create an array of size `n + 1` to store the net shift value for each index. By incrementing the start index and decrementing the index after the end, we can compute the total shift for each character in linear time using a prefix sum scan.

### Complexity Analysis
- **Time Complexity**: `O(n + m)`, where `n` is the length of the string and `m` is the number of shift operations. We iterate through the shifts once and the string once.
- **Space Complexity**: `O(n)`, required to store the difference array of size `n + 1`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(s: str, shifts: list[list[int]]) -> str:
    n = len(s)
    # diff array to store the net shift at each index
    # size n + 1 to handle the end boundary easily
    diff = [0] * (n + 1)

    for start, end, direction in shifts:
        val = 1 if direction == 1 else -1
        diff[start] += val
        if end + 1 < n:
            diff[end + 1] -= val

    # Compute prefix sums to get the actual shift for each character
    current_shift = 0
    result = []
    for i in range(n):
        current_shift += diff[i]

        # Calculate the new character
        # ord(s[i]) - ord('a') gives 0-25 index
        # Apply shift and use modulo 26 to handle wrapping
        original_pos = ord(s[i]) - ord('a')
        new_pos = (original_pos + current_shift) % 26
        result.append(chr(ord('a') + new_pos))

    return "".join(result)
```
</details>
