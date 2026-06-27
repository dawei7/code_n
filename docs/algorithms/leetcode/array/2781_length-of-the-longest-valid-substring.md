# Length of the Longest Valid Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2781 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Sliding Window |
| Official Link | [length-of-the-longest-valid-substring](https://leetcode.com/problems/length-of-the-longest-valid-substring/) |

## Problem Description & Examples
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

## Underlying Base Algorithm(s)
The problem is solved using a **Sliding Window** approach combined with a **Hash Set** for efficient lookup. By maintaining a left pointer that tracks the start of the current valid window, we iterate through the string with a right pointer. For every position, we check all possible forbidden substrings ending at that position (up to a maximum length of 10, as per problem constraints). If a forbidden substring is found, we shrink the window by moving the left pointer to the position immediately after the start of that forbidden substring.

---

## Complexity Analysis
- **Time Complexity**: $O(N \cdot L^2)$, where $N$ is the length of the string and $L$ is the maximum length of a forbidden string (capped at 10). Since $L$ is small, this is effectively $O(N)$.
- **Space Complexity**: $O(M \cdot L)$, where $M$ is the number of forbidden strings and $L$ is the average length of those strings, used to store the forbidden set.
