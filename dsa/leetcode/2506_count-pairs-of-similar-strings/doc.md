# Count Pairs Of Similar Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2506 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Bit Manipulation, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [count-pairs-of-similar-strings](https://leetcode.com/problems/count-pairs-of-similar-strings/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/count-pairs-of-similar-strings/).

### Goal
Determine the number of pairs of indices `(i, j)` such that `i < j` and the strings at these indices consist of the exact same set of unique characters.

### Function Contract
**Inputs**

- `words`: A list of strings consisting of lowercase English letters.

**Return value**

- An integer representing the total count of pairs `(i, j)` where `i < j` and `words[i]` is "similar" to `words[j]`.

### Examples
**Example 1**

- Input: `words = ["aba","aabb","abcd","bac","aabc"]`
- Output: `2`

**Example 2**

- Input: `words = ["aabb","ab","ba"]`
- Output: `3`

**Example 3**

- Input: `words = ["nba","cyp","ocm"]`
- Output: `0`

---

## Solution
### Approach
The problem relies on **canonical representation** of sets. Since the order and frequency of characters do not matter, we can represent each string by the set of unique characters it contains. This can be implemented efficiently using a **bitmask** (where the $k$-th bit represents the presence of the $k$-th letter of the alphabet) or by sorting the unique characters of the string. Using a **Hash Map (Frequency Table)** allows us to count occurrences of each canonical form in linear time.

### Complexity Analysis
- **Time Complexity**: $O(N \cdot K)$, where $N$ is the number of words and $K$ is the maximum length of a word. We iterate through each word once and process its characters to build a set or bitmask.
- **Space Complexity**: $O(N)$, as we store the frequency of each unique canonical representation in a hash map.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter

def solve(words: list[str]) -> int:
    """
    Counts pairs of similar strings by mapping each string to a bitmask
    representing the set of unique characters present in the string.
    """
    # Map each word to a bitmask where the i-th bit is 1 if the i-th
    # letter of the alphabet is present.
    masks = []
    for word in words:
        mask = 0
        for char in word:
            mask |= (1 << (ord(char) - ord('a')))
        masks.append(mask)

    # Count occurrences of each mask
    counts = Counter(masks)

    # For a mask that appears 'n' times, the number of pairs is n * (n - 1) / 2
    total_pairs = 0
    for count in counts.values():
        if count > 1:
            total_pairs += (count * (count - 1)) // 2

    return total_pairs
```
</details>
