# Check Distances Between Same Letters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2399 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-distances-between-same-letters](https://leetcode.com/problems/check-distances-between-same-letters/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-distances-between-same-letters/).

### Goal
Determine if every character in a given string appears exactly twice, and if the number of characters between the two occurrences of each character matches a specified distance provided in an integer array.

### Function Contract
**Inputs**

- `s`: A string consisting of lowercase English letters where each letter appears exactly twice.
- `distance`: A list of 26 integers where `distance[i]` represents the required number of characters between the two occurrences of the i-th letter of the alphabet.

**Return value**

- `bool`: Returns `True` if all characters satisfy their respective distance requirements, otherwise `False`.

### Examples
**Example 1**

- Input: `s = "abaccb"`, `distance = [1, 3, 0, 5, 0, 0, ...]`
- Output: `True`

**Example 2**

- Input: `s = "aa"`, `distance = [0, 0, ...]`
- Output: `True`

**Example 3**

- Input: `s = "abcba"`, `distance = [1, 0, 0, 0, ...]`
- Output: `False`

---

## Solution
### Approach
The problem is solved using a Hash Table (or a fixed-size array of size 26) to track the first occurrence index of each character. By iterating through the string once, we can calculate the distance between the current index and the stored first index, then compare it against the provided `distance` array.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the string `s`. We traverse the string exactly once.
- **Space Complexity**: `O(1)`, as the auxiliary storage (the distance array or a tracking map) is bounded by the constant size of the alphabet (26).

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(s: str, distance: list[int]) -> bool:
    # Store the first occurrence index of each character
    first_occurrence = {}

    for current_index, char in enumerate(s):
        char_code = ord(char) - ord('a')

        if char in first_occurrence:
            # Calculate distance: number of characters between the two occurrences
            # Distance = (current_index - first_index - 1)
            prev_index = first_occurrence[char]
            actual_distance = current_index - prev_index - 1

            if actual_distance != distance[char_code]:
                return False
        else:
            # Record the first time we see the character
            first_occurrence[char] = current_index

    return True
```
</details>
