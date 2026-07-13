# Compare Strings by Frequency of the Smallest Character

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1170 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [compare-strings-by-frequency-of-the-smallest-character](https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/).

### Goal
For each query string, count how many word strings have a larger frequency of their smallest character.

### Function Contract
**Inputs**

- `queries`: query strings.
- `words`: comparison strings.

**Return value**

Array where each entry is the number of words with `f(word) > f(query)`, where `f(s)` counts occurrences of the lexicographically smallest character in `s`.

### Examples
**Example 1**

- Input: `queries = ["cbd"]`, `words = ["zaaaz"]`
- Output: `[1]`

**Example 2**

- Input: `queries = ["bbb","cc"]`, `words = ["a","aa","aaa","aaaa"]`
- Output: `[1,2]`

**Example 3**

- Input: `queries = ["abcd","aabb"]`, `words = ["zzzz","abc","aa"]`
- Output: `[2,1]`

---

## Solution
### Approach
Frequency transform, sorting, and binary search.

### Complexity Analysis
- **Time Complexity**: `O((q + w) * L + w log w + q log w)` where `L` is max string length.
- **Space Complexity**: `O(w)`

### Reference Implementations
<details>
<summary>python</summary>

```python
from bisect import bisect_right


def _frequency(word):
    smallest = min(word)
    return word.count(smallest)


def solve(queries, words):
    word_scores = sorted(_frequency(word) for word in words)
    n = len(word_scores)
    return [n - bisect_right(word_scores, _frequency(query)) for query in queries]
```
</details>
