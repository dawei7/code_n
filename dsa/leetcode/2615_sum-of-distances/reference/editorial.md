### Approach: Grouping + Prefix Sum

#### Intuition

For each index $i$, we need to compute the sum of $|i - j|$ for all indices $j$ such that $\textit{nums}[i] = \textit{nums}[j]$.

First, we group all indices with the same value together using a hash table. For a group of indices $a_0 < a_1 < \cdots < a_{m-1}$, we want to efficiently compute the result for each $a_i$.

For $a_i$:

$\textit{res}[a_i] = \sum_{j=0}^{m-1} |a_i - a_j|$

Since the indices within each group are sorted, we can split the sum into two parts:

$\textit{res}[a_i] = \sum_{j=0}^{i-1}(a_i - a_j) + \sum_{j=i+1}^{m-1}(a_j - a_i)$

Let $S$ be the sum of all indices in the group, and let $P_i = \sum_{j=0}^{i-1} a_j$ be the prefix sum (that is, $a_0 + \cdots + a_{i-1}$). We compute the two parts separately and then combine them.

**Left side** ($j < i$, total of $i$ terms):

$$
\sum_{j=0}^{i-1}(a_i - a_j)
= \sum_{j=0}^{i-1} a_i - \sum_{j=0}^{i-1} a_j
= i \times a_i - P_i
$$

**Right side** ($j > i$, total of $m - i - 1$ terms):

The sum $\sum_{j=i+1}^{m-1} a_j$ equals the total sum $S$ minus the elements up to index $i$, that is, $S - P_i - a_i$. Since each term subtracts $a_i$, we further subtract $(m - i - 1) \times a_i$:

$$
\sum_{j=i+1}^{m-1}(a_j - a_i)
= (S - P_i - a_i) - (m - i - 1) \times a_i
$**Combining** the left and right parts:$
\begin{aligned}
\textit{res}[a_i]
&= (i \times a_i - P_i) + \bigl((S - P_i - a_i) - (m - i - 1) \times a_i\bigr) \
&= S - 2P_i + a_i \times (2i - m)
\end{aligned}
$$

We process each group while maintaining the prefix sum $P_i$, which allows us to compute all results for that group in $O(m)$ time. Since the total size across all groups is $n$, the overall time complexity is $O(n)$.

#### Implementation

```python
class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        n = len(nums)
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)
        res = [0] * n
        for group in groups.values():
            total = sum(group)
            prefix_total = 0
            sz = len(group)
            for i, idx in enumerate(group):
                res[idx] = total - prefix_total * 2 + idx * (2 * i - sz)
                prefix_total += idx
        return res
```

#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n)$.

  Each index is processed once while grouping and once while computing results, resulting in linear time.

- Space complexity: $O(n)$.

  The hash table stores all indices, requiring linear space.

---