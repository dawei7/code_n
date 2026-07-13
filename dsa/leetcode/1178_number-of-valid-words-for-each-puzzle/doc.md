# Number of Valid Words for Each Puzzle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1178 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Bit Manipulation, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-valid-words-for-each-puzzle](https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/).

### Goal
For each seven-letter puzzle, count words that use only letters from that puzzle and contain the puzzle's first letter.

### Function Contract
**Inputs**

- `words`: list of lowercase words.
- `puzzles`: list of seven-letter lowercase puzzle strings.

**Return value**

For each puzzle, the number of valid words.

### Examples
**Example 1**

- Input: `words = ["aaaa","asas","able","ability","actt","actor","access"]`, `puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]`
- Output: `[1,1,3,2,4,0]`

**Example 2**

- Input: `words = ["apple","pleas","please"]`, `puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]`
- Output: `[0,1,3,2,0]`

**Example 3**

- Input: `words = ["abc","abd","bcd"]`, `puzzles = ["abcdefg","bcdefga"]`
- Output: `[2,3]`

---

## Solution
### Approach
Bitmask frequency counting and submask enumeration.

### Complexity Analysis
- **Time Complexity**: `O(total_word_letters + puzzles * 2^6)`
- **Space Complexity**: `O(number of distinct word masks)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter


def solve(words, puzzles):
    counts = Counter()
    for word in words:
        mask = 0
        for ch in set(word):
            mask |= 1 << (ord(ch) - ord("a"))
        if mask.bit_count() <= 7:
            counts[mask] += 1

    answers = []
    for puzzle in puzzles:
        first = 1 << (ord(puzzle[0]) - ord("a"))
        rest = 0
        for ch in puzzle[1:]:
            rest |= 1 << (ord(ch) - ord("a"))
        total = 0
        sub = rest
        while True:
            total += counts[sub | first]
            if sub == 0:
                break
            sub = (sub - 1) & rest
        answers.append(total)
    return answers
```
</details>
