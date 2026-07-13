# Maximum Palindromes After Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3035 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Greedy, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-palindromes-after-operations](https://leetcode.com/problems/maximum-palindromes-after-operations/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-palindromes-after-operations/).

### Goal
Given a list of strings, you are permitted to rearrange the characters of all strings arbitrarily. The objective is to maximize the total number of palindromic strings you can form by redistributing these characters across the original string lengths.

### Function Contract
**Inputs**

- `words`: A list of strings representing the available characters and the target lengths for the resulting palindromes.

**Return value**

- An integer representing the maximum number of palindromes that can be formed.

### Examples
**Example 1**

- Input: `words = ["abbb","ba","aa"]`
- Output: `3`

**Example 2**

- Input: `words = ["abc","ab"]`
- Output: `2`

**Example 3**

- Input: `words = ["cdl","abc","ab"]`
- Output: `1`

---

## Solution
### Approach
The problem is solved using a **Greedy** approach combined with **Frequency Counting**.
1. Count the total occurrences of every character across all strings.
2. Determine the number of "pairs" (two identical characters) available.
3. Sort the input strings by length.
4. Iterate through the sorted strings, attempting to fill each palindrome by using as many pairs as possible. If a string has an odd length, it will require one "center" character (which can be any remaining character).
5. Keep track of the number of pairs used and the number of leftover characters to satisfy the odd-length requirements.

### Complexity Analysis
- **Time Complexity**: $O(N \log N + \sum L_i)$, where $N$ is the number of words and $L_i$ is the length of each word. Sorting the words takes $O(N \log N)$, and counting characters takes $O(\sum L_i)$.
- **Space Complexity**: $O(1)$ (or $O(\Sigma)$ where $\Sigma$ is the alphabet size, which is constant at 26).

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter

def solve(words: list[str]) -> int:
    # Count total frequency of each character
    total_counts = Counter()
    for word in words:
        for char in word:
            total_counts[char] += 1

    # Calculate total number of pairs available
    num_pairs = 0
    for char in total_counts:
        num_pairs += total_counts[char] // 2

    # Sort words by length to prioritize filling shorter palindromes first
    words.sort(key=len)

    ans = 0
    leftover_chars = 0

    for word in words:
        length = len(word)
        pairs_needed = length // 2

        # If we have enough pairs to satisfy the current word's structure
        if num_pairs >= pairs_needed:
            num_pairs -= pairs_needed
            # If length is odd, we need one extra character in the middle
            if length % 2 == 1:
                leftover_chars += 1
            ans += 1
        else:
            # Cannot form this palindrome
            # All characters in this word become "leftover"
            leftover_chars += length

    return ans
```
</details>
