[TOC]

## Solution

---

### Approach: Simulation

#### Intuition

According to the problem, we should simulate the process by traversing each string and checking whether it contains the character $x$. If it does, we add the index of the string to the result array.

Finally, we return the result array.

#### Implementation

```python
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        n = len(words)
        for i in range(n):
            if x in words[i]:
                res.append(i)
        return res
```

#### Complexity Analysis

Let $n$ be the length of the array and $m$ be the length of the string.

- Time complexity: $O(n * m)$.

  We traverse each string to check if it contains the character `x`.

- Space complexity: $O(1)$.

  The space required for the return variable is not included in the calculation.