### Approach 1: Brute Force Matching

#### Intuition

For each string $\textit{pattern}$ in the array $\textit{patterns}$, we check whether it is a substring of $\textit{word}$ and count how many strings satisfy this condition.

We define a function $\textit{check}(\textit{pattern}, \textit{word})$ to determine whether $\textit{pattern}$ is a substring of $\textit{word}$. Let the length of $\textit{pattern}$ be $m$. In this function, we compare $\textit{pattern}$ with every substring of $\textit{word}$ of length $m$.

To avoid unnecessary comparisons, we immediately stop checking the current substring once a mismatch is found and move on to the next candidate substring. If a complete match is found, we return $\texttt{true}$. If none of the substrings match, we return $\texttt{false}$.

#### Implementation


```python
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        def check(pattern: str, word: str) -> bool:
            m = len(pattern)
            n = len(word)
            for i in range(n - m + 1):
                flag = True
                for j in range(m):
                    if word[i + j] != pattern[j]:
                        flag = False
                        break
                if flag:
                    return True
            return False

        res = 0
        for pattern in patterns:
            res += check(pattern, word)
        return res
```


#### Complexity Analysis

Let $n$ be the length of the string $\textit{word}$, and let $m_i$ be the length of the string $\textit{patterns}[i]$.

- Time complexity: $O\left(n \times \sum_i m_i\right)$.
  
  For each string $\textit{patterns}[i]$, determining whether it is a substring of $\textit{word}$ using brute-force matching requires $O(n \cdot m_i)$ time.

- Space complexity: $O(1)$.

---

### Approach 2: KMP Algorithm

#### Intuition

In Approach 1, each call to $\textit{check}(\textit{pattern}, \textit{word})$ performs a brute-force comparison between $\textit{pattern}$ and all candidate substrings of $\textit{word}$. If the lengths of $\textit{pattern}$ and $\textit{word}$ are $m$ and $n$, respectively, this matching process takes $O(nm)$ time.

We can optimize the matching process using the Knuth-Morris-Pratt (KMP) algorithm. Instead of restarting comparisons after a mismatch, KMP uses information from previously matched characters to skip unnecessary comparisons, resulting in a linear-time matching procedure.

#### Implementation


```python
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        def check(pattern: str, word: str) -> bool:
            m = len(pattern)
            n = len(word)
            # generate the prefix array of the pattern
            pi = [0] * m
            j = 0
            for i in range(1, m):
                while j and pattern[i] != pattern[j]:
                    j = pi[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                pi[i] = j
            # using prefix arrays for matching
            j = 0
            for i in range(n):
                while j and word[i] != pattern[j]:
                    j = pi[j - 1]
                if word[i] == pattern[j]:
                    j += 1
                if j == m:
                    return True
            return False

        res = 0
        for pattern in patterns:
            res += check(pattern, word)
        return res
```


#### Complexity Analysis

Let $n$ be the length of the string $\textit{word}$, let $k$ be the number of strings in $\textit{patterns}$, and let $m_i$ be the length of $\textit{patterns}[i]$.

- Time complexity: $O(nk + \sum_i m_i)$.
  
  For each string $\textit{patterns}[i]$, building the prefix array takes $O(m_i)$ time, and the KMP matching process takes $O(n)$ time. Therefore, the total time complexity is $O\left(\sum_i (n + m_i)\right) = O\left(nk + \sum_i m_i\right)$.

- Space complexity: $O(\max_i(m_i))$.
  
  This is the space required for the prefix array of the longest pattern.

---