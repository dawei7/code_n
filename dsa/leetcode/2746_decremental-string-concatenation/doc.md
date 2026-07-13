# Decremental String Concatenation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2746 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [decremental-string-concatenation](https://leetcode.com/problems/decremental-string-concatenation/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/decremental-string-concatenation/).

### Goal
Given an array of strings `words`, we perform sequential concatenations starting with the first word. For each subsequent word, we can either append it to the end of the current concatenated string or prepend it to the beginning.

If the adjacent characters at the junction of the concatenation are identical, they merge into a single character, reducing the total length of the resulting string by 1. The goal is to find the minimum possible length of the final string after joining all words in the given order.

### Function Contract
**Inputs**
- `words`: `List[str]` - An array of lowercase English strings to be concatenated sequentially.

**Return value**
- `int` - The minimum possible length of the final concatenated string.

### Examples
**Example 1**
- Input: `words = ["aa", "ab", "bc"]`
- Output: `4`
- Explanation:
  - Start with $S_0 = \text{"aa"}$ (length 2).
  - Append "ab" to the end of $S_0$: $S_1 = \text{"aa"} + \text{"ab"} \rightarrow \text{"aab"}$ (length 3, since 'a' matches 'a').
  - Append "bc" to the end of $S_1$: $S_2 = \text{"aab"} + \text{"bc"} \rightarrow \text{"aabc"}$ (length 4, since 'b' matches 'b').
  - The minimum length is 4.

**Example 2**
- Input: `words = ["ab", "b"]`
- Output: `2`
- Explanation:
  - Start with $S_0 = \text{"ab"}$ (length 2).
  - Append "b" to the end of $S_0$: $S_1 = \text{"ab"} + \text{"b"} \rightarrow \text{"ab"}$ (length 2, since 'b' matches 'b').
  - The minimum length is 2.

**Example 3**
- Input: `words = ["aaa", "c", "aba"]`
- Output: `6`
- Explanation:
  - Start with $S_0 = \text{"aaa"}$ (length 3).
  - Prepend "c" to $S_0$: $S_1 = \text{"caaa"}$ (length 4).
  - Append "aba" to $S_1$: $S_2 = \text{"caaa"} + \text{"aba"} \rightarrow \text{"caaaba"}$ (length 6, since 'a' matches 'a').
  - The minimum length is 6.

---

## Solution
### Approach
This problem can be modeled using **Dynamic Programming**.

At any step $i$ of the concatenation process, the only properties of the current concatenated string $S_i$ that affect future merges are:
1. Its **first character**.
2. Its **last character**.

Since the alphabet size is small ($\Sigma = 26$ lowercase English letters), we can represent the state at step $i$ as `dp[first][last]`, which stores the minimum length of the concatenated string starting with character `first` and ending with character `last`.

### Transitions
For each word $W$ in `words[1:]` with length $L$, first character $f$, and last character $l$:
1. **Append $W$ to the end of the current string:**
   - The new first character remains `first`.
   - The new last character becomes `l`.
   - The new length is `dp[first][last] + L - 1` if `last == f`, else `dp[first][last] + L`.
2. **Prepend $W$ to the beginning of the current string:**
   - The new first character becomes `f`.
   - The new last character remains `last`.
   - The new length is `dp[first][last] + L - 1` if `l == first`, else `dp[first][last] + L`.

By maintaining a 2D table of size $26 \times 26$ and updating it iteratively for each word, we can find the optimal solution efficiently.

### Complexity Analysis
- **Time Complexity**: $O(N \cdot \Sigma^2)$ where $N$ is the number of words and $\Sigma = 26$ is the alphabet size. Since $\Sigma$ is a constant, the time complexity simplifies to $O(N)$, which is highly optimal and runs in milliseconds.
- **Space Complexity**: $O(\Sigma^2)$ auxiliary space to store the DP table. Since $\Sigma = 26$, the space complexity is $O(1)$ auxiliary space.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(words: List[str]) -> int:
    if not words:
        return 0

    # dp[first][last] stores the minimum length of a string starting with 'first' and ending with 'last'
    # We map 'a'-'z' to 0-25
    INF = float('inf')
    dp = [[INF] * 26 for _ in range(26)]

    first_char = ord(words[0][0]) - 97
    last_char = ord(words[0][-1]) - 97
    dp[first_char][last_char] = len(words[0])

    for i in range(1, len(words)):
        word = words[i]
        L = len(word)
        f = ord(word[0]) - 97
        l = ord(word[-1]) - 97

        next_dp = [[INF] * 26 for _ in range(26)]

        for first in range(26):
            for last in range(26):
                val = dp[first][last]
                if val == INF:
                    continue

                # Option 1: Append word to the end
                # New string starts with 'first' and ends with 'l'
                cost1 = val + L - (1 if last == f else 0)
                if cost1 < next_dp[first][l]:
                    next_dp[first][l] = cost1

                # Option 2: Prepend word to the beginning
                # New string starts with 'f' and ends with 'last'
                cost2 = val + L - (1 if l == first else 0)
                if cost2 < next_dp[f][last]:
                    next_dp[f][last] = cost2

        dp = next_dp

    ans = INF
    for first in range(26):
        for last in range(26):
            if dp[first][last] < ans:
                ans = dp[first][last]

    return ans
```
</details>
