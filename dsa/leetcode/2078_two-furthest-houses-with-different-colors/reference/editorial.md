### Approach: Enumeration

#### Intuition

We can compute the maximum distance between two houses with different colors by enumerating all possible pairs of houses.

Specifically, we first iterate over houses with smaller indices, and for each such house, we iterate over the houses to its right. For each pair, we compare their colors. If the colors are different, we compute the distance between them and update the maximum distance accordingly. Otherwise, we skip the pair. After considering all pairs, we return the maximum distance found.

#### Implementation

```python
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        res = 0  # the maximum distance between two houses of different colors
        # traverse the indices of two houses and maintain the maximum distance
        for i in range(n):
            for j in range(i + 1, n):
                if colors[i] != colors[j]:
                    res = max(res, j - i)
        return res
```

#### Complexity Analysis

Let $n$ be the length of $\textit{colors}$.

- Time complexity: $O(n^2)$.

  We enumerate all pairs of houses and update the maximum distance when their colors differ.

- Space complexity: $O(1)$.

---

### Approach 2: Greedy

#### Intuition

The brute-force approach checks every pair, but the optimal pair always has one endpoint at house 0 or house $n-1$. Suppose the best pair is $(i, j)$ with $i > 0$ and $j < n-1$ and $\textit{colors}[i] \ne \textit{colors}[j]$.

- If $\textit{colors}[0] \ne \textit{colors}[j]$, then pair $(0, j)$ is valid and has distance $j > j - i$, which contradicts the optimality of $(i, j)$.
- So $\textit{colors}[0] = \textit{colors}[j] \ne \textit{colors}[i]$.
- If $\textit{colors}[i] \ne \textit{colors}[n-1]$, then pair $(i, n-1)$ is valid with distance $n-1-i > j-i$, another contradiction.
- So $\textit{colors}[i] = \textit{colors}[n-1]$, which means $\textit{colors}[0] \ne \textit{colors}[n-1]$ and pair $(0, n-1)$ is valid with distance $n-1 > j-i$, a final contradiction.

In every case the assumption fails, so the optimal pair must touch index 0 or index $n-1$.

Given this, a single left-to-right pass suffices. For each index $i$ where $\textit{colors}[i] \ne \textit{colors}[n-1]$, pair $(i, n-1)$ is valid with distance $n-1-i$. At the same time, when $\textit{colors}[0] = \textit{colors}[n-1]$, the condition $\textit{colors}[i] \ne \textit{colors}[n-1]$ also implies $\textit{colors}[i] \ne \textit{colors}[0]$, so pair $(0, i)$ is valid with distance $i$. When $\textit{colors}[0] \ne \textit{colors}[n-1]$, pair $(0, n-1)$ is already captured at $i = 0$ as a candidate distance of $n-1$. Either way, taking $\max(\textit{ans}, i, n-1-i)$ whenever $\textit{colors}[i] \ne \textit{colors}[n-1]$ is safe and correct.

#### Implementation

```python
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        n = len(colors)
        for i in range(n - 1):
            if colors[i] != colors[n - 1]:
                ans = max(ans, i, n - 1 - i)
        return ans
```

#### Complexity Analysis

Let $n$ be the length of $\textit{colors}$.

- Time complexity: $O(n)$.

  We make a single pass over the array, performing constant work per element.

- Space complexity: $O(1)$.

---