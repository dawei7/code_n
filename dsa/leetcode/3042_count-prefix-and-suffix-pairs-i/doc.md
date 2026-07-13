# Count Prefix and Suffix Pairs I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3042 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String, Trie, Rolling Hash, String Matching, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-prefix-and-suffix-pairs-i](https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/).

### Goal
Given an array of strings, identify all pairs of indices (i, j) such that i < j and the string at index i is both a prefix and a suffix of the string at index j. The objective is to return the total count of such valid pairs.

### Function Contract
**Inputs**

- `words`: A list of strings consisting of lowercase English letters.

**Return value**

- An integer representing the total number of pairs (i, j) where 0 <= i < j < len(words) and `words[i]` is both a prefix and a suffix of `words[j]`.

### Examples
**Example 1**

- Input: `words = ["a","aba","ababa","aa"]`
- Output: `4`
- Explanation: Valid pairs are (0,1), (0,2), (1,2), (0,3).

**Example 2**

- Input: `words = ["pa","papa","ma","mama"]`
- Output: `2`
- Explanation: Valid pairs are (0,1), (2,3).

**Example 3**

- Input: `words = ["abab","ab"]`
- Output: `0`

---

## Solution
### Approach
The problem utilizes a brute-force comparison approach. For each pair of indices (i, j) where i < j, we verify the prefix and suffix condition using string slicing or built-in methods like `startswith()` and `endswith()`. Given the constraints of this specific problem (N <= 50), an O(N^2 * L) approach is efficient enough.

### Complexity Analysis
- **Time Complexity**: O(N^2 * L), where N is the number of strings in the array and L is the maximum length of a string. We iterate through all pairs and perform string matching operations.
- **Space Complexity**: O(1), as we only use a counter variable and do not allocate extra space proportional to the input size.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(words: List[str]) -> int:
    """
    Counts the number of pairs (i, j) such that i < j and
    words[i] is both a prefix and a suffix of words[j].
    """
    count = 0
    n = len(words)

    for i in range(n):
        for j in range(i + 1, n):
            str1 = words[i]
            str2 = words[j]

            # A string cannot be a prefix/suffix of a shorter string
            if len(str1) > len(str2):
                continue

            if str2.startswith(str1) and str2.endswith(str1):
                count += 1

    return count
```
</details>
