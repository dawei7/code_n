# Construct String with Minimum Cost

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3213 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming, Suffix Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [construct-string-with-minimum-cost](https://leetcode.com/problems/construct-string-with-minimum-cost/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/construct-string-with-minimum-cost/).

### Goal
Given a target string and a dictionary of words with associated costs, determine the minimum total cost required to construct the target string by concatenating words from the dictionary. If it is impossible to form the target string, return -1.

### Function Contract
**Inputs**

- `target`: A string representing the sequence to be constructed.
- `words`: A list of strings representing the available building blocks.
- `costs`: A list of integers where `costs[i]` is the cost to use `words[i]`.

**Return value**

- An integer representing the minimum cost to construct the target, or -1 if construction is impossible.

### Examples
**Example 1**

- Input: `target = "abcdef"`, `words = ["ab", "abc", "cd", "def", "abcd"]`, `costs = [1, 2, 3, 10, 10]`
- Output: `8`

**Example 2**

- Input: `target = "aaaa"`, `words = ["aaaa", "aaa"]`, `costs = [3, 2]`
- Output: `3`

**Example 3**

- Input: `target = "abcdef"`, `words = ["abfff", "abc"], costs = [1, 2]`
- Output: `-1`

---

## Solution
### Approach
The problem is solved using Dynamic Programming combined with a Trie (Prefix Tree). We define `dp[i]` as the minimum cost to construct the prefix of `target` of length `i`. For each position `i`, we traverse the Trie using the suffix of the target starting at `i` to find all dictionary words that match the target starting at that position, updating the DP table accordingly.

### Complexity Analysis
- **Time Complexity**: O(N * L + M * K), where N is the length of the target, L is the maximum length of a word in the dictionary, M is the number of words, and K is the average length of words. The Trie construction takes O(M * K) and the DP transition takes O(N * L).
- **Space Complexity**: O(M * K) to store the Trie structure and O(N) for the DP array.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict


def solve(target: str, words: list[str], costs: list[int]) -> int:
    base = 911_382_323
    mask = (1 << 64) - 1
    n = len(target)

    powers = [1] * (n + 1)
    prefix = [0] * (n + 1)
    for i, char in enumerate(target):
        powers[i + 1] = (powers[i] * base) & mask
        prefix[i + 1] = (prefix[i] * base + ord(char)) & mask

    by_length: dict[int, dict[int, int]] = defaultdict(dict)
    for word, cost in zip(words, costs):
        word_hash = 0
        for char in word:
            word_hash = (word_hash * base + ord(char)) & mask
        bucket = by_length[len(word)]
        previous = bucket.get(word_hash)
        if previous is None or cost < previous:
            bucket[word_hash] = cost

    buckets = [(length, by_length[length]) for length in sorted(by_length) if length <= n]
    inf = 10**30
    dp = [inf] * (n + 1)
    dp[0] = 0

    for end in range(1, n + 1):
        best = inf
        for length, bucket in buckets:
            start = end - length
            if start < 0:
                break
            previous = dp[start]
            if previous == inf:
                continue
            segment_hash = (prefix[end] - ((prefix[start] * powers[length]) & mask)) & mask
            cost = bucket.get(segment_hash)
            if cost is not None:
                candidate = previous + cost
                if candidate < best:
                    best = candidate
        dp[end] = best

    return -1 if dp[n] == inf else dp[n]
```
</details>
