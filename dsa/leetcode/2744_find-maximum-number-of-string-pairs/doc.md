# Find Maximum Number of String Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2744 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-maximum-number-of-string-pairs](https://leetcode.com/problems/find-maximum-number-of-string-pairs/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-maximum-number-of-string-pairs/).

### Goal
Given an array of distinct 2-character strings, find the maximum number of pairs you can form. A pair consists of two strings at different indices where one string is the reverse of the other. Since all strings in the input array are guaranteed to be unique, each string can participate in at most one pair.

### Function Contract
**Inputs**

- `words`: `List[str]` - A list of distinct strings, where each string has a length of exactly 2 and consists only of lowercase English letters.

**Return value**

- `int` - The maximum number of pairs that can be formed.

### Examples
**Example 1**

- Input: `words = ["cd","ac","dc","ca","zz"]`
- Output: `2`
- Explanation: We can form 2 pairs:
  - "cd" and "dc"
  - "ac" and "ca"

**Example 2**

- Input: `words = ["ab","ba","cc"]`
- Output: `1`
- Explanation: We can form 1 pair:
  - "ab" and "ba"

**Example 3**

- Input: `words = ["aa","ab"]`
- Output: `0`
- Explanation: No pairs can be formed because "aa" has no distinct reverse in the list, and "ab" has no reverse "ba" in the list.

---

## Solution
### Approach
The problem can be solved efficiently using a **Hash Set** to track the strings we have encountered.

As we iterate through the list of `words`:
1. For each word, we check if its reversed counterpart is already present in our set of seen words.
2. If the reversed word is in the set, we have successfully identified a pair. We increment our pair count and remove the reversed word from the set (to prevent any potential double-counting, though the uniqueness of the input strings already guarantees each string is unique).
3. If the reversed word is not in the set, we add the current word to the set and continue.

Since each string has a constant length of 2, reversing a string and hashing it are $O(1)$ operations.

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N)$, where $N$ is the number of strings in `words`. We perform a single pass over the array, and for each string, we perform constant-time $\mathcal{O}(1)$ set lookups, insertions, and string reversals.
- **Space Complexity**: $\mathcal{O}(N)$ to store the visited strings in the hash set.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(words: List[str]) -> int:
    seen = set()
    pairs = 0

    for word in words:
        reversed_word = word[::-1]
        if reversed_word in seen:
            pairs += 1
            seen.remove(reversed_word)
        else:
            seen.add(word)

    return pairs
```
</details>
