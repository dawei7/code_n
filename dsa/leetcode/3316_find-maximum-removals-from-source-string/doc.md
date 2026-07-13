# Find Maximum Removals From Source String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3316 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Two Pointers, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-maximum-removals-from-source-string](https://leetcode.com/problems/find-maximum-removals-from-source-string/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-maximum-removals-from-source-string/).

### Goal
Given a source string `source`, a target string `pattern`, and an array of indices `targetIndices`, determine the maximum number of characters that can be removed from `source` such that `pattern` remains a subsequence of the modified `source`. A removal is only valid if the index of the character being removed is present in `targetIndices`.

### Function Contract
**Inputs**

- `source` (str): The original string.
- `pattern` (str): The string that must remain a subsequence.
- `targetIndices` (List[int]): A list of indices in `source` that are eligible for removal.

**Return value**

- `int`: The maximum number of characters that can be removed from `source` while keeping `pattern` as a subsequence.

### Examples
**Example 1**

- Input: `source = "abbaac", pattern = "aba", targetIndices = [0, 1, 2, 3, 4, 5]`
- Output: `2`

**Example 2**

- Input: `source = "bcda", pattern = "d", targetIndices = [0, 3]`
- Output: `2`

**Example 3**

- Input: `source = "dda", pattern = "dda", targetIndices = [0, 1, 2]`
- Output: `0`

---

## Solution
### Approach
The problem is solved using Dynamic Programming. We define `dp[i][j]` as the maximum number of removals possible using the first `i` characters of `source` to form the first `j` characters of `pattern`. For each character in `source`, we have two choices: either keep it (if it matches the current character in `pattern`) or remove it (if its index is in `targetIndices`).

### Complexity Analysis
- **Time Complexity**: `O(N * M)`, where `N` is the length of `source` and `M` is the length of `pattern`.
- **Space Complexity**: `O(N * M)` (can be optimized to `O(M)`), where `N` is the length of `source` and `M` is the length of `pattern`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(source: str, pattern: str, targetIndices: list[int]) -> int:
    n = len(source)
    m = len(pattern)

    # Create a set for O(1) lookup of removable indices
    removable = [False] * n
    for idx in targetIndices:
        removable[idx] = True

    # dp[i][j] = max removals using first i chars of source to match first j of pattern
    # Initialize with -1 to represent unreachable states
    dp = [[-1] * (m + 1) for _ in range(n + 1)]

    # Base case: 0 chars of pattern matched using 0 chars of source
    dp[0][0] = 0

    for i in range(n):
        for j in range(m + 1):
            if dp[i][j] == -1:
                continue

            # Option 1: Remove source[i] if it is in targetIndices
            if removable[i]:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + 1)
            else:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

            # Option 2: Keep source[i] if it matches pattern[j]
            if j < m and source[i] == pattern[j]:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])

    return dp[n][m]
```
</details>
