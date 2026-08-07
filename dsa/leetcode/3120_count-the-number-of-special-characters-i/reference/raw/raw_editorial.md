### Approach: Hash set

#### Intuition

Use a hash set to store all characters in the string, then traverse all $26$ letters and check whether both the lowercase and uppercase versions of each letter exist.

#### Implementation


```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        return sum(c in s and c.upper() in s for c in string.ascii_lowercase)
```


#### Complexity Analysis

Let $n$ be the length of the string $\textit{word}$, and let $|\Sigma| = 26$.

- Time complexity: $O(n + |\Sigma|)$.

- Space complexity: $O(|\Sigma|)$.

---