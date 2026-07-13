# Stream of Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1032 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Design, Trie, Data Stream |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [stream-of-characters](https://leetcode.com/problems/stream-of-characters/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/stream-of-characters/).

### Goal
Design a stream checker. After each queried character, return whether any configured word is a suffix of the stream seen so far.

### Function Contract
**Inputs**

- `words`: List[str] dictionary initialized once.
- `queries`: stream of characters passed one by one to `query`.

**Return value**

List[bool] - for each query, whether the current stream ends with at least one dictionary word.

### Examples
**Example 1**

- Input: `words = ["cd", "f", "kl"], queries = ["a","b","c","d"]`
- Output: `[False, False, False, True]`

**Example 2**

- Input: `words = ["cd", "f", "kl"], queries = ["f"]`
- Output: `[True]`

**Example 3**

- Input: `words = ["ab", "ba"], queries = ["a","b","a"]`
- Output: `[False, True, True]`

---

## Solution
### Approach
Reversed trie for suffix matching.

### Complexity Analysis
- **Time Complexity**: `O(L)` per query, where `L` is the maximum word length
- **Space Complexity**: `O(total dictionary characters + L)`

### Reference Implementations
<details>
<summary>python</summary>

```python
class StreamChecker:
    def __init__(self, words: list[str]):
        self.trie: dict[str, dict] = {}
        self.max_len = 0
        for word in words:
            self.max_len = max(self.max_len, len(word))
            node = self.trie
            for char in reversed(word):
                node = node.setdefault(char, {})
            node["$"] = {}
        self.stream: list[str] = []

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        if len(self.stream) > self.max_len:
            self.stream.pop(0)

        node = self.trie
        for char in reversed(self.stream):
            if char not in node:
                return False
            node = node[char]
            if "$" in node:
                return True
        return False


def solve(words: list[str], queries: list[str]) -> list[bool]:
    checker = StreamChecker(words)
    return [checker.query(char) for char in queries]
```
</details>
