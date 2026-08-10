
## Solution

---

### Approach: Dynamic Programming

#### Intuition

The task is to find the **longest subsequence** in ${0, 1, ..., n - 1}$, where the subsequence satisfies two conditions: the values of the $\textit{groups}$ corresponding to adjacent indices are different, and the Hamming distance between the $\textit{words}$ corresponding to adjacent indices is 1. This is similar to "[Longest Unequal Adjacent Groups Subsequence I](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/)," where we can still use dynamic programming to solve the problem.

Let $\textit{dp}[i]$ represent the length of the **longest subsequence** ending at index $i$, and let $\text{HammingDistance}(s,t)$ represent the Hamming distance between two strings $s$ and $t$. If index $i$ can be added after index $j$ in the subsequence, then it must satisfy $\textit{groups}[i] \neq \textit{groups}[j]$ for $j < i$, and $\text{HammingDistance}(\textit{words}[i], \textit{words}[j]) = 1$. When these conditions hold, the length of the **longest subsequence** ending at index $i$ is updated as $\textit{dp}[i] = \max(\textit{dp}[i], \textit{dp}[j] + 1)$.

We can obtain the dynamic programming recurrence formula as follows:

$\textit{dp}[i] = \max(\textit{dp}[i], \textit{dp}[j] + 1) \quad \text{if} \quad \textit{groups}[i] \neq \textit{groups}[j], \text{HammingDistance}(\textit{words}[i], \textit{words}[j]) = 1$

For each index $i$, we enumerate the indices before $i$ to find the length of the **longest subsequence** ending at $i$. By performing this for each index, we can find the length of the **longest subsequence** in $[0, 1, ..., n - 1]$. To facilitate the calculation, we use $\textit{prev}[i]$ to record the index of the previous index in the **longest subsequence** ending at $i$. Once we identify the ending index $i$ of the **longest subsequence**, we can trace back through the indices to recover the entire subsequence and add the corresponding strings to an array. Reversing this array gives us the final answer.

#### Implementation

```python
class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        n = len(groups)
        dp = [1] * n
        prev_ = [-1] * n
        max_index = 0

        for i in range(1, n):
            for j in range(i):
                if (
                    self.check(words[i], words[j])
                    and dp[j] + 1 > dp[i]
                    and groups[i] != groups[j]
                ):
                    dp[i] = dp[j] + 1
                    prev_[i] = j
            if dp[i] > dp[max_index]:
                max_index = i

        ans = []
        i = max_index
        while i >= 0:
            ans.append(words[i])
            i = prev_[i]
        ans.reverse()
        return ans

    def check(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1
```

#### Complexity Analysis

Let $n$ be the length of the given array and $L$ be the length of each string in the string array $\textit{word}$.

- Time complexity: $O(n^2L)$.

  The time required to calculate the Hamming distance between two strings is $L$. To determine the **longest subsequence** ending at index $i$, we must traverse all indices before $i$, which takes $O(nL)$ time. Therefore, to compute the length of the **longest subsequence** ending at each index, the total time required is $O(n^2 L)$.

- Space complexity: $O(n)$.

  The space required is $O(n)$ to store the length of the **longest subsequence** ending at each index.