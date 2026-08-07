### Approach: Traversal

#### Intuition

First, we use a hash table to record the number of occurrences of each character in the string. Then, we traverse all lowercase letters, separating them into vowels and consonants to find the maximum frequency in each group. Finally, summing these two values gives the answer.

#### Implementation


```python
from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        mp = Counter(s)
        vowel = max((mp[ch] for ch in mp if ch in "aeiou"), default=0)
        consonant = max((mp[ch] for ch in mp if ch not in "aeiou"), default=0)
        return vowel + consonant
```


#### Complexity Analysis

Let $n$ be the length of the string $s$, and $C$ be the number of lowercase English letters, which is $26$.

- Time complexity: $O(n)$.

- Space complexity: $O(C)$.

---