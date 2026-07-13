# Count Prefix and Suffix Pairs II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3045 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Trie, Rolling Hash, String Matching, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-prefix-and-suffix-pairs-ii](https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/).

### Goal
Given an array of strings, identify the total number of index pairs (i, j) such that i < j and the string at index i is both a prefix and a suffix of the string at index j.

### Function Contract
**Inputs**

- `words`: A list of strings consisting of lowercase English letters.

**Return value**

- An integer representing the total count of valid pairs (i, j) where `words[i]` is a prefix and suffix of `words[j]`.

### Examples
**Example 1**

- Input: `words = ["a","aba","ababa","aa"]`
- Output: `4`

**Example 2**

- Input: `words = ["pa","papa","ma","mama"]`
- Output: `2`

**Example 3**

- Input: `words = ["abab","ab"]`
- Output: `0`

---

## Solution
### Approach
The problem is efficiently solved using a **Trie (Prefix Tree)**. Since we need to check if `words[i]` is both a prefix and a suffix of `words[j]`, we can represent the prefix-suffix pair as a tuple of characters `(words[j][k], words[j][n-len(words[j])+k])`. By inserting these pairs into a Trie as we iterate through the array, we can count how many previously seen strings match the current string's prefix-suffix structure in linear time relative to the total number of characters.

### Complexity Analysis
- **Time Complexity**: `O(N * L)`, where `N` is the number of words and `L` is the maximum length of a word. We iterate through each word once and perform constant-time Trie operations for each character.
- **Space Complexity**: `O(N * L)` in the worst case to store the Trie nodes representing the prefix-suffix pairs.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

def solve(words: list[str]) -> int:
    root = TrieNode()
    total_pairs = 0

    for word in words:
        # A word is a prefix and suffix of another if the sequence of
        # pairs (word[k], word[n-len(word)+k]) matches.
        # We traverse the Trie using these character pairs.
        node = root
        n = len(word)

        for i in range(n):
            char_pair = (word[i], word[n - n + i]) # This logic simplifies to (word[i], word[i])
            # Actually, the condition is: word[i] is prefix and suffix of word[j].
            # This means word[i] == word[j][:len(word[i])] AND word[i] == word[j][-len(word[i]):]
            # We can represent the state by the pair of characters at the current index
            # relative to the start and end of the word.
            pair = (word[i], word[n - len(word) + i]) # Placeholder logic for Trie path

        # Correct approach: Use a Trie to store the prefix-suffix pairs.
        # For each word, we check how many times this specific word structure
        # has appeared as a prefix/suffix combination.

        # Re-implementing with a simpler Trie approach:
        # Since we need prefix AND suffix, we store the word in the Trie.
        # But wait, the constraint is word[i] is prefix AND suffix of word[j].
        # This is equivalent to saying word[i] is a prefix of word[j]
        # AND word[i] is a suffix of word[j].

        # Using a Trie to store the words:
        curr = root
        for i in range(n):
            pair = (word[i], word[n - n + i]) # This is just word[i]
            # Actually, the standard approach for this specific problem:
            # Insert (word[i], word[n-1-i]) into Trie.
            pass

    # Optimized implementation using a Trie of (prefix, suffix) pairs
    root = {}
    ans = 0
    for w in words:
        n = len(w)
        curr = root
        for i in range(n):
            pair = (w[i], w[n - 1 - i])
            if pair not in curr:
                curr[pair] = {}
            curr = curr[pair]
            if 'count' in curr:
                ans += curr['count']

        # After traversing, increment the count at the end of this word's path
        curr['count'] = curr.get('count', 0) + 1

    return ans
```
</details>
