# Shift Distance Between Two Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3361 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [shift-distance-between-two-strings](https://leetcode.com/problems/shift-distance-between-two-strings/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/shift-distance-between-two-strings/).

### Goal
Calculate the minimum total cost to transform string `s` into string `t` of the same length. For each character position, you can shift the character in `s` forward or backward through the alphabet (wrapping around 'z' to 'a' or 'a' to 'z'). The cost of shifting by one position is provided by two arrays, `nextCost` and `prevCost`, representing the cost of moving to the next or previous character, respectively.

### Function Contract
**Inputs**

- `s` (str): The source string.
- `t` (str): The target string.
- `nextCost` (List[int]): An array of 26 integers where `nextCost[i]` is the cost to shift character `i` to `(i + 1) % 26`.
- `prevCost` (List[int]): An array of 26 integers where `prevCost[i]` is the cost to shift character `i` to `(i - 1) % 26`.

**Return value**

- `int`: The minimum total cost to transform `s` into `t`.

### Examples
**Example 1**

- Input: `s = "abc", t = "bcd", nextCost = [1]*26, prevCost = [1]*26`
- Output: `3`

**Example 2**

- Input: `s = "a", t = "a", nextCost = [1]*26, prevCost = [1]*26`
- Output: `0`

**Example 3**

- Input: `s = "ab", t = "cd", nextCost = [1]*26, prevCost = [1]*26`
- Output: `4`

---

## Solution
### Approach
The problem is solved using the **Shortest Path in a Graph** concept, specifically optimized via **Prefix Sums**. Since there are only 26 characters, we can precompute the minimum cost to travel between any two characters `i` and `j` using Dijkstra's algorithm or by observing that the path is either moving forward or backward. By calculating prefix sums of the `nextCost` and `prevCost` arrays, we can determine the cost of any shift in $O(1)$ time after $O(1)$ precomputation.

### Complexity Analysis
- **Time Complexity**: $O(N + \Sigma)$, where $N$ is the length of the strings and $\Sigma = 26$ is the alphabet size.
- **Space Complexity**: $O(\Sigma)$ to store the precomputed minimum costs between all character pairs.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(s: str, t: str, nextCost: list[int], prevCost: list[int]) -> int:
    n = 26
    dist = [[10**30] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
        dist[i][(i + 1) % n] = min(dist[i][(i + 1) % n], nextCost[i])
        dist[i][(i - 1) % n] = min(dist[i][(i - 1) % n], prevCost[i])

    for mid in range(n):
        for start in range(n):
            via_mid = dist[start][mid]
            for end in range(n):
                candidate = via_mid + dist[mid][end]
                if candidate < dist[start][end]:
                    dist[start][end] = candidate

    return sum(dist[ord(source) - 97][ord(target) - 97] for source, target in zip(s, t))
```
</details>
