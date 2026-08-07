### Approach: Transitivity of Restrictions

#### Intuition

**Hint $1$**

Since each building appears at most once in the array $\textit{restrictions}$, for convenience, we represent a restriction as $(i, h_i)$, indicating that the height of building $i$ cannot exceed $h_i$.

Although $(i, h_i)$ is a restriction on building $i$, it also affects other buildings.

**Hint $1$ Explaination**

If the height of building $i$ cannot exceed $h_i$, and the height difference between adjacent buildings cannot exceed $1$, then:

- The height of building $i - 1$ cannot exceed $h_i + 1$.
- The height of building $i + 1$ cannot exceed $h_i + 1$.

More generally:

- The height of building $j$ cannot exceed $h_i + |i - j|$.

**Hint $2$**

According to Hint 1, each restriction $(i, h_i)$ effectively imposes a constraint on all $n$ buildings. If we can somehow propagate all restrictions to obtain the true minimum upper bound for each building $i$, denoted by $\textit{limit}_i$, then the height of building $i$ cannot exceed $\textit{limit}_i$.

Therefore, an optimal construction is to build building $i$ with height exactly $\textit{limit}_i$.

**Hint $3$**

According to Hint 2, we can determine the height of every building. However, the constraint is $n \le 10^9$, so even an $O(n)$ algorithm would exceed the time and space limits. Therefore, we can only compute $\textit{limit}_i$ for the buildings that appear in the restriction array.

Can we determine the maximum building height without explicitly considering every building?

**Hint $3$ Explaination**

In fact, we only care about the maximum height among all $n$ buildings.

Consider two buildings $i$ and $j$ such that $i < j$, and suppose no other building between them appears in the restriction array. According to the propagated restrictions, the heights of the buildings between $i$ and $j$ will form a "mountain" shape: starting from building $i$, the heights increase toward a peak and then decrease toward building $j$.

Let this peak height be $\textit{best}(i, j)$. Then it must satisfy

$\big( \textit{best}(i, j) - \textit{limit}_i \big) + \big( \textit{best}(i, j) - \textit{limit}_j \big) \leq j-i$

Solving this inequality gives

$\textit{best}(i, j) = \lfloor \frac{(j - i) + \textit{limit}_i + \textit{limit}_j}{2} \rfloor$

Thus, we can compute the maximum possible height among all buildings.

**Approach and Algorithm**

First, we compute all values of $\textit{limit}_i$.

To simplify boundary handling (i.e., for the first and last buildings), we add the two restrictions $(1, 0)$ and $(n, n - 1)$ to the restriction array, then sort the array by building index in ascending order.

Next, we propagate the restrictions. This can be done with two passes over the sorted array: one from left to right and one from right to left.

- During the left-to-right pass, consider two adjacent restrictions $(i, h_i)$ and $(j, h_j)$. The restriction $(i, h_i)$ propagates to building $j$ as $(j, h_i + (j - i))$. Therefore, we update $h_j$ to the minimum of its current value and $h_i + (j - i)$. This propagates all restrictions coming from the left.

- During the right-to-left pass, consider two adjacent restrictions $(i, h_i)$ and $(j, h_j)$. The restriction $(j, h_j)$ propagates to building $i$ as $(i, h_j + (j - i))$. Therefore, we update $h_i$ to the minimum of its current value and $h_j + (j - i)$. This propagates all restrictions coming from the right.

After these two passes, every $h_i$ becomes the corresponding $\textit{limit}_i$.

Finally, for every pair of adjacent restricted buildings, we compute the maximum achievable height between them using the formula derived in Hint 3, and take the maximum over all such values.

#### Implementation

```python
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        r = restrictions
        # Add restriction (1, 0)
        r.append([1, 0])
        r.sort()

        # Add restriction (n, n-1)
        if r[-1][0] != n:
            r.append([n, n - 1])

        m = len(r)

        # Pass restrictions from left to right
        for i in range(1, m):
            r[i][1] = min(r[i][1], r[i - 1][1] + (r[i][0] - r[i - 1][0]))
        # Pass restrictions from right to left
        for i in range(m - 2, 0, -1):
            r[i][1] = min(r[i][1], r[i + 1][1] + (r[i + 1][0] - r[i][0]))

        ans = 0
        for i in range(m - 1):
            # Calculate the maximum height of the buildings between r[i][0] and r[i][1]
            best = ((r[i + 1][0] - r[i][0]) + r[i][1] + r[i + 1][1]) // 2
            ans = max(ans, best)

        return ans
```

#### Complexity Analysis

Let $m$ be the length of the array $\textit{restrictions}$.

- Time complexity: $O(m \log m)$.

  Sorting the restriction array takes $O(m \log m)$ time. The two propagation passes and the final scan each take $O(m)$ time. Therefore, the overall time complexity is $O(m \log m)$.

- Space complexity: $O(\log m)$.

  This is the auxiliary stack space required by the sorting algorithm.

---