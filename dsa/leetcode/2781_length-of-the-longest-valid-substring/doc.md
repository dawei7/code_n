# Length of the Longest Valid Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2781 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [length-of-the-longest-valid-substring](https://leetcode.com/problems/length-of-the-longest-valid-substring/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/length-of-the-longest-valid-substring/).

### Goal
Given a string `word` and a list of `forbidden` strings, determine the length of the longest substring of `word` that does not contain any of the forbidden strings as a substring.

### Function Contract
**Inputs**

- `word`: A string consisting of lowercase English letters.
- `forbidden`: A list of strings, where each string is a forbidden pattern.

**Return value**

- An integer representing the maximum length of a valid substring.

### Examples
**Example 1**

- Input: `word = "cbaaaabc"`, `forbidden = ["aaa","cb"]`
- Output: `4`

**Example 2**

- Input: `word = "leetcode"`, `forbidden = ["de","le","e"]`
- Output: `4`

**Example 3**

- Input: `word = "abc"`, `forbidden = ["a","b","c"]`
- Output: `0`

---

## Solution
### Approach
The problem is solved using a **Sliding Window** approach combined with a **Hash Set** for efficient lookup. By maintaining a left pointer that tracks the start of the current valid window, we iterate through the string with a right pointer. For every position, we check all possible forbidden substrings ending at that position (up to a maximum length of 10, as per problem constraints). If a forbidden substring is found, we shrink the window by moving the left pointer to the position immediately after the start of that forbidden substring.

### Complexity Analysis
- **Time Complexity**: $O(N \cdot L^2)$, where $N$ is the length of the string and $L$ is the maximum length of a forbidden string (capped at 10). Since $L$ is small, this is effectively $O(N)$.
- **Space Complexity**: $O(M \cdot L)$, where $M$ is the number of forbidden strings and $L$ is the average length of those strings, used to store the forbidden set.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(word: str, forbidden: list[str]) -> int:
    forbidden_set = set(forbidden)
    max_len = 0
    left = 0
    n = len(word)

    # The problem constraints state forbidden strings have length at most 10.
    # We only need to check substrings ending at 'right' with length up to 10.
    for right in range(n):
        # Check all possible forbidden substrings ending at 'right'
        # A forbidden string can have a max length of 10.
        for length in range(1, 11):
            if right - length + 1 < left:
                break

            sub = word[right - length + 1 : right + 1]
            if sub in forbidden_set:
                # If found, move left pointer to just after the start of this forbidden string
                left = right - length + 2
                break

        max_len = max(max_len, right - left + 1)

    return max_len
```
</details>
