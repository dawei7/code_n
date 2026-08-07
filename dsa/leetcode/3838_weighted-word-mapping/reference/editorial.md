### Approach: Simulation

#### Intuition

We can directly simulate the process described in the problem statement. For each string in $\textit{words}$, we traverse all of its characters, look up the corresponding character weight in $\textit{weights}$, and accumulate the total weight.

The problem then requires us to take the total weight modulo $26$ and map it in reverse alphabetical order to a character. This is equivalent to subtracting the modulo result from the character 'z'. In other words, if the total weight is $s$, the resulting character is $'z' - (s \bmod 26)$.

#### Implementation

```python
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for word in words:
            s = 0
            for c in word:
                s += weights[ord(c) - ord("a")]
            ans.append(chr(ord("z") - s % 26))
        return "".join(ans)
```

#### Complexity Analysis

Let $n$ be the total number of characters across all strings in $\textit{words}$.

- Time complexity: $O(n)$.

  We traverse each character exactly once.

- Space complexity: $O(1)$.

  The output string is not included in the space complexity. Aside from the output, only a few auxiliary variables are used.

---