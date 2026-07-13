# Frequencies of Shortest Supersequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3435 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Bit Manipulation, Graph Theory, Topological Sort, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [frequencies-of-shortest-supersequences](https://leetcode.com/problems/frequencies-of-shortest-supersequences/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/frequencies-of-shortest-supersequences/).

### Goal
Given a list of strings, determine the frequency of each character (from 'a' to 'z') across all possible shortest common supersequences (SCS) of the input strings. A shortest common supersequence is a string of minimum length that contains every input string as a subsequence. Since there may be multiple such supersequences, you must return the count of each character at every position across all valid SCSs, normalized or aggregated as required by the problem constraints.

### Function Contract
**Inputs**

- `words`: A list of strings consisting of lowercase English letters.

**Return value**

- A list of strings (or a structured format) representing the frequency distribution of characters in the shortest common supersequences.

### Examples
**Example 1**

- Input: `words = ["ab", "ba"]`
- Output: `["aba", "bab"]` (The SCSs are "aba" and "bab", frequencies are aggregated accordingly).

**Example 2**

- Input: `words = ["a", "b"]`
- Output: `["ab", "ba"]`

**Example 3**

- Input: `words = ["aa", "aa"]`
- Output: `["aa"]`

---

## Solution
### Approach
The problem is solved by modeling the dependencies between characters as a directed graph. Since we are looking for the shortest common supersequence, we identify the relative ordering constraints imposed by each word. We use topological sort to find valid orderings and dynamic programming (often involving bitmasking if the number of strings is small) to determine the length and structure of the SCS.

### Complexity Analysis
- **Time Complexity**: `O(2^N * N + L)`, where `N` is the number of unique characters (up to 26) and `L` is the total length of all strings. The exponential component arises from the state-space search for the shortest path in the dependency graph.
- **Space Complexity**: `O(2^N + L)` to store the DP table and the dependency graph.

### Reference Implementations
<details>
<summary>python</summary>

```python
from itertools import combinations


def solve(words):
    letters = sorted(set("".join(words)))
    index = {letter: pos for pos, letter in enumerate(letters)}
    m = len(letters)
    edges = [(index[word[0]], index[word[1]]) for word in words]

    def acyclic(duplicated: set[int]) -> bool:
        state = [0] * m

        def dfs(node: int) -> bool:
            state[node] = 1
            for source, target in edges:
                if source != node or target in duplicated:
                    continue
                if state[target] == 1:
                    return False
                if state[target] == 0 and not dfs(target):
                    return False
            state[node] = 2
            return True

        for node in range(m):
            if node in duplicated or state[node] != 0:
                continue
            if not dfs(node):
                return False
        return True

    answers = []
    for duplicate_count in range(m + 1):
        for combo in combinations(range(m), duplicate_count):
            duplicated = set(combo)
            if not acyclic(duplicated):
                continue
            freq = [0] * 26
            for letter, pos in index.items():
                freq[ord(letter) - ord("a")] = 2 if pos in duplicated else 1
            answers.append(freq)
        if answers:
            return answers

    return []
```
</details>
