# Apply Operations to Make String Empty

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3039 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [apply-operations-to-make-string-empty](https://leetcode.com/problems/apply-operations-to-make-string-empty/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/apply-operations-to-make-string-empty/).

### Goal
Given a string `s`, repeatedly remove the first occurrence of every character that appears at least once in the current string until the string becomes empty. The task is to return the string formed by the characters removed in the very last operation.

### Function Contract
**Inputs**

- `s`: A string consisting of lowercase English letters.

**Return value**

- A string representing the characters removed during the final pass of the deletion process.

### Examples
**Example 1**

- Input: `s = "aabcbbca"`
- Output: `"ba"`
- Explanation:
  1. First pass: remove 'a', 'b', 'c' -> remaining "abca"
  2. Second pass: remove 'a', 'b', 'c' -> remaining "a"
  3. Third pass: remove 'a' -> remaining ""
  The last characters removed were 'b' and 'a'.

**Example 2**

- Input: `s = "abcd"`
- Output: `"abcd"`

**Example 3**

- Input: `s = "aaa"`
- Output: `"a"`

---

## Solution
### Approach
The problem relies on frequency counting and tracking the last index of occurrence. Since we remove the first occurrence of every character in each pass, the characters removed in the final pass are exactly those that have the maximum frequency in the original string, appearing in the order of their last occurrence in the original string.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the string. We iterate through the string once to count frequencies and once more to identify the last indices.
- **Space Complexity**: `O(k)`, where `k` is the size of the alphabet (at most 26), used to store frequency counts and last indices.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(s: str) -> str:
    from collections import Counter

    # Count the frequency of each character
    counts = Counter(s)
    max_freq = max(counts.values())

    # Identify characters that appear with the maximum frequency
    # We need to keep track of their last occurrence index to maintain relative order
    last_indices = {}
    for i, char in enumerate(s):
        last_indices[char] = i

    # Filter characters that have the max frequency
    result_chars = []
    for char, count in counts.items():
        if count == max_freq:
            result_chars.append((last_indices[char], char))

    # Sort by the index of their last occurrence to get the correct order
    result_chars.sort()

    return "".join(char for index, char in result_chars)
```
</details>
