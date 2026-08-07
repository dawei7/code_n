### Approach: Enumeration

#### Intuition

We can enumerate all possible substrings and determine the longest one that is balanced.

Specifically:

- We enumerate the left endpoint $i$ of the substring and then enumerate the right endpoint $j$, where $i \le j < n$.
- While extending the right endpoint, we maintain a frequency table $\textit{cnt}$ to count the occurrences of each character in the current substring.
- For each substring $[i, j]$, we iterate through $\textit{cnt}$ and check whether all characters that appear in the substring have the same frequency. If this condition is satisfied, we update the answer.

#### Implementation


```python
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(i, n):
                cnt[s[j]] += 1
                if len(set(cnt.values())) == 1:
                    res = max(res, j - i + 1)
        return res
```


#### Complexity Analysis

Let $C$ be the size of the character set, which is $26$ in this case, and let $n$ be the length of the string $s$.

- Time complexity: $O(Cn^2)$.
  
  Enumerating all substrings takes $O(n^2)$ time, and checking whether a substring is balanced takes $O(C)$ time.

- Space complexity: $O(C)$.

---