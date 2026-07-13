# Odd String Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2451 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [odd-string-difference](https://leetcode.com/problems/odd-string-difference/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/odd-string-difference/).

### Goal
Given a list of strings of equal length, identify the "odd one out." The difference between two adjacent characters in a string is defined as the numerical distance between them (e.g., 'b' - 'a' = 1). A string is considered different if its sequence of character differences does not match the sequence shared by all other strings in the input array.

### Function Contract
**Inputs**

- `words`: A list of strings where each string has the same length `n` (where `n >= 2`).

**Return value**

- A string that represents the unique sequence of differences compared to the rest of the list.

### Examples
**Example 1**

- Input: `words = ["adc","wzy","abc"]`
- Output: `"abc"`
- Explanation: "adc" -> [3, -1] and "wzy" -> [3, -1], while "abc" -> [1, 1].

**Example 2**

- Input: `words = ["aaa","bob","ccc","ddd"]`
- Output: `"bob"`
- Explanation: "aaa" -> [0, 0], "bob" -> [13, -13], "ccc" -> [0, 0], "ddd" -> [0, 0]. "bob" is the only one with a different difference pattern.

**Example 3**

- Input: `words = ["abm","bcn","alm"]`
- Output: `"alm"`

---

## Solution
### Approach
The solution utilizes a Hash Map (Dictionary) to store the frequency of difference arrays. By calculating the difference vector for each string, we can map these vectors to the original strings. Since only one string is unique, we can either count the occurrences of each vector or compare the first three strings to determine the "common" pattern and identify the outlier.

### Complexity Analysis
- **Time Complexity**: O(n * m), where `n` is the number of strings and `m` is the length of each string. We iterate through each string once and compute differences in linear time relative to string length.
- **Space Complexity**: O(n * m) to store the difference vectors in a hash map.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(words: list[str]) -> str:
    def get_diff(s: str) -> tuple:
        diffs = []
        for i in range(len(s) - 1):
            diffs.append(ord(s[i+1]) - ord(s[i]))
        return tuple(diffs)

    # Map difference patterns to the list of words that share that pattern
    diff_map = {}

    for word in words:
        pattern = get_diff(word)
        if pattern not in diff_map:
            diff_map[pattern] = []
        diff_map[pattern].append(word)

    # The odd string is the one whose pattern appears only once
    for pattern in diff_map:
        if len(diff_map[pattern]) == 1:
            return diff_map[pattern][0]

    return ""
```
</details>
