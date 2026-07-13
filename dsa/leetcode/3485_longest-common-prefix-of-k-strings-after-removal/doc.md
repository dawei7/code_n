# Longest Common Prefix of K Strings After Removal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3485 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [longest-common-prefix-of-k-strings-after-removal](https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/).

### Goal
Given a list of strings and an integer `k`, determine the length of the longest common prefix that can be formed by at least `k` strings after removing at most one character from each string.

### Function Contract
**Inputs**

- `strs`: A list of strings consisting of lowercase English letters.
- `k`: An integer representing the minimum number of strings that must share the resulting prefix.

**Return value**

- An integer representing the maximum possible length of a common prefix shared by at least `k` strings, where each string is allowed to have one character deleted.

### Examples
**Example 1**

- Input: `strs = ["flower","flow","flight"], k = 3`
- Output: `3`

**Example 2**

- Input: `strs = ["apple","apply","ape"], k = 2`
- Output: `4`

**Example 3**

- Input: `strs = ["dog","racecar","car"], k = 1`
- Output: `3`

---

## Solution
### Approach
The problem is solved using a Trie (Prefix Tree) combined with a depth-first search (DFS) or a greedy approach. Since we can remove at most one character, for each string, we consider two states: "no character removed yet" and "one character already removed". We traverse the Trie while tracking how many strings reach each node under these two states.

### Complexity Analysis
- **Time Complexity**: `O(N * L)`, where `N` is the number of strings and `L` is the maximum length of a string. We process each character of each string to build/traverse the state-space.
- **Space Complexity**: `O(N * L)` to store the Trie structure representing the prefixes.

### Reference Implementations
<details>
<summary>python</summary>

```python
class SegmentTree:
    def __init__(self, active: list[int]):
        self.size = 1
        while self.size < len(active):
            self.size *= 2
        self.tree = [-1] * (2 * self.size)
        for index, value in enumerate(active):
            self.tree[self.size + index] = index if value else -1
        for index in range(self.size - 1, 0, -1):
            self.tree[index] = max(self.tree[2 * index], self.tree[2 * index + 1])

    def set(self, index: int, enabled: bool) -> None:
        node = self.size + index
        self.tree[node] = index if enabled else -1
        node //= 2
        while node:
            self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])
            node //= 2

    def max_active(self) -> int:
        return self.tree[1]


def solve(words: list[str], k: int) -> list[int]:
    if len(words) - 1 < k:
        return [0] * len(words)

    children: list[dict[str, int]] = [{}]
    counts = [0]
    depths = [0]

    for word in words:
        node = 0
        for char in word:
            nxt = children[node].get(char)
            if nxt is None:
                nxt = len(children)
                children[node][char] = nxt
                children.append({})
                counts.append(0)
                depths.append(depths[node] + 1)
            node = nxt
            counts[node] += 1

    max_depth = max(depths, default=0)
    valid_by_depth = [0] * (max_depth + 1)
    for node in range(1, len(counts)):
        if counts[node] >= k:
            valid_by_depth[depths[node]] += 1

    active = [1 if count else 0 for count in valid_by_depth]
    tree = SegmentTree(active)
    answer: list[int] = []

    for word in words:
        node = 0
        disabled: list[int] = []
        seen_depths: set[int] = set()
        for char in word:
            node = children[node][char]
            depth = depths[node]
            if (
                counts[node] == k
                and valid_by_depth[depth] == 1
                and depth not in seen_depths
            ):
                tree.set(depth, False)
                disabled.append(depth)
                seen_depths.add(depth)
        answer.append(max(0, tree.max_active()))
        for depth in disabled:
            tree.set(depth, True)

    return answer
```
</details>
