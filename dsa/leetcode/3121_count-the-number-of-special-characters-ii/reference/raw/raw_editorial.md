### Approach: Record the Start and End Positions

#### Intuition

For each letter, record the last occurrence position of its lowercase form and the first occurrence position of its uppercase form. A letter is considered special if and only if both positions exist and the last occurrence position of the lowercase form is strictly smaller than the first occurrence position of the uppercase form.

#### Implementation


```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_low = [-1] * 26
        first_up = [-1] * 26
        for i, c in enumerate(word):
            if c.islower():
                last_low[ord(c) - ord('a')] = i
            else:
                idx = ord(c) - ord('A')
                if first_up[idx] == -1:
                    first_up[idx] = i
        ans = 0
        for i in range(26):
            if last_low[i] != -1 and first_up[i] != -1 and last_low[i] < first_up[i]:
                ans += 1
        return ans
```


#### Complexity Analysis

Let $n$ be the length of the string and let $|\Sigma| = 26$.

- Time complexity: $O(n + |\Sigma|)$.

- Space complexity: $O(|\Sigma|)$.

---