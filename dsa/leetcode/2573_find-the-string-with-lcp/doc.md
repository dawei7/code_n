# Find the String with LCP

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2573 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming, Greedy, Union-Find, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-string-with-lcp](https://leetcode.com/problems/find-the-string-with-lcp/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-string-with-lcp/).

### Goal
Given an $n \times n$ matrix `lcp` where `lcp[i][j]` represents the length of the longest common prefix between the suffixes starting at index `i` and index `j` of an unknown string `s` of length `n`, reconstruct the lexicographically smallest string `s` that satisfies these constraints. If no such string exists, return an empty string.

### Function Contract
**Inputs**

- `lcp`: A 2D list of integers of size $n \times n$.

**Return value**

- A string representing the lexicographically smallest string `s` that generates the given `lcp` matrix, or an empty string if the matrix is inconsistent.

### Examples
**Example 1**

- Input: `lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]`
- Output: `"abab"`

**Example 2**

- Input: `lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]`
- Output: `"aaaa"`

**Example 3**

- Input: `lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]`
- Output: `""`

---

## Solution
### Approach
The solution relies on the properties of the LCP matrix:
1. `lcp[i][j] == lcp[j][i]` and `lcp[i][i] == n - i`.
2. If `s[i] == s[j]`, then `lcp[i][j] = 1 + lcp[i+1][j+1]`.
3. If `s[i] != s[j]`, then `lcp[i][j] = 0`.
We greedily assign characters starting from 'a'. We use a counter to track the current character and verify the consistency of the matrix by checking if the generated string actually produces the input `lcp` matrix.

### Complexity Analysis
- **Time Complexity**: $O(n^2)$, where $n$ is the length of the string. We iterate through the matrix once to build the string and once to verify the constraints.
- **Space Complexity**: $O(n)$ to store the resulting string and the auxiliary array used for character assignment.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(lcp: list[list[int]]) -> str:
    n = len(lcp)

    labels = [-1] * n
    next_label = 0
    for i in range(n):
        if labels[i] != -1:
            continue
        if next_label == 26:
            return ""
        for j in range(i, n):
            if lcp[i][j] > 0:
                labels[j] = next_label
        next_label += 1

    produced = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        if lcp[i][i] != n - i:
            return ""
        for j in range(n - 1, -1, -1):
            if labels[i] == labels[j]:
                produced[i][j] = produced[i + 1][j + 1] + 1
            if produced[i][j] != lcp[i][j]:
                return ""

    return "".join(chr(ord("a") + label) for label in labels)
```
</details>
