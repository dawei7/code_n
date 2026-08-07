[TOC]

## Solution

---

### Approach: Count The Frequency Of Each Character

#### Intuition

We use a hash map to count the number of occurrences of each character in the string $s$. In each key-value pair of the hash map, the key represents a character, and the value represents the number of times that character appears.

After the statistics are completed, we traverse the values in the hash map to find the largest odd number $\textit{maxOdd}$ and the smallest even number $\textit{minEven}$. The final answer is $\textit{maxOdd} - \textit{minEven}$.

#### Implementation


```python
class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        maxOdd = max(x for x in c.values() if x % 2 == 1)
        minEven = min(x for x in c.values() if x % 2 == 0)
        return maxOdd - minEven
```


#### Complexity Analysis

Let $n$ be the length of the string $s$, and $|\Sigma|$ the size of its character set. Since $s$ contains only lowercase letters, $|\Sigma| = 26$.

- Time complexity: $O(n)$.

- Space complexity: $O(|\Sigma|)$.