# Shortest Uncommon Substring in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3076 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [shortest-uncommon-substring-in-an-array](https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/).

### Goal
Given an array of strings, determine the shortest substring for each string that does not appear as a substring in any other string within the array. If multiple such substrings exist for a given string, choose the lexicographically smallest one. If no such substring exists, return an empty string for that index.

### Function Contract
**Inputs**

- `arr`: A list of strings (`List[str]`) where each string consists of lowercase English letters.

**Return value**

- A list of strings (`List[str]`) where the $i$-th element is the shortest, lexicographically smallest uncommon substring of `arr[i]`.

### Examples
**Example 1**

- Input: `arr = ["cab","ad","bad","c"]`
- Output: `["ab","ad","ba",""]`

**Example 2**

- Input: `arr = ["abc","bcd","abcd"]`
- Output: `["","","abcd"]`

**Example 3**

- Input: `arr = ["xyz","xyz","xyz"]`
- Output: `["","",""]`

---

## Solution
### Approach
The problem is solved by generating all possible substrings for each string in the input array. We use a frequency map (Hash Table) to count the occurrences of every substring across all strings. A substring is "uncommon" if its frequency count is exactly 1 and it belongs to the string currently being processed. We iterate through lengths from 1 to the string length to ensure we find the shortest substring first, and sort lexicographically for ties.

### Complexity Analysis
- **Time Complexity**: $O(N \cdot L^3)$, where $N$ is the number of strings and $L$ is the maximum length of a string. Generating all substrings takes $O(L^2)$ and string slicing/hashing takes $O(L)$, resulting in $O(N \cdot L^3)$.
- **Space Complexity**: $O(N \cdot L^3)$ to store all possible substrings in a hash map.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List
from collections import Counter

def solve(arr: List[str]) -> List[str]:
    # Count occurrences of every substring across all strings
    # A substring is only valid if it appears in exactly one string
    # and that string is the one we are currently checking.

    substring_counts = Counter()

    # Pre-calculate all substrings for every string
    # We use a set for each string to avoid counting the same substring
    # multiple times within the same string.
    all_substrings_per_word = []
    for s in arr:
        n = len(s)
        subs = set()
        for i in range(n):
            for j in range(i + 1, n + 1):
                subs.add(s[i:j])
        all_substrings_per_word.append(subs)
        for sub in subs:
            substring_counts[sub] += 1

    result = []
    for idx, s in enumerate(arr):
        n = len(s)
        found = False
        # Check lengths from 1 to n to find the shortest
        for length in range(1, n + 1):
            candidates = []
            for i in range(n - length + 1):
                sub = s[i:i + length]
                # If this substring appears only in the current string
                if substring_counts[sub] == 1:
                    candidates.append(sub)

            if candidates:
                # Sort lexicographically to pick the smallest
                candidates.sort()
                result.append(candidates[0])
                found = True
                break

        if not found:
            result.append("")

    return result
```
</details>
