### Approach: Hash Table + Geometry Mathematics

#### Intuition

The problem asks us to find the number of horizontal trapezoids. To do this, we can count how many points lie at each height, that is, at each distinct y value. Suppose there are $p_y$ points at height $y$. Then the number of horizontal edges that can be formed at this height is $\frac{p_y (p_y - 1)}{2}$.

A horizontal trapezoid can be formed by choosing one such edge from one height and another from a different height. We count all possible combinations of these edges.

#### Implementation


```python
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        point_num = defaultdict(int)
        mod = 10**9 + 7
        ans, total_sum = 0, 0
        for point in points:
            point_num[point[1]] += 1
        for p_num in point_num.values():
            edge = p_num * (p_num - 1) // 2
            ans = (ans + edge * total_sum) % mod
            total_sum = (total_sum + edge) % mod
        return ans
```


#### Complexity Analysis

Let $n$ be the length of $\textit{points}$.

- Time complexity: $O(n)$.

- Space complexity: $O(n)$.