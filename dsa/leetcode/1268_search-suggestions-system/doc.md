# Search Suggestions System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1268 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Binary Search, Trie, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [search-suggestions-system](https://leetcode.com/problems/search-suggestions-system/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/search-suggestions-system/).

### Goal
After each typed character of `searchWord`, return up to three lexicographically smallest product names that start with the current prefix.

### Function Contract
**Inputs**

- `products`: product name strings.
- `searchWord`: typed search word.

**Return value**

A list of suggestion lists, one for each prefix of `searchWord`.

### Examples
**Example 1**

- Input: `products = ["mobile","mouse","moneypot","monitor","mousepad"]`, `searchWord = "mouse"`
- Output: `[["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]`

**Example 2**

- Input: `products = ["havana"]`, `searchWord = "havana"`
- Output: `[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]`

**Example 3**

- Input: `products = ["bags","baggage","banner","box","cloths"]`, `searchWord = "bags"`
- Output: `[["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]`

---

## Solution
### Approach
Sorting and binary search over prefix ranges.

### Complexity Analysis
- **Time Complexity**: `O(p log p + L log p)` plus output size, where `p` is product count and `L = len(searchWord)`.
- **Space Complexity**: `O(p)` if sorting creates a copy; output excluded.

### Reference Implementations
<details>
<summary>python</summary>

```python
from bisect import bisect_left


def solve(products, search_word):
    products.sort()
    answer = []
    prefix = ""
    for ch in search_word:
        prefix += ch
        start = bisect_left(products, prefix)
        suggestions = []
        for product in products[start:start + 3]:
            if product.startswith(prefix):
                suggestions.append(product)
        answer.append(suggestions)
    return answer
```
</details>
